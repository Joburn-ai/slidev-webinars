# AIOS Operator Ladder — internal team-alignment deck

**Format:** Internal Training / SOP (slidev_presentation skill). **Runtime:** ~20-25 min, run live.
**Aesthetic:** atomic-era retro-futurist Joburn (cream/navy/gold/rust), `colorSchema: light` pinned.
**Backbone doc:** `ai-os/00_Foundations/team_alignment_aios_upskill_ladder_2026_06_16.md`

## What it is
The one ladder everyone climbs, in order: **Foundations → AIOS Operator Cert → your Skill Path.** Built to hyper-align the team. Centerpiece = the animated **skill tree** (slide 13). 21 slides, 6 acts (FRAME → Layer 0 → Layer 1 → Layer 2 → Roadmap → LAND). Live whiteboard moment on slide 16 (drauu, persist on).

## Run / build
```bash
cd /root/slidev-webinars
pnpm dev:internal-aios-ladder      # live, hot-reload (presenter mode at /presenter/1)
pnpm build:internal-aios-ladder    # build -> internal/aios_operator_ladder_2026_06_16/dist
npx slidev export internal/aios_operator_ladder_2026_06_16/slides.md --format png --output /tmp/aios_png   # PNG QC
```

## Hosting (INTERNAL — do not make public)
This deck names team members + internal strategy. It is **internal/private** per the docs-privacy lock — do NOT deploy to a public Vercel URL. Present live from `pnpm dev`, or host behind the portal / a private/auth-gated surface only. `vercel.json` here is the build config IF John chooses a private/protected Vercel project.

## QC log (2026-06-16)
- Build: clean (`✓ built`), 21 slides, mermaid + skill-tree compile.
- Pass 3 visual QC (PNG export, 1280×720): all 21 slides checked. No overflow/clip. Dark slides (1,2,4,8,12,19,21) render correctly (z-index stacking fixed). Skill tree (13), competency grid (10), credential badge (12), step-path (17) all fit + on-brand. Em-dash zero; no emoji (CSS motifs only).
- Fixes applied: `.al-dark` z-index 0 + `.al-dark-wrap` z-index 1 (dark slides were rendering as cream); ladder (5) tightened to fit; roadmap mermaid replaced with HTML stepper (mermaid LR overflowed at any usable scale); credential div balance.

## Open (per the backbone doc §10)
Mission/Vision/Values are DRAFT (slide 8) — John ratifies before this ships. Proposed skill-path directions (slide 15) — John confirms Febi/Keziah/Ronald/others.
