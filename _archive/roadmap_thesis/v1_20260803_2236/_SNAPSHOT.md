# SNAPSHOT -- Roadmap Thesis deck, v1

**Taken:** 2026-08-03 22:36 UTC · **live at:** https://roadmap-thesis.vercel.app
**slidev-webinars commit:** 8b8fa4d

## Why this snapshot exists

John, 2026-08-03: *"save this as a backup copy somewhere as a decent example of a deck
that would do quite well... I want to save kind of our record of this over time because
this one's not bad."*

**This is the reference point.** Later versions get compared against it, and if a rebuild
goes backwards this is what we return to. **Do not edit anything in this folder.** Work on
`internal/roadmap_thesis_2026_08_03/` and take a new snapshot when a version is worth
keeping.

## What v1 is

| | |
|---|---|
| **Slides** | 145 |
| **Source** | `_SCRIPT.md`, John's Thesis draft, 16 sections |
| **Built by** | 5 parallel section agents against `_BUILD_SPEC.md`, then per-file QC |
| **Ground** | white, with a 4-slide dark peak budget |
| **Runtime target** | 24-32 min before tightening |

## Verified working at snapshot time

- production rolldown build passes, 5.3s
- 145 slides render
- **8/8 toolbar icons visible** (fixed in this commit: they had valid masks on 0x0 transparent boxes)
- no tofu, no element below the slide bottom on the slides checked
- deep links serve HTML, hashed assets serve their own bytes
- `/flows/01_restart_loop.png` loads, used on 3 slides

## Known open at snapshot time

- 🔴 **inline mermaid renders an empty `<div class="mermaid">`** on all 16 diagram slides.
  Source validates against the mermaid CLI, mermaid 11.15.0 is bundled, no console errors,
  no failed requests. **The CLI-rendered PNG path works and is what John reviewed and
  liked**, so the resolution is to pre-render diagrams as images.
- coherence critic never finished, so no `_QC_REPORT.md` and no consolidated review list
- John is still to supply: imagery and symbolism, transition and copy improvements,
  the funnel flowchart and architecture, verbatim tongue-in-cheek language from a Loom,
  animations and pop-ups
