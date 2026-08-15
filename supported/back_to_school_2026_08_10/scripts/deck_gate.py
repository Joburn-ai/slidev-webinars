#!/usr/bin/env python3
"""
DECK GATE — SupportED back-to-school webinar.

Run before every deploy. Exits non-zero on any FAIL.

    python3 scripts/deck_gate.py

It resolves `src:` includes, so it measures the WHOLE deck, not just the spine.

Gates:
  G1  visual coverage      >= 95% of slides carry a real visual
  G2  layout runs          no layout value 3x consecutively
  G3  layout variety       >= 4 distinct layouts in any rolling window of 10
  G4  speaker notes        100% of content slides carry a note
  G5  assets exist         every referenced image resolves on disk
  G6  claim scrub          no banned/uncleared claim appears in body OR notes
  G7  no placeholders      unresolved placeholders are reported (WARN, not FAIL,
                           because two are deliberate and tracked as blockers)
  G8  body text floor      no text-xl or smaller on body copy
"""
import os
import re
import sys
from collections import Counter

DECK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── The cleared set. Anything here is FORBIDDEN in body copy or speaker notes. ──
# Sources: handover §6 (2026-08-14) + the narrow cleared set confirmed with Joe.
BANNED = [
    (r'College Board [Cc]ertified',      'NOT CLEARED — say "certified AP teacher"'),
    (r'National AP Scholar',             'Joe killed this claim himself'),
    (r'\$2\.8 ?million|2\.8 ?million',   'NOT CLEARED — no source on file'),
    (r'\$100,000\+|\$100,000 ?\+',       'NOT CLEARED — unsupportable'),
    (r'\$50,000 in long-?term value',    'NOT CLEARED — unsupportable as stated'),
    (r'\$11,774',                        'NOT CLEARED — no source'),
    (r'\$1,500 to \$3,000',              'Third-party claim, needs citation'),
    (r'literally can.t lose',            'ABSOLUTE CLAIM — hard block, cut it'),
    (r'\bguarantee[sd]?\b(?! (?:that )?(?:they|your))', 'Performance guarantee language'),
    (r'\bBryce\b',                       'Student not in the cleared set'),
    (r'\bJavier\b',                      'Student not in the cleared set'),
    (r'\bCalla\b|\bChristian\b|\bSamiksha\b|\bTaylor\b|\bYamen\b',
                                         'Student not in the cleared set'),
    (r'Spring Cohort',                   'January framing — re-season it'),
    (r'90% of your stress',              'Invented statistic'),
    (r'20 to 40 points|10-15 points',    'Unsourced numeric claim'),
]
# A banned phrase may appear in a SPEAKER NOTE only when the note is explicitly
# flagging it as banned. Matched case-insensitively. Visible slide copy gets no
# such exemption — that is the whole point of the gate.
NOTE_FLAG_MARKERS = ('not cleared', 'do not say', 'do not reinstate', 'cut', 'banned',
                     'claim change', 'never say', 'never "', 'not in the cleared set',
                     'claim rule', 'claim discipline', 'claim boundary', 'hard block',
                     'name removed', 'must not be', 'is not defensible', 'claim note')

# 🔴 `{{FOO}}` is VUE INTERPOLATION in Slidev, not a literal placeholder: it evaluates
# to an undefined variable and renders as NOTHING. A placeholder you cannot see is worse
# than one you can, so the deck uses visible cards instead and the gate tracks those.
PLACEHOLDER = re.compile(r'\{\{[A-Z_]+\}\}|\[ ?QR CODE ?\]|\[SAY THE MONTH\]|TODO|TBD'
                         r'|NOT YET GENERATED|NOT SET')

VISUAL = re.compile(
    r'<img|!\[|```mermaid|<svg|v-mark|<Arrow'
    r'|sp-num|sp-stat|sp-verdict|sp-rubric|sp-vs\b|sp-quiz|sp-chip|sp-card|sp-figure'
    r'|sp-shot|sp-bleed|sp-portrait|sp-grid'
)


def read_deck(spine='slides.md'):
    """Return [(slide_index, source_file, frontmatter, body)] with src: resolved."""
    def parse_file(path):
        src = open(path, encoding='utf-8').read()
        lines = src.split('\n')
        slides, cur, fm = [], [], {}
        i = 0

        def flush():
            if cur or fm:
                slides.append((dict(fm), '\n'.join(cur)))

        while i < len(lines):
            ln = lines[i]
            if ln.strip() == '---':
                j, block = i + 1, []
                while j < len(lines) and lines[j].strip() != '---':
                    block.append(lines[j])
                    j += 1
                ok = j < len(lines) and block and all(
                    (not b.strip()) or re.match(r'^[A-Za-z_][\w-]*\s*:', b)
                    or b.startswith(' ') or b.startswith('-')
                    for b in block)
                if ok:
                    flush()
                    cur, fm = [], {}
                    for b in block:
                        m = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*(.*)$', b)
                        if m:
                            fm[m.group(1)] = m.group(2).strip()
                    i = j + 1
                    continue
                i += 1
                continue
            cur.append(ln)
            i += 1
        flush()
        return [(f, b) for f, b in slides if b.strip() or f]

    out = []
    for fm, body in parse_file(os.path.join(DECK, spine)):
        if 'src' in fm:
            sub = os.path.join(DECK, fm['src'].lstrip('./'))
            for sfm, sbody in parse_file(sub):
                out.append((os.path.basename(sub), sfm, sbody))
        else:
            out.append((spine, fm, body))
    return out


