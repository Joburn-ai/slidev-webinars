# Build Spec v2 — the DENSITY + IMAGERY upgrade (John, 2026-07-23)
The single biggest lesson from past slide-hack decks: **not enough imagery/visualization woven through — that's where they go weak.** This spec fixes that. It governs the SLIDES phase (the script is DONE — `_SCRIPT.md`, voice-accurate from the Tara transcript). Read alongside `_EVERGREEN_STRUCTURE.md` (beats), `_ASSET_REFERENCE_SHEET.md` (his images), `_COMPLIANCE_QC_FLAGS.md`, `_BRAND_KIT.md`, and the `slidev_presentation` skill.

## 1. Density — go for the true 400-hack feel
- **Target ~90-100 slides** for the ~22-min cut (was ~50). True Fladlien rapid-fire: one idea per slide, fast cuts, ≤7 visible words on hooks (SAY-copy in speaker notes). Split every beat that carries two ideas into two slides.
- v-clicks densify WITHIN slides (value-density-per-click); the higher slide count densifies the CUTS. Both.
- We can A/B the tighter ~50 vs the ~90-100 later; **build the 90-100 first.**

## 2. Imagery — EVERY slide carries a strong visual (the core fix)
No naked text slides. Each slide gets a visual that is **on-brand consistent AND emotionally impactful.** Two image classes woven together:

**A. His REAL assets** (proof / positioning / data / the sticky hooks) — from `assets/source_images/`:
- Brad headshot cutout (img-019), family "Big Why" (img-034), logo (img-021), the Mack-truck loophole (img-004), money-fan (img-078), framing/construction (img-073), retirement (img-086), the 5-icon FTHB row (img-039), the congrats client photos (img-102/103), Equal Housing (img-075).
- 🔴 **The two ZOOM heroes** get his real (re-sourced hi-res) visuals: the Slime-Green/Apartment-Beige 100%-financing MAP and the 401k Secret Ninja.

**B. GENERATED on-brand emotional concept imagery** (the gap to fill — for the belief/emotion beats that currently have no visual). Run the skill's image-symbolism protocol: emotion → metaphor → image, then **grade every generated image to the orange #FF7300 / navy #0A3466 brand** so the deck reads as ONE visual system. Map per emotion:
| Beat emotion | Metaphor → generate |
|---|---|
| Curiosity (open, "programs you never heard of") | hidden door / light through a crack / key |
| Pain / self-doubt ("I make too much / my credit's bad") | fog, maze, locked gate, person at a wall |
| Relief ("relax, down payment is the easiest problem") | exhale, weight lifting, calm sunrise |
| Clarity (the 3 ingredients, the programs) | clean path, sorted shelves, map lighting up |
| Momentum / pride (yes-momentum) | mountain summit, finish line, open road |
| Trust / safety (positioning, guarantee) | shield, steady hands, Texas roots |
| Transformation (offer, "your new home") | before/after, keys-in-hand, lit-up house at dusk |
Generate via the image model (Nano Banana per skill) or source + re-host, curate from N candidates (log the human-edit step for IP), grade to brand. **Curation matters — this is the step that fixes "weak imagery," so do NOT fire-and-forget; pick the strongest, kill the generic.**

## 3. Visual flow — it should feel like one cinematic system
- Consistent treatments: full-bleed hero (frosted card for text), image-left/right for proof beats, centered-hero-number for stats, navy→deep-navy section-gradient dividers between Fladlien sections.
- Consistent color grade across ALL images (his + generated) to orange/navy. No two-era rainbow look (kill the off-brand testimonial cards).
- Consistent type: heavy condensed display caps + Poppins. Consistent accent-word color (orange).
- **Visual rhythm** = the pacing tempo made visible: FRAME (slow, breathe) → MOVE-FAST (rapid image cuts) → STOP (one strong image, no clicks) → ZOOM (the map / 401k, annotated) → LAND (identity payoff + CTA).

## 4. Animations — simple, for emphasis only
- `<v-clicks>` sequential reveal on every 2+ list (default).
- `v-mark` (rough-notation) circle/underline/box on the exact punch word at the exact beat — object form for brand hex: `<span v-mark="{ at: 2, color: '#FF7300', type: 'circle' }">`.
- `@vueuse/motion` subtle enter (fade/rise) on hero elements. Slide transitions (slide-left/fade).
- Never animate for decoration; every motion earns a beat.

## 5. Process for the slide build (next session)
1. **Per-slide visual map first** (the reference-sheet discipline): for all ~90-100 slides, map slide → beat → emotion → visual (his-asset id OR generate-this) → treatment. This is the shopping list.
2. **Generate/source + grade** the concept images (batch, curate, brand-grade).
3. **Build the section files** from `_SCRIPT.md` at 90-100 density, wiring every visual, animations, compliance footers.
4. **Assemble + build + deploy** the Vercel review preview.
5. **3-pass QC** incl. the imagery pass: does every slide have a strong on-brand visual, does the visual flow read as one system, content-fits-frame at every click, WebKit + deep-link.

## What's DONE (do not redo)
- `_SCRIPT.md` — full voice-accurate script (from the Tara transcript). This is the source for all speaker notes / SAY-copy.
- Structure, asset catalog, compliance flags, brand kit, scaffold, 107 images extracted.

## Still needs John
- Real **book-a-call URL** (swap the `/book` placeholder + regen QR).
- **Brand-hex confirm** + font pick.
- 🔴 **Hi-res re-sources** (Brad/John): the CRA financing MAP, the book cover, the San Antonio map — the signature visuals can't be low-res.
- **401k slide** stays (with disclaimer) unless John says cut.
- Density call confirmed: **90-100** (this spec).
