# PER-SLIDE VISUAL MAP — Brad Evergreen "60+ Programs" (the ~100-slide build shopping list)

> The reference-sheet discipline applied to the whole deck. One row per slide. Drives BOTH the concept-image batch (every `gen:` slug → `images_config_brad.json`) AND the section-file build (every agent builds to THIS map). Source copy = `_SCRIPT.md` (speaker notes verbatim). Bar = `_BUILD_SPEC_V2_imagery.md`.
>
> **Columns:** `id` · on-slide headline (≤7 visible words) · tempo (FRAME/MOVE-FAST/STOP/ZOOM/LAND) · emotion · **VISUAL** (`his:img-NNN` real asset | `gen:cNN_slug` concept image | `html:` CSS-built | `none` navy card) · treatment · animation · `foot` = standing compliance footer on.
>
> **Visual system (LOCKED):** every generated concept image is the flat-editorial orange `#FF7300` / deep-navy `#011937` / brand-navy `#0A3466` / cream `#FBF6EF` / white set (see `assets/gen/runner_brad.py` preamble). His real photos sit on orange/navy fields with a consistent frame. NEVER generate testimonial faces (his real img-102/103 only). NEVER fabricate a real eligibility map (his real img-072 only, framed at native size + hi-res-resource flag).
>
> **Rules in force:** ≤7 visible words on hooks · v-clicks on every 2+ list · NO em-dash · NO emoji (Iconify/text) · NO fake mid-slide button (Rule 11) · content-fits-frame (Rule 9) · `layout: cover` on full-bleed (Rule 8) · brand classes in `style.css` `.hbs-*` (Rule 7) · `v-mark` object-form for brand hex.

---

## Treatments legend (consistent visual grammar across the deck)
- **HERO-BLEED** — full-bleed concept image, headline in a frosted/solid card. `layout: cover`.
- **IMG-SIDE** — image one half, copy the other (proof/positioning beats). alternate L/R so no 3 in a row same side.
- **STAT-HERO** — centered giant number/word on orange or navy, image as accent. (60+, 620/640, 3 ingredients).
- **ORANGE-STATEMENT** — full orange field, big white/navy condensed caps. the brand's default "shout" slide.
- **NAVY-CARD** — deep-navy `#011937` field, white caps + orange accent word. title cards + ALL yes-momentum (zero images).
- **REVEAL-CARDS** — 2-4 cards/chips revealed via `<v-clicks>`, each with its own small concept image or Iconify icon.
- **ZOOM** — one image big, `<v-clicks>` reveal annotation callouts beside it (the map, the 401k).
- **DIVIDER** — navy→deep-navy gradient section break, section title + Iconify, 1 slide between Fladlien sections.

---

# SECTION FILE: opening.md — O1-O7 (Fladlien §1-3) · target ~21 slides

