# SLIDE-BY-SLIDE IMAGE AND BUILD PLAN
## SupportED Back-to-School Webinar, rebuild
**Target:** `/root/slidev-webinars/supported/back_to_school_2026_08_10/`
**Built:** 2026-08-10 · **Executes:** the deck spec + the script gap audit
**Verified on disk before writing:** 174 parsed slides / 173 built, 137 `layout: center`, 5 `two-cols`, `public/` absent, `dist/` present.

---

## 0. THREE GROUND-TRUTH CORRECTIONS THAT CHANGE THE PLAN

**0a. The build target is 315 slides, not 348 and not 173.** 348 counts separators. The parser returns 174 and the build emits 173. The rebuild is specced below at **315 physical slides** across 12 blocks, inside the 250 to 400 gate.

**0b. Nine compliance-cleared product screenshots already exist and nobody has used them.** `/root/ai-os/06_Clients/supported/strategy/university_asset_extraction_2026_07_27/finals/` holds 9 finals in PNG and WEBP, already PII-redacted, already Draft-card-excluded, already carrying the College Board disclaimer bar. `university_course_catalog_composite.png` is a 34-course mosaic. That is the single best product-tangibility asset SupportED owns and it costs zero generations.

**0c. The hard build rule the plan is organised around: any visual that contains legible text is HTML, CSS or SVG. Never a generated image.** Report cards, essay paragraphs, rubric lines, scoreboards, score forecasts, the 89 versus 22 bar. Image models cannot spell, and this deck's entire demonstration section is text on screen. Generated images carry **zero lettering, zero numbers, zero logos**. This is why the plan below splits into `gen:`, `html:`, `mermaid:` and `real:` rather than "add images."

### Rebuild block map (all slide numbers in this document refer to this numbering)

| Block | Section | Slides | Range | Register |
|---|---|---|---|---|
| S0 | Pre-webinar hold | 8 | 001-008 | POLISHED |
| S1 | Pop Quiz, 6 questions | 37 | 009-045 | POLISHED |
| S2 | Pain, full CFA restored | 40 | 046-085 | POLISHED |
| S3 | Agenda, future pace, the WHY | 20 | 086-105 | POLISHED |
| S4 | Positioning, origin, promise, commitment | 24 | 106-129 | **BTS** |
| S5 | Mechanisms, 3 breakthroughs | 54 | 130-183 | **BTS** |
| S6 | Demonstration, Essay A versus B | 62 | 184-245 | **BTS** |
| S7 | Post-demo payoff and bridge | 14 | 246-259 | **BTS** |
| S8 | Recap | 12 | 260-271 | POLISHED |
| S9 | Yes Momentum | 18 | 272-289 | POLISHED |
| S10 | Back-to-school turn | 12 | 290-301 | POLISHED |
| S11 | Booking ask | 14 | 302-315 | POLISHED |

**Bare-slide budget:** 5% of 315 = 15.75, so **15 bare slides maximum, deck-wide.** All 15 are spent inside S9. The other 3 S9 slides carry a `v-mark` only, which counts as a visual under §3.1. Every one of the remaining 297 slides carries a real visual. Final ratio: **15 / 315 = 4.8%. Passes G1.**

---

## 1. THE RECURRING CHARACTER SPEC

### 1.1 Who she is

**Build codename: MAYA. The name never appears on screen, in a caption, in alt text, or in speaker notes.**

| Attribute | Locked value |
|---|---|
| Who | The **parent** of a high-school junior taking two or three AP classes. Not the student. |
| Age read | Mid-forties. Old enough to have a junior, young enough to still be in the working day. |
| Build and hair | Medium build, shoulder-length dark hair worn back. Same silhouette in every state so she is recognisable at thumbnail size. |
| Dress | **Locked outfit, identical in all nine states:** deep navy `#1B365D` crew-neck top, cream `#E8E0D0` open cardigan, charcoal trousers. One gold `#C5A55A` accent, a thin bracelet. The cardigan is the recognition device: it is the only cream shape on screen when she stands on navy. |
| Rendering | **Bold editorial flat-vector illustration.** Simple graphic face: two dot-and-arc eyes, a single brow line, a single mouth line. **No photorealism, no 3D, no rendered skin.** |
| Why illustrated and not photographic | A flat-vector character with a graphic face **cannot be mistaken for a real person**, so she cannot read as a testimonial or imply a real client. That is the compliance reason, not a style preference. A photographic cut-out of a woman in a kitchen next to the words "89% of our students" is an implied endorsement. This one is not. |
| Exaggeration | **Comic exaggeration is allowed and lands better than earnest.** Oversized posture, oversized gesture. Hands to head, fists up, shoulders to ears. |
| Settings, rotating | Kitchen table with a laptop · school pickup line seen from behind the wheel · standing in a doorway with paper in hand · sofa at night with a phone · standing beside a seated teen |
| Never | Never captioned with a student name. Never beside a quoted result. Never on the same slide as the 89% claim. Never holding a document with legible text (text goes on an HTML layer beside her, never inside the generated PNG). |

### 1.2 The locked style preamble

Every character prompt is `PREAMBLE + CHARACTER_LOCK + STATE`. Ship this verbatim in `assets/gen/runner_supported.py` as `STYLE_PREAMBLE`, forked from `/root/slidev-webinars/bradley_pounds/evergreen_60programs_2026_07/assets/gen/runner_brad.py` (which is proven, reads `GEMINI_API_KEY` from `/root/ai-os/.env`, model `gemini-3-pro-image-preview`).

```
STYLE_PREAMBLE =
"Bold editorial flat-vector illustration for a premium, calm, credible American
academic-coaching brand. Cinematic composition with one clear focal point and
generous negative space. Confident geometric shapes, clean flat fills, subtle
paper-grain texture only. Color palette STRICTLY limited to these six values and
nothing else: deep navy #1B365D for dark fields and primary shapes, muted gold
#C5A55A for the single hero accent, warm cream #E8E0D0 for light backgrounds and
soft shapes, near-black #111111 for line work and shadow fields, pure white
#FFFFFF, and one restrained brick red #C0392B reserved for error, loss or the
wrong path. No other hues. No teal, no purple, no orange, no pastel. No
photorealism. No 3D render. No gradient mesh. No drop shadows. No text, no
lettering, no numbers, no logos, no watermarks, no signage of any kind.
Emotionally literate, grown-up, never cute, never corporate stock. Fills a 16:9
landscape 1600x900 frame with breathing room. Concept: "
```

