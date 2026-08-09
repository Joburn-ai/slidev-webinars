# Roadmap VSL v7 -- build + deploy

**v7 is the final deck.** `slides_v7.md` + `style_v7.css`.
`style.css` is already a copy of `style_v7.css` (Slidev only auto-loads `style.css`).
The pre-v7 stylesheet is kept at `style.css.pre_v7.bak`.

```bash
cd /root/slidev-webinars
cp internal/roadmap_vsl_2026_08_05/style_v7.css internal/roadmap_vsl_2026_08_05/style.css
npx slidev build internal/roadmap_vsl_2026_08_05/slides_v7.md --base / --out dist-rv7
cp internal/roadmap_vsl_2026_08_05/vercel.json internal/roadmap_vsl_2026_08_05/dist-rv7/
cd internal/roadmap_vsl_2026_08_05/dist-rv7
npx vercel --prod --yes --token "$VERCEL_TOKEN" --scope team_AcbqD1MAg7WOqx4lMqGSZXoa
```

## The QC gate that has to pass before every deploy

64 slides, every click state, bounding boxes against the slide box. Slidev's slide
container is `overflow: hidden`, so overflowing text is **clipped, not scrolled** --
`scrollWidth` never exceeds `clientWidth` and a naive sweep passes on a broken slide.

```js
const slide = [...document.querySelectorAll('.slidev-layout')]
  .find(e => e.offsetParent !== null && e.getBoundingClientRect().width > 100);
const s = slide.getBoundingClientRect();
const over = [...slide.querySelectorAll('*')].filter(e => {
  if (e.offsetParent === null) return false;
  if (getComputedStyle(e).position === 'fixed') return false;
  const r = e.getBoundingClientRect();
  if (r.width === 0 || r.height === 0) return false;
  if (e.tagName === 'IMG' && e.closest('.rt-band')) return false; // deliberate crop
  return r.right > s.right + 1 || r.bottom > s.bottom + 1 ||
         r.left  < s.left  - 1 || r.top    < s.top    - 1;
});
// over.length must be 0, at EVERY click state, then LOOK at the screenshots.
```

Walk click states by pressing Space until `.slidev-vclick-hidden` count hits 0.
`?clicks=N` on the URL does **not** set the click index in a built deck, so a sweep that
uses it silently tests click 0 on all 64 slides and reports clean.

## Four things that were only visible in the render

1. `/flows/02b_funnel_the_call.svg` contains a node reading **"We install the Roadmap
   Funnel"**. That phrase is banned in this asset. Grep SVG node text, not just filenames:
   `grep -o '<p>[^<]*</p>' public/flows/*.svg`.
2. `site/ff-*--hero.png` and `stage/john-coburn-our-system-*.jpg` all render revenue
   figures legibly. Zero income claims means zero, including numbers in the background
   of a photograph. `.rt-band.crest` exists to crop above them.
3. `.rt-split` is `height: 100%`; under a headline it computes past the bottom edge.
   Use `.rt-split.auto` whenever a split is not the only child.
4. `v-mark` renders only at its `at:` click. It is invisible at click 0, which is exactly
   what a broken directive also looks like. Advance one click before judging it.
