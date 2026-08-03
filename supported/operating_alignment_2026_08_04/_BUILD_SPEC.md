# _BUILD_SPEC — SupportED × Funnel Futurist · Operating Alignment deck

**Deck:** `supported/operating_alignment_2026_08_04/`
**Audience:** Dr. Joe Sebestyen (client/partner) + John Coburn. **Two people, one working session.**
**Occasion:** Tue 2026-08-04, 8:00 PM EST. ~20-25 minutes, then open discussion.
**Presenter:** John.
**Purpose:** get product, acquisition, sales and customer success onto one strategy, one roadmap, one promotion calendar, one cadence. Then force the fifteen decisions.

Content source of truth: `/root/ai-os/06_Clients/supported/strategy/promo_calendar_august_2026_08_03.md`. Read it before writing.

---

## 1. Register — read this twice, it is the thing most likely to go wrong

**This is an internal working deck between two principals. It is NOT a webinar, NOT a VSL, NOT a sales asset.**

- **No offer spine.** No pop quiz, no pain section, no value stack, no price reveal, no scarcity, no guarantee. None of the Fladlien 14 sections apply.
- **No selling to Joe.** He is the client and a co-owner of the outcome. The frame is "here is what I found and what I propose," not "here is why you should believe me."
- 🔴 **The educational/motivational doctrine in the skill (section 9) DOES NOT APPLY HERE and must not be applied.** That rule exists so a *prospect* does not talk themselves out of a purchase. Joe is not a prospect. He needs to genuinely understand how the machine works, because he has to run it. **Be fully educational. Show the mechanism. Explain the why.**
- **What DOES apply from the Specificity Stack:** the tool is the hero not the operator (#1), format changes as pattern interrupts (#3), map-reveal then zoom-navigate (#4), and above all 🔴 **#5 EXACT figures, never rounded**.

**Tone:** direct, confident, precise. Plain language. No corporate speak, no hedging. Where something is broken, say it is broken and say what it costs. Where something is a judgment call, say whose call it is. Joe's time is the scarce thing.

**Banned openers:** "in today's world" / "let me explain" / "let's dive in" / "today we're going to talk about" / any generic recap framing.

**The one thing the deck must land:** the problem in July was never a shortage of activity. It was that four valid initiatives competed for the same audience, the same calendar and the same team, because there was no single plan. August fixes the plan, not the effort.

---

## 2. Brand + theme

Dark navy field, cream ink. Tokens and every component class live in the co-located `style.css` — **read it before writing and use only classes defined there.** Do not add inline `<style>` blocks for anything cross-slide (skill Rule 7).

| Role | Token | Meaning — keep it consistent |
|---|---|---|
| Field | `--oa-bg` `#071A33` → `#0E3A6E` gradient | background, already applied to `.slidev-layout` |
| Ink | `--oa-ink` `#F7F5EE` | all body + heading text |
| **Gold** `--oa-gold` `#E4A92A` | **the decision, the goal, the ruling** | the hero beat, the one metric, a locked call |
| **Rust** `--oa-rust` `#E0755C` | **the blocker, the broken thing, the cost** | never decorative |
| **Teal** `--oa-teal` `#4FBDBD` | **the mechanism, the fix, the system** | eyebrows, process, the how |
| Mute | `--oa-mute` `#8CA2C2` | captions, metadata, de-emphasis |

**Available classes** (all in style.css): `.oa-eyebrow[.gold|.rust]` · `.oa-h1[.xl]` `.oa-h2` `.oa-h3` `.oa-lead` `.oa-body` `.oa-meta` · `.oa-gold-t` `.oa-teal-t` `.oa-rust-t` `.oa-mute-t` · `.oa-cover-sub` · `.oa-footer` · `.oa-ghostnum` · `.oa-card` (with `.k[.gold|.rust]`, `.v`, `.s`) · `.oa-row[.blocker|.fix|.ruling]` (with `.tag`) · `.oa-stat[.hero]` (with `.lbl`, `.val[.rust|.gold|.teal]`) · `.oa-week[.peakwk|.closewk]` (with `.wk`, `.nm`, `.bd`) · `.oa-table[.mono]` · `.oa-heroCard[.rustline]` · `.oa-callout[.rustline]` · `.oa-shot` `.oa-shotcap[.rust]` · `.oa-chip[.gold|.rust]` · `.oa-diamond[.rust|.teal]`

UnoCSS utility classes are available and expected for layout (`flex`, `grid`, `grid-cols-3`, `gap-4`, `px-16`, `mt-6`, `max-w-...`).

---

## 3. 🔴 EXACT figures — copy these verbatim, never round, never invent

Every number below is verified from `marketing.ghl_contacts` / `marketing.ghl_opportunities` (synced 2026-08-02) or from a live capture on 2026-08-03. **An unrounded figure is the proof. "About 7,000" destroys it.** If you need a number that is not on this list, do not invent one: put it in `johnJoeDecisions` instead.

**The list:**
| Figure | Value |
|---|---|
| Total SupportED contacts | **14,639** |
| `email unsubscribed` | **4,975** (34%) |
| `email bounced` | **2,363** (16%) |
| `contact_type = dnc` | **321** (2%) |
| Any suppression, deduped | **7,344** (50%) |
| **Mailable ceiling** | **7,293** |
| Of those, carrying any engager tag | **671** (4.6%) |
| The engager tags are a bulk stamp: 7/30/60/90-day all sit at exactly | **1,687** |

**Attribution:**
| Fact | Value |
|---|---|
| `marketing.ghl_appointments` rows, every client | **0** |
| Last email-tagged contact in GHL | **2026-05-22** |
| `ghl_payments` last row, while the sync log reports success | **2026-04-21** |
| July opps stamped `won_at` but sitting in a non-won stage | **6 of 18** |

**Dates (all calendar-verified):**
| Date | Day | What |
|---|---|---|
| Aug 4 | **Tuesday** | this session, 8:00 PM EST |
| Aug 6 | Thursday | first re-engagement send. UTM capture must exist by now |
| Aug 14 | Friday | MVP1 exit gate |
| Aug 17 | Monday | registration opens |
| **Aug 26** | **Wednesday** | **the webinar, 7:00 PM ET / 4:00 PM PT** |
| Aug 24-28 | Mon-Fri | product freeze |
| **Aug 31** | **Monday** | **hard close** |
| Sep 3 | Thursday | grace ends. no extension |
| Registration runway | | **9 days** |

---

## 4. Image map — only these exist

Local paths under `public/images/`. **Any other path is broken: use a styled `.oa-card` panel instead, never a broken `<img>`.**

| File | What it shows | How to use it |
|---|---|---|
| `06_acingapexams_home.png` | acingapexams.com | the cold / ad surface |
| `01_ap_application_funnel.png` | supportedtutoring.com home | the main site |
| `07_supported_home.png` | **byte-identical to the above** | use as the PROOF that /webinars serves the homepage |
| `04_webinar_reg.png` | **also byte-identical** | same proof. This is the point, not a mistake |
| `03_booking_strategy_call.png` | the live booking page | 🔴 it is the **College** Strategy Session, not AP |
| `02_lt_gameplan_47.png` | gameplan.supportedtutoring.com | 🔴 renders a **Vercel Security Checkpoint**, 403 |
| `05_ap_strat_tool.png` | apstrattool.supportedtutoring.com | the AP strategy tool |

Wrap every screenshot in `.oa-shot` and caption it with `.oa-shotcap` (use `.oa-shotcap.rust` when the caption states a problem). Set width via the wrapper, never both width and height on the img.

**The three-identical-screenshots slide is a load-bearing beat.** Showing 01, 04 and 07 side by side and saying "these are three different URLs" is the single most persuasive proof in the deck. Build it deliberately.

---

## 5. Hard rules (from the skill, non-negotiable)

1. **Every list of 2+ items is a `<v-clicks>` reveal.** No slide where a list lands all at once.
2. `<v-click>` is a wrapper with NO modifiers. `<v-click.fade>` is invalid Vue and renders as literal text. Use `<div v-click.fade>` as a directive on an existing element instead.
3. **Zero em-dashes.** Use a period, comma or colon.
4. **No emoji anywhere in slide body.** They render as tofu boxes. Use `.oa-diamond`, a text label, or an Iconify class (`<div class="i-mdi-alert" />`). This includes the warning triangle and the red circle: use `.oa-diamond.rust` or the word BLOCKER.
5. **CONTENT-FITS-FRAME.** Fixed 16:9 canvas, anything past the bottom edge is clipped with no scroll. Max ~5 stacked blocks per slide. Content headlines capped at `.oa-h2` (2.15rem); `.oa-h1` is for cover and dividers only. If a slide is getting full, split it.
6. Slide ID comment goes **after** the frontmatter close, as the first body line: `<!-- slide:diagnosis-03 -->`.
7. Every content slide ends with a speaker-notes HTML comment: `HOOK:` one line, `BEATS:` bulleted, `TIMING:` seconds, `TRANSITION:` the cue into the next slide. **John is presenting cold. The notes are what he actually says.**
8. Never repeat the same layout 3+ times consecutively.
9. No clickable-looking buttons. There is no CTA in this deck anyway.
10. `layout: cover` on any slide whose root is `<div class="absolute inset-0 ...">`, otherwise absolute children collapse.
11. In `v-for`, bind `:class` dynamically, never a fully static `class` (WebKit static-hoisting drops the reveal).
12. **No `[VERIFY]` / `[TODO]` / `[PROOF]` / placeholder tags on any slide.** Every slide ships finished. Anything needing Joe or John goes into the returned `johnJoeDecisions` array.

**Mermaid** is native and encouraged for the ecosystem map and the product interlock. Style overrides are already in `style.css`. Keep diagrams to at most ~10 nodes: show a complete system, not every node.

---

## 6. Deck structure — one agent per file

`slides.md` is the entry point: headmatter, cover, then `src:` includes in this order. Each section file's first slide carries its own frontmatter as a standalone slide.

| File | Section | Slides | Owns |
|---|---|---|---|
| `opening.md` | Frame + the diagnosis | ~9 | Cover already lives in slides.md. Identity-level open, the July read, the coordination diagnosis, the four competing lanes, what one system produces |
| `ecosystem.md` | One ecosystem | ~10 | The map-reveal (Mermaid). High-intent vs lower-intent lanes. Why high and low ticket do not compete. The unified intake. The one metric. The live surfaces strip |
| `findings.md` | What the audit found | ~12 | The four blockers with exact figures and the screenshots. The three-identical-screenshots beat. The list reality (14,639 → 7,293 → 671). The attribution before/after |
| `august.md` | August, week by week | ~13 | The five-week spine, one slide per week. The Aug 26 webinar beat. The close-date change and why. The product interlock and freeze. The send structure grid |
| `close.md` | Cadence + decisions | ~10 | Mon/Wed/Fri cadence, source-of-truth table, the Slack boundary, the fifteen decisions as the working agenda, the operating standard, first action |

Target **~54 slides total**, ~20-25 min. Tempo: FRAME on the open, MOVE FAST through findings, STOP on the ecosystem map, ZOOM on the week grid and the list numbers, LAND on decisions.

---

## 7. Output contract

Write your assigned file complete. Then return:
- `file` — the filename
- `slideCount` — actual count of `---` slide separators
- `imagesUsed` — array of `/images/...` paths referenced
- `johnJoeDecisions` — array of `{slideId, whatToConfirm}` for anything a principal must rule on. **This replaces every placeholder.** Be generous here: a decision captured is better than a guessed fact on a slide.
- `flags` — anything you could not resolve, or a risk you want the orchestrator to see