```
CHARACTER_LOCK =
"A single recurring character: a mid-forties mother of a high-school student,
medium build, shoulder-length dark hair worn back off the face, wearing a deep
navy #1B365D crew-neck top under an open warm cream #E8E0D0 cardigan and
charcoal trousers, one thin gold #C5A55A bracelet on the left wrist. Rendered as
a flat-vector illustration with a simple graphic face: two small dot-and-arc
eyes, one single brow line, one single mouth line, no rendered skin texture, no
photorealistic features. Identical face construction, identical hair, identical
outfit and identical proportions in every image of this set. Full body or
three-quarter body, never a floating head. Posture and gesture carry the entire
emotion. Comic exaggeration of posture is encouraged. She is centred on a
completely flat, uniform, pure magenta #FF00FF background field with no shadow
and no contact shadow, so she can be keyed out to transparency. Nothing else in
the frame except the props named. State: "
```

**Transparency:** the image model will not return reliable alpha. Generate on the flat `#FF00FF` field, then key to alpha with a Pillow pass in `assets/gen/cutout.py` (chroma distance threshold 40, 2px feather, then `rembg` as a fallback only if the key leaves halo). Verify each output with a 1px alpha-edge scan before it enters `public/images/`. **This is the step that kills the halo ring, and skipping it is what makes cut-outs look cheap.**

### 1.3 The nine states, with exact `STATE` strings and slide landings

Each is appended to `PREAMBLE + CHARACTER_LOCK`. Generate **N=4 candidates per state, curate to 1.** Consistency is enforced by feeding the winning `char-parent-relieved.png` back as a reference image on the remaining eight calls.

| # | File | `STATE` string (exact) | Lands on slides |
|---|---|---|---|
| 1 | `char-parent-relieved.png` | `She is standing at a kitchen counter in the morning light, holding a single blank sheet of paper at arm's length, shoulders down and loose, a small satisfied half-smile, head tilted slightly back. Relief and quiet pride. One cream coffee mug on the counter beside her. Nothing on the paper.` | 013, 016, 047, 052 |
| 2 | `char-parent-uneasy.png` | `Same kitchen counter, same blank sheet of paper now held closer to her chest, one hand half-raised toward her chin, head tilted down and to one side, brow line angled inward, mouth a short flat line. The first flicker of doubt, not yet fear. Her body has turned five degrees away from the paper.` | 022, 057, 061, 143 |
| 3 | `char-parent-stuck.png` | `She is seated at a kitchen table at night, both hands gripping the sides of her head, elbows planted wide on the table, shoulders pulled up to her ears, eyes closed, mouth a tight downward line. A closed laptop and a loose stack of blank papers in front of her. Comic exaggeration of the grip. Overwhelm and being trapped.` | 069, 073, 078, 084 |
| 4 | `char-parent-burned.png` | `She is standing in a doorway holding a small stack of blank receipts fanned in one hand, the other palm turned upward and open in a gesture of exhausted disbelief, one eyebrow line raised higher than the other, mouth pulled to one side. Weary, spent, slightly wry. Not defeated. She has paid for this before.` | 081, 083, 118 |
| 5 | `char-parent-leaning.png` | `She is seated leaning sharply forward toward an open laptop, forearms flat on the table, chin lifted, both eyes wide and open, mouth slightly parted, one hand paused mid-air as if about to point at the screen. Total forward attention. Curiosity overriding fatigue. The laptop screen is a plain flat gold #C5A55A rectangle with absolutely nothing on it.` | 008, 095, 131, 140, 172 |
| 6 | `char-parent-realising.png` | `She is seated upright and pulled back from the table, both hands lifted flat and open beside her head, palms forward, eyes wide, eyebrow lines high, mouth open in a clear round shape. The unmistakable posture of a penny dropping. Comic exaggeration. Behind her a single flat gold #C5A55A circle like a struck bell.` | 189, 231, 238, 247, 253 |
| 7 | `char-parent-deciding.png` | `She is standing in three-quarter view with arms folded loosely, weight settled onto one hip, chin level, jaw set, eyes steady and looking slightly off-frame toward the right, mouth a calm firm line. Resolved. Not excited, not anxious. A person who has just made a decision and is not going to unmake it.` | 258, 288, 291, 305 |
| 8 | `char-parent-winning.png` | `She is standing with both fists raised high above her head, elbows bent, feet apart, head thrown back, eyes squeezed shut in delight, mouth wide open in an unrestrained shout. Full comic exaggeration, maximum energy. Behind her three flat gold #C5A55A confetti shapes, no more than three.` | 250, 300, 313, 315 |
| 9 | `char-parent-with-teen.png` | `Same mother seated on the left, and to her right a second figure: a high-school teenager in a plain charcoal hoodie, hair short, seated at the same table, both of them facing the same open laptop, the mother's arm resting along the back of the teen's chair. Both calm and level. The teen's face uses the same simple graphic construction. This is the only image in the set containing a second figure. The laptop screen is a plain flat gold #C5A55A rectangle with nothing on it.` | 099, 296, 310 |

**Total character landings: 31 slides.** Reuse is deliberate. A recurring character earns its power by returning, not by appearing once.

**QC gate on the character set:** open all nine as a contact sheet at 200px wide. If you cannot tell at a glance that it is the same woman in all nine, regenerate with tighter reference conditioning. That check takes 30 seconds and it is the whole point of the device.

---

## 2. THE IMAGE PLAN, BY SECTION

Asset key: `gen:` generated concept · `char:` character state · `html:` CSS or SVG built in-slide, text-safe · `mermaid:` native diagram · `real:` asset already on disk.

Treatment vocabulary, adopted from the Brad deck: **HERO-BLEED** (full-bleed image, `layout: cover`, headline in a solid card) · **IMG-SIDE** (image one half, alternate L and R) · **STAT-HERO** (giant number or word, image as accent) · **GOLD-STATEMENT** · **NAVY-CARD** · **REVEAL-CARDS** · **ZOOM** (one image, annotation callouts revealed beside it) · **DIVIDER**.

Tempo vocabulary: **FRAME** (slow, breathe) · **MOVE-FAST** (rapid cuts) · **STOP** (one image, no clicks) · **ZOOM** (annotated hero) · **LAND** (identity payoff).

---

### S0 — Pre-webinar hold · slides 001-008 · POLISHED · tempo FRAME