| id | headline (≤7 words) | tempo | emotion | VISUAL | treatment | anim | foot |
|---|---|---|---|---|---|---|---|
| op-01 | Programs for first-time buyers | FRAME | curiosity | `his:img-019` (Brad cutout) over `gen:c01_horizon_home` bg + `his:img-021` logo TR | HERO-BLEED cover, search-bar frame device | motion fade-rise on Brad | – |
| op-02 | You'll be happy to be wrong | FRAME | intrigue | `gen:c08_hidden_door` | HERO-BLEED, headline card | fade | – |
| op-03 | Where is your new home? | FRAME | aspiration | `gen:c02_picture_home` | HERO-BLEED, one line | – | – |
| op-04 | WHERE is it? | FRAME | aspiration | `gen:c02_picture_home` (dimmed) | text-over-image, 1 v-click line | v-click | – |
| op-05 | WHAT does it look like? | MOVE-FAST | aspiration | `gen:c03_house_shapes` (1-story/2-story silhouettes) | REVEAL-CARDS (3 room ideas) | v-clicks | – |
| op-06 | HOW does life change? | STOP | longing | `gen:c04_keys_in_hand` (silhouette at own front door) | HERO-BLEED, hold | – | – |
| op-07 | Some are restrictive and tricky | MOVE-FAST | wary | `gen:c05_red_tape` (navy maze / red tape) | IMG-SIDE L | fade | – |
| op-08 | Loopholes you can drive a truck through | MOVE-FAST | intrigue | `his:img-004` (Mack truck on orange) | HERO-BLEED | motion | – |
| op-09 | Some so easy you'll be furious | ORANGE-STATEMENT | regret→hope | `gen:c06_furious_waited` (tree seedling beside grown tree) | ORANGE-STATEMENT | v-mark on "furious" | – |
| op-10 | Plant the tree today | FRAME | resolve | `gen:c07_plant_tree` (single tree, sunrise) | IMG-SIDE R | fade | – |
| op-11 | How are you feeling right now? | STOP | named anxiety | `gen:c09_anxiety_fog` (figure in navy fog) | NAVY-CARD + Iconify feeling row | – | – |
| op-12 | Concerned · Stressed · Anxious | STOP | named anxiety | Iconify `i-mdi-emoticon-worried/confused/sad-outline` | REVEAL-CARDS (feeling words, NO emoji) | v-clicks | – |
| op-13 | Congratulations. You're a first-time buyer | FRAME | relief/belonging | `gen:c10_you_belong` (many silhouettes at one door) | ORANGE-STATEMENT | v-mark | – |
| op-14 | Our goal: whew, we got this | FRAME | relief | `his:img-010` (calm sunset) | NAVY-CARD over image | fade | – |
| op-15 | You walk away with a plan | MOVE-FAST | control | `gen:c11_clear_path` (fog lifting to clear path) | IMG-SIDE L | fade | – |
| op-16 | Watch through and book to get: | MOVE-FAST | reward | `gen:c12_gift_stack` (3 wrapped shapes) | REVEAL-CARDS header | – | – |
| op-17 | The free book | MOVE-FAST | reward | `html:book_mock` (navy book, orange spine, HTML title overlay "The Texas First-Time Homebuyer Blueprint") | REVEAL-CARDS card 1 | v-click | – |
| op-18 | The full 60+ program list | MOVE-FAST | reward | `html:list_mock` (document card, "60+ PROGRAMS" overlay) | REVEAL-CARDS card 2 | v-click | – |
| op-19 | A $50 Amazon gift card | MOVE-FAST | reward | Iconify `i-mdi-gift` on orange chip (no brand logos) | REVEAL-CARDS card 3 | v-click | – |
| op-20 | Not lawyers or magicians, just experts | FRAME | trust/honesty | `his:img-019` (Brad) + `his:img-005` (wand, small) | IMG-SIDE R | fade | – |
| op-21 | Brad Pounds. 23 years. Thousands of families | FRAME | authority | `his:img-019` + `his:img-034` (family) + `his:img-021` logo | IMG-SIDE L, NMLS text footer + `his:img-075` Equal Housing | v-clicks on cred lines | **NMLS footer** |

**Concept images from opening:** c01_horizon_home, c02_picture_home, c03_house_shapes, c04_keys_in_hand, c05_red_tape, c06_furious_waited, c07_plant_tree, c08_hidden_door, c09_anxiety_fog, c10_you_belong, c11_clear_path, c12_gift_stack. HTML mocks: book_mock, list_mock.

---

# SECTION FILE: teaching.md — T1-T18 (Fladlien §4-6) · target ~55 slides · LONGEST

