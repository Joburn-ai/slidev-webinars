# Portal Onboarding Ramp — Slidev Course

The `/learn` ramp inside `portal.joburn.com`, produced with Slidev + the companion-guide pattern. Reuses the toolkit proven in `_demo/unit_economics_bowtie_2026_05_27/` (v-motion, v-mark, Magic Move, Excalidraw, reactive widgets, FF palette).

## The workflow (script-first, per video)

1. **Script first** — one script per lesson (or per section), written in John's voice. Source of truth. Lives in `ai-os/06_Clients/joburn_internal/02_growth_starter_launch/scripts/`.
2. **Slides from script** — build the Slidev deck for conceptual lessons here, copying a sibling deck as the template. How-to lessons are screen recordings instead (no deck).
3. **Run through it** — `pnpm slidev module_NN_*/lesson.md` → present in browser → record (Slidev's built-in camera + 2-file recording, no OBS).
4. **Companion guide** — same script → FF-branded DOCX (`ff_doc_branding.js`, never pandoc) → upload to Drive as a Google Doc. One per module.
5. **Wire it** — drop the recording's Cloudinary URL into `joburn.lessons.video_url`, the doc link into `doc_url`. Portal serves it automatically.

> Decks are the **recording vehicle**, not the deliverable. Learners get the video + the companion doc. So decks don't need hosting — John runs them locally to record. (Optional later: build a self-paced SPA.)

## "Draw without drawing" (the programmatic annotation toolkit)

Everything that looks hand-drawn is scripted and repeatable, so a re-record looks identical:
- **`v-mark`** (rough-notation) — `.circle` `.underline` `.box` `.highlight` `.strike-through` `.crossed-off`, with colors, triggered per click. This is the programmatic circle/underline.
- **`<Arrow>` / `slidev-addon-fancy-arrow`** — hand-drawn annotation arrows.
- **`v-click` / `v-clicks`** — reveal a diagram piece by piece.
- **`v-motion`** — pieces fly into place on each click.
- **Mermaid** — flowcharts/funnels that build click-by-click.
- **Excalidraw** addon — crisp hand-sketched diagrams from a `.excalidraw` file.
- **Pen layer** (`drawings: { persist: true }`) — live freehand on camera when you want it.
Full ref: `copy-brain/06_Webinars/sop/ref_slidev_interactive_workshop_capabilities_2026_05_27.md`.

## Course index

| Module | Lesson | Type | Script | Deck | Recorded | Companion | Wired |
|---|---|---|---|---|---|---|---|
| 1 Start Here | 1.1 Welcome | Slidev | ✅ | ☐ | ☐ | ☐ | ☐ |
| 1 | 1.3 7-day path | Slidev | ✅ | ☐ | ☐ | ☐ | ☐ |
| 1 | 1.4 Operator-Owner | Slidev | ✅ | ☐ | ☐ | ☐ | ☐ |
| 1 | **1.5 Priority Lever** | Slidev | ✅ | ✅ (template) | ☐ | ☐ | ☐ |
| 1 | 1.6–1.9 how-to | Screen-record | ✅ | n/a | ☐ | ☐ | ☐ |
| 1 | 1.10 Ground Rules | Checkpoint | ✅ | n/a | n/a | ☐ | ☐ |
| 2 Foundations Light | 2.1–2.7 | Slidev | ☐ | ☐ | ☐ | ☐ | ☐ |
| 3 Operating Cadence | 3.1–3.6 | mixed | ☐ | ☐ | ☐ | ☐ | ☐ |
| 5 Credit + Unlock | 5.1–5.3 | mixed | ☐ | ☐ | ☐ | ☐ | ☐ |

## Structure

```
_courses/portal_onboarding/
  README.md                       ← this index
  module_01_start_here/
    style.css                     ← FF palette, shared by all decks in the module
    1_5_priority_lever.md         ← flagship template deck
    public/                       ← images / .excalidraw files
  module_02_foundations_light/
  ...
```

Build rules (skill Rules 7–12): co-located unscoped `style.css`, `colorSchema: light` pinned, every slide CONTENT-FITS-FRAME (no overflow — eyeball every slide post-build with clicks advanced), no nav buttons, never pandoc for companions.