| Slides | Run | Assets |
|---|---|---|
| 001 | Hold card, logo centred on navy, live countdown | `real:logo.png` (from `06_Clients/supported/brand/supported_logo_with_name.png`) + `html:h13_countdown` |
| 002 | **Title.** `<AutoFitText>` on the proven headline, over a dimmed full-bleed | `gen:c01_report_card_glow` HERO-BLEED + `real:logo.png` top-right |
| 003 | Chat prompt, which AP classes | `gen:c02_chat_bubbles_navy` IMG-SIDE L |
| 004-006 | Chat responses, three fast cuts | `html:h12_chip_row` + Iconify `i-mdi-flask`, `i-mdi-scale-balance`, `i-mdi-function-variant` |
| 007 | Got your pen | `gen:c03_pen_notebook` STOP, no clicks |
| 008 | What you will walk out with | `char:leaning` on navy + `html:` three-chip row |

Concept slugs: `c01_report_card_glow` (a single sheet of paper on a dark table, one warm gold light falling across it, nothing written on it), `c02_chat_bubbles_navy` (a rising column of flat cream speech shapes on navy, all empty), `c03_pen_notebook` (a single pen resting on an open blank notebook, overhead, cream on navy).

---

### S1 — Pop Quiz · slides 009-045 · POLISHED · tempo MOVE-FAST

**Structural ruling made here:** six questions, not five and not seven. Q1 is the back-to-school thesis question (new, the best strategic material in either document). Q4 tutors and Q5 effort are the two beats restored from the January script. **The old deck's Q4 is deleted:** it duplicates Q2 and its answer block is summer-slide residue sitting inside a back-to-school deck. Q6 stays TRUE as the pattern break.

Repeating unit, 5 slides per question: **statement card → chat gate → TRUE or FALSE stamp → the reason → the sting line.**

| Slides | Run | Assets |
|---|---|---|
| 009-012 | Quiz frame, not for your teen, for you | `gen:c04_two_chairs_one_lit` HERO-BLEED, `html:h12_quiz_card` |
| **013-017** | **Q1: the first report card tells you whether your teen is on track. FALSE** | `html:h01_report_card_a_row` (a CSS report card, straight A column, gold) → `char:relieved` on 013 and 016 → **`mermaid:m01_term_timeline`** on 017, the front-load / back-load hero |
| 018-022 | Q2: an A in the AP class means a 4 or a 5. FALSE | **`html:h10_two_scorecards_split`** two-cols, the deck's spine visual → `char:uneasy` 022 |
| 023-027 | Q3: more practice and more content. FALSE | `gen:c07_freethrow_bad_form` HERO-BLEED (a lone figure mid-shot, the ball arcing visibly wide, flat navy court) → `v-mark` circle on "form" |
| **028-032** | **Q4: expensive private tutors. FALSE. RESTORED** | `gen:c08_hourglass_over_coins` IMG-SIDE R + `html:` line "certified AP teacher who has scored the exam" |
| **033-037** | **Q5: hard work alone will work out. FALSE. RESTORED** | `gen:c09_treadmill_uphill` HERO-BLEED + `v-mark` box on "expensive failure" |
| 038-042 | Q6: strong scores can move real tuition money. **TRUE**, the pattern break | `gen:c10_credit_ladder` STAT-HERO + `html:h15_aggregate_claim_bar` |
| 043-045 | How many did you get right, and why that matters | `html:h11_quiz_scorecard` ZOOM with three revealed callouts |

**Claim controls in S1:** Q4 says "not certified AP teachers and have never scored an exam." It never says "lack College Board certification." Q4 drops the "$125 per hour" market stat. Q6 says "meaningful savings," never a dollar figure. **The single cleared aggregate claim lives on slide 041 and nowhere else in the deck**, rendered as `html:h15_aggregate_claim_bar`, a two-bar SVG reading 89% against about 22%, with `results vary` set in `text-xl` beneath it. That is its one and only appearance.

---

### S2 — Pain, the full CFA block · slides 046-085 · POLISHED · tempo FRAME then STOP

This is the section the audit calls the thinnest relative to source: eleven script paragraphs currently compressed into six thin slides. Forty slides here, and the visual grade goes progressively darker across the run, cream ground at 046 to near-black `#111111` at 080, then the first crack of gold at 084. **The colour is the argument.**

| Slides | Run | Assets |
|---|---|---|
| 046-050 | The dream. Why you are here tonight | `gen:c12_college_gate_dawn` HERO-BLEED, cream ground |
| **051-055** | **The wins acknowledgment. RESTORED** | `gen:c13_shelf_of_small_wins` IMG-SIDE L + `char:relieved` 052 |
| 056-062 | The first trap. The A that means nothing yet | `html:h01_report_card_a_row` re-entering, now with a `v-mark` red box landing on one row → `gen:c15_trapdoor_under_paper` STOP 060 → `char:uneasy` 061 |
| **063-068** | **The second trap: more reps will break through. RESTORED** | `gen:c16_more_reps_same_wall` HERO-BLEED + **`mermaid:m08_two_paths`** |
| **069-076** | **The consequence cascade. RESTORED, 4 beats** | `char:stuck` 069 and 073 · `gen:c17_burnout_candle` · `gen:c18_confidence_draining` · `gen:c19_hallway_apart` (two figures at opposite ends of a dark hallway) |
| **077-080** | **The fear, fully stated. RESTORED. The highest-voltage sentence in the script** | 077 `gen:c20_senior_year_envelope` STOP on near-black `#111111`, **zero clicks, hold it** · 078 `char:stuck` alone on black · 079-080 `html:` single line, `text-4xl` white |
| 081-083 | The objection: you have been burned before | `char:burned` 081 and 083 + `gen:c23_receipts_fanned` |
| **084-085** | **The permission block. RESTORED. "The problem is not that you tried"** | `char:stuck` 084 turning toward the first gold light + `gen:c24_open_palm_light` 085, the tonal pivot of the whole deck |

Also inside this run, verbatim parent quotes get `layout: quote` at 070, 072, 074, 076. **Blocker:** those four quotes are attributed "Real parent, last month" and the sourcing is unverified. Either Joe confirms them in writing or they ship relabelled as composite. Do not build them until that is ruled.

Also inside: the absolution beat, "this is not your fault," and "most AP teachers have never graded a single AP exam," at 064-066, on `gen:c25_rules_changed_page` and `gen:c26_empty_grading_desk`. **The line "College Board changed the rules" is softened on the slide face to "the exam rewards reasoning and structure, and the rubric is where the points live."** The overstatement about a named organisation does not ship.

---

### S3 — Agenda, future pace, the WHY · slides 086-105 · POLISHED · tempo MOVE-FAST then STOP

Entirely restored material. None of this exists in the current deck.

