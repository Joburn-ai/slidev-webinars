# Slidev Webinars Registry

> Master directory of all client decks. Update on every new deck + every status change.
> SOP: `copy-brain/06_Webinars/sop/sop_slidev_deployment_v1_2026_05_24.md`

Last updated: 2026-05-24

---

## In production (building toward Wed 2026-05-27 launch)

| Client | Deck | Status | Production URL | Preview URL | Presenter | Notes |
|---|---|---|---|---|---|---|
| supported | college_2026_05_27 | GATE_2_PREVIEW | supported.slides.funnelfuturist.com/college | pending | Joe Sebestyen | Wed 8pm EST launch. Script v3 2026-05-17. |
| giftedgabber | bsmd_2026_05_27 | SCAFFOLDED | giftedgabber.slides.funnelfuturist.com/bsmd | pending | Jothsna Kethar | Wed launch. Script v1 GOAT 95/100 from 2026-05-23. |

---

## Live decks

| Client | Deck | Live Period | Production URL |
|---|---|---|---|
| (none migrated to new structure yet. Existing AP Domination deck lives on `client-supported` branch root, separate deploy.) |

---

## Archived

| Client | Deck | Live Period | Reason Archived |
|---|---|---|---|

---

## Status values

- `SCAFFOLDED`. Folder created, basic structure in place, no copy yet
- `IN_PRODUCTION`. Slides being built, not yet pushed to preview
- `GATE_1_REVIEW`. SOP review pause (architectural)
- `GATE_2_PREVIEW`. Preview deployed, founder reviewing live
- `LIVE`. In production, presenting or available to clients
- `ARCHIVED`. Past launch, kept for record

---

## Client directory

| Client slug | Folder | Active decks | Vercel project |
|---|---|---|---|
| `supported` | `supported/` | 1 | slidev-supported |
| `giftedgabber` | `giftedgabber/` | 1 | slidev-giftedgabber |

---

## Legacy

Pre-restructure content (March 2026 era) lives at repo root: `slides.md`, `components/Counter.vue`, `pages/`, `snippets/`, `SupportED/`. These were the original starter scaffolding. New decks ignore them and use the per-client folder structure below.
