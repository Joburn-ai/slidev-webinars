# FF Town Hall · Standing Monthly Template

The reusable Slidev deck for the monthly all-hands town hall. **The structure never changes; only the tokens do.** Spec: `ai-os/11_Operations/ref_team_operating_cadence_2026_07_25.md`. Format: internal training deck (Mermaid-driven, no offer spine), dark atomic-clean.

**21 slides · ~20 min runtime** · deck spine (locked):

| Slides | Section |
|---|---|
| 1 | Cold open · FF Town Hall · month |
| 2-4 | 01 Why we do this (vision + mission · values · self-improving system) |
| 5-7 | 02 Where we've been (divider · planned vs actual · Mermaid timeline) |
| 8-13 | 03 Where we are (format divider · 5 department reports, 90 sec each) |
| 14-16 | 04 Where we're going (divider · month goal · Mermaid gantt) |
| 17-18 | 05 Shoutouts + team reward |
| 19 | 06 The misses, acknowledged + the system change |
| 20-21 | 07 Close (the one thing · next town hall date) |

---

## The 15-minute monthly fill-in SOP

**Step 0 · Copy, never edit the template (1 min).**
```bash
cp -r ff_internal/town_hall_template ff_internal/town_hall_YYYY_MM
cd ff_internal/town_hall_YYYY_MM
```
The template folder stays pristine. Each month gets its own copy.

**Step 1 · Pull the numbers (5 min).** Every number on slides 6 and 9-13 comes out of the **ClickUp weekly review ritual** (the end-of-week REVIEW + RETRO sitting, per the operating cadence doc). Nothing is invented at deck-fill time:

- **Planned** = what last month's town hall deck put in its "Next target" column. Roll it forward.
- **Actual** = what the last weekly review of the month recorded (planned vs accomplished, per objective).
- **Next target** = what the Sunday PLANNING ritual set for the coming month.
- Each department owner brings their own objective / DoD / win / miss / ask; the deck-filler just transcribes. The **ask** must name who it's for (another department or a founder).

**Step 2 · Find-replace the tokens (7 min).** All `{{TOKENS}}` live in `slides.md`, wrapped in `v-pre` spans so the braces render literally until you replace them. Grep to confirm none are left:
```bash
grep -n '{{' slides.md
```

| Token group | Tokens | Slide |
|---|---|---|
| Cover | `{{MONTH YEAR}}` on the slide; the frontmatter `title:` uses bare `MONTH_YEAR` (Slidev Vue-renders the title, so braces would break the build) | 1 |
| Why (set once after the sitting, then FROZEN) | `{{VISION}}` `{{MISSION}}` `{{VALUES_LOCKED_LIST}}` | 2-3 |
| Last month | `{{LAST MONTH}}` `{{OBJ_1..4_NAME}}` `{{OBJ_1..4_PLANNED}}` `{{OBJ_1..4_ACTUAL}}` `{{LAST_MONTH_VERDICT}}` | 5-6 |
| Departments ×5 (prefixes `ACQ_` `DEL_` `SYS_` `TOPS_` `FIN_`) | `_OWNER` `_OBJECTIVE` `_DOD` `_PLANNED` `_ACTUAL` `_NEXT_TARGET` `_WIN` `_MISS` `_ASK` | 9-13 |
| Next month | `{{NEXT MONTH}}` `{{NEXT_MONTH_GOAL}}` `{{QUARTER_TARGET}}` `{{NEXT_MONTH_DOD}}` | 14-15 |
| Shoutouts + reward | `{{SHOUTOUT_1_NAME}}` `{{SHOUTOUT_1_WHAT}}` `{{SHOUTOUT_2_NAME}}` `{{SHOUTOUT_2_WHAT}}` `{{TEAM_REWARD}}` | 17-18 |
| Misses | `{{MISS_1}}` `{{MISS_2}}` `{{SYSTEM_CHANGE}}` | 19 |
| Close | `{{ONE_THING}}` `{{NEXT_TOWNHALL_DATE}}` | 20-21 |

**Mermaid blocks are the exception:** the two diagrams (slides 7 and 16) use **bare CAPS tokens with NO curly braces** (braces break the diagram parser): `LAST_MONTH_NAME`, `W1_HEADLINE`..`W4_HEADLINE`, `QUARTER_NAME`, `QUARTER_TARGET_LABEL`, `NEXT_MONTH_GOAL_LABEL`, `MILESTONE_1/2_LABEL`. The gantt on slide 16 also needs its **dates updated to real calendar dates** every month (the parser requires valid `YYYY-MM-DD`).

**Step 3 · Verify + present (2 min).**
```bash
npx slidev build slides.md    # must exit clean; catches any token you broke
npx slidev slides.md --open   # present; presenter mode at /presenter/1
```
Advance every v-click once at ~1280×720 and confirm nothing clips the bottom edge (long fill-ins are the usual culprit; shorten the line, don't shrink the type).

---

## The rules that make this work

1. **Slides 2-4 (WHY WE DO THIS) NEVER change structure.** After the sitting locks vision, mission, and the 3-5 values, fill those tokens ONCE, then freeze the slides. The recap opens every town hall verbatim; after a certain point people don't need new information, they need to remember the core things. Changing vision/mission/values is a sitting decision, never a deck edit.
2. **The whole spine is locked.** Don't add sections, don't reorder, don't let a department bring extra slides. A department report is one slide, 90 seconds: objective + DoD, three numbers, one win, one miss, one ask.
3. **Misses are named, never dramatized.** Slide 19's register is honest and level; it always ends in a system change. The doctrine line stays on the slide: a miss just means "okay, what do we have to do."
4. **No client or offer content.** Internal deck. Finance shares only what the whole team should see.

## Build notes (for future operators)

- Deps ride on the repo root (`/root/slidev-webinars/` · pnpm · `@slidev/cli` 52.x). No per-deck install needed.
- Root `package.json` scripts: `pnpm build:ff-townhall` / `pnpm dev:ff-townhall`.
- `style.css` is co-located and auto-loaded unscoped (skill Rule 7); all classes are `.th-*` prefixed. Palette: deep-navy field `#0A1524..#14304F`, cream ink `#F7F5EE`, gold win `#E2C25C`, rust miss `#E0755C`, teal ask `#4FBDBD`.
- `colorSchema: dark` is pinned in the frontmatter (skill Rule 12); force-hide v-click CSS included (Rule 3); no emoji, no em-dashes, no external images.
- `{{TOKENS}}` are inside `v-pre` spans on purpose: without `v-pre`, Vue treats `{{...}}` as template interpolation and either renders empty or fails the build. After you replace a token with real text, the `v-pre` is harmless. If you ADD a new token anywhere, keep it inside a `v-pre` element.