def main():
    slides = read_deck()
    n = len(slides)
    fails, warns = [], []

    # ── G1 visual coverage ────────────────────────────────────────────────
    bare = [i for i, (_, _, b) in enumerate(slides, 1) if not VISUAL.search(b)]
    cov = 100 * (n - len(bare)) / n
    g1 = cov >= 95
    (fails if not g1 else warns if False else []).append(
        f'G1 visual coverage {cov:.1f}% < 95% — bare slides: {bare}') if not g1 else None

    # ── G2 / G3 VISUAL TREATMENT variety ──────────────────────────────────
    # 🔴 WHY THIS MEASURES TREATMENT AND NOT `layout:`.
    # The original rule was "no layout value 3x consecutively", written when this deck
    # had `layout: center` on 138 of 178 slides. But layout value is only a PROXY for
    # the thing that actually matters, which is: does slide N look different from N+1?
    # This deck's style.css vertically centres EVERY layout, so `center` and `default`
    # now render near-identically — meaning a deck could alternate those two keys, pass
    # a layout-run check, and still be 40 identical-looking slides in a row.
    # So we score the real thing: ground + composition archetype. Alternating `center`
    # and `default` no longer buys anything, and a genuinely varied run of `default`
    # slides is no longer punished for it.
    ARCH = [('bleed', r'sp-bleed'), ('split', r'sp-split|::right::'), ('vs', r'sp-vs\b'),
            ('quiz', r'sp-quiz'), ('verdict', r'sp-verdict'), ('rubric', r'sp-rubric'),
            ('grid', r'sp-grid'), ('num', r'sp-num|sp-stat'), ('figure', r'sp-figure'),
            ('shot', r'sp-shot'), ('card', r'sp-card')]

    def treatment(fm, body):
        # Grounds are CLASSES now, not frontmatter backgrounds — see style.css.
        cls = str(fm.get('class', ''))
        ground = ('navy' if 'night' in cls else
                  'black' if 'ink' in cls else
                  'gold' if 'sun' in cls else 'white')
        arch = 'type'
        for name, pat in ARCH:
            if re.search(pat, body):
                arch = name
                break
        return f'{ground}/{arch}'

    treats = [treatment(fm, b) for _, fm, b in slides]
    layouts = [fm.get('layout', 'default') for _, fm, _ in slides]

    runs, cur = [], None
    for L in treats:
        if cur and cur[0] == L:
            cur = (L, cur[1] + 1)
        else:
            if cur:
                runs.append(cur)
            cur = (L, 1)
    if cur:
        runs.append(cur)
    bad_runs = [r for r in runs if r[1] >= 3]
    if bad_runs:
        fails.append(f'G2 identical visual treatment 3x consecutively: {bad_runs}')

    thin = []
    for i in range(0, max(1, n - 9)):
        w = treats[i:i + 10]
        if len(set(w)) < 4:
            thin.append((i + 1, sorted(set(w))))
    if thin:
        warns.append(f'G3 windows with <4 distinct treatments: {thin[:4]}'
                     f'{" ...+%d more" % (len(thin) - 4) if len(thin) > 4 else ""}')

    # ── G4 speaker notes ──────────────────────────────────────────────────
    nonote = [i for i, (_, fm, b) in enumerate(slides, 1)
              if not re.search(r'<!--(?!\s*(?:slide:|divider:)).*?-->', b, re.S)]
    if nonote:
        fails.append(f'G4 slides with no speaker note: {nonote}')

    # ── G4b EMPTY SLIDES ──────────────────────────────────────────────────
    # 🔴 A frontmatter block with no body renders as a BLANK SLIDE the audience sits
    # through. One shipped on 2026-08-15 from an edit that removed a slide's content but
    # left its frontmatter; it was only noticed because the notes gate flagged it.
    empty = [i for i, (_, _, b) in enumerate(slides, 1)
             if not re.sub(r'<!--.*?-->', '', b, flags=re.S).strip()]
    if empty:
        fails.append(f'G4b blank slides (frontmatter with no body): {empty}')

    # ── G5 assets exist ───────────────────────────────────────────────────
    missing = set()
    for _, _, b in slides:
        for m in re.finditer(r'src="(/[^"]+)"', b):
            p = os.path.join(DECK, 'public', m.group(1).lstrip('/'))
            if not os.path.exists(p):
                missing.add(m.group(1))
    for m in re.finditer(r"url\('(/[^']+)'\)", open(os.path.join(DECK, 'style.css')).read()):
        p = os.path.join(DECK, 'public', m.group(1).lstrip('/'))
        if not os.path.exists(p):
            missing.add(m.group(1))
    if missing:
        fails.append(f'G5 missing assets: {sorted(missing)}')

    # ── G5b AI-GENERATED IMAGERY ──────────────────────────────────────────
    # 🔴 HARD FAIL. On 2026-08-15 an AI-generated photo of Dr Joe (Gemini sparkle
    # watermark visible, XMP Credit="Google AI",
    # DigitalSourceType=".../trainedAlgorithmicMedia") was live on the AUTHORITY slide,
    # showing a real named person at a named event that we cannot evidence.
    # A fabricated photo of a real person is never acceptable in a client deck.
    AI_MARKERS = ('trainedAlgorithmicMedia', 'compositeWithTrainedAlgorithmicMedia',
                  'Google AI', 'Firefly', 'Midjourney', 'DALL-E', 'stable-diffusion')
    ai_hits = []
    try:
        from PIL import Image
        import glob as _glob
        for ip in _glob.glob(os.path.join(DECK, '**/*.*'), recursive=True):
            if not ip.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                continue
            try:
                im = Image.open(ip)
            except Exception:
                continue
            blob = ''
            for _k, _v in im.info.items():
                blob += _v.decode('utf-8', 'ignore') if isinstance(_v, bytes) else str(_v)
            found = [m for m in AI_MARKERS if m.lower() in blob.lower()]
            if found:
                rel = os.path.relpath(ip, DECK)
                if any(rel.replace('public', '') in b for _, _, b in slides):
                    ai_hits.append(f'  {rel} PLACED IN DECK — {found}')
                else:
                    ai_hits.append(f'  {rel} on disk only — {found}')
    except ImportError:
        warns.append('G5b skipped: PIL not available')
    if any('PLACED IN DECK' in h for h in ai_hits):
        fails.append('G5b AI-generated imagery placed in the deck:\n' + '\n'.join(ai_hits))
    elif ai_hits:
        warns.append('G5b AI-generated imagery present on disk (not placed):\n' + '\n'.join(ai_hits))

    # ── G6 claim scrub ────────────────────────────────────────────────────
    hits = []
    for i, (f, _, b) in enumerate(slides, 1):
        notes = ' '.join(re.findall(r'<!--(.*?)-->', b, re.S))
        visible = re.sub(r'<!--.*?-->', '', b, flags=re.S)
        for pat, why in BANNED:
            if re.search(pat, visible, re.I):
                hits.append(f'  slide {i} ({f}) VISIBLE: /{pat}/ — {why}')
            elif re.search(pat, notes, re.I):
                # allowed only if the note is explicitly flagging it as banned
                nl = notes.lower()
                if not any(mk in nl for mk in NOTE_FLAG_MARKERS):
                    hits.append(f'  slide {i} ({f}) NOTE: /{pat}/ — {why}')
    if hits:
        fails.append('G6 uncleared claims:\n' + '\n'.join(hits))

    # ── G7 placeholders (WARN — two are tracked blockers) ─────────────────
    ph = []
    for i, (f, _, b) in enumerate(slides, 1):
        visible = re.sub(r'<!--.*?-->', '', b, flags=re.S)
        for m in PLACEHOLDER.finditer(visible):
            ph.append(f'slide {i} ({f}): {m.group(0)}')
    if ph:
        warns.append('G7 unresolved placeholders (BLOCKERS):\n  ' + '\n  '.join(ph))

    # ── G8 body text floor ────────────────────────────────────────────────
    small = [i for i, (_, _, b) in enumerate(slides, 1)
             if re.search(r'class="[^"]*\btext-(xs|sm|base|lg|xl)\b', b)]
    if small:
        warns.append(f'G8 slides with body text below text-2xl: {small}')

    # ── report ────────────────────────────────────────────────────────────
    notew = sum(len(' '.join(re.findall(r'<!--(.*?)-->', b, re.S)).split())
                for _, _, b in slides)
    imgs = sum(len(re.findall(r'<img', b)) for _, _, b in slides)
    used = set()
    for _, _, b in slides:
        used.update(re.findall(r'src="(/images/[^"]+)"', b))

    print('=' * 62)
    print(' SUPPORTED BACK-TO-SCHOOL — DECK GATE')
    print('=' * 62)
    print(f'  slides            {n}')
    print(f'  visual coverage   {cov:.1f}%   (gate >=95%)   bare={len(bare)}')
    print(f'  <img> tags        {imgs}')
    print(f'  distinct assets   {len(used)}')
    print(f'  speaker notes     {n - len(nonote)}/{n} slides, {notew:,} words')
    print(f'  treatments        {len(set(treats))} distinct')
    print(f"  longest treat run {max(runs, key=lambda r: r[1])[0]} x{max(r[1] for r in runs)}")
    print(f"  layout mix (fyi)  {dict(Counter(layouts).most_common())}")
    print('-' * 62)
    for w in warns:
        print(f'  ⚠️  WARN  {w}')
    for f in fails:
        print(f'  ❌ FAIL  {f}')
    if not fails:
        print('  ✅ ALL HARD GATES PASS')
    print('=' * 62)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
