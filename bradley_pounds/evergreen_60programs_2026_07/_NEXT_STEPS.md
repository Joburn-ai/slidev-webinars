# NEXT STEPS — Bradley Pounds Evergreen "60+ Programs FTHB" (Shorty)

> The ordered build plan from here to a deployed, self-running evergreen replay deck.
> **Source of truth for structure:** `_EVERGREEN_STRUCTURE.md`. **For assets:** `_ASSET_REFERENCE_SHEET.md`. **For compliance:** `_COMPLIANCE_QC_FLAGS.md`. **For meta/QC gates:** `README.md`.
> Legend: **[DONE]** already shipped this pass · **[JOHN]** needs John/Brad · **[NEXT]** I can do unattended once the gate above it clears.

---

## SUMMARY (read first)

1. **Set up:** structure blessed-pending (`_EVERGREEN_STRUCTURE.md`), 34-row asset sheet mapped, compliance flags logged, and the 9-file Slidev skeleton scaffolded (theming + section files + vite/Vercel fix). All lint-clean, zero copy written.
2. **The single biggest gate:** Rule 14. No final slide copy gets written until (a) the shorty **narration script** is derived from the big-webinar transcript AND (b) John/Brad **bless** both the shortened structure and that script. Everything downstream is drop-in once this clears.
3. **Recommended next action:** I write the ~22-min shorty narration script (compressed cut of `brad_slides.txt`, mapped beat-for-beat to O1-F7) and hand it to John/Brad for bless. That one artifact unblocks the entire build.
4. Parallel unblocked-now track while script is in review: 4 text-rebuild assets (NMLS card, program-name chips, VA slide, CTA slide) + emoji replacements + the recolor/de-emoji passes. The 5 hi-res re-sources and 4 brand-hex/URL confirms need John.

---

## STAGE 0 — WHAT'S DONE

- **[DONE]** Structure keep/compress/cut verdict + section-by-section outline + 6-Aha map + evergreen adaptations (`_EVERGREEN_STRUCTURE.md`). 78 -> ~50 slides, ~22 min.
- **[DONE]** Asset catalog: 107 images extracted, 34-row Reference Sheet mapped (reuse / recolor / re-source / rebuild status per beat).
- **[DONE]** Compliance flags logged (`_COMPLIANCE_QC_FLAGS.md`): 401k highest-risk, credit-repair CROA, dated rate/FICO/USDA/MCC qc_locks, emoji list, live-mechanic list, required disclosures.
- **[DONE]** Slidev skeleton (9 files): `slides.md` + 5 section files + `style.css` (placeholder hex) + `vite.config.ts` + `README.md`. Lint-clean, no copy.

---

## STAGE 1 — THE RULE-14 GATE (blocks everything below)

1. **[NEXT]** Produce the shorty **narration/SAY script** — a compressed cut of the big-webinar transcript (`brad_slides.txt`), written beat-for-beat to the O1-O7 / T1-T18 / Y1-Y3 / F1-F7 map. Runtime-budgeted to ~22 min. This is the artifact the structure was always waiting on; skeleton is drop-in per section once it exists.
   - Retrieve Brad voice DNA first (`copy_brain_retrieve` / `load_client_context`) so the script is in-register.
   - Bake compliance into the script at write-time: educational-only framing, "as advertised" on rates, no "you will qualify", 401k "consult plan admin / not tax advice", credit-repair no promised outcome.
2. **[JOHN]** **Bless the shortened structure** (the 78->50 compression, esp. the catalog collapse T13-T16) AND the narration script. This is the hard gate — Rule 14. Nothing in Stage 3 starts before this.

---

## STAGE 2 — ASSET FINISH (can run in parallel with Stage 1 review)

**Reuse as-is (~14, no work):** Brad cutout `img-019`, logo `img-021`, mack-truck `img-004`, sunset `img-010`, family `img-034`, money-fan `img-078`, framing `img-073`, retirement `img-086`, Equal Housing `img-075`, 3 brush cutouts `img-097/098/099`, congrats photos `img-102/103` (pending consent), 5-icon row `img-039`, wand `img-005`.

