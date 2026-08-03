# SupportED × Funnel Futurist — Operating Alignment

Internal working deck. **John Coburn + Dr. Joe Sebestyen, Tue 2026-08-04, 8:00 PM EST.** ~20-25 min then open discussion.

## What this is

One plan covering August to December 2026: one commercial strategy, one product roadmap, one promotion calendar, one customer journey, one operating cadence, one source of truth per job. It ends on the fifteen decisions that are Joe's or John's to make.

**Register:** internal working deck between two principals. **No offer spine, no CTA, nothing sold to Joe.** The skill's educational-versus-motivational doctrine deliberately does not apply here (that rule protects a *prospect* from talking themselves out of a purchase; Joe has to run the machine, so he needs the mechanism).

## Run it

```bash
cd /root/slidev-webinars
pnpm dev:supported-alignment      # local, opens a browser
pnpm build:supported-alignment    # production build -> supported/operating_alignment_2026_08_04/dist/
pnpm export:supported-alignment   # PDF, notes stripped, for sending to Joe after
```

Presenter mode (split screen + speaker notes + timer) is path-based: append `/presenter/1` to the deck URL. Overview grid: `/overview`.

## Structure

| File | Section | Owns |
|---|---|---|
| `slides.md` | entry + cover | headmatter, cover, `src:` includes |
| `opening.md` | Frame + diagnosis | July was not short of effort. Four lanes competed for one audience, calendar and team |
| `ecosystem.md` | One ecosystem | The journey map-reveal. Why high and low ticket do not compete. Two CTAs. The one metric |
| `findings.md` | What the audit found | The four blockers with exact figures + the live screenshots. The list reality. Attribution |
| `august.md` | August week by week | The dated five-week spine, product interlock and freeze, the 16-email send structure |
| `close.md` | Cadence + decisions | Mon/Wed/Fri, source-of-truth table, the Slack boundary, the fifteen decisions |

Shared contract all section agents built against: `_BUILD_SPEC.md`. Theme: `style.css` (all classes prefixed `.oa-`, first line imports the mandatory carbon toolbar icons). `vite.config.ts` is required for the production build (skill Rule 18).

## Content source of truth

`/root/ai-os/06_Clients/supported/strategy/promo_calendar_august_2026_08_03.md`

**No email copy is written yet, and that is deliberate.** Copy drafts after Joe signs off the spine, so the argument is not written twice. Path: `email_copywriter` → `humanize_copy` → `voice_qc` against Joe's voice DNA, then bulk review.

## Evidence assets

`public/images/` holds seven live captures from 2026-08-03. Three of them (`01_ap_application_funnel.png`, `04_webinar_reg.png`, `07_supported_home.png`) are **byte-identical on purpose** — that is the proof that `supportedtutoring.com/webinars`, `/tested-offer` and `/` all serve the homepage, which is why no webinar registration page exists.

`02_lt_gameplan_47.png` shows a Vercel Security Checkpoint, not the $47 page. Also on purpose.

## Known items for the session

The deck carries no placeholders. Everything a principal must rule on was routed into the decisions section rather than left on a slide. The two that matter most:

- The live booking page is the **College** Strategy Session, not AP. Confirm which asset August drives to.
- The August booked-call target must be set against **7,293 mailable**, not 14,639 contacts.

## Deploy

Per-client Vercel project pattern in the skill's deployment section. The SPA rewrite **must** negative-lookahead the asset dirs (`/((?!assets/|fonts/|images/).*)`) or deep-links serve HTML where JS, fonts and images were expected.

## QC log

Built via the skill's multi-agent pattern: one agent per section file against a shared `_BUILD_SPEC.md`, a per-file QC stage, then a whole-deck coherence pass for cross-file duplication, number accuracy, register drift and transition handoffs. Pre-deploy still needs: full production build (not just dev), a cold deep-link to a mid-deck slide, and a WebKit/Safari pass (skill Rules 16 and 18).
