# GG Team Re-Onboarding — Early Read (internal report deck)

**Format:** Internal Training / SOP (no offer spine, no 14-section Fladlien spine).
**Runtime:** ~7 minutes. 18 slides, fast cuts.
**Audience:** John first. Client-facing only after John's review (airlock, R11).

## Live
- Deployed: https://gg-team-early-read-ptgxqkvp3-joburn.vercel.app
- Behind the team Vercel SSO gate (team default `all_except_custom_domains`). John sees it logged in.
  To share externally, attach a custom domain (bypasses SSO + masks the vercel.app URL) rather than disabling protection.
- Presenter mode: `/presenter/1` · Overview: `/overview`

## Build
```
npx slidev build giftedgabber/team_reonboarding_early_read/slides.md --base / --out dist   # from repo root
npx slidev giftedgabber/team_reonboarding_early_read/slides.md --open                      # dev
```
`public/vercel.json` carries the SPA rewrite so it is baked into every `dist` rebuild (lesson 29).
`vite.config.ts` present per Rule 18 (rolldown fs.allow).

## Source of the content
- Individual reads (fairness-checked): workflow `wf_482f400b-6e7`
- Team-level report: `06_Clients/jothsna_kethar/07_team_re_onboarding/` + scratchpad `team_report.md`
- Response bundles + Loom transcripts: `06_Clients/jothsna_kethar/07_team_re_onboarding/responses/`

## QC log
- 2026-07-26 Pass 2 functional: 18/18 exported to PNG, every slide fits frame (Rule 9).
  First pass overflowed the 6-finding grid (only 4 cards visible, clipped) → split into two slides
  (3+3) and tightened the global type scale. Re-exported clean.
- Dark surfaces verified: white text, teal eyebrow, full opacity (lessons 19/26/27 clear).
- colorSchema pinned `light` (Rule 12). No emoji (Rule 13). No em-dashes.
- Full production build passes, not just dev (Rule 18). Deep-links return the SSO redirect, not a 404.

## Notes
- Every stat on slide 2 is computed from the recovered response data, not estimated.
- The 90% ghosting figure is self-reported by Loryn and is labelled as needing verification against GHL.
