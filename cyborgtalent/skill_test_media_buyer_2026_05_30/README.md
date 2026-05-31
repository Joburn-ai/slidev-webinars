# Media Buyer Diagnostic · Walkthrough Deck

A 6-slide walkthrough video that runs above the brief on `/c/{token}/skill-test/media_buyer_diagnostic_v2`.

## Voice

Calm, transparent, no marketing register. Character > skill is the thesis. Cards-on-the-table register (Fladlien) without the sell. John records VO over a live walkthrough of this deck on Slidev.

## Slides

1. **Cover** · "Hey. You're here because we want to figure out where you actually are."
2. **Cards on the table** · "An 8-minute screen-share. Not a hard gate."
3. **What we actually care about** · "Skill is one input. Not the most important one." (THE thesis slide)
4. **How it works** · 3-step card grid (screen / mic / 8 min) + Path B fallback note
5. **What lands. What lands flat.** · Two-column expectations
6. **Recording + start** · Transparency on recording, soft CTA, "no clock running until you do"

## Aesthetic

Aurora dark. Matches the candidate-facing page so the walkthrough → page transition feels continuous. Palette + components defined in `style.css` (co-located, auto-loaded UNSCOPED, `ct-*` prefix).

## Local dev

```bash
cd /root/slidev-webinars
pnpm install
pnpm dev:cyborgtalent-skill-test-media-buyer
```

## Build

```bash
pnpm build:cyborgtalent-skill-test-media-buyer
# Output lands at cyborgtalent/skill_test_media_buyer_2026_05_30/dist/
```

## Reuse for other scenarios

The structure scales to all 4 active scenarios in `team_ops.pre_hire_scenarios`. Clone this folder, swap copy + closing line, keep `style.css` identical (or symlink it). When the deck is wired into the candidate-facing page, add a `walkthrough_video_url` column on `team_ops.pre_hire_scenarios` and render conditionally.

## QC

- Em-dash count: 0 (verified)
- `colorSchema: dark` pinned (matches aurora aesthetic)
- v-click syntax: wrapper component, no modifier in tag name
- Force-hide CSS: `.slidev-vclick-hidden { opacity: 0 !important; }` set
- All component classes prefixed `ct-*` to avoid cross-client collision