| Slides | Run | Assets |
|---|---|---|
| **086-090** | **The questions that should be on your mind. RESTORED** | `gen:c27_five_questions_doors` REVEAL-CARDS, one door per question, `<v-clicks>`. Claim-stripped: no guarantee, no dollar figure |
| **091-097** | **The future-pace ladder. RESTORED** | `gen:c29_exam_hall_walkout` HERO-BLEED 091 · `gen:c22_packed_schedule_asset` 094, the only slide in the deck that speaks to the student-athlete · `char:leaning` 095 · `gen:c30_horizon_road` 097 |
| **098-105** | **The WHY block. RESTORED. The single highest-value chat interaction in the script** | 098 `gen:c31_hand_on_chest` NAVY-CARD, "I want your answer in the chat, and not just any answer" · 099 `char:with-teen` · 100-102 `gen:c32_letter_at_the_door`, `gen:c33_who_else_lifted` (concentric cream rings on navy) · 103-105 `html:` chat-harvest cards |

**Note for the presenter track:** slides 098 to 105 are the deck's only true open-ended chat ask. Every other prompt is "type YES." Real answers are what keep a room to the CTA. The `[PAUSE]` markers matter more here than anywhere.

---

### S4 — Positioning · slides 106-129 · **BEHIND-THE-SCENES** · tempo FRAME

Register switches here and the visual grammar switches with it: **`slidev-addon-fancy-arrow` Rough.js hand-drawn marks are permitted from 106 to 259 and nowhere else in the deck.** That is the register signal. Polished `<Arrow>` never appears inside this range.

| Slides | Run | Assets |
|---|---|---|
| 106-109 | Who am I, fair question | `real:dr_joe_2026.jpg` IMG-SIDE L, cut to a soft cream field. **The first human photograph in the deck, at slide 106.** |
| **110-116** | **Joe's origin moment. RESTORED, 90 words, currently absent entirely** | `gen:c34_years_of_classrooms` (a receding row of empty desks) · `gen:c35_system_gears_misaligned` · `gen:c36_incomplete_map` · `FancyUnderline` under "incomplete information" |
| 117-121 | Credentials, and the products behind them | **`real:university_course_catalog_composite.png`** ZOOM at 118, the 34-course mosaic, with three `<v-clicks>` callouts · `real:university_courses_grid_01.png` 119 · `real:university_calendar.png` 120 · `real:05_ap_strat_tool.png` 121 |
| 122-124 | Why I share this with you | `char:burned` 118 already placed, here `gen:c37_room_from_inside` |
| 125-127 | The big promise | `gen:c38_bridge_across` HERO-BLEED |
| **128-129** | **The commitment ask. RESTORED. "Then would you commit to me to take action"** | `gen:c39_two_hands_meeting` STOP + `v-mark` circle on "commit". One slide, no clicks, then the ask |

**All four banned aggregate claims are deleted from this section and not replaced.** No "600+ students," no "$2.8 million," no "95% earn college credit," no "150+ perfect 5s." The section's proof is now: Joe's face, the real platform, the 34-course catalog, and the one cleared claim already spent on slide 041. **Named proof, Nabila, Laura and Avery, enters at 122 to 124 as three short outcome lines with no dollar figures and no school names**, each on `html:` cards beside `real:university_courses_grid_02.png`.

---

### S5 — Mechanisms · slides 130-183 · **BTS** · tempo MOVE-FAST

Currently at roughly 50% of the script's argument. Every named component, analogy, phase system and outcome block from the audit sections 2.14, 2.15 and 2.16 is restored here.

**Mechanism 1, AP Insider Intelligence, 130-149**

| Slides | Run | Assets |
|---|---|---|
| 130-133 | The exam is a skill test, not a content test | **`html:h10_two_scorecards_split`** returning as the full hero, two-cols, `<VSwitch>` between them · `char:leaning` 131 |
| 134-137 | The poker analogy, the language analogy | `gen:c41_rules_versus_game` · `gen:c42_speaking_grader` |
| **138-143** | **The three named components. RESTORED: Rubric Revelation, Pattern Recognition, Expectation Management** | REVEAL-CARDS, one Iconify per card (`i-mdi-file-document-outline`, `i-mdi-eye-outline`, `i-mdi-target`) over `gen:c40_seeing_the_pattern` · `char:uneasy` 143 |
| **144-147** | **Implementation. RESTORED: analysis before creation, Reverse Engineering, Grader Empathy** | **`mermaid:m12_reverse_engineering_loop`** 145 · `gen:c44_target_made_visible` 146 |
| **148-149** | **The outcome block. RESTORED: "they will stop asking is this good enough, because they will know"** | `gen:c43_lens_over_page` STOP |

**Mechanism 2, Subject-Specific Response Mastery, 150-168**

| Slides | Run | Assets |
|---|---|---|
| 150-153 | Drive safely analogy, chef versus cooking show | `gen:c45_road_without_rules` · `gen:c46_kitchen_versus_studio` |
| 154-156 | A different key for each lock | `gen:c47_key_per_lock` HERO-BLEED |
| **157-162** | **Per-subject depth. RESTORED from 4 one-line bullets to 6 slides** | History `mermaid:m07_dbq_seven_paragraph` · Sciences `html:h11_frq_step_map` · English `gen:c48_blueprint_english` · Math `html:` process-point card. **This is the beat where a parent decides whether Joe actually knows the subject.** It is currently one slide. |
| **163-167** | **Template, Practice, Perfect. RESTORED, the whole phase system** | **`mermaid:m05_template_practice_perfect`** ZOOM, three phases revealed by `<v-clicks>` · `gen:c49_scaffold_to_freehand` |
| 168 | Structure first, then content, and why most prep inverts it | `gen:c52_automatic_execution` STOP |

**Mechanism 3, Pre-Grade Confidence System, 169-183**

| Slides | Run | Assets |
|---|---|---|
| 169-171 | The stakes without it, second-guessing and changed answers | `gen:c53_cook_who_never_tastes` IMG-SIDE R · `char:leaning` 172 |
| **172-177** | **The three components. RESTORED: Internal Scoring Calibration, Performance Forecasting, Gap Analysis Mastery** | REVEAL-CARDS over `gen:c55_calibration_dial` · `gen:c56_forecast_gauge` · `gen:c57_gap_xray` |
| **178-181** | **The four phases. RESTORED. Phase 4 is the strongest proof in the section and is currently absent entirely** | **`mermaid:m06_pregrade_four_phases`** with Phase 4 revealed last and `v-mark` boxed |
| 182-183 | The Score Forecast Report, and Hope is not a strategy | **`html:h09_score_forecast_report`** ZOOM, a CSS-built report card with "Projected: 5" revealed on click. **Text-bearing, so HTML, never generated.** |

