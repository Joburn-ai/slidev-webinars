# SECTION BUILD CONTRACT — how to write each Slidev section file (READ FIRST)

You are building ONE section file of Brad Pounds' evergreen "60+ Programs" webinar deck. Follow this contract EXACTLY so all sections read as one deck. Your output is a finished Slidev markdown file written to the exact path you were given.

## Inputs you must read
1. `_SCRIPT.md` — the approved say-copy, per BEAT (O1-O7, T1-T18, Y1-Y3, F1-F7). Your speaker notes come from here VERBATIM. Do NOT rewrite the copy.
2. `_VISUAL_MAP.md` — the per-slide plan for your section (id · headline · tempo · emotion · VISUAL · treatment · animation · footer). Build EVERY row as one slide, in order.
3. This contract — format + brand classes + image inventory + rules.

## Golden rules (hard fails if broken)
- **One idea per slide. ≤7 visible words on any hook/headline.** The words on screen are sparse; the speaker notes carry the full sentence(s). Rapid-fire 400-slide-hack feel.
- **v-clicks on every list of 2+ items** — wrap in `<v-clicks>`. Each reveal = one spoken beat.
- **NO em-dashes anywhere. NO emoji anywhere** (use Iconify `<div class="i-mdi-NAME" />` or a text badge). NO markdown H1 `#` (use `<h1>`/`<h2>` inside divs or the layouts below).
- **NO fake clickable buttons** (Rule 11). CTAs = QR + visible URL + statement headline only.
- **Content must fit a 16:9 frame at every click** (Rule 9). Never stack more than ~5 vertical blocks. Cap inline headline size; prefer the classes below.
- **Every slide gets a strong visual** per its VISUAL cell — never a naked text slide (except the yes-momentum navy cards, which are deliberately image-free).
- **Speaker notes on EVERY slide**, in an HTML comment at the end of the slide body. Segment the beat's SAY copy across its slides at sentence boundaries so each slide's notes = what's said while it's on screen.
- **Compliance footer** on every slide whose visual-map `foot` cell is set (see footer snippet). Beat-specific disclaimers (replay-rate, 401k, soft-pull, FTC-not-typical, NMLS) are already written into the `_SCRIPT.md` compliance notes — put them on-slide where the script says.

## Per-slide anatomy (COPY THIS SHAPE)
The FIRST slide in your file starts with its own frontmatter block. Every later slide is separated by a lone `---` line, with per-slide frontmatter only if it needs a non-default layout/class/transition.

```
---
layout: cover
class: bp-slide
transition: slide-left
---

<!-- slide:te-14 -->

<div class="absolute inset-0">
  <img src="/images/concept/c21_many_doors.png" class="hbs-bleed" />
  <div class="hbs-scrim-b"></div>
</div>
<div class="absolute inset-0 flex flex-col justify-center px-20 z-10">
  <div class="hbs-stat hbs-stat-white">60+</div>
  <h2 class="text-white mt-2">Programs out there</h2>
</div>

<!--
T4 (AHA #1). SAY: With sixty-plus programs out there, the chances are high that you qualify, at least in part, for several of them...
-->
```

- Slide-id comment (`<!-- slide:ID -->`) goes AFTER the frontmatter close, as the first body line (Rule 4). Use the visual-map `id`.
- Use `layout: cover` on any slide whose root is `<div class="absolute inset-0 ...">` (Rule 8), so full-bleed works.
- Give hooks `v-motion :initial="{opacity:0,y:20}" :enter="{opacity:1,y:0}"` for a subtle enter where the map says "motion".

## Treatments → exact markup

**HERO-BLEED** (full-bleed image + text card):
```
---
layout: cover
---

<!-- slide:ID -->

<div class="absolute inset-0">
  <img src="/images/concept/cNN_slug.png" class="hbs-bleed" />
  <div class="hbs-scrim"></div>   <!-- left-dark scrim for left-aligned text; use hbs-scrim-b for bottom -->
</div>
<div class="absolute inset-0 flex flex-col justify-center px-20 z-10">
  <div class="hbs-eyebrow hbs-eyebrow-light">Eyebrow</div>
  <h1 class="text-white max-w-3xl">Headline in ≤7 words</h1>
</div>
```

**ORANGE-STATEMENT** (the brand shout):
```
---
layout: center
class: hbs-orange
---

<!-- slide:ID -->

<div class="flex flex-col items-center text-center px-16">
  <h1 class="text-white" style="font-size:3.6rem;">Some so easy you'll be <span class="hbs-accent">furious</span></h1>
</div>
```
(`.hbs-accent` = navy on orange. Use `<span v-mark="{ at: 1, color: '#0A3466', type: 'circle' }">word</span>` for a punch-mark.)

**NAVY-CARD** (deep-navy title card + ALL yes-momentum, image-free):
```
---
layout: center
class: hbs-navy
---

<!-- slide:ID -->

<div class="flex flex-col items-center text-center px-16">
  <h1 class="text-white">Feeling <span class="hbs-accent">less</span> concerned now?</h1>
</div>
```
(`.hbs-accent` on navy = orange.)

