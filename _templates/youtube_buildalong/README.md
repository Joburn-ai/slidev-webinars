# Joburn YouTube Build-Along · Format Spec

> **The template that builds the series.** Slidev deck + OBS scene config + drawing-surface policy. Refill in 90 minutes per episode. Format stays recognizable so the brand compounds.

## Files

| File | Purpose |
|---|---|
| `episode_template.md` | Blank 6-slot template. Copy to `episodes/episode_NN_topic.md`, refill the slots, ship. |
| `episode_01_build_the_template.md` | The meta-episode 1 script. Builds the format on camera. |
| `style.css` | Joburn atomic-era retro-futurist CSS. Inherits `ff-*` palette + adds YouTube-format classes (section tags, step counters, code frames, whiteboard scene, fig captions). |
| `assets/` | Per-episode images, diagrams, screenshots. Sub-folder per episode. |

## The 6-slot format

| # | Slot | Duration | OBS scene | Job |
|---|---|---|---|---|
| 1 | Hook | 5-10s | A (slides + cam corner) | Curiosity gap. Promise. No "hey guys." |
| 2 | Topic | 20-30s | B (slides + large cam) | What they'll have at the end. Expectation set. |
| 3 | Build Phase 1 | 4-7min | A | Code-along, steps 1-3 of N. Monaco editable. |
| 4 | Whiteboard | 2-4min | C (iPad fullscreen) OR drauu in place | Zoom out. Diagram the concept. |
| 5 | Build Phase 2 | 5-8min | A | Code-along, steps 4-N. Magic Move for state morphs. |
| 6 | Recap + CTA | 30-45s | D (cam only) | Three bullets. One CTA: subscribe. Tease next episode. |

**Total runtime:** 14-22 min. Sweet spot for build-along on YouTube. Long enough to deliver. Short enough to finish.

## OBS scene config

Four scenes. Bind once. Stop fiddling.

| Scene | Hotkey | What's on it |
|---|---|---|
| **A · Slides + Cam Corner** | `Cmd+1` | Browser source (Slidev fullscreen 1920×1080), webcam bottom-right ~320×180. **Default. Lean back here between slots.** |
| **B · Slides + Large Cam** | `Cmd+2` | Browser source center, webcam ~640×360 on the right. Slot 2 only. Talking-head expectation-set energy. |
| **C · Whiteboard Fullscreen** | `Cmd+3` | iPad via Sidecar OR a second browser window with tldraw, fullscreen. Webcam tiny corner. **Slot 4 only when whiteboard is the work.** Skip this scene when drauu suffices. |
| **D · Cam Only** | `Cmd+4` | Webcam fullscreen 1920×1080. Slot 6 only. Sign-off intimacy. Hold the final beat 2 full seconds before cutting. |

**Capture settings:** 1920×1080 @ 60fps, x264 CRF 18, AAC 192kbps. 2560×1440 if your machine handles it. Audio: dedicated USB mic, denoise filter ON, gain calibrated so peaks hit -6dB on the meter.

## Drawing-surface policy

> Pick the surface ONCE. Stop relitigating mid-recording.

| Need | Surface | When |
|---|---|---|
| Quick annotation on what's already on screen (arrow, circle, underline) | **drauu (Slidev built-in)** | Default for slot 4. Press pen icon. SVG persists per slide via `drawings: persist: true`. |
| Persistent diagram that survives between recordings | **`slidev-addon-tldraw`** | When the diagram is the asset and you want it in `public/tldraw/*.json` for reuse. 800×800 visible area cap. |
| From-scratch ideation, sustained whiteboard teaching | **iPad + Apple Pencil + Sidecar + tldraw web** | When you need to step away from the slide entirely. Hotkey OBS Scene C. Pressure-sensitive. |

**Joburn default policy (locked):** drauu in slot 4 unless the whiteboard moment justifies the iPad scene switch. Use the iPad sparingly so it stays special.

## Master template usage

1. Copy `episode_template.md` to `episodes/episode_NN_topic.md` (snake_case the topic).
2. Fill the bracketed placeholders in each slot. Keep the slot order. Don't add a 7th.
3. Replace `EP NN` everywhere with the actual episode number.
4. Update the `info:` frontmatter block.
5. Run `npx slidev episodes/episode_NN_topic.md` from the repo root.
6. Open OBS. Confirm Scene A is selected.
7. Record.

## Production checklist (before pressing record)

- [ ] Slidev running fullscreen in Chromium (not Safari, not Firefox; Chromium for Monaco editor reliability)
- [ ] OBS Scene A selected. Other scenes confirmed via hotkeys.
- [ ] Audio meter peaking -6 to -12dB on loud syllables
- [ ] Webcam framed: chest up, eyes one-third from top, room background clean
- [ ] Notifications silenced (system + Slack + iMessage)
- [ ] Phone face-down
- [ ] Glass of water in frame
- [ ] Open the deck to slot 1. Take three breaths. Press record.

## Post-production

| Tool | Job |
|---|---|
| **OBS** | Captures raw `.mkv` to `~/Movies/joburn-buildalong/raw/`. |
| **Descript** | Edit: trim long pauses, kill ums, polish audio. Export `.mp4` 1080p @ 60fps. |
| **Thumbnail** | Cinema 4:3 ratio crop of slot 1 hook with episode number + topic. Atomic-era aesthetic (cream bg, navy headline, gold accent, tiny mono caption). |
| **Upload** | YouTube. Title = "Episode NN · [Topic] (Joburn Build-Along)". First sentence of description quotes the hook headline verbatim. |

## What stays the same every episode

- Joburn atomic-era retro-futurist aesthetic (cream / navy / teal / gold)
- 6-slot order (Hook · Topic · Build 1 · Whiteboard · Build 2 · Recap)
- OBS scene-to-slot map
- Drawing-surface policy
- Recap pattern: "You just built [artifact]" → 3-4 bullets → next episode tease → subscribe CTA

## What changes every episode

- Topic
- Code in slots 3 + 5
- Diagram in slot 4
- Three recap bullets

## Cross-references

- `00_Foundations/ref_visual_style_guide.md` · base Slidev style discipline
- Memory: `feedback_joburn_visual_aesthetic_atomic_retro_futurist_2026_05_29.md` · full aesthetic spec
- Memory: `reference_slidev_youtube_buildalong_workflow_2026_05_29.md` · the research that shaped this template
- `/root/slidev-webinars/_courses/portal_onboarding/` · parallel deck family (client-facing, same palette)

## Hardware status (as of 2026-05-31)

| Item | Status | Notes |
|---|---|---|
| OBS Studio | ✅ Installed | Per John 2026-05-31 |
| Webcam + mic | ⏳ Confirm before EP01 | Audio quality is the single biggest channel killer |
| iPad + Apple Pencil | ⏳ Confirm | Required only for Scene C (sustained whiteboard). drauu carries the format without it. |
| Sidecar | ⏳ Confirm | Free with macOS, only needed if iPad path goes live |

**Episode 1 can ship on Scene A + Scene D alone if iPad isn't ready.** drauu covers slot 4 entirely. Scene C unlocks later.
