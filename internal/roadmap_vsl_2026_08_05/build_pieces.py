#!/usr/bin/env python3
"""
PIECES — disconnected vs connected, on brand.

WHY THIS EXISTS
`01a_pieces_disconnected.svg` and `01b_pieces_connected.svg` were RAW MERMAID EXPORTS used on
7 slides between them. Inspected 2026-08-11, they carried:
  background-color: white     -> a white letterbox strip on a cream (#FAF6EA) deck
  font-family: trebuchet ms   -> foreign typography next to Inter
  fill: #333                  -> a grey that is not in the FF palette
  viewBox 684 x 70            -> a 9.8:1 sliver rendering at ~1.7% of the frame
That is what "inserted in a strange way" looks like, and no assertion catches it because the
file is a perfectly valid SVG.

🔴 AND THEY WERE LABELLED, WHICH MADE IT WORSE.
The mermaid version printed "A course / A tool / An agency / A hire" directly beneath slide
copy that said "Bought the course / Hired the agency / Ran the ads / Still stuck" -- the same
list, in a second visual language, with different words. It invented "A tool" and "A hire" and
dropped "ads".

**So this version carries NO TEXT AT ALL.** The slide owns the words; the diagram owns the
shape. That is also what lets one asset serve all four beats without ever contradicting the
copy above it.

Usage:  python3 build_pieces.py
"""

import pathlib

VOID, TEAL, TEALB = "#0A2230", "#209080", "#2BB3A0"
STAR, EMBER, FOG = "#FAF6EA", "#C4552F", "#7A9199"

W, H = 1600, 560
CY = H / 2


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(connected: bool, out_name: str):
    """Four blocks. Disconnected = scattered and unjoined. Connected = one line through them."""
    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'font-family="Inter, ui-sans-serif, system-ui, sans-serif">')
    a(f'<rect width="{W}" height="{H}" fill="{STAR}"/>')

    # 🔴 THE BLOCKS ARE DELIBERATELY MISMATCHED IN THE DISCONNECTED STATE, and that is a
    # correction to my own first pass. I stripped the mermaid version's labels (right: they
    # contradicted the slide copy) but left four IDENTICAL EMPTY BOXES -- which say nothing at
    # all, on five slides where they are the only visual carrying "you got a piece, not a plan".
    # The review called them blank white rectangles and it was correct.
    # Fix: make the SHAPES carry the meaning. Different widths, heights, angles and heights off
    # the baseline read as "assorted things that do not fit together" WITHOUT any text to
    # contradict the slide. Connected state: uniform, aligned, one line through them.
    if connected:
        sizes = [(250, 132)] * 4
        xs    = [140, 500, 860, 1220]
        dy    = [0, 0, 0, 0]
        rot   = [0, 0, 0, 0]
    else:
        sizes = [(210, 108), (286, 156), (168, 92), (250, 130)]
        xs    = [128, 452, 856, 1132]
        dy    = [-62, 44, -34, 66]
        rot   = [-5.5, 4.0, -3.0, 5.0]

    if connected:
        # One continuous line THROUGH the blocks, drawn first so the blocks sit on it.
        a(f'<line x1="{xs[0]+sizes[0][0]/2:.0f}" y1="{CY:.0f}" x2="{xs[-1]+sizes[-1][0]/2:.0f}" y2="{CY:.0f}" '
          f'stroke="{TEAL}" stroke-width="10" stroke-linecap="round"/>')
        for i in range(len(xs) - 1):
            mx = (xs[i] + sizes[i][0] + xs[i + 1]) / 2
            a(f'<path d="M {mx-16:.0f} {CY-13:.0f} L {mx+12:.0f} {CY:.0f} L {mx-16:.0f} {CY+13:.0f}" '
              f'fill="none" stroke="{TEAL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')

    for i, x in enumerate(xs):
        bw, bh = sizes[i]
        y = CY - bh / 2 + dy[i]
        fill = "#DFF1ED" if connected else "#FFFFFF"
        stroke = TEAL if connected else FOG
        sw = 3 if connected else 2
        a(f'<g transform="rotate({rot[i]} {x+bw/2:.0f} {y+bh/2:.0f})">'
          f'<rect x="{x}" y="{y:.0f}" width="{bw}" height="{bh}" rx="12" '
          f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/></g>')

    if not connected:
        # The absence IS the message: severed stubs where the joins should be.
        for i in range(len(xs) - 1):
            mx = (xs[i] + sizes[i][0] + xs[i + 1]) / 2
            ya = CY + dy[i]
            yb = CY + dy[i + 1]
            a(f'<line x1="{mx-46:.0f}" y1="{ya:.0f}" x2="{mx-20:.0f}" y2="{ya:.0f}" '
              f'stroke="{EMBER}" stroke-width="5" stroke-linecap="round" opacity="0.85"/>')
            a(f'<line x1="{mx+20:.0f}" y1="{yb:.0f}" x2="{mx+46:.0f}" y2="{yb:.0f}" '
              f'stroke="{EMBER}" stroke-width="5" stroke-linecap="round" opacity="0.85"/>')

    a('</svg>')
    out = pathlib.Path(__file__).parent / "public" / "flows" / out_name
    out.write_text("\n".join(p))
    return out


if __name__ == "__main__":
    for connected, name in [(False, "01a_pieces_disconnected.svg"),
                            (True, "01b_pieces_connected.svg")]:
        f = build(connected, name)
        print(f"wrote {f.name} ({f.stat().st_size} bytes)")
