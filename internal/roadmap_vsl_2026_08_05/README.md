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
