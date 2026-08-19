#!/usr/bin/env python3
"""Structural validator. Run before every build.

Exists because a splice put a second frontmatter block directly after the first, which Slidev renders
as an EMPTY slide followed by the literal text `class: g-green` on screen. It built clean, exported
clean, and was only visible by looking at the render. This makes it a failing check instead."""
import re, glob, sys
errs=[]
for p in sorted(glob.glob('sections/*.md'))+['slides.md']:
    s=open(p,encoding='utf-8').read()
    fm=''
    blocks=re.split(r'\n---\n', s)
    # 🔴 A STACKED FRONTMATTER PAIR is the bug this file exists to catch, and the first version
    # missed it: two consecutive frontmatter-shaped blocks means the FIRST becomes an empty slide
    # and the SECOND renders on screen as literal text like 'class: g-cream ecf-onwhite'.
    prev_was_fm = False
    for bi, b in enumerate(blocks):
        stripped = b.strip().lstrip('-').strip()
        is_fm = bool(stripped) and bool(re.match(r'^(layout|class|transition|src)\s*:', stripped)) \
                and '<!-- slide:' not in b
        if is_fm and prev_was_fm:
            errs.append(f"{p} :: STACKED FRONTMATTER before block {bi} -> {stripped[:48]!r} "
                        f"(renders as visible body text on a blank slide)")
        prev_was_fm = is_fm
    for b in blocks:
        body=b.strip().lstrip('-').strip()
        m=re.search(r'<!-- slide:([^>]+?) -->', b)
        if m:
            sid=m.group(1)
            if not re.search(r'g-green|g-deep|g-cream', fm):
                errs.append(f"{p} :: {sid} has NO ground class")
            if not re.search(r'<!--\n', b.split('-->',1)[1] if '-->' in b else ''):
                pass
            fm=''
        else:
            # a block with no slide marker that is not frontmatter-shaped is a leaked body
            if body and not re.match(r'^(layout|class|src|transition|title|theme|info|highlighter|lineNumbers|colorSchema|drawings|persist|mdc|fonts|sans|serif|provider|weights|titleTemplate|favicon)\s*:', body) \
               and not body.startswith('<style') and not body.startswith('#'):
                errs.append(f"{p} :: leaked body between slides -> {body[:60]!r}")
            fm=b
# every slide needs speaker notes
for p in sorted(glob.glob('sections/*.md'))+['slides.md']:
    s=open(p,encoding='utf-8').read()
    n_slides=len(re.findall(r'<!-- slide:', s)); n_notes=len(re.findall(r'\n<!--\n', s))
    # A read-off-the-screen (Fladlien) deck carries no notes by design: the script IS the slide.
    # Only enforce coverage on decks that use notes at all, or this fires on every slide of one.
    if n_slides and 0 < n_notes < n_slides:
        errs.append(f"{p} :: {n_slides} slides but only {n_notes} note blocks")
for e in errs: print("🔴", e)
print(("FAIL: %d" % len(errs)) if errs else "PASS: structure clean")
sys.exit(1 if errs else 0)