- **[NEXT] Emoji -> Iconify/text (Rule 13):** feeling row (p6) -> `i-mdi-emoticon-*`; congrats 🎉 (p75/76) -> `i-mdi-party-popper` or text badge "WON". Yes-momentum "Type YES 👇" (p68-71) -> rhetorical text, no chat.
- **[NEXT] Recolor / de-emoji medium-res reuse (~8):** coins illustration p22 (royal-blue -> brand orange/navy), money-pile p5, roofs p15, credit p37, down-payment p32, income p33, recap bar p49, yes-momentum navy bgs p68-71.
- **[NEXT] Text-rebuilds (4):** NMLS card (verbatim NMLS #2731896 / Rapid Mortgage #2425173 / "separate brokerage, not a lender" / Equal Housing), program-name chips (statewide/gov), VA slide, CTA slide (button/QR/URL, not "in the chat").
- **[NEXT] Compliance fixes into copy/footers:** standing replay-rate disclaimer footnote on every rate/FICO slide (T16 + CRA/builder beats); 401k disclaimer block; credit-repair softened; pick ONE program count (60+ vs 65); soften "$100K+ in rent" and "several thousand homes".
- **[JOHN] Re-source 5 hi-res assets (priority order):**
  1. 🔴 **Slime-Green / Apartment-Beige CRA map** (`img-072` only 800x433) — THE signature visual; recapture full-res from the CRA-eligibility map tool. Needs Brad/John to pull it.
  2. 🔴 **Book cover** "The Texas First-Time Homebuyer Blueprint" — not in deck; need real cover art or design one.
  3. 🔴 **65-program list + $50 Amazon gift-card** mockups — create on-brand.
  4. 🔴 **San Antonio eligibility map** (`img-067` 800x447) — recapture hi-res.
  5. 🔴 **Amandrea Jenkins testimonial** (`img-104` off-brand rainbow) — rebuild as orange/navy card.
- **[JOHN] Testimonial consent** on file (Buddy/Rocio, Peter/Esther, Amandrea) + "results not typical".

---

## STAGE 3 — FULL SLIDE BUILD (after Stage 1 bless)

Fill each section file from the blessed script + structure. One idea/slide, <=7 words on hooks (notes carry script), `<v-clicks>` on every 2+ list, `<!-- slide:id -->` per slide, speaker-notes block per slide, `<AutoFitText>` on hooks.

- **[NEXT]** `opening.md` (O2-O7) — Pop Quiz / Pain / Positioning. Compress 4 cred slides -> 1-2.
- **[NEXT]** `teaching.md` (T1-T18) — the 3 ingredients + the RUTHLESS catalog compression (~15 source slides -> 4). Keep + elevate the 2 hooks: the MAP (T15, full ZOOM) + 401k Ninja (T17). Aha #1-#5 harvest points.
- **[NEXT]** `recap_momentum.md` (Y1-Y3) — internal/rhetorical, no chat, ZERO images. Mirror of O4.
- **[NEXT]** `offer.md` (F1-F7) — free-call soft offer, §9-12 collapsed, booking-incentive value reframe (F4), 2 social-proof cards, QR/URL CTA (F7). Aha #6.
- **[NEXT]** `close.md` — final LAND beat folded into F7 + standing replay disclaimer card.
- **[JOHN] Brand-hex confirm:** swap `style.css` :root placeholder hex for the real HomeBuyerSchool kit (orange #FF7300 / navy #0A3466 / deep #011937), confirm fonts (Anton/Oswald + Poppins) in `slides.md` frontmatter. Standardize on the orange/navy register (kill the two-era rainbow testimonial look).

---

## STAGE 4 — SELF-RUNNING NARRATION (evergreen mode)

- **[NEXT]** Choose path: **production = ElevenLabs MP3 per beat** (voice ceiling) + narrator/auto-advance on `onend`; demo/fallback = `slidev-addon-tts` on speaker notes (Web-Speech). Optional `slidev-addon-fancy-arrow` for the ZOOM annotation beats (MAP + 401k).
- **[NEXT]** Auto-advance timing tuned to the ~22-min budget; play-button gate to satisfy the browser autoplay gesture.
- **[JOHN]** Confirm narrator/voice choice (Brad's own vs ElevenLabs clone) — voice is the ceiling on an evergreen replay.

---

## STAGE 5 — DEPLOY + REPLAY-PAGE CTA WIRING

- **[JOHN] Book-a-call URL** — the real booking link (e.g. `homebuyerschool.com/call`) for the QR + visible URL + page button. Needed before QR generation.
- **[NEXT]** Add build script to repo `package.json` (`build:bradley_pounds-evergreen_60programs_2026_07`); full rolldown `slidev build` must pass (Rule 18 / `vite.config.ts`).
- **[NEXT]** Vercel per-client project per deployment SOP: `outputDirectory` = this deck's `dist/`; SPA rewrite MUST negative-lookahead asset dirs (`assets/|fonts/|images/`) or deep-links serve HTML for JS/fonts/images.
- **[NEXT]** Replay page: video player + real `BOOK A FREE STRATEGY CALL` button directly below + QR + monospace URL fallback. In-deck F7 mirrors it (QR white card + visible URL, no fake mid-slide button, Rule 11 evergreen exception).
- Note: Vercel MCP needs auth in an interactive session before deploy; not available headless.

---

## STAGE 6 — THE 3-PASS QC (README gate)

- **[NEXT] Pass 1 — copy:** F6/voice, compliance + no-no scan, CFA per section, Aha A1-A6 each has a harvest point, Clean Claims, read-aloud, em-dash ZERO.
- **[NEXT] Pass 2 — functional:** slide:id per slide, notes per slide, v-clicks on 2+ lists, <=7 words on hooks, no emoji (grep), no em-dash (grep), colorSchema pinned, all images local + mapped, content fits 16:9 at every click.
- **[NEXT] Pass 3 — live post-deploy:** full build passes, loads <3s, cold deep-link keeps theme, WebKit + Chromium, QR decodes to real URL, `--without-notes` PDF export, Vercel asset-dir rewrite verified.

---

## GATE SUMMARY

| Gate | Owner | Blocks |
|---|---|---|
| Bless structure + narration script | **JOHN/Brad** | ALL of Stage 3+ (hard Rule 14 gate) |
| Brand-hex + font confirm | **JOHN** | Stage 3 visual build |
| Book-a-call URL | **JOHN** | QR/CTA (Stage 5) |
| 5 hi-res re-sources + testimonial consent | **JOHN/Brad** | MAP beat + bonus visuals + social proof |
| Narrator/voice choice | **JOHN** | Stage 4 narration |

Everything marked **[NEXT]** I run unattended the moment the gate above it clears. The script (Stage 1.1) is the one artifact that unblocks the most, so it goes first.