**Claim control:** the Bryce practice-exam story is recast onto one of the three cleared names at 180. Line 1202's "we have sat in the rooms where College Board trains graders" is rewritten to "our coaches have scored AP exams," **and only ships if that is literally true of the current coaching staff.** That needs Joe's confirmation.

---

### S6 — The Demonstration · slides 184-245 · **BTS** · tempo ZOOM

**62 slides, and the guide's instruction for this section is verbatim: "Actual content on screen. This IS the visual, no stock here."** The current deck spends its largest section on this and puts zero essay text, zero rubric and zero scoreboard on screen. This is the single highest-leverage fix in the build, and **almost none of it is a generated image.** It is HTML and SVG.

| Slides | Run | Assets |
|---|---|---|
| **184-189** | **The disarm. RESTORED: "you have not been in a history class for 20 years"** | `gen:c60_two_sealed_envelopes` · `char:realising` 189 |
| 190-193 | Two real openings, same prompt, both students got A's in class | **`html:h03_essay_a_text`** and **`html:h04_essay_b_text`**, two-cols, monospace-adjacent serif at `text-2xl`, cream card on navy |
| **194-198** | **The CAN'T TELL poll. RESTORED. The highest-value single restore in the audit** | 194 the ask, `v-mark` circle red on "CAN'T TELL" · 196 **the payoff: "your teen cannot tell either"** STOP, `text-5xl`, no clicks. The current deck's poll, "which one scored a 5," is a guessing game. This one is a diagnosis. |
| 199-204 | The actual rubric revealed | `gen:c61_vault_opening` 199 then **`html:h05_rubric_line_contextualization`**, the real rubric line set as a document card, `FancyUnderline` landing under "describes a broader historical context" |
| **205-214** | **Contextualization scored, both essays, one criterion at a time** | `<VSwitch>` between A and B · chat vote before each answer · **`html:h07_scoreboard_running`** appears at 210 and **stays on screen for the rest of the section**, updating by click. Restore "This is a classroom A. But it is an AP fail." at 209 |
| 215-224 | Thesis scored, both essays | `<VSwitch>` + Magic Move morphing A's generic thesis into B's specific one at 220, which is exactly what Magic Move is for. Restore the "generic thesis" label at 217 |
| 225-234 | Evidence, Analysis, Complexity, fast | MOVE-FAST, `html:h07` incrementing on every click · `char:realising` 231 |
| **235-240** | **Final scores** | **`html:h08_scoreboard_final`** STAT-HERO, `text-8xl`. **Fix the arithmetic before building this slide, see below.** |
| 241-243 | Both got A's. One understood the game | `gen:c63_same_knowledge_split` two-cols + `v-mark` circle gold on "game" |
| 244-245 | Type MIND BLOWN | `gen:c62_struck_bell` STOP |

**The arithmetic defect that must be fixed before slide 235 is built.** The deck's Essay B line items sum to 8 and it reports 7 of 7. The script's Essay A sums to 2 and reports 3 of 7. Root cause: the real APUSH DBQ rubric is 7 points as Thesis 1, Contextualization 1, Evidence 3, Analysis and Reasoning 2, where **complexity is one of the two Analysis points, not a sixth separate criterion.** Both documents double-count it. **Rebuild ruling: five criteria displayed, Thesis 1, Contextualization 1, Evidence 3, Analysis and Reasoning 2, totalling 7. Essay A = 2 of 7. Essay B = 6 of 7.** Then fix the setup line at the top of the section, currently "one scored a 3," to match 2 of 7. `html:h07` and `h08` are built from a single JS object so the running total is computed, never typed. **The one parent in the room who checks will check this one.**

---

### S7 — The post-demo payoff and the bridge · slides 246-259 · **BTS** · tempo STOP

Currently missing entirely. Fourteen script lines of the best payoff in the document, gone. The deck goes from "that is the invisible scoring gap" to "type MIND BLOWN" to the recap with no meaning made.

| Slides | Run | Assets |
|---|---|---|
| 246-249 | They stop guessing. They read a prompt and know | `char:realising` 247 · `gen:c66_walking_in_knowing` |
| **250-252** | **"The anxiety disappears because the mystery disappears." The thesis sentence of the whole webinar, and it is currently not on a slide** | 250 `char:winning` · **251 the line alone, `text-5xl` white on near-black, `gen:c64_fog_dissolving` behind at 15% opacity, zero clicks, hold it.** This is the STOP slide of the deck |
| 253-255 | And that was one criterion, one essay type | `char:realising` 253 · `gen:c67_one_of_many_doors` |
| **256-259** | **The bridge. RESTORED: "that was JUST Mechanism 1" plus Grader Vision** | **`mermaid:m04_three_mechanisms_flow`** ZOOM, all three named, then `gen:c59_grader_vision_eye` STOP. Without this the demo just ends |

---

### S8 — Recap · slides 260-271 · POLISHED · tempo MOVE-FAST · density LOW by design

Eleven script items, currently 6, all emotional, **and not one of the three mechanisms is named**, so the parent leaves with no retrievable label for what they just bought into. Restore to 9 items, and name all three mechanisms.

| Slides | Run | Assets |
|---|---|---|
| 260 | Section divider | `gen:c68_thread_pulled_through` DIVIDER |
| 261-269 | Nine callbacks, one per slide, MOVE-FAST | Each slide reuses **a 200px thumbnail of the visual from the moment it recaps**, revealed by `v-click`. That is the recap device: the parent sees the picture again and the memory reloads. Nine reused assets, zero new generations |
| 270-271 | The three mechanisms named, together | `mermaid:m04_three_mechanisms_flow` again, compact |

**All money figures come out of the recap.** The current recap repeats "$95,000 to $125,000 in scholarships." Deleted, not replaced.

---

### S9 — Yes Momentum · slides 272-289 · POLISHED · **ZERO IMAGES, BY DESIGN**

Style guide §1.5: *"7. Yes Momentum | None | Clean slides, text only | Audience internal dialogue, no distractions."* The Brad deck runs its 16-slide Yes-Momentum file at zero image refs on purpose. **These are the sanctioned bare slides and they are the entire bare-slide budget.**

Seven rungs, one question per slide, `[PAUSE]` between each, plus the three rungs the audit found missing:
- the wrong scorecard rung
- **the regret pivot: "if you had this six months ago, everything would be different right now"** at 284. This is the on-ramp to the seasonal ask and it is currently absent
- the payoff cascade at 287 to 289

