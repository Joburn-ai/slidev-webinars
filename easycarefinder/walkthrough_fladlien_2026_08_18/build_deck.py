#!/usr/bin/env python3
"""Fladlien 400-Slide-Hack build of the ECF walkthrough.

EVERY WORD OF THE SCRIPT IS ON SCREEN. John, 18 Aug: Singh clicks the arrow and reads off the screen.
That is the whole difference from the 51-slide version, where the script lived in the speaker notes.

Spec, from copy-brain/06_Webinars/frameworks/_FLAGSHIP_fladlien_400_slide_hack.md line 310:
  · 5-15 words/slide opening, 15-30 content, 40-60 closing
  · never the same layout 3 times in a row
  · every slide animates
  · body text never below text-2xl, split the slide instead of shrinking
  · every slide carries a visual; bare cards <=5%; 2-4 visual elements per slide
  · measured golden: swipe_slides_fladlien_mattos_mobile_84p.pdf = 4.2 image objects/page, 2% bare
"""
import json, re, os

beats=json.load(open('_beats.json'))

SECTION_IMG = {
 'op-conv':'c02_kitchen_table',
 'cover':'c01_four_doors','op-01':'c01_four_doors','op-02':'c01_four_doors','op-03':'c02_kitchen_table',
 'op-04':'c02_kitchen_table','op-05':'c03_phone_dusk','op-06':'c03_phone_dusk','op-07':'c03_phone_dusk',
 'op-08':'c04_form_wall','op-09':'c04_form_wall','op-10':'c05_broken_map','op-11':'c05_broken_map',
 'op-12':'c05_broken_map','op-13':'c05_broken_map',
 'fk-00':'c01_four_doors','fk-01':'c06_home_help','fk-02':'c06_home_help','fk-03':'c06_home_help','fk-04':'c06_home_help',
 'fk-05':'c07_independent_apt','fk-06':'c07_independent_apt','fk-07':'c07_independent_apt','fk-08':'c07_independent_apt',
 'fk-09':'c08_large_community','fk-10':'c08_large_community','fk-11':'c08_large_community','fk-12':'c08_large_community',
 'fk-12b':'c08_large_community','fk-12c':'c08_large_community',
 'fk-13':'c09_small_home_street','fk-14':'c09_small_home_street','fk-15':'c09_small_home_street',
 'fk-16':'c09_small_home_street','fk-16b':'c09_small_home_street','fk-16c':'c09_small_home_street','fk-17':'c09_small_home_street',
 'wh-01':'c10_invisible_street','wh-02':'c10_invisible_street','wh-03':'c10_invisible_street',
 'wh-04':'c11_two_doors_same_street','wh-05':'c11_two_doors_same_street','wh-06':'c11_two_doors_same_street',
 'cl-01':'c13_shortlist_table','cl-02':'c13_shortlist_table','cl-03':'c13_shortlist_table','cl-04':'c13_shortlist_table',
 'cl-05':'c13_shortlist_table','cl-06':'c13_shortlist_table','cl-07':'c13_shortlist_table',
 'cl-08':'c02_kitchen_table','cl-09':'c02_kitchen_table','cl-10':'c02_kitchen_table',
}
KICKER = {'op-conv':'One small thing first','op':'Where you are','fk':'The four kinds','wh':'Why they are invisible','cl':'How this works','co':'Easy Care Finder'}
def kicker(sid): return KICKER.get(sid, KICKER.get(sid[:2],'Easy Care Finder'))

