# Deck: 60+ Programs for High-Earning First-Time Buyers (EVERGREEN shorty)

**Status: SKELETON ONLY (Rule 14).** Folder structure + theming + section files are scaffolded.
No final slide copy or SAY-scripts are written yet. Fill after the script is blessed.

## Deck meta

| Field | Value |
|---|---|
| **Client** | Bradley Pounds / HomeBuyerSchool.com |
| **Deck slug** | `bradley_pounds/evergreen_60programs_2026_07` |
| **Format** | Fladlien 14-section webinar, EVERGREEN self-running / narrated (auto-advance) on-demand replay cut |
| **Runtime target** | ~22 min (band 20-25) vs the 60-90 min live |
| **Funnel** | cold FB (Housing Special Ad Category, broad-only) -> registration -> on-demand webinar -> BOOK A CALL -> high-ticket homebuyer coaching |
| **Offer** | FREE STRATEGY CALL (soft, book-a-call). No priced components / value-stack line / price reveal / guarantee / hard scarcity. |
| **Skill** | slidev_presentation V-07 v3.1 |
| **Slidev pinned** | v52.15.2 (repo-level) |
| **Source live deck** | 78 slides / 107 images. `./assets/source_images/` + scratchpad `brad_slides.pdf` / `brad_slides.txt` |
| **Outline (source of truth)** | `./_EVERGREEN_STRUCTURE.md` (keep/compress/cut verdicts, section-by-section, aha map, evergreen adaptations) |

## Files

| File | Owns |
|---|---|
| `slides.md` | Entry. Frontmatter (theme, title, `colorSchema: light` pinned, `transition: slide-left`, fonts), Rule 3 force-hide `<style>`, note pointing to `style.css`, cover placeholder, `src:` includes for the 5 section files. |
| `opening.md` | Fladlien 1 Pop Quiz + 2 Pain + 3 Positioning (O2-O7). ~7 slides / ~3 min / 12%. |
| `teaching.md` | Fladlien 4 Mechanisms + 5 Demonstration + 6 Recap (T1-T18). ~24 slides / ~10.5 min / 48% (longest). |
| `recap_momentum.md` | Fladlien 7 Yes Momentum (Y1-Y3). ~3 slides / ~1.5 min. Zero images. |
| `offer.md` | Fladlien 8 Offer Intro (F1-F7). §9-12 collapse (soft offer). ~12 slides / ~6 min / 28%. |
| `close.md` | Fladlien 13 Guarantee + 14 Scarcity (collapsed). Final LAND CTA + replay disclaimer. ~2 min / 8%. |
| `style.css` | UNSCOPED brand + component CSS (Rule 7). `.hbs-*` prefix. Brand tokens are HARDCODED HEX PLACEHOLDERS -> replace from `_ASSET_REFERENCE_SHEET.md`. |
| `vite.config.ts` | Rule 18 `fs.allow` fix so the rolldown production build (and Vercel) resolve leading-slash public paths. |
| `_EVERGREEN_STRUCTURE.md` | The blessed-pending outline (already present). |
| `assets/source_images/` | 107 extracted images from the live deck (map to the Reference Sheet before build). |

## Fladlien 14-section mapping (evergreen)