**STAT-HERO** (giant number/word): use `<div class="hbs-stat">60+</div>` (orange) or `hbs-stat hbs-stat-navy` / `hbs-stat-white`. One number, one sub-line `<h2>`.

**IMG-SIDE** (image half, copy half — alternate L/R across the section, never 3 same side in a row):
```
---
layout: default
---

<!-- slide:ID -->

<div class="grid grid-cols-2 gap-10 h-full items-center">
  <div>
    <div class="hbs-bar"></div>
    <h2>Headline</h2>
    <v-clicks><p class="hbs-lead mt-4">Point one.</p><p class="hbs-lead">Point two.</p></v-clicks>
  </div>
  <img src="/images/concept/cNN_slug.png" class="rounded-2xl w-full" />
</div>
```

**REVEAL-CARDS** (2-4 cards/chips revealed sequentially):
```
<div class="grid grid-cols-3 gap-6 mt-8">
  <v-clicks>
    <div class="hbs-card"><div class="i-mdi-book-open-variant hbs-icon" /><div class="hbs-card-title mt-2">The free book</div></div>
    <div class="hbs-card">...</div>
    <div class="hbs-card">...</div>
  </v-clicks>
</div>
```

**ZOOM** (one image big + annotation cards reveal beside it — the map te-49/50): image in a framed card (NOT stretched full-bleed if low-res), `<v-clicks>` reveal 2-3 small callout cards.

**DIVIDER** (section break, 1 slide): `class: hbs-divider`, big section title + an Iconify icon centered.

## Image inventory (use EXACT paths)
- **Concept images** (generated, on-brand): `/images/concept/cNN_slug.png` — all 53 exist (c01-c53). See `_VISUAL_MAP.md` for which slide uses which and what it depicts.
- **Brad's real assets**: `/images/brad/img-NNN.png`. Key ones: `img-019` Brad cutout (transparent) · `img-021` logo (white+red, ONLY on color/dark bg) · `img-004` Mack truck on orange · `img-005` magic-wand · `img-010` calm sunset · `img-034` family · `img-035` roofs on navy · `img-039` 5-icon FTHB row · `img-050` down-payment graphic · `img-054` income graphic · `img-056` credit graphic · `img-067` San Antonio map (low-res, frame native) · `img-068` 3-ingredient bar · `img-072` THE shaded 100%-financing map (low-res, frame native, do NOT stretch full-bleed) · `img-073` construction framing · `img-075` Equal Housing logo · `img-086` retirement photo · `img-090` suburban homes · `img-098` brush-cutout two men talking · `img-102` real SOLD client photo · `img-103` real congrats client photo.
- **NEVER** stretch a low-res asset (img-072/067) to full-bleed — put it in a centered `.hbs-card` at its native aspect.
- **NEVER** invent an image path not in this inventory. If the map says `html:` build it in HTML (below).

## HTML/CSS mocks (build in-slide, do NOT reference a file)
- **book_mock**: `<div class="hbs-book"><div class="t">The Texas First-Time Homebuyer Blueprint</div><div class="b">161 pages · $29.99 on Amazon</div></div>`
- **list_mock**: `<div class="hbs-doc"><div class="h">60+</div><div class="hbs-quiet" style="font-size:0.8rem;">Texas programs</div><div class="rows"><i/><i/><i/><i/><i/></div></div>`
- **program chips** (te-39): `<div class="hbs-chip">My First Texas Home</div>` etc, wrapped in `<v-clicks>`.
- **rule ladder** (te-29): `<div class="hbs-rule"><div class="step">620</div><div class="i-mdi-arrow-right hbs-icon-navy" /><div class="step">640</div></div>`
- **qr_card** (cl-02): render a QR to `https://homebuyerschool.com/book`. Use `<img src="/images/qr/book.png" class="w-48" />` inside `<div class="hbs-qr-card">` — the QR PNG is generated separately and will exist at build; also show `<div class="hbs-url">homebuyerschool.com/book</div>` below it.

## Compliance footer snippet (add when visual-map `foot` is set)
```
<div class="hbs-foot hbs-fineprint">Educational purposes only, not a commitment to lend. Rates, limits, and program terms change and vary by lender, borrower, area, and market. Equal Housing Opportunity.</div>
```
On dark slides add class `hbs-fineprint-light`. Verbatim NMLS block (op-21 + cl-02): *"Bradley Pounds, Mortgage Loan Originator NMLS #2731896. Licensed through Rapid Mortgage, LLC NMLS #2425173. HomeBuyerSchool.com is a separate licensed real estate brokerage and not a mortgage lender. All loans subject to credit approval and program guidelines. Equal Housing Lender."*

## Output
Write your finished file to the exact path given in your task. It must be valid Slidev markdown: correct frontmatter, one `---` between slides, slide-id + speaker-notes on every slide, brand classes only, zero em-dashes, zero emoji. Return a one-line summary (slide count + any `[JOHN]` items you left as TODO) — the file itself is the deliverable.
