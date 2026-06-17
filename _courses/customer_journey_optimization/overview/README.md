# Customer Journey Optimization, Overview Deck

Internal training deck for the FF / Joburn team. Teaches the 4-Pillar Journey Framework, John's 5-stage spine, the 3 motion types, and the 5-industry adaptation matrix. NOT a Fladlien pitch deck. NOT a YouTube build-along. This is the internal training format: Mermaid-driven, no offer spine, value-density-per-click via v-clicks.

## Built on

- The `customer_journey_optimizer` skill at `/root/ai-os/.claude/skills/customer_journey_optimizer/SKILL.md` (the runnable framework).
- The curriculum at `/root/ai-os/00_Foundations/curriculum_customer_journey_optimization_v1_2026_06_16.md` (the lesson architecture).
- The cyborgtalent worked example at `/root/ai-os/00_Foundations/cyborgtalent_moments_architecture_2026_06_14.md`.
- The SaaS adaptation guide at `/root/ai-os/.claude/skills/customer_journey_optimizer/saas_b2c_adaptation_guide.md`.
- Joburn brand palette per `/root/slidev-webinars/_courses/portal_onboarding/module_01_start_here/style.css`.
- The Slidev build rules at `/root/ai-os/.claude/skills/slidev_presentation/SKILL.md`.

## Deck contents

30 slides covering:

1. Cover, 4-Pillar Framework branding
2. The diagnosis (4 failure modes per missing pillar)
3. The double-bowtie macro frame (Mermaid)
4. The 5-stage spine (visual swimlane)
5. Stage 0 + Stage 6 bookends
6. Motion-type sensitivity (Product-led / Sales-led / Marketing-led)
7. Pillar 1, Key Moments
8. Pillar 2, Triggers (4 types)
9. Pillar 3, Actions (action surfaces table)
10. Pillar 4, Tracking (schema preview)
11. All 4 pillars in alignment (Day 1 founder note worked moment with YAML)
12. Empathy + dopamine overlay map
13. HERO VISUAL: full Mermaid journey flow chart
14. Master Flow table adapted (with Motion variant column)
15. Tool-tier adaptation (3 tiers)
16. Frameworks layered (Coleman + Fogg + Heath + Brunson + ours, with source-attribution honesty)
17. Anti-patterns to reject on sight (9 rows)
18. Database Reactivation as a standalone moment-class
19. The Art of the Follow Up, 10-day cadence
20. HERO VISUAL TWO: 5-industry adaptation matrix
21. Worked example, cyborgtalent placement
22. Worked example, SaaS trial-to-paid
23. Thought experiments (12 listed, 3 expanded)
24. Workshop format (90-min, 5 blocks)
25. The context-doc prompt
26. Cost discipline + Journey Economics formula
27. Self-application discipline (5 FF/Joburn journey types)
28. What's next: Customer Journey in a Box
29. Three concrete next steps for Monday
30. Closing: the litmus test

## Brand + format locks

- Joburn palette hardcoded in `style.css` (cream + navy + teal + gold + warm + rust + charcoal).
- `colorSchema: light` pinned in frontmatter (Slidev skill Rule 12).
- All component classes prefixed `cjo-*` (Rule 7).
- v-click syntax: wrapper component, no modifier in tag name (Rule 1).
- Force-hide CSS `.slidev-vclick-hidden { opacity: 0 !important; }` in `style.css` (Rule 3).
- `layout: cover` only on full-bleed cover and closing slides (Rule 8).
- Slide ID comments after frontmatter close, on first body line (Rule 4).
- Speaker notes block at end of every slide body (Rule 5).
- No clickable buttons (Rule 11). Callouts and visible URLs only.
- Em-dash zero throughout.

## Run locally

From the slidev-webinars repo root:

```bash
pnpm install
pnpm dev:cjo-overview
```

Open http://localhost:3030 (Slidev default port). Press `Space` or `Right` to advance.

## Build for deploy

```bash
pnpm build:cjo-overview
```

Output lands at `_courses/customer_journey_optimization/overview/dist/`.

## Presenter mode

After running dev or visiting the deployed deck, open `/presenter/1` (path-based, not query string per Slidev skill).

## Export to PDF

```bash
pnpm slidev export _courses/customer_journey_optimization/overview/slides.md --without-notes
```

PDF lands at the same dist folder.

## Speaker pacing

- Total runtime target: 25 to 35 minutes when presented (internal training, not a webinar).
- Cover + diagnosis: 2 min (slow open, set the frame).
- Spine + bookends + motion: 6 min (the structure beats).
- 4 pillars (slides 7 to 11): 10 min (the load-bearing teaching).
- Hero visual + master flow + tool-tier: 6 min (the application beats).
- Frameworks attribution + anti-patterns + reactivation + follow-up cadence: 5 min.
- Industry matrix + 2 worked examples: 4 min.
- Thought experiments + workshop + prompt + economics: 3 min.
- Self-application + what's next + next steps + litmus: 2 min.

## QC checklist before deploy

- [ ] `grep -c "$(printf '\\u2014')" slides.md style.css README.md` returns 0 (em-dash zero)
- [ ] `pnpm build:cjo-overview` builds clean
- [ ] All 30 slides render at 1280x720 with no overflow
- [ ] All v-clicks reveal content sequentially (no flash before click)
- [ ] All Mermaid diagrams render (slides 3, 12, 13)
- [ ] `colorSchema: light` confirmed in frontmatter
- [ ] No clickable-looking buttons (all CTAs are callout text)
- [ ] Speaker notes present at end of every slide body
- [ ] PDF export passes via `slidev export --without-notes`

## Open decisions for John

1. Where this deck deploys (Vercel project under joburn-content? Internal-only? A shared `slides.joburn.com/cjo-overview` route?)
2. Whether to record a Loom narration for an evergreen self-running version (uses `slidev-addon-tts` + the recorded-once Loom pattern).
3. Whether the next build (Customer Journey in a Box) gets its own subdirectory under `_courses/customer_journey_optimization/` or its own repo.

## Status

- Built: 2026-06-17
- Skill version: V-07 v3.0 (Slidev) + O-22 v1.0 (CJO)
- Author: Claude Opus 4.7, FF / Joburn internal training stream
