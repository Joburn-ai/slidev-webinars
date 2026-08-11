# Roadmap VSL v8 -- the SCREEN-SHARE deck

**v8 supersedes v7 and absorbs `slides_broll.md`.** John, 2026-08-11: the deck IS the asset
again, recorded as a screen share in the indirect-training register.

`slides_v8.md` + `style.css` (v7 system + the v8 extension appended at the bottom).
Pre-v8 stylesheet preserved at `style.css.pre_v8.bak`.

```bash
cd /root/slidev-webinars
npx slidev build internal/roadmap_vsl_2026_08_05/slides_v8.md --base / --out dist-rv8
cp internal/roadmap_vsl_2026_08_05/vercel.json internal/roadmap_vsl_2026_08_05/dist-rv8/
cd internal/roadmap_vsl_2026_08_05/dist-rv8
npx vercel --prod --yes --token "$VERCEL_TOKEN" --scope team_AcbqD1MAg7WOqx4lMqGSZXoa
```

## Recording it

Press **P** for presenter mode. **Every spoken word is in the notes**, on the slide it belongs
to, in order. Read the notes; the visible slide only ever carries the short form.

106 slides (slide 00 is a holding frame, never recorded) + 38 v-clicks = 144 interactions.
Six slides carry a 🟡 `>>> JOHN <<<` decision in their notes: 79 (time the form), 92 (the
deliverables list), 95 (say the capacity number or not).

## The QC gate -- run it before every deploy

Slidev's slide container is `overflow: hidden`, so overflowing content is **clipped, not
scrolled** and `scrollWidth` never exceeds `clientWidth`. A naive sweep passes on a broken
slide. The sweep that actually works walks every slide AND every click state and compares
bounding boxes against the slide box. It found 24 overflow states on the first pass of v8,
all of them invisible in the markup.

Serve the build with SPA fallback first -- `python3 -m http.server` 404s on `/40` and the
sweep will report "no slide" for all 106 frames.

## Three failure modes v8 added to the list

1. **A variable font declared as fixed weights renders at its DEFAULT instance.** Google
   serves Space Grotesk and Work Sans as single variable files (identical md5 across the
   400/500/600/700 URLs). Space Grotesk's variable default is **300**, so six fixed-weight
   `@font-face` rules would have rendered every headline THIN while the CSS said 700. Each
   variable family gets ONE face with a weight RANGE. Verify with `fontTools` fvar, not by
   eye.
2. **`height: 100%` under a headline is the same bug as `.rt-split`.** `.rt-plate` had it.
   Capping the image height fixed nothing because the DIV itself still computed to
   (headline + 100%). Anything `height: 100%` that is not the only child needs `height: auto`.
3. **Not every asset on disk is light-grounded.** All 17 `public/gen8/*.png` and 7 of 9
   `public/gen/concept-*.png` are dark navy. Measure corner luminance before deciding a page
   ground; the v8 plan's premise that "every image on disk is light-grounded" was false and
   would have put 40 dark rectangles on a cream page.

## Asset edits made on 2026-08-11 (permanent, in `public/`)

- `flows/bowtie_0*.svg` -- baked `font-family` retargeted from Inter to Space Grotesk; the
  em-dash in `bowtie_03_team.svg` replaced with `--`.
- `flows/02a_*.svg`, `02b_*.svg` -- "24 to 48 hrs" -> "48 hrs at the latest" (John, 08-09).
- `flows/03_bowtie_overlay.svg` -- the banned phrase "roadmap funnel" removed from its
  aria-label (it was never in visible text).
- `proof2/meet-dr-joe-portrait.png` -- NEW. The left 40% of `meet-dr-joe-jan-2026.png`. The
  original renders "$6.2M in college tuition" legibly. **Do not swap the original back in.**
- `public/fonts/` -- NEW. Space Grotesk + Work Sans variable, Space Mono static, latin subset.

## Verified state, 2026-08-11

| | |
|---|---|
| Content slides | **105** (+ slide 00, a holding frame never recorded) |
| Slides carrying a real image file | **92 = 87.6%** |
| v-clicks | **38** (144 total interactions) |
| Average visible words per slide | **16.7** |
| Overflow states across every slide AND every click | **0** |
| Fonts actually applied in the render | Space Grotesk 700 (display) + Space Mono 700 (labels) |
| Backgrounds in the render | star `#FAF6EA` x183 states, void `#0A2230` x27 |
| Peak slides | **10** (the budget, exactly) |
| v-mark | **5** &middot; v-motion **3** &middot; `transition: fade` **12** (both bowtie runs + the two futures) |
| Console errors | 0 real (headless Wake Lock warnings only) |