| Slides | Visual | Note |
|---|---|---|
| 272-283 | **`none`. 12 truly bare slides.** | Navy field, one question, `text-4xl` white, `v-click` reveal of the question then a second `v-click` on the pause beat. **Animated, therefore G5 passes with zero imagery** |
| 284-286 | `v-mark` only | `<span v-mark="{ at: 1, color: '#C5A55A', type: 'circle' }">six months ago</span>`. Counts as a visual under §3.1, so these three are not charged to the bare budget |
| 287-289 | `none`. 3 bare. | The payoff cascade, three short lines |

**Bare total: 15. Exactly at budget. No other slide in the deck may be bare.**

---

### S10 — The back-to-school turn · slides 290-301 · POLISHED · tempo LAND

The seasonal argument the whole deck is built on finally gets its own block instead of being buried in the close.

| Slides | Run | Assets |
|---|---|---|
| 290-292 | You have those six months right now | `gen:c69_six_months_runway` HERO-BLEED · `char:deciding` 291 |
| **293-295** | **The first six weeks window** | **`mermaid:m09_first_six_weeks_window`** ZOOM, the term timeline from slide 017 returning, now with a gold window drawn over weeks 1 to 6. **The same diagram opening and closing the argument is the deck's strongest structural device** |
| 296-298 | Ahead versus reactive | `char:with-teen` 296 + `gen:c71_two_paths_fork` two-cols |
| 299-301 | What the fall looks like from here | `gen:c76_calm_exam_morning` · `char:winning` 300 |

---

### S11 — The booking ask · slides 302-315 · POLISHED · tempo LAND

**No price. No value stack. No guarantee. No scarcity block. No two-paths close. No FAQ. No downsell. John's ruling holds and nothing from script lines 187 to 505 comes back.**

| Slides | Run | Assets |
|---|---|---|
| 302-304 | Not to sell you anything. To build you a plan | `gen:c73_plan_on_the_table` HERO-BLEED |
| 305-307 | What the call actually is | `char:deciding` 305 + **`real:03_booking_strategy_call.png`** ZOOM, an actual screenshot of the real booking flow the parent is being asked to enter. **This is BTS register doing its job at the exact moment it matters** |
| **308-309** | **What happens on the call and in the 48 hours after** | **`mermaid:m10_what_happens_next`**, the shape stolen from the script's post-enrollment timeline and repointed at the call. Currently three thin bullets |
| 310-311 | Who this is for | `char:with-teen` 310 |
| **312-313** | **The CTA. Rebuilt.** | **`html:h14_qr_card`**, QR on a white card, plus the URL in monospace at `text-3xl`, plus a chat-drop instruction. `char:winning` 313. **The current CTA is gold text on a gold background, contrast 1:1, the most important line in the webinar rendered invisible. The rebuilt CTA is `text-white` on navy `#1B365D`, full stop.** |
| 314 | No pressure either way. You leave with a real plan | `gen:c75_open_door_light` STOP. The strongest single line in the close |
| 315 | End card | `real:logo.png` + `char:winning` + `layout: end` |

**Build blocker:** `{{BOOKING_LINK}}` at line 3036 is unresolved and `[ QR CODE ]` is literal text. The QR cannot be generated until John supplies the real URL. Generate with the `qrcode` npm package and **verify the decode with jsQR plus pngjs before it ships.** Also fix the third seasonal speaker-note variant, currently labelled AUGUST and duplicating the first.

---

## 3. THE HERO VISUALS

Twelve moments that carry the whole argument and earn a custom build rather than a stock treatment. **Ten of the twelve are code, not generated images.** That is the correct ratio for a deck whose argument is about scoring.

| # | Hero | Slides | Form | Why it is a hero |
|---|---|---|---|---|
| **H1** | **The term timeline, front-load / back-load** | 017, and again at 293-295 | **Mermaid** `m01_term_timeline` | The core thesis is a timeline: content arrives first, the rubric is tested last, so the first report card is measuring the wrong thing. Currently three centred sentences. Opening and closing on the same diagram is the deck's spine |
| **H2** | **The two scorecards split** | 018-022, returning 130-133 | **SVG**, `h10_two_scorecards_split` | Classroom scorecard versus exam scorecard, side by side, same student. `<VSwitch>` to flip between them. This is the single image the whole webinar exists to plant |
| **H3** | **Essay A versus Essay B** | 190-193, then throughout S6 | **HTML**, `h03` / `h04` | Real student text on screen. Text-bearing, so never generated. Two-cols, cream cards on navy, `text-2xl` floor |
| **H4** | **The rubric line, as the document it is** | 199-204 | **HTML card + FancyUnderline** | "Contextualization, 1 point. Describes a broader historical context relevant to the prompt." The moment the invisible becomes visible |
| **H5** | **The running scoreboard** | 210-240, persistent | **HTML + JS-computed**, `h07` / `h08` | Updates on every click, stays on screen for 30 slides. Computed from one data object so the arithmetic cannot drift |
| **H6** | **Exam score composition, free response is more than half** | inside S1, slide 020 | **Mermaid pie or SVG stacked bar**, `m02` | The seasonal argument depends on this being visually obvious. It is currently a sentence |
| **H7** | **The DBQ seven-paragraph map** | 157-159 | **Mermaid** `m07` | Turns "we teach structure" from a claim into a thing you can see. The script's own outcome line is already a paragraph-by-paragraph list, which is a diagram written as prose |
| **H8** | **Template, Practice, Perfect** | 163-167 | **Mermaid** `m05` | Three phases with week markers. Restored material, currently absent |
| **H9** | **The Pre-Grade four phases** | 178-181 | **Mermaid** `m06` | Phase 4, real-time mid-exam adjustment, is the most concrete claim in the mechanism section and is currently nowhere |
| **H10** | **The Score Forecast Report** | 182-183 | **HTML**, `h09` | A CSS-built artifact with "Projected: 5" on a click. Concrete where the script was abstract |
| **H11** | **89% versus about 22%** | 041, once only | **SVG two-bar**, `h15` | The one cleared aggregate claim, given a real chart so it lands once and hard, with `results vary` set beneath it |
| **H12** | **The three mechanisms working together** | 256-259, again 270-271 | **Mermaid** `m04` | The bridge out of the demo. Its absence is why the demo currently just stops |

**Excalidraw is used for exactly one thing:** `assets/rubric_scorecard.excalidraw`, the hand-drawn rubric scorecard at 205, because a hand-drawn scorecard in the BTS register reads as Joe's own working, which is the entire point of that register. Prop name is `drawFilePath`, verified in `node_modules/slidev-addon-excalidraw/components/Excalidraw.vue`.

---

## 4. THE ANIMATION PASS

Zero slides without animation. Do not write 315 individual animation calls. **Nine slide types, one rule each. Every slide is tagged with a type in the visual map, and the type determines the animation.**