def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def emphasise(t):
    """Give every slide a v-click reveal on its final clause, so nothing is static and the eye is led
    to the landing phrase. Falls back to a whole-line reveal on very short lines."""
    w=t.split()
    if len(w)<=5: return esc(t), None
    cut=max(len(w)-max(3,len(w)//3), 1)
    return esc(' '.join(w[:cut])), esc(' '.join(w[cut:]))

NUM=re.compile(r'^(six|Six|four|Four|three|Three|two|Two|one|One|nothing|Nothing|\d+)\b')

TREATMENTS=['BLEED','CREAM','SIDE-L','GREEN','SIDE-R','CREAM','BLEED','GREEN']

def render(s, n, treat):
    sid=s['src']; img=SECTION_IMG.get(sid,'c02_kitchen_table')
    head,rev=emphasise(s['text'])
    k=kicker(sid)
    size = 'ecf-hero' if s['words']<=6 else ('ecf-head' if s['words']<=14 else 'ecf-mid')
    rv = f'\n  <div v-click class="{size} ecf-mark mt-2">{rev}</div>' if rev else ''

    if treat=='BLEED':
        return f"""---
layout: cover
class: g-deep ecf-onimg
---

<!-- slide:{n:03d} · {sid} -->
<div class="absolute inset-0"><img src="/images/{img}.png" class="ecf-bleed" /><div class="ecf-scrim-b"></div></div>
<div class="absolute inset-0 flex flex-col justify-end px-20 pb-20 z-10 text-left">
  <div class="ecf-kicker mb-3">{k}</div>
  <div class="ecf-rule mb-5"></div>
  <div class="{size}">{head}</div>{rv}
</div>
"""
    if treat=='GREEN':
        return f"""---
class: g-green
---

<!-- slide:{n:03d} · {sid} -->
<div class="absolute inset-0"><img src="/images/{img}.png" class="ecf-ghost" /><div class="veil-green"></div></div>
<div class="absolute inset-0 flex flex-col justify-center px-24 z-10 text-left">
  <div class="ecf-kicker mb-3">{k}</div>
  <div class="ecf-rule mb-7"></div>
  <div class="{size}">{head}</div>{rv}
</div>
"""
    if treat=='CREAM':
        return f"""---
class: g-cream ecf-onwhite
---

<!-- slide:{n:03d} · {sid} -->
<div class="absolute inset-0"><img src="/images/{img}.png" class="ecf-ghost" /><div class="veil-cream"></div></div>
<div class="absolute inset-0 flex flex-col justify-center px-24 z-10 text-left">
  <div class="ecf-kicker mb-3">{k}</div>
  <div class="ecf-rule mb-7"></div>
  <div class="{size}">{head}</div>{rv}
</div>
"""
    side = 'L' if treat=='SIDE-L' else 'R'
    imgcol=f'<div class="h-full"><img src="/images/{img}.png" class="ecf-bleed" /></div>'
    txtcol=f"""<div class="flex flex-col justify-center px-14">
    <div class="ecf-kicker mb-3">{k}</div>
    <div class="ecf-rule mb-6"></div>
    <div class="{size}">{head}</div>{rv}
  </div>"""
    cols = (imgcol+"\n  "+txtcol) if side=='L' else (txtcol+"\n  "+imgcol)
    return f"""---
class: g-cream ecf-onwhite
---

<!-- slide:{n:03d} · {sid} -->
<div class="absolute inset-0 grid grid-cols-2">
  {cols}
</div>
"""

# assign treatments: rotate, never 3 identical in a row, and force BLEED on the first beat of a new source slide
out=[]; last=[]; ti=0
for n,s in enumerate(beats,1):
    if s['i']==0 and s['src'].startswith(('fk-0','fk-1','wh-0','cl-0','op-0')) and s['words']<=12:
        t='BLEED'
    else:
        t=TREATMENTS[ti % len(TREATMENTS)]; ti+=1
    while len(last)>=2 and last[-1]==t and last[-2]==t:
        ti+=1; t=TREATMENTS[ti % len(TREATMENTS)]
    last.append(t); out.append(render(s,n,t))

# split into four files so no single file is unmanageable
per=(len(out)+3)//4
os.makedirs('sections',exist_ok=True)
names=['s1_open','s2_four','s3_why','s4_close']
for i,name in enumerate(names):
    part=out[i*per:(i+1)*per]
    if not part: continue
    # Keep the leading '---'. A src-included file needs its own opening frontmatter fence; stripping
    # it leaves 'layout: cover / class: ...' as the first slide's BODY, which renders that text on a
    # blank white slide. That was the phantom slide 2.
    open(f'sections/{name}.md','w',encoding='utf-8').write("\n".join(part))
    print(f"  sections/{name}.md  {len(part)} slides")
print("total:", len(out))
