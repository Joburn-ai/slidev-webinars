# Roadmap VSL -- deck scaffold

**Waiting on John's finalised script.** Everything here is deliberately structure-independent,
so no beat ordering can invalidate it.

| Piece | State |
|---|---|
| `style.css` | thesis-deck theme, per John: *"same theme as the thesis deck, just to keep everything the same"* |
| `vite.config.ts` | Rule 18 fs.allow, or the Vercel production build fails |
| `diagrams/*.mmd` | the ONE diagram v2 calls for, in two states |
| `public/flows/*.svg` | rendered via the mermaid CLI. **Not inline mermaid** |

## The diagram, and why it is two files not one

Beat 8 of `TEMPLATE_roadmap_vsl_v2_2026_08_05.md`: *"Other people hand you one piece of the
puzzle. This gives you the picture, the pieces, and the order to put them in."*

- **`01a_pieces_disconnected`** -- four boxes, horizontal, **nothing joining them.** The absence
  IS the argument.
- **`01b_pieces_connected`** -- ember WHERE YOU ARE, the same four pieces **on the path in
  order**, teal WHERE YOU WANT TO GO.

🔴 **`~~~` (invisible link) is load-bearing in 01a.** With no edges at all, dagre has no
horizontal signal and stacks the nodes into a 186x530 vertical column. The invisible link gives
layout without drawing a line.

## Render command

```bash
cd diagrams
echo '{"args":["--no-sandbox","--disable-setuid-sandbox"]}' > pc.json   # or the browser launch fails
mmdc -i 01a_pieces_disconnected.mmd -o ../public/flows/01a_pieces_disconnected.svg -b white -p pc.json
```

## 🔴 Both states were rendered to PNG and LOOKED AT before this was committed

Per the INVISIBLE-RENDER LAW. A DOM assertion cannot see a vertical stack where a horizontal row
was intended, and that is exactly the defect the first render had.

**Aspect: 9.78:1 and 11.50:1.** Both are full-bleed horizontal bands by design, with the headline
above. **We own the viewBox now, so the ratio is ours to change if a band is wrong.**

---

## 🔴 DEPLOY TRAP: `slidev build` deletes `dist/.vercel`

`slidev build --out dist` **recreates the directory**, which wipes the Vercel project link inside
it. Deploying after a rebuild therefore creates a **brand new project named after the folder** --
this happened once and produced a stray `dist-*.vercel.app` project.

**The fix, every time after a build:**

```bash
cd dist
npx vercel link --yes --project roadmap-vsl --token "$VERCEL_TOKEN"
npx vercel deploy --prod --yes --token "$VERCEL_TOKEN"
```

A copy of the link lives at `../.vercel-link` for reference.

**Live: https://roadmap-vsl.vercel.app**

## Verified on the live deploy, not asserted

- **30 slides**, all render
- **all 30 checked for frame overflow: zero.** Slide 2 failed this first time round (the proof
  band pushed the closing line past the bottom edge) and the band was re-cropped 2.6:1 -> 4.0:1
- **all 3 images confirmed painted** (`complete && naturalWidth > 0`), not merely present in the DOM
- **42 wins is VERIFIED**: the wall container on `funnelfuturist.com/proof` has exactly 42 children
  and the page prints "42 -- WINS ON THE WALL BELOW"

---

## 🔴 NEXT: the roadmap-funnel flow (John, 2026-08-06)

**Requirement:** *"a mermaid + UI mockup flow of the roadmap funnel and how it works, in the deck too."*

**Two artefacts, one beat.** They do different jobs and both are needed:

| | What it shows | Why |
|---|---|---|
| **The mermaid flow** | the **logic**: entry -> form -> roadmap built -> discovery call -> the three doors | the shape of the thing, abstract and fast to read |
| **The UI mockup** | the **actual screens** they will touch: the form, the roadmap page, the calendar | 🔴 **removes the imagination tax.** *"Seeing is believing"* -- they stop picturing it and start recognising it |

**Where it goes:** after **rv-38 (the three steps)**, before the risk reversal. That beat currently
*describes* the process in three cards and never shows it. **The flow is the proof the process exists.**

**Build notes:**
- **Render to SVG via the mermaid CLI, not inline.** Inline renders an empty div. Pipeline is proven twice in this deck
- **Node grammar stays:** gold rhombus = decision · grey rect = process · teal = terminal win · ember hex = restart · teal forward edges
- **UI mockups from REAL screens**, screenshotted: the live roadmap form, `funnelfuturist.com/proof`, the GHL calendar embed. **Not wireframes** -- a wireframe reintroduces the imagination tax it exists to remove
- **Reveal per band, accumulating**, so the funnel assembles while he talks it

## Assets pulled 2026-08-06

| Folder | Count | Source |
|---|---|---|
| `public/proof2/` | **66** | Phoenix's Drive proof folder. 69 downloaded, 3 lost to slug collisions |
| `public/stage/` | **7** | 4 Drive posters + **3 real ffmpeg frames from the C&C LIVE talk** |
| `public/wins/` | 12 | ff-site originals |
| `public/proof/` | 1 | the wall density band |

🔴 **The Drive video "thumbnails" are FIRST FRAMES and one showed a completely different speaker on
the C&C stage.** Do not use a Drive poster as a stage shot without looking at it. **Real frames come
from ffmpeg seeking over the Drive media URL with an Authorization header** -- no full download needed:

```bash
ffmpeg -headers "Authorization: Bearer $TOK"$'\r\n' -ss 600 -i \
  "https://www.googleapis.com/drive/v3/files/<ID>?alt=media&supportsAllDrives=true" \
  -frames:v 1 -q:v 2 out.jpg
```

**The best frame in the estate: `stage/cc_live_600s.jpg`.** John on the Clients & Community LIVE
stage teaching the customer bow-tie. **C&C is Case File 002**, so the frame proves he is invited on
stage by the client whose $1.81M we produced, to teach the thing we sell. **Three claims, none stated.**
Placement recommendation: **rv-39, the trust beat.** Not the opening -- it is the wrong flex before
attention is earned.