| Type | Where | Rule | Exact component |
|---|---|---|---|
| **T1 DIVIDER** | Section opens, 8 slides | Title rises and fades in, no clicks | `v-motion :initial="{ y: 30, opacity: 0 }" :enter="{ y: 0, opacity: 1 }"` |
| **T2 HERO-BLEED statement** | ~55 slides | Image scales in, then one `v-mark` lands on the punch word | `v-motion` scale 1.04 to 1.0 + `<span v-mark="{ at: 1, color: '#C5A55A', type: 'circle' }">` |
| **T3 STAT-HERO** | ~22 slides | Number rises from below, `v-mark` box lands after | `v-motion :initial="{ y: 60, opacity: 0 }"` + `v-mark.box` |
| **T4 REVEAL-CARDS** | ~70 slides, every 2+ list | Sequential reveal, always | `<v-clicks>` wrapping the list. `depth="2" every="2"` on nested lists |
| **T5 TWO-COL comparison** | ~40 slides | Left column on click 1, right on click 2, verdict on click 3 | `<div v-click="1">` / `<div v-click="2">` / `<VSwitch>` where it is a swap rather than a comparison |
| **T6 QUIZ card** | 30 slides in S1 | Statement in, chat gate, then the TRUE or FALSE stamp scales in | `v-click.fade.up` on the statement, `v-motion :click-2="{ scale: 1 }"` on the stamp |
| **T7 DEMO / SCOREBOARD** | ~50 slides in S6 | One click per criterion, scoreboard total increments, `v-mark` on the point awarded or missed | `v-click` chain + `{{ $clicks }}` driving the computed total. Magic Move at 220 only |
| **T8 MERMAID / ZOOM** | ~20 slides | Diagram fades in, then annotation callouts reveal beside it | `v-motion` on the diagram wrapper + `<v-clicks>` on the callout list |
| **T9 BARE, S9 only** | 15 slides | The question reveals, then the pause beat reveals | `<v-click>` on the question, `<v-click>` on the beat line. **Two clicks, zero imagery, gate passed** |

**Directional entries alternate by slide parity** so the deck does not tic: odd slides `v-click.fade.up`, even slides `v-click.fade.right`. Set once in the map, not per slide.

**Motion is never decorative.** Every `v-motion` in this deck is on a hero element at a beat. Anything else gets cut in QC.

**`layout: cover` is mandatory on every slide using `absolute inset-0` or `<Arrow>` / `<FancyArrow>` coordinates.** Without it absolute children collapse to 0x0 and paint nothing. That is the Invisible-Render Law and it has cost this codebase four shipped-blank builds.

---

## 5. THE LAYOUT ROTATION

Current state: `layout: center` on 137 of 174 slides, 78%, with 18 runs of 3 or more identical consecutive layouts and a longest unbroken run of 14 across the entire close.

**The rotation is a 6-beat cycle, driven by tempo, applied per run rather than per slide:**

```
cover  ->  two-cols  ->  center  ->  image-left  ->  default  ->  image-right  ->  (repeat)
```

with three injections that also break runs:
- `layout: quote` on **every** verbatim parent quote, no exceptions
- `layout: center` on navy as a DIVIDER at each section open, exactly one slide
- `layout: cover` on every HERO-BLEED and every absolute-positioned slide

**Two hard invariants, enforced by a lint script, not by eye:**
1. **No layout value appears 3 times consecutively.** Ever.
2. **Within any rolling window of 10 slides, at least 4 distinct layout values appear.**

**Two content invariants from the style guide:**
3. `two-cols` on **every** comparison moment. This deck has at least 14: classroom versus exam, Essay A versus B on every criterion, content knowledge versus exam performance, hope versus system, ahead versus reactive. It currently uses `two-cols` five times.
4. `image-left` and `image-right` **alternate**. Never 3 IMG-SIDE slides on the same side in a row.

Budget after rotation, approximate: `center` ~90 (29%, down from 78%), `cover` ~60, `two-cols` ~55, `default` ~45, `image-left` ~30, `image-right` ~30, `quote` ~4, `end` 1.

**The lint script is the deliverable, not the intention.** `scripts/layout_lint.py` parses the frontmatter of every slide, asserts both invariants, and exits non-zero. It runs in the same pass as the gate table.

---

## 6. BUILD ORDER

Five stages. **Each stage ends with something shippable**, so work is never stranded half-built.

### Stage 0 — Stop the bleeding. 30 minutes. Ships a deck that does not 404.
1. `mkdir -p public/images` and copy `06_Clients/supported/brand/supported_logo_with_name.png` to `public/images/logo.png`. **One command fixes 173 broken renders.**
2. Copy `dr_joe_2026.jpg`, the 9 university finals, and `03_booking_strategy_call.png` / `05_ap_strat_tool.png` / `06_acingapexams_home.png` into `public/images/`. **17 real assets, zero generation cost.**
3. Move all CSS out of the inline `<style>` block into co-located, unscoped `style.css` with `.sup-` prefixed classes. Inline `<style>` is scoped per slide and `:root` vars die there.
4. **Strip the four banned claims** at lines 999-1005 and 1117, plus the money figures at 832, 834, 2778, 2945, 2646. Recast Bryce.
5. **Fix the gold-on-gold CTA.** Navy ground, `text-white`.
6. Pin `colorSchema: light` in the headmatter.
7. `pnpm add slidev-addon-fancy-arrow` and register both addons.

### Stage 1 — The visual map. Half a day. **No slide gets written until this exists.**
Write `_VISUAL_MAP.md` in the Brad format, all 315 rows, columns: id, headline at 7 visible words maximum, tempo, emotion, VISUAL slug, treatment, animation type T1 to T9, claim-flag. **The VISUAL column may be blank on no more than 15 rows, and all 15 are in S9.** This file is simultaneously the shopping list for the image batch and the build contract for the section files. **Skipping this step is precisely why the deck has zero images today.**

### Stage 2 — The highest-impact 40 slides. One day. Ships a demo-able core.
Not the first 40. **The 40 that carry the argument:**

| Slides | What | Count |
|---|---|---|
| 190-193, 199-214, 235-240 | **The demonstration core**: essay text, the rubric line, contextualization scored, the final scoreboard. All HTML and SVG, zero image generation, and it is the section the guide rates HIGH density and the deck currently rates zero | 26 |
| 017, 018-022 | **H1 term timeline + H2 two scorecards.** The spine | 6 |
| 194-196 | **The CAN'T TELL poll and "your teen cannot tell either."** The highest-value single restore in the audit | 3 |
| 251 | **"The anxiety disappears because the mystery disappears."** The thesis sentence, currently not on a slide | 1 |
| 312-315 | **The rebuilt CTA**, contrast-correct, QR on white | 4 |

