# SKETCH -- the training-deck aesthetic, as markup

**The look John asked for: behind-the-scenes, polished but not produced. Stick figures and cheap fast drawings that make a point land, in the Josh Gavin / Alen style.**

**This proves it is producible without an art step.** `node _sketch/build.mjs` turns declarative diagram specs into seeded SVG. A diagram is markup we diff and regenerate, not art we redraw.

Proof of concept: `out/impulse_intention.png`, recreated from the reference John shared. It was chosen because it exercises every primitive at once -- two figure poses, eight icons, rough boxes, straight and curved arrows, dashed panel dividers, a strike-through and a checkmark.

---

## The one rule that makes this work

> **Sketch the drawings. Typeset the words. Never a handwriting font.**

Look closely at the reference and the text is clean bold caps while only the *drawings* are hand-drawn. **That hybrid is why it reads as fast-but-legible instead of messy.** Sketch the type too and it stops being a diagram and starts being a napkin.

## The other four

| Rule | Why |
|---|---|
| **Roughness 1.4-1.9** | Below 1.4 reads as a bad vector; above 2.5 reads as broken |
| **Seeds are fixed, never random** | Output is byte-stable, so a rebuild produces no diff. Change a seed only to re-roll a shape you dislike |
| **Black ink on white paper** | The reference has no colour and does not need any. One accent, if ever, on the single thing being pointed at |
| **A frame makes it a panel** | Without the outer border, marks float. With it, the diagram reads as a deliberate exhibit |

---

## Writing a diagram

Drop a file in `diagrams/`. Export `name` and `render()`.

```js
import { svg, rect, arrow, text, figure, icon } from "../sketch.mjs";

export const name = "my_diagram";
export const render = () => {
  let s = "";
  s += text(600, 70, "The point being made", { size: 38, weight: 900, caps: true });
  s += figure(200, 400, 165, "walk-phone");
  s += rect(345, 235, 160, 72);
  s += text(425, 281, "$17-$27", { size: 27 });
  s += arrow(425, 318, 425, 360);
  s += icon.clock(95, 440, 38);
  return svg(1200, 990, s);
};
```

Then `node _sketch/build.mjs`. SVG lands in `out/`.

## What exists

**Primitives:** `rect` · `circle` · `line` · `poly` · `curve` · `dashed` · `arrow` (straight, or `{curved: n}`) · `text` · `lines` · `underline` · `crossout`

**Figures:** `figure(x, y, height, pose)` where pose is `stand` · `walk-phone` · `sit-think`, plus `desk()`

**Icons:** `envelope` · `video` · `speech` · `stairs` · `clock` · `bolt` · `money` · `target` · `handshake` · `check` · `cash`

**Two geometry notes learned the hard way, both visible in the first render:**
- **`walk-phone` must keep the phone clear of the head.** An arm across the face reads as a broken figure, not a distracted one, which defeats the pose.
- **`sit-think` draws no legs on purpose.** The desk occludes them in the reference; drawing them makes the figure look like it is sitting *on* the table.

## Getting it into a deck

Two ways, and the first is better for anything reused:

1. **Static SVG.** Build it, then `![](/sketch/name.svg)` or inline it. Deterministic, no runtime cost, survives every export path.
2. **Excalidraw** via `slidev-addon-excalidraw`, already a dependency. Right choice when John wants to draw one by hand rather than spec it.

## Rasterising

No `rsvg-convert` or `inkscape` on this box. Use the playwright chromium that is already installed:

```bash
python3 -c "
from playwright.sync_api import sync_playwright
import pathlib
out=pathlib.Path('_sketch/out'); h=out/'_view.html'
h.write_text('<style>html,body{margin:0;padding:0}</style>'+(out/'NAME.svg').read_text())
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox']); pg=b.new_page(viewport={'width':1200,'height':990})
    pg.goto('file://'+str(h),wait_until='load'); pg.screenshot(path=str(out/'NAME.png')); b.close()"
```

## Open

**The icon set is eleven glyphs deep because that is what the proof diagram needed.** It grows on demand rather than up front -- a speculative icon library is a good way to spend a day and produce nothing anyone uses.

**Waiting on John's further reference examples** before committing to a wider set of figure poses.
