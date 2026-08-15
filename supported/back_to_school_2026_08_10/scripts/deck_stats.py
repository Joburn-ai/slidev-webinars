#!/usr/bin/env python3
"""Parse a Slidev slides.md into slide records. Truth, not estimate."""
import re, sys, json, os

def parse(path):
    src = open(path, encoding='utf-8').read()
    lines = src.split('\n')
    # slide separators: '---' at col0 that are NOT inside a frontmatter block
    slides, cur, fm, in_fm = [], [], {}, False
    i = 0
    # Slidev: file may open with frontmatter
    def flush():
        if cur or fm:
            slides.append({'fm': dict(fm), 'body': '\n'.join(cur)})
    while i < len(lines):
        ln = lines[i]
        if ln.strip() == '---' and not in_fm:
            # start of a new slide; peek if next lines are frontmatter
            flush(); cur, fm = [], {}
            j = i + 1
            block = []
            while j < len(lines) and lines[j].strip() != '---':
                block.append(lines[j]); j += 1
            # it's frontmatter only if every non-blank line looks like key: value
            # and we found a closing '---'
            ok = j < len(lines) and block and all(
                (not b.strip()) or re.match(r'^[A-Za-z_][\w-]*\s*:', b) or b.startswith(' ') or b.startswith('-')
                for b in block)
            if ok:
                for b in block:
                    m = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*(.*)$', b)
                    if m: fm[m.group(1)] = m.group(2).strip()
                i = j + 1
                continue
            i += 1
            continue
        cur.append(ln); i += 1
    flush()
    return [s for s in slides if s['body'].strip() or s['fm']]

def stats(slides):
    out = []
    for n, s in enumerate(slides, 1):
        b = s['body']
        imgs = len(re.findall(r'<img|!\[', b))
        vis = imgs + len(re.findall(r'<(Arrow|VSwitch)\b|```mermaid|<svg|v-mark', b))
        words = len(re.sub(r'<[^>]+>|<!--.*?-->', ' ', b, flags=re.S).split())
        notes = re.findall(r'<!--(.*?)-->', b, re.S)
        h = re.search(r'^#{1,3} (.+)$', b, re.M)
        out.append({
            'n': n, 'layout': s['fm'].get('layout', 'default'),
            'imgs': imgs, 'visuals': vis, 'words': words,
            'note_words': sum(len(x.split()) for x in notes),
            'clicks': len(re.findall(r'v-click', b)),
            'head': (h.group(1)[:58] if h else ''),
        })
    return out

if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else 'slides.md'
    sl = parse(p); st = stats(sl)
    n = len(st)
    bare = [s for s in st if s['visuals'] == 0]
    print(f"FILE            {p}")
    print(f"SLIDES          {n}")
    print(f"WITH VISUAL     {n-len(bare)} = {100*(n-len(bare))/n:.1f}%   (gate >=95%)")
    print(f"BARE            {len(bare)} = {100*len(bare)/n:.1f}%   (gate <=5%)")
    print(f"IMG TAGS        {sum(s['imgs'] for s in st)}")
    print(f"VISUALS/SLIDE   {sum(s['visuals'] for s in st)/n:.2f}   (Fladlien 4.2)")
    print(f"NOTE WORDS      {sum(s['note_words'] for s in st)}")
    print(f"SLIDES W/ NOTES {len([s for s in st if s['note_words']>0])} = {100*len([s for s in st if s['note_words']>0])/n:.1f}%")
    print(f"CLICKS          {sum(s['clicks'] for s in st)}")
    print(f"NO ANIMATION    {len([s for s in st if s['clicks']==0])}")
    # layout runs
    runs, cur, longest = [], None, ('', 0)
    for s in st:
        if s['layout'] == cur[0] if cur else False: cur = (cur[0], cur[1]+1)
        else:
            if cur: runs.append(cur)
            cur = (s['layout'], 1)
    if cur: runs.append(cur)
    longest = max(runs, key=lambda r: r[1])
    bad = [r for r in runs if r[1] >= 3]
    print(f"LAYOUT RUNS >=3 {len(bad)}   longest = {longest[0]} x{longest[1]}   (gate 0)")
    from collections import Counter
    print("LAYOUT MIX     ", dict(Counter(s['layout'] for s in st).most_common()))
    return_json = os.environ.get('JSON')
    if return_json:
        json.dump(st, open(return_json, 'w'), indent=1)