**40 slides. Of those, 33 are HTML, SVG or Mermaid.** Only 7 need generated imagery. Stage 2 is therefore mostly code, and it can start before a single image comes back from the model.

### Stage 3 — The image batch. One day of wall clock, mostly unattended.
1. Fork `runner_brad.py` to `runner_supported.py` with the SupportED preamble from §1.2.
2. Write `images_config_supported.json`: 76 concept slugs plus 9 character states.
3. **Character first**, N=4 candidates, curate to 1, then condition the remaining 8 on the winner. Contact-sheet check at 200px.
4. Concepts, N=3 candidates each, curate to 1. **Curate. Do not fire and forget. Killing the generic one is the step that fixes "weak imagery."**
5. `cutout.py` chroma-key pass on the 9 character PNGs, alpha-edge verified.
6. Compress. **Nothing over 500KB.** Note `01_ap_application_funnel.png` is 810KB and `05_ap_strat_tool.png` is 1.68MB, both need resizing before they enter `public/`.

### Stage 4 — Sections and the script. Two days.
Build the 12 section files at the §2 targets, wiring every visual, every animation type, the rotation.
**In the same pass, port the script into speaker notes.** The deck currently carries 269 of 10,980 script words, 2.4%. `[click]`-marked, section by section, register declared in a header comment at the top of each file. **A presenter cannot run the deck without this, and John's stated requirement is that the entire script is in there.**

### Stage 5 — QC. Half a day.
1. `scripts/gate_table.py`: G1 through G20, exits non-zero on any fail.
2. `scripts/layout_lint.py`: the two rotation invariants.
3. `scripts/claim_lint.py`: greps for every banned string, exits non-zero on a hit. **Run this on every commit, not once.**
4. **Then screenshot and LOOK at all 315 slides at 1280x720, advancing every `v-click`.** The gold-on-gold CTA would have passed every automated check ever written. An assertion that passes is not a picture that works.

---

## 7. HONEST EFFORT ESTIMATE

### What gets built, by class

| Class | Distinct assets | Slides covered | Notes |
|---|---|---|---|
| **Generated concept images** (`gen:`) | **76** | ~150 | At N=3 candidates, **228 model calls**. At roughly 20s each, about 76 minutes of API time, plus curation |
| **Character states** (`char:`) | **9** | 31 | At N=4 on state 1 and N=3 on the rest, **28 model calls**, plus the chroma-key and alpha-verify pass |
| **HTML / CSS / SVG builds** (`html:`) | **17** | ~70 | All text-bearing visuals. The heaviest single item is `h07`/`h08`, the JS-computed scoreboard persisting across 30 slides |
| **Mermaid diagrams** (`mermaid:`) | **12** | ~28 | Zero install, native, survives PDF export |
| **Excalidraw** | **1** | 2 | The hand-drawn rubric scorecard, BTS register only |
| **Real assets already on disk** (`real:`) | **17** | ~24 | Logo, Joe, 9 university finals, 3 funnel screenshots, 3 charts. **Zero generation cost, and 9 of them are already compliance-cleared** |
| **Iconify** | ~20 icon calls | ~35 | The cheap path to 2-to-4 elements per slide on card and list runs. No emoji, they render as tofu in the headless build |
| **Bare, by design** | 0 | 15 | S9 only |
| **TOTAL distinct assets** | **132** | **315** | |

### Time

| Stage | Effort | Ships |
|---|---|---|
| 0 Stop the bleeding | **30 min** | A deck whose logo renders, whose CTA is visible, and which carries no banned claims |
| 1 The visual map, 315 rows | **4 to 5 hours** | The build contract and the shopping list |
| 2 The highest-impact 40 | **1 day** | A demo-able core: the whole demonstration, the spine diagrams, the close. 33 of 40 are code |
| 3 Image batch, 256 model calls, curate to 85 | **1 day wall clock**, ~2 hours attended | `public/images/` fully populated |
| 4 Sections plus the 10,980-word script into notes | **2 days** | The full 315-slide deck, presenter-runnable |
| 5 QC: 3 lint scripts plus 315 eyes-on screenshots | **4 hours** | Gate table green, and a human has seen every slide |
| **TOTAL** | **~4.5 working days** | |

### What a realistic first pass actually covers

**Stages 0 through 2, about one and a half days, is the honest first pass.** It delivers: no broken logo, no banned claims, a visible CTA, the complete demonstration section with real essay text and a live scoreboard, the two spine diagrams, the restored CAN'T TELL poll, and the deck's thesis sentence on a slide. **That is roughly 60 of 315 slides fully built, and it is the 60 that decide whether the webinar works.**

It does **not** cover: the pain section's full CFA restoration, the WHY block, Joe's origin story, the mechanism components and phase systems, or the speaker-note track. Those are Stage 4, and Stage 4 is the one that cannot be compressed, because 10,980 words of script have to be read and placed by a human judgment about where each `[click]` falls.

### The two failure modes to plan against

1. **Character consistency across nine states is the single hardest technical item in the plan.** Budget a second batch. If reference conditioning does not hold the face and the cardigan across all nine, fall back to back-view and three-quarter-away framing on states 3, 4 and 7, where posture carries the emotion anyway and the face is doing the least work.
2. **The demonstration section is 62 slides of interlocking state**, one scoreboard persisting across 30 of them. Build it from a single data object, never by typing totals onto slide faces. The current deck's totals do not add up in either direction, and that is exactly what typing them produces.

---

## 8. BLOCKERS THAT NEED A RULING BEFORE STAGE 4

1. **`{{BOOKING_LINK}}`** is unresolved at line 3036. The QR at slide 312 cannot be generated or decode-verified without the real URL.
2. **The four parent quotes** attributed "Real parent, last month" have unverified sourcing. Joe confirms in writing, or they ship relabelled as composite. They currently occupy slides 070 to 076.
3. **"We have sat in the rooms where College Board trains graders"** rewrites to "our coaches have scored AP exams," and only if that is literally true of the current staff.
4. **Mechanism architecture conflict.** `Webinar_Offer.md` names a **4-step Comprehensive Score Certainty System**; the deck teaches **3 breakthroughs**. Two architectures for one client, and the booking call will use the 4-step language. **Someone rules which is canon before S5 is built**, because S5 is 54 slides and a rebuild costs a day.
5. **The attendance bribe** (the free AP Success Starter Kit) is neither in nor out. Either fold it into the call, "you leave the call with your teen's AP map," or drop it deliberately. Right now the deck has no stick strategy at all beyond asking for 45 minutes.