| id | headline (≤7 words) | tempo | emotion | VISUAL | treatment | anim | foot |
|---|---|---|---|---|---|---|---|
| te-01 | THE #1 MISTAKE BUYERS MAKE | ZOOM | recognition | `his:img-035` (roofs on navy) | DIVIDER→ORANGE-STATEMENT | v-mark "#1" | – |
| te-02 | Most buyers screw this up | MOVE-FAST | candor | `gen:c13_wrong_house` (figure at wrong fork) | IMG-SIDE L | fade | – |
| te-03 | First-timers skip first-timer programs | STOP | irony | `gen:c14_money_left` (orange coins left on table) | ORANGE-STATEMENT | v-mark | – |
| te-04 | Follow the money | MOVE-FAST | insight | `gen:c15_follow_money` (orange trail to a hand) | IMG-SIDE R | fade | – |
| te-05 | WHAT A PROGRAM ACTUALLY IS | FRAME | clarity | `his:img-039` (5-icon FTHB row) | STAT-HERO header | – | foot |
| te-06 | Tied to the location | MOVE-FAST | clarity | Iconify `i-mdi-map-marker` + `gen:c16_street_split` (one side qualifies) | IMG-SIDE L | v-click | foot |
| te-07 | Some have income caps | MOVE-FAST | clarity | Iconify `i-mdi-cash` | REVEAL card | v-click | foot |
| te-08 | Some want you to hold it | MOVE-FAST | clarity | Iconify `i-mdi-calendar-clock` | REVEAL card | v-click | foot |
| te-09 | Some drop your rate | MOVE-FAST | clarity | Iconify `i-mdi-trending-down` | REVEAL card | v-click | foot |
| te-10 | Some are 100% financing | ZOOM | surprise | `gen:c17_hundred_percent` (whole house filled orange, zero) | STAT-HERO | v-mark "100%" | foot |
| te-11 | Don't memorize. The pieces move | FRAME | ease | `gen:c18_puzzle_pieces` (loose orange puzzle pieces) | IMG-SIDE R | fade | – |
| te-12 | A first-timer again in 3 years | MOVE-FAST | surprise | `gen:c19_reopened_door` (door reopening, "3 YR" html) | ORANGE-STATEMENT | v-mark "3 years" | foot |
| te-13 | Sell Friday, buy again Tuesday | MOVE-FAST | insider | `gen:c20_calendar_flip` (calendar flip) | IMG-SIDE L | v-clicks | foot |
| te-14 | 60+ PROGRAMS | ZOOM | abundance | `gen:c21_many_doors` (grid of orange doors) | STAT-HERO giant "60+" | motion scale, HOLD | foot |
| te-15 | You qualify too. Even high earners | ZOOM | hope (AHA #1) | `gen:c21_many_doors` | STAT-HERO | v-mark "you qualify" | foot |
| te-16 | Not too big, not too small | MOVE-FAST | clarity | `gen:c22_goldilocks` (3 houses S/M/L, middle orange) | REVEAL-CARDS | v-clicks | foot |
| te-17 | BUILT TO HELP, NOT BUY IT FOR YOU | STOP | honesty | `gen:c23_hand_up` (a hand up, not a handout) | ORANGE-STATEMENT | – | – |
| te-18 | Who this is really for | FRAME | belonging | `gen:c24_hard_worker` (silhouette clearing low fence) | IMG-SIDE R | v-clicks | – |
| te-19 | RELAX | STOP | relief | `gen:c06_relief_exhale` (regen clean) | NAVY-CARD one word | motion | – |
| te-20 | Down payment is the EASIEST problem | ZOOM | relief (AHA #2) | `his:img-050` (down payment graphic) OR `gen:c25_weight_lifted` | STAT-HERO | v-mark "EASIEST" | foot |
| te-21 | Reduced rates. No PMI. More house | MOVE-FAST | momentum | Iconify row | REVEAL-CARDS | v-clicks | foot |
| te-22 | INGREDIENT 2: YOUR INCOME | FRAME | honesty | `his:img-054` (income graphic) | DIVIDER→IMG-SIDE L | – | foot |
| te-23 | The computer loves a salary | MOVE-FAST | reassurance | `gen:c26_income_streams` (streams merging to one) | IMG-SIDE R | v-clicks | foot |
| te-24 | If it's not on the tax return, it didn't happen | STOP | tough-love | `gen:c27_tax_return` (document + magnifier) | ORANGE-STATEMENT | v-mark | foot |
| te-25 | Stack a three-layer income cake | MOVE-FAST | reassurance | `gen:c28_income_cake` (3 stacked layers) | REVEAL-CARDS (salary/retirement/support...) | v-clicks | foot |
| te-26 | THE BOOGEYMAN: YOUR CREDIT | STOP | named fear | `his:img-056` (credit graphic) OR `gen:c29_boogeyman` (monster shadow small) | NAVY-CARD | – | foot |
| te-27 | You have more control than you think | FRAME | empowerment | `gen:c30_dial_control` (hand on a dial) | IMG-SIDE L | fade | foot |
| te-28 | FAIR CREDIT, NOT GREAT | ZOOM | relief (AHA #3) | `gen:c31_credit_ladder` (low rung glowing orange) | STAT-HERO | v-mark "FAIR" | foot |
| te-29 | 620 opens it. 640 is easier | MOVE-FAST | relief | `html:` ladder card "620 → 640" | STAT-HERO | v-clicks | foot |
| te-30 | 580 is possible, not always smart | MOVE-FAST | honesty | Iconify caution | REVEAL card (hedge) | v-click | foot |
| te-31 | CREDIT: THE 2ND-EASIEST PROBLEM | FRAME | momentum | `gen:c32_fixable` (points climbing orange) | ORANGE-STATEMENT | v-mark | foot |
| te-32 | It stings 3 to 5 seconds, then it's a plan | MOVE-FAST | relief | `gen:c33_coach_shoulder` (two silhouettes at a screen) | IMG-SIDE R | v-clicks | foot |
| te-33 | Credit Karma is not your mortgage score | STOP | myth-bust | `gen:c34_two_gauges` (two different gauges) | ORANGE-STATEMENT | v-mark | foot |
| te-34 | A credit-improvement partner, no promises | MOVE-FAST | help | Iconify handshake | REVEAL card | v-click | foot |
| te-35 | DOWN PAYMENT · INCOME · CREDIT | FRAME | structure | `his:img-068` (3-ingredient bar) OR `gen:c35_three_ingredients` | STAT-HERO 3-up | v-clicks | foot |
| te-36 | That's the whole recipe | FRAME | mastery | `gen:c35_three_ingredients` | ORANGE-STATEMENT | – | – |
| te-37 | SOME WE LOVE. SOME ARE BIGFOOT | MOVE-FAST | insider candor | `gen:c36_three_lanes` (green light / cone / bigfoot) | DIVIDER→REVEAL-CARDS | v-clicks | – |
| te-38 | STATEWIDE + GOVERNMENT PROGRAMS | FRAME | legitimacy (AHA #4 begins) | `his:img-067` (San Antonio map, framed native, hi-res flag) | DIVIDER→IMG-SIDE L | – | foot |
| te-39 | Names that are real | MOVE-FAST | legitimacy | `html:` program chips (My First Texas Home · TSAHC · USDA · VA · MCC) | REVEAL-CARDS chips | v-clicks | foot |
| te-40 | USDA uses old maps | MOVE-FAST | intrigue | `gen:c37_old_map` (map with pin, suburb still "rural") | IMG-SIDE R | v-click | foot |
| te-41 | Veterans: one of the best deals | MOVE-FAST | respect | Iconify `i-mdi-shield-star` | REVEAL card | v-click | foot |
| te-42 | Get part of your interest back | MOVE-FAST | bonus | Iconify `i-mdi-cash-refund` | REVEAL card | v-click | foot |
| te-43 | We tune it to your exact numbers | FRAME | partnership | `gen:c38_tuning_dials` | ORANGE-STATEMENT | – | foot |
| te-44 | CRA PRIVATE PROGRAMS: OUR FAVORITES | FRAME | insider edge | `gen:c39_secret_shelf` (a file glowing in a drawer) | DIVIDER→IMG-SIDE L | – | foot |
| te-45 | Born from a 1977 law | MOVE-FAST | context | `gen:c40_1977` (subtle, redlining→lend) | IMG-SIDE R eyebrow only | fade | foot |
| te-46 | The program lives in a drawer | STOP | secret | `gen:c39_secret_shelf` | ORANGE-STATEMENT | v-mark | foot |
| te-47 | They will not advertise it | MOVE-FAST | insider | `gen:c41_quiet_bank` (bank, finger to lips motif abstract) | IMG-SIDE L | v-clicks | foot |
| te-48 | The one picture you'll never forget | ZOOM | anticipation | `his:img-072` (THE map) framed, dimmed pre-reveal | HERO-BLEED setup | – | foot |
| te-49 | 100% FINANCING ON THE MAP | ZOOM | wonder (AHA #4 lands) | `his:img-072` (THE map, full, native res, framed) | ZOOM + callout cards | v-clicks annotations, HOLD | **foot: eligibility varies** |
| te-50 | Shaded means zero down, no income cap | ZOOM | wonder | `his:img-072` + callouts | ZOOM | v-clicks | foot |
| te-51 | The banks keep it quiet | STOP | insider | `gen:c41_quiet_bank` | ORANGE-STATEMENT | v-mark | foot |
| te-52 | BUILDERS COMPETING ON ZERO DOWN | MOVE-FAST | timeliness | `his:img-073` (framing photo) + `his:img-075` Equal Housing | DIVIDER→IMG-SIDE R | – | foot |
| te-53 | Rates bought into the low-to-mid fives | MOVE-FAST | good news | `gen:c42_rate_down` (arrow down, "at time of recording" html) | IMG-SIDE L | v-click | **foot: replay rate** |
| te-54 | FICO as low as 600, on some programs | MOVE-FAST | hope | `html:` stat card, hedge text | STAT-HERO | v-click | foot |
| te-55 | Advertised when recorded. Replays change | STOP | honesty | `gen:c43_replay_disclaimer` (clock/rewind motif) | ORANGE-STATEMENT full disclaimer | – | **foot: replay rate** |
| te-56 | THE SECRET NINJA: YOUR OWN 401(K) | ZOOM | delight (AHA #5) | `his:img-086` (retirement photo) | DIVIDER→HERO-BLEED | v-mark "OWN" | foot |
| te-57 | The low rate needs 3.5% down | MOVE-FAST | setup | `gen:c44_down_gap` (small orange slice of a house) | IMG-SIDE L | v-click | foot |
| te-58 | Borrow from yourself. You're the bank | ZOOM | delight | `gen:c45_you_are_bank` (figure lending to itself, loop) | ORANGE-STATEMENT | v-mark "the bank" | foot |
| te-59 | Have your cake and eat it too | MOVE-FAST | delight | Iconify | IMG-SIDE R | v-clicks | foot |
| te-60 | Not tax advice. Talk to your plan admin | STOP | compliance | `gen:c46_caution_shield` (shield) | NAVY-CARD full disclaimer | – | **foot: 401k disclaimer** |
| te-61 | WE CAN'T COVER ALL 60+ HERE | MOVE-FAST | FOMO→book | `his:img-090` (suburban homes) | DIVIDER→HERO-BLEED | – | foot |
| te-62 | Obscure programs. Rehab loans | MOVE-FAST | abundance | `gen:c47_more_doors` (doors receding) | REVEAL-CARDS | v-clicks | foot |
| te-63 | Your situation is unique | STOP | the pivot | `gen:c48_unique_path` (one distinct orange path) | ORANGE-STATEMENT | v-mark | – |

**Concept images from teaching:** c13_wrong_house, c14_money_left, c15_follow_money, c16_street_split, c17_hundred_percent, c18_puzzle_pieces, c19_reopened_door, c20_calendar_flip, c21_many_doors, c22_goldilocks, c23_hand_up, c24_hard_worker, c25_weight_lifted, c26_income_streams, c27_tax_return, c28_income_cake, c29_boogeyman, c30_dial_control, c31_credit_ladder, c32_fixable, c33_coach_shoulder, c34_two_gauges, c35_three_ingredients, c36_three_lanes, c37_old_map, c38_tuning_dials, c39_secret_shelf, c40_1977, c41_quiet_bank, c42_rate_down, c43_replay_disclaimer, c44_down_gap, c45_you_are_bank, c46_caution_shield, c47_more_doors, c48_unique_path. (+ regen c06_relief_exhale clean.)

---

# SECTION FILE: recap_momentum.md — Y1-Y3 (Fladlien §7) · target ~8 slides · ZERO images (internal-dialogue rule)

| id | headline (≤7 words) | tempo | emotion | VISUAL | treatment | anim | foot |
|---|---|---|---|---|---|---|---|
| ym-01 | Let me ask you the same thing | STOP | reflection | `none` NAVY-CARD | NAVY-CARD | – | – |
| ym-02 | Feeling less concerned now? | STOP | relief (mirror O4) | `none` (mirror of op-12, flipped) | NAVY-CARD, feeling words flipped | v-clicks | – |
| ym-03 | LESS concerned · LESS stressed · LESS frozen | STOP | relief | `none` text only | NAVY-CARD | v-clicks | – |
| ym-04 | I'll take 30% more confident | FRAME | permission | `none` | NAVY-CARD, orange "30%" | v-mark | – |
| ym-05 | Got your arms around it now? | STOP | mastery | `none` | NAVY-CARD | – | foot |
| ym-06 | 60+ programs. You qualify in part | MOVE-FAST | belief harvest | `none` text (A1+A2 recap) | NAVY-CARD | v-clicks | foot |
| ym-07 | Want to know what's next? | STOP | readiness | `none` | NAVY-CARD orange "next" | v-mark | – |
| ym-08 | A plan is what gets you keys. That's my job | FRAME | pivot (→offer) | `none` | NAVY-CARD | v-clicks | – |

---

# SECTION FILE: offer.md — F1-F6 (Fladlien §8; §9-14 collapsed) · target ~16 slides

| id | headline (≤7 words) | tempo | emotion | VISUAL | treatment | anim | foot |
|---|---|---|---|---|---|---|---|
| of-01 | THAT'S NOT YOUR JOB. IT'S MINE | FRAME | relief | `his:img-010` (sunset) OR `gen:c11_clear_path` | NAVY-CARD over image | v-mark "MINE" | foot |
| of-02 | Leave the rule book to me | FRAME | trust | `gen:c49_rulebook` (orange book handed over) | IMG-SIDE L | v-clicks | foot |
| of-03 | YOUR JOB: TELL ME YOUR HOME RUN | STOP | partnership (AHA #6) | `gen:c50_home_run` (silhouette batter rounding third, orange sunset) | ORANGE-STATEMENT | v-mark, HOLD | – |
| of-04 | Where? What? The payment that works? | MOVE-FAST | clarity | `gen:c50_home_run` | REVEAL-CARDS (questions) | v-clicks | – |
| of-05 | You dream it. I'll map it | FRAME | partnership | `gen:c51_dream_map` (dream cloud → map) | ORANGE-STATEMENT | v-mark | – |
| of-06 | BOOK YOUR FREE STRATEGY CALL | LAND | invitation | `his:img-098` (brush cutout, two talking) on orange | HERO-BLEED, URL chip `homebuyerschool.com/book` | motion | foot |
| of-07 | Straight to my calendar. 15 minutes | MOVE-FAST | access | Iconify `i-mdi-calendar-check` | IMG-SIDE R | v-clicks | foot |
| of-08 | The call is free. Nothing to buy | STOP | safety | `gen:c52_free_tag` (open hand / no price) | ORANGE-STATEMENT | v-mark "free" | foot |
| of-09 | WHAT YOU WALK AWAY WITH | FRAME | value | `gen:c12_gift_stack` (reuse) | DIVIDER→REVEAL-CARDS header | – | foot |
| of-10 | A plan for YOUR numbers | MOVE-FAST | value | Iconify `i-mdi-clipboard-text` | REVEAL card 1 | v-click | foot |
| of-11 | The book. The full 60+ list | MOVE-FAST | value | `html:book_mock` + `html:list_mock` (reuse) | REVEAL card 2 | v-clicks | foot |
| of-12 | A free soft credit check. No ding | MOVE-FAST | value | Iconify `i-mdi-credit-card-check` | REVEAL card 3 | v-click | **foot: soft pull** |
| of-13 | You won't sign a thing | STOP | safety | `gen:c53_no_pressure` (open door, no lock) | ORANGE-STATEMENT | v-mark | foot |
| of-14 | BUDDY & ROCIO, SAN ANTONIO | ZOOM | belonging | `his:img-102` (real SOLD photo) on-brand card, "WON" text badge (NO emoji) | IMG-SIDE L | fade | **foot: not typical** |
| of-15 | PETER & ESTHER, SAME AFTERNOON | ZOOM | momentum | `his:img-103` (real congrats photo) on-brand card | IMG-SIDE R | fade | **foot: not typical** |
| of-16 | Results like theirs aren't typical | STOP | honesty | `none` NAVY-CARD (spoken + printed disclaimer) | NAVY-CARD | – | **foot: FTC** |

---

# SECTION FILE: close.md — F7 (final LAND) · target ~3 slides

| id | headline (≤7 words) | tempo | emotion | VISUAL | treatment | anim | foot |
|---|---|---|---|---|---|---|---|
| cl-01 | This was never about a house | LAND | meaning | `gen:c04_keys_in_hand` (reuse, callback to op-06) | HERO-BLEED | motion | – |
| cl-02 | BOOK YOUR FREE STRATEGY CALL | LAND | decision | `html:qr_card` (QR white card → homebuyerschool.com/book) + monospace URL + `his:img-021` logo | ORANGE-STATEMENT, QR + URL (Rule 11: no fake button) | v-clicks | **foot: full NMLS + Equal Housing + educational** |
| cl-03 | Whew. We got this | LAND | relief payoff | `gen:c06_relief_exhale` (reuse, callback to op-14 goal) | NAVY-CARD, HOLD 2s | motion | foot |

---

## CONCEPT IMAGE BATCH (unique slugs → `assets/gen/images_config_brad.json`)
Count: **53 unique concept images** (c01-c53), several reused across slides (c04, c06, c11, c12, c21, c39, c41, c50). Plus **HTML/CSS mocks** (book_mock, list_mock, qr_card, program chips, ladder/stat cards) built in-slide, NOT generated (reliable text, editable, on-brand). His real assets referenced: img-019, 021, 004, 005, 010, 034, 035, 039, 050, 054, 056, 067, 068, 072, 073, 075, 086, 090, 098, 102, 103.

## HERO-QUALITY / HI-RES FLAGS (surface to John)
- 🔴 `his:img-072` (THE map, te-48/49/50) — 800×433, too small for full-bleed. Framed at native size in a card (not stretched). **Re-source hi-res.**
- 🔴 `his:img-067` (San Antonio map, te-38) — 800×447. Same.
- 🔴 book cover + 60+ list → built as `html:` mocks now; swap for real cover art when Brad sends it.
- Testimonials `his:img-102/103` — real photos, KEEP (never generate faces); confirm consent on file before public/ads use.

## COMPLIANCE FOOTER (auto on every `foot` row)
Standing footer component `.hbs-fineprint`: *"Educational purposes only, not a commitment to lend. Rates, limits, and program terms change and vary by lender, borrower, area, and market. Equal Housing Opportunity."* — plus the beat-specific disclaimers already written into `_SCRIPT.md` speaker notes (replay-rate on te-53/55, 401k on te-60, soft-pull on of-12, FTC-not-typical on of-14/15/16, full NMLS on op-21 + cl-02).