| # | Section | File | Beats | Notes |
|---|---|---|---|---|
| 1 | Pop Quiz | opening.md | O2 future-pace | Puts viewer IN the house |
| 2 | Pain | opening.md | O3 Mack-truck loophole (sticky hook #1), O4 how-feeling | Emoji -> Iconify/text (Rule 13) |
| 3 | Positioning | opening.md | O5 goal, O6 watch-through stack, O7 Brad credibility + NMLS footer | Compress 4 cred slides -> 1-2 |
| 4 | Mechanisms | teaching.md | T1 Mistake #1, T2-T11 the 3 ingredients | Aha #1/#2/#3 harvest |
| 5 | Demonstration | teaching.md | T12-T17 program tour (compressed), T15 the MAP (hook #2), T17 401k Ninja (hook #3) | Aha #4/#5 harvest; highest image density |
| 6 | Recap | teaching.md | T18 can't-cover-all-60 bridge | The reason to book |
| 7 | Yes Momentum | recap_momentum.md | Y1-Y3 | CRITICAL. Internal/rhetorical, no chat. Zero images. |
| 8 | Offer Intro | offer.md | F1-F3 free strategy call | Aha #6 |
| 9-12 | Components / Bonuses / Value-Stack / Price | offer.md | COLLAPSED | Soft offer -> bonuses (book/65-list/$50) migrate to F4 as booking incentives. No fake price stack. |
| 13-14 | Guarantee / Scarcity | close.md | COLLAPSED | No guarantee, no hard scarcity on a free-call soft offer. |

Aha-Stack: 6 belief swaps (A1-A6), full map in `_EVERGREEN_STRUCTURE.md` section 2.

## Evergreen adaptations (live -> on-demand)

- **Chat prompts CUT.** "Type YES in the chat", "type your questions in the chat", "quick check-in" -> converted to rhetorical/internal beats or a passive on-screen line. No response mechanism on a replay.
- **Live/time language CUT.** "tonight", "an hour on a random weeknight", "$50 gift card tomorrow" -> "our goal", "watch through + book", "$50 gift card when you book + attend".
- **Stay-till-end stack reframed** as a watch-through / booking incentive (migrates to offer F4).
- **Replay-rate disclaimer KEPT + made standing** (T16 + close C2): rates advertised at recording may have moved since; educational only, not a commitment to lend.
- **Emoji -> Iconify / text** (Rule 13): feeling faces -> `i-mdi-emoticon-*`; party-popper -> `i-mdi-party-popper` or "WON".
- **Self-running mode**: auto-advance / narrated (evergreen). Production narration path = ElevenLabs MP3 + narrator addon (Web-Speech only for demo).
- **CTA affordance**: this is a replay PAGE, not a live Zoom. Real page-level button + QR + visible URL below the video is fine. On the slide: QR in a white card + visible monospace URL. No fake mid-slide "click" pill (Rule 11).

## QC checklist (skill 3-pass gate)

### Pass 1 -- block-by-block copy (per section, after bless)
- [ ] F6 / brand alignment; voice DNA (Brad register)
- [ ] Compliance + no-no list scanned; NMLS/Rapid + Equal Housing + educational-only present
- [ ] CFA pillar mapped per section; Aha-Stack (A1-A6) cross-checked, each has a harvest point
- [ ] Clean Claims (rates = "as advertised", no implied guarantee, no "you will qualify")
- [ ] Read out loud; em-dash ZERO

### Pass 2 -- slide-by-slide functional
- [ ] Every slide has a `<!-- slide:id -->` after frontmatter close (Rule 4)
- [ ] Speaker notes block present per slide (Rule 5)
- [ ] Every list of 2+ -> `<v-clicks>` (Rule 0); at least one v-click per slide
- [ ] `<=7` visible words on hook/opening slides; notes carry the script
- [ ] Body text >= text-2xl; fine print >= text-xl
- [ ] No layout repeated 3x consecutively
- [ ] **No emoji in body** -> grep the deck (Rule 13)
- [ ] **No em-dashes** -> grep the deck (zero tolerance)
- [ ] `colorSchema: light` pinned (Rule 12)
- [ ] All images exist locally + mapped in the Reference Sheet + registered; no hotlinks
- [ ] Content fits the 16:9 frame at ~1280x720, every v-click state (Rule 9)

### Pass 3 -- live deck post-deploy
- [ ] **Full `slidev build` passes**, not just dev (Rule 18 / vite.config.ts)
- [ ] Loads < 3s; animations trigger; presenter mode via `/presenter/N` path
- [ ] Cold deep-link to a mid-deck slide keeps theme (e.g. `/2?clicks=6`) (Rule 16)
- [ ] Verify in WebKit/Safari, not only Chromium (Rules 15-16)
- [ ] QR decodes to the real booking URL; visible URL matches
- [ ] `--without-notes` PDF export works for client replay
- [ ] Vercel SPA rewrite negative-lookaheads asset dirs (`assets/|fonts/|images/`)

### Visual proof / Reference Sheet (before build)
- [ ] Build `_ASSET_REFERENCE_SHEET.md`: every evidence claim -> exact asset -> "does it demonstrate the point?" QC -> compliance/lane -> status
- [ ] F5/F6 social-proof cards: OPEN AND READ the pixels (Buddy/Rocio, Peter/Esther) -- real, lane-clean, not generic symbolic
- [ ] The MAP (T15) + the 401k Ninja (T17) sourced from `assets/source_images/` and QC'd against claim
- [ ] Nothing below status `✔` is referenced by the deck

## Rule 14 status

**Structure: BLESSED PENDING.** `_EVERGREEN_STRUCTURE.md` holds the keep/compress/cut verdict + full
section outline + aha map. **Script: NOT YET WRITTEN.** The shorty script is a compressed cut of the
big-webinar transcript. Do NOT write final slide copy or SAY-scripts, and do NOT deploy, until:
1. The shorty script is produced from the big-webinar transcript and
2. John/Brad bless it.

Skeleton exists so the fill step is drop-in per section.

## Addons

None installed yet. Candidates for build (install from repo root `npx slidev addon add <name>`, then list here):
- `slidev-addon-tts` -- narration from speaker notes for the self-running replay (pairs with the video edit compiler). Production narration likely ElevenLabs MP3 + narrator instead.
- `slidev-addon-fancy-arrow` -- optional annotation on the ZOOM beats (the MAP, the 401k Ninja).

## Setup note (deps / build)

- The repo (`/root/slidev-webinars`) already has `node_modules` + `pnpm-lock.yaml` (Slidev v52.15.2). No per-deck install expected; if a fresh clone: `pnpm install --no-frozen-lockfile` at repo root.
- **`slidev build` was NOT run** (skeleton only, and per task). Before first deploy, add this deck's build script to repo `package.json` (`build:bradley_pounds-evergreen_60programs_2026_07`) and a Vercel project per the deployment SOP, with `outputDirectory` = this deck's `dist/` and the asset-dir negative-lookahead rewrite.
