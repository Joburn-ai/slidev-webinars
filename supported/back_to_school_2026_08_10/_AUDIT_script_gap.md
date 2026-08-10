# SCRIPT COMPLETENESS AUDIT
**Script:** `/root/ai-os/06_Clients/supported/strategy/webinar_script_2026_08_10/Full_Script_Jan_26_.md` (510 lines)
**Deck:** `/root/slidev-webinars/supported/back_to_school_2026_08_10/slides.md` (348 slides, 3,095 lines)
**Intermediate found:** `/root/slidev-webinars/supported/back_to_school_2026_08_10/test_script_v2.md` (V2, dated 2026-03-11, 1,150 lines)

> All script quotes below have had em-dashes and en-dashes normalized to commas, colons or periods. Content is otherwise verbatim.

---

## 0. THE HEADLINE FINDING

**The deck was not built from the Jan script. It was built from V2**, a March rewrite sitting in the deck's own folder. The deck is a near-verbatim slide render of V2 sections 1 to 7, plus a new back-to-school pop-quiz Q1 and a new booking close. V2 sections 8 to 14 (the sale) were correctly dropped per John's ruling.

So the loss happened one generation upstream. **V2 compressed the Jan script by roughly 65 percent and silently deleted six whole Fladlien beats.** The deck inherited those holes without ever seeing the Jan script.

Counted against the Jan script:
- **6 beats missing entirely** and not excluded by design
- **9 beats partially present**, most at 40 to 60 percent of the script's argument
- **17 beats excluded by design** (the entire offer spine)
- **16 items exist in the deck that are not in the Jan script**, and most of them are better than what they replaced

---

## 1. SECTION-BY-SECTION MAP

| # | Script beat | Script lines | Status | Deck location | Note |
|---|---|---|---|---|---|
| 1 | Pop quiz frame, "5 simple True/False questions" | 15 | **PRESENT** | 140 to 185 | Deck adds "at least two of these will surprise you" |
| 1a | Q: A in AP class = guaranteed 4 or 5 | 16 | **PRESENT** | 299 to 297 (deck Q2) | Rationale kept, `$40,000` claim correctly dropped |
| 1b | Q: more practice tests and longer hours | 18 | **PARTIAL** | 346 to 344 (deck Q3, reframed as "memorizing more content") | Free-throw analogy and "volume without strategy" both lost |
| 1c | Q: expensive private tutors | 20 | **MISSING** | none | Whole question absent |
| 1d | Q: admissions competition, AI screening | 22 | **MISSING** | none | Should stay out. `300%` stat is unsupported |
| 1e | Q: hard work alone will work out | 25 | **MISSING** | none | The strongest of the five. Absent |
| 1f | Post-quiz transition | 27 | **PRESENT** | 446 to 483 | Deck version is better |
| 2 | The CFA pain block: dream, wins, trap, second trap, consequence, fear, obstacle, reframe | 29 to 39 | **PARTIAL, ~25%** | 491 to 933 | 11 script paragraphs compressed into a handful of slides. Biggest gap in the deck |
| 3 | "Burned before" objection pre-handle | 40 to 42 | **PARTIAL** | 884 to 922 | Deck keeps the list of failed solutions, loses the entire emotional permission block |
| 4 | "Here are the questions that should be on your mind" | 43 | **MISSING** | none | Whole agenda-setting beat absent |
| 5 | Future-pace ladder, "wouldn't it be great if" | 44 | **MISSING** | none | Deck has no future pacing anywhere |
| 6 | Attendance bribe: free AP Success Starter Kit | 45 | **MISSING** | none | Needs a ruling, see section 6 |
| 7 | The WHY block, "why are you here today", chat interrogation | 46 | **MISSING** | none | Highest-value chat interaction in the script |
| 8 | Joe's origin moment, "I still remember my moment" | 47 | **MISSING** | none | Deck positioning is credentials only, no story |
| 9 | "On this webinar you'll discover", 18 curiosity bullets | 48 | **MISSING** | none | A whole Fladlien section absent |
| 10 | Credentials and authority | 49 | **PARTIAL** | 941 to 1009 | Stats kept, doctorate, school placements and insider access all dropped |
| 11 | "Why I share this with you today" | 54 | **PRESENT** | 1015 to 1041 | Deck version is tighter |
| 12 | Big promise plus the commitment ask | 55 | **PARTIAL** | 1044 to 1091 | Promise present. "Would you commit to me" ask MISSING |
| 13 | Mechanism 1, AP Insider Intelligence | 57 to 61 | **PARTIAL, ~55%** | 1141 to 1356 | 3 named components, all analogies, full implementation and outcome blocks lost |
| 14 | Mechanism 2, Subject-Specific Response Mastery | 62 to 66 | **PARTIAL, ~50%** | 1358 to 1524 | Per-subject depth flattened to 4 bullets, phase system lost |
| 15 | Mechanism 3, Pre-Grade Confidence System | 67 to 71 | **PARTIAL, ~45%** | 1526 to 1749 | 3 components and 4 phases gone. Phase 4 is the best proof and it is absent |
| 16 | Demo setup and disarm | 72 to 78 | **PARTIAL** | 1777 to 1856 | "You haven't been in a history class for 20 years" and the CAN'T TELL poll both MISSING |
| 17 | Essay A and Essay B presented | 79 to 84 | **PRESENT** | 1858 to 1961 | Faithful |
| 18 | Actual rubric reveal | 85 to 89 | **PRESENT** | 1988 to 2057 | Faithful |
| 19 | Contextualization scored, both essays | 90 to 105 | **PRESENT** | 2059 to 2182 | One line lost: "This is a classroom A. But it's an AP fail." |
| 20 | Thesis scored, both essays | 106 to 129 | **PRESENT** | 2184 to 2357 | "Generic thesis" label lost |
| 21 | Remaining 3 criteria | 130 to 133 | **PRESENT, expanded** | 2402 to 2574 | Deck is fatter here than the script |
| 22 | Final scores and real-number meaning | 134 to 140 | **PRESENT, altered** | 2576 to 2703 | Deck changed 3/7 to 2/7 and 6/7 to 7/7. See arithmetic flag below |
| 23 | "Type MIND BLOWN" | 141 to 143 | **PRESENT** | 2705 to 2714 | |
| 24 | Post-demo meaning-making, "the anxiety disappears because the mystery disappears" | 144 to 157 | **MISSING** | none | 14 lines of the script's best payoff, gone |
| 25 | "That was JUST Mechanism #1" bridge plus Grader Vision | 158 to 163 | **MISSING** | none | The structural bridge out of the demo is absent |
| 26 | Recap | 164 | **PARTIAL, 6 of 11** | 2742 to 2801 | |
| 27 | Yes momentum ladder | 165 to 183 | **PARTIAL, 6 of 7** | 2809 to 2949 | The regret pivot and the payoff cascade are MISSING |
| 28 | Transition to offer | 184 to 186 | **REPLACED by design** | 2951 to 2970 | Replaced with "Not sell you anything. Build you a plan." Correct |
| 29 | Offer intro plus ACE origin story | 187 to 198 | **EXCLUDED by design** | none | But lines 188 to 192 are narrative, not sale. Recommend lifting. See section 6 |
| 30 | Components 1 to 4 | 199 to 287 | **EXCLUDED by design** | none | |
| 31 | Bonuses 1 to 4 | 290 to 330 | **EXCLUDED by design** | none | |
| 32 | Value stack | 333 to 341 | **EXCLUDED by design** | none | |
| 33 | Price reveal | 343 to 354 | **EXCLUDED by design** | none | |
| 34 | Score guarantee | 357 to 367 | **EXCLUDED by design** | none | Also carries 3 banned claims |
| 35 | Scarcity and urgency | 370 to 384 | **EXCLUDED by design** | none | Deck's "call slots each week are limited" is the allowable soft version |
| 36 | Two paths close | 387 to 407 | **EXCLUDED by design** | none | |
| 37 | The real math | 410 to 423 | **EXCLUDED by design** | none | |
| 38 | What happens after you enroll | 426 to 435 | **EXCLUDED by design** | 3007 to 3025 (3 bullets) | The *shape* is worth stealing for "what happens on the call" |
| 39 | Call to action | 438 to 446 | **REPLACED by design** | 3027 to 3040 | Booking ask |
| 40 | FAQ | 449 to 471 | **EXCLUDED by design** | none | |
| 41 | Final CTA repeat | 474 to 480 | **REPLACED by design** | 3042 to 3069 | |
| 42 | Optional downsell, `$97/mo` | 483 to 505 | **EXCLUDED by design** | none | |

---

## 2. THE MISSING BEATS, IN FULL

Drop-in text. Claim-safe edits flagged inline.

### 2.1 Pop quiz Q on tutors (script L20) — MISSING

> "True or False: Expensive private tutors give you the best chance of AP success. **False.** Most private tutors charge `$125+` per hour but lack College Board certification and insider knowledge of how exams are actually scored. They teach content, not scoring strategy. That's why parents spend thousands on tutoring and still watch their kids miss college credits. The most successful students use certified AP teachers who know the scoring systems from the inside."

**Rebuild edit required:** delete "lack College Board certification". Replace with "are not certified AP teachers and have never scored an exam." The final sentence, "certified AP teachers", is already compliant as written.

### 2.2 Pop quiz Q on effort (script L25) — MISSING

> "True or False: As long as your student works hard, everything will work out for college admissions and AP success. **False.** Hard work without the right system leads to burnout, wasted time, and devastating disappointment. Right now, thousands of hardworking students are heading toward 2s and 3s on their AP exams, losing tens of thousands in college credits, all while their parents think 'working harder' is the answer. The painful truth is that effort without strategy is just expensive failure."

This is the single best line in the quiz and it is absent from the deck. "Effort without strategy is just expensive failure" is a stronger version of what the deck's Section 7 is groping for.

### 2.3 The free-throw analogy (script L18) — MISSING

> "More practice without the right strategy actually reinforces wrong approaches. It's like practicing free throws with terrible form, you'll get really good at missing the mark. Students who score 4s and 5s don't study more; they study strategically using the exact frameworks AP graders use. Volume without strategy is why exhausted students still fail."

The deck has "you can't cram a skill" but no image. This is the image.

### 2.4 The wins acknowledgment and the second trap (script L30, L33, L34) — MISSING

> "And maybe you've had some wins. Your teen is ahead academically with solid grades in AP classes, you've found tutoring support that's helping with homework consistency, and your child seems more college-ready than you were at that age."

> "But here's the second trap most families fall into, believing that working harder and doing more practice tests will eventually break through, when strategy matters more than volume."

> "And what happens when you try to push through this limitation? Students burning out from endless practice tests while still scoring 2s and 3s, families spending more money on ineffective tutoring that reinforces wrong approaches, teens losing confidence as they watch others who study less score better, and the whole family sacrificing mental health and relationships in pursuit of scores that never improve because the strategy is fundamentally wrong."

The deck's pain section has no wins acknowledgment at all, and never names a second trap. Both are structural CFA requirements, not decoration.

### 2.5 The fear, fully stated (script L35) — MISSING

> "The thing you fear most? Their teen becoming another heartbreaking statistic, a brilliant, hardworking student whose dreams crumble in senior year when low AP scores destroy college plans, forcing parents to tell their accomplished child that despite all their sacrifices it wasn't enough, while wondering if they failed by not knowing how to navigate a system other families somehow figured out."

The deck's "the real fear" slide (line 793) says only "You're worried about the trajectory." This paragraph is the actual fear and it is the highest-voltage sentence in the entire script.

### 2.6 The reframe: the packed schedule as an asset (script L38) — MISSING

> "But here's what most parents don't realize, once you understand the hidden scoring gap, you have the unfair advantage of knowing exactly what AP graders want while other families waste time on irrelevant classroom skills. And your teen's packed schedule actually becomes an asset when you have the right system, they learn efficiency and time management that average students never develop."

Nothing in the deck speaks to the student-athlete or over-scheduled kid. This is the only place the script does it and it is gone.

### 2.7 The objection permission block (script L41, L42) — MISSING

> "No wonder it's so scary to invest in another AP solution. The problem isn't trying to help your teen succeed, it's the certainty that you might waste more money and time while your child's college dreams hang in the balance. And I get it. Because of the invisible gap between classroom grades and AP exam scoring, and because of all the conflicting advice from tutors who don't understand the real scoring systems, it's now even more complicated to know what will actually work."

> "These are the challenges I know you're dealing with, which is why when you see the approach I have for you today, you'll say 'Ok, now I see how this time will be different.' So that no matter what has happened to you in the past, today is a new day with a new hope and completely new possibility. How does that sound?"

The deck lists the failed solutions but never absolves the buyer for having bought them. That is what makes the list land instead of shame.

### 2.8 The questions that should be on your mind (script L43) — MISSING

> "Now when it comes to your teen scoring 4s and 5s on AP exams, here are the questions that should be on your mind: How easy is it to turn classroom A's into exam 5s? What's the best way to prepare for AP exams with the least stress and overwhelm? What should you realistically expect? How quickly can you go from worried parent to confident? How much effort does it take to finally bridge that gap between good grades and actual AP success? I've got the answers, in fact, better answers than you'll find anywhere else."

**Rebuild edit required:** the script original opens "when it comes to guaranteeing your teen scores 4s and 5s while saving `$40,000+`". Both the guarantee and the dollar figure must go. Quoted above already stripped.

### 2.9 The future-pace ladder (script L44) — MISSING

> "Now, how would you like to watch your teen walk out of every AP exam knowing they scored a 5? You can, and more. But let's not get ahead of ourselves. And wouldn't it be great if when your teen takes these exams, not only did they score 4s and 5s, but they also gained the confidence and study skills that make them unstoppable in college? You can, and you will. Now what if your busy student-athlete just learned the exact scoring frameworks AP graders use and then suddenly exams became predictable instead of stressful? And what if you didn't even have to sacrifice their sports, activities, or mental health to get there? Yes. That's more than possible."

> "Let's say only your teen's confidence and test-taking abilities improved dramatically, what would that do for you? Could it eliminate the stress of wondering if they're prepared? Or give you peace of mind knowing they have every advantage? What about watching them become the kind of student who makes success look effortless?"

**Rebuild edit required:** the script also carries "if just one AP exam went from a potential 2 or 3 to a guaranteed 5, and that led to `$10,000+` in college credit savings". Cut that sentence entirely. The rest is clean.

### 2.10 The WHY block (script L46) — MISSING

> "Before we get into the how and what, I want to start with something more important, your why. Why are you here today? Why are you willing to invest your time, your energy, maybe even your hopes, just for the chance at something better for your child? This isn't rhetorical. I want your answer right now, in the chat. And not just any answer, the real one. The one that makes you feel something."

> "Is it the way your child will look at you when they get that acceptance letter, knowing you gave them every advantage? Is it the moment you wake up stress-free, smiling, knowing you're not one of those families scrambling in senior year because the AP scores came back as 2s and 3s? Is it watching your hardworking teen finally get the recognition they deserve?"

> "What will it look like when your child confidently walks into every AP exam knowing they're prepared? What will it feel like in your body, your heart, your chest, your gut, when you see those 5s come back? Who else gets lifted when your teen wins? Your spouse who stops worrying about college costs? Your younger children who see what's possible? Your extended family who watches your child thrive? That reason, that's what makes today matter."

The deck's chat prompts are all "type YES". This is the one place the script asks for a real answer, and real answers are what keep people in the room to the CTA.

### 2.11 Joe's origin moment (script L47) — MISSING

> "I still remember my moment. After years in the school system, watching brilliant students get crushed by a system that should have lifted them up, watching parents like you throw money at solutions that didn't work, I knew I had to do something. I couldn't keep watching families fail when I knew exactly what it took to succeed. That was my why. And once I owned it, everything started to shift."

The deck's positioning is four stat bullets and two "I'm tired of" lines. There is no story. This is the story, and it is 90 words.

### 2.12 The "you'll discover" curiosity stack (script L48) — MISSING

The full 18-bullet block is at script line 48. **Do not lift it wholesale**, it is the single densest concentration of banned claims in the document. These bullets survive a rewrite:

- The shocking truth about why straight-A students score 2s and 3s (it's not what you think)
- Why working harder on AP prep is like practicing free throws with terrible form
- The scoring rubrics that even certified AP teachers don't see, and exactly what graders look for in every question type
- How to spot the difference between a classroom A and an exam 5 in under 30 seconds
- The devastating 15-minute conversation thousands of families have in senior year
- The simple question that reveals whether your teen is heading for a 2 or a 5, before they even start studying
- How to turn a packed sports schedule into an academic advantage instead of a liability
- The emotional moment when your teen walks out of their final AP exam with confidence instead of tears

These must be cut or rewritten: "89% of parents", "one mom saved `$64,000`", "guarantees improvement", "5-scorers overnight", "the same advantages as admissions officers' own children", "Why the College Board doesn't want you to know", "three-sport athlete scored a perfect 5", "waste `$40,000+`", "`$30,000-$50,000`".

### 2.13 The commitment ask (script L55) — MISSING

> "If I were to show you exactly how these scoring frameworks work, then would you commit to me to take action on what we cover today?"

One slide. It is the micro-close that makes the booking ask at the end feel pre-agreed rather than sprung.

### 2.14 Mechanism 1: the missing 45 percent (script L57 to L61)

Components, all three named and all three MISSING:

> "First, **Rubric Revelation**, we decode the actual scoring rubrics that AP graders use. These aren't the generic guidelines your teen's teacher shows in class. These are the detailed, point-by-point criteria that determine whether an essay gets a 2 or a 6. Second, **Pattern Recognition**, we show your teen the response patterns that consistently score high. It's like learning to see the Matrix, once they know what graders are looking for, they can't unsee it. Third, **Expectation Management**, your teen will understand exactly what 'good enough for a 5' looks like versus 'perfectionist overkill' that wastes time without adding points."

Analogies, MISSING:
> "Most parents think success comes from content mastery, but that's like thinking you can win at poker just by knowing the rules. You need to understand how the game is actually played and scored."
> "Think of it like learning to speak a new language, except instead of Spanish or French, your teen is learning to speak 'AP Grader.'"

Implementation, MISSING:
> "Your teen starts by analyzing high-scoring sample responses alongside the actual grader comments. They see exactly why one essay earned a 6 while another earned a 3, even when both students clearly knew the material. Next, they practice **Reverse Engineering**, taking their own past work and evaluating it using the real rubrics. This creates those 'aha' moments where they finally understand why their classroom A's didn't translate. Finally, they develop **Grader Empathy**, the ability to read any AP question and immediately know what the grader wants to see. The key is starting with analysis before creation. Most students jump straight to practice tests, but that's like trying to hit a target you can't see. First, we make the target visible."

Outcome, MISSING:
> "They'll stop asking 'Is this good enough?' because they'll know. Their practice scores will jump immediately, not because they learned more content, but because they finally understand the game."

### 2.15 Mechanism 2: the missing 50 percent (script L62 to L66)

Analogies, MISSING:
> "Telling your teen to 'write a good essay' is like telling them to 'drive safely' without teaching them the specific rules of the road. It's not actionable, and it leads to crashes."
> "AP exams don't test what you know, they test how well you can demonstrate what you know using very specific formats. It's the difference between being a great chef and being able to compete on a cooking show with strict rules and time limits."
> "It's like giving your teen a different key for each specific lock, instead of one generic key that doesn't quite fit anywhere."

Per-subject depth, flattened in the deck to four one-line bullets. Script version:
> "**For AP History:** the exact DBQ and LEQ structures that graders expect. Your teen learns the 7-paragraph formula, the contextualization requirements, and the evidence integration patterns that separate 5s from 3s. **For AP Sciences:** FRQ response sequences, the specific steps, vocabulary, and explanation depth required for maximum points. No more losing points for 'not showing work' when your teen actually knew the answer. **For AP English:** the literary analysis frameworks that turn book discussions into sophisticated arguments. Thesis construction, evidence selection, and commentary techniques. **For AP Math:** the problem-solving methodologies that demonstrate understanding clearly, even when calculations get messy."

The Template-Practice-Perfect phase system, MISSING:
> "**Week 1-2: Template Installation.** Your teen learns the specific structure for each question type they'll face. We don't just show them examples; we give them fill-in-the-blank frameworks they can use immediately. **Week 3-4: Guided Practice.** Your teen applies these templates to past exam questions with coaching feedback. **Week 5-6: Timed Mastery.** Your teen practices under exam conditions until the templates become automatic. By this point they're not thinking about structure anymore, they're focused entirely on content because the format is habitual. The critical insight: we teach structure first, then overlay content. Most prep does the opposite and wonders why students freeze up under pressure."

Outcome, MISSING and highly visual:
> "They'll read a DBQ prompt and immediately know: paragraph 1 needs contextualization, paragraph 2 starts the argument, paragraphs 3-5 develop evidence, paragraph 6 addresses complexity, paragraph 7 concludes with significance."

### 2.16 Mechanism 3: the missing 55 percent (script L67 to L71)

The stakes, MISSING:
> "Without this system, your teen remains dependent on external validation and prone to test anxiety. They'll second-guess themselves, change correct answers, and leave exams feeling uncertain even when they performed well."

Analogy, MISSING:
> "Traditional prep focuses on input (studying) without teaching output evaluation (self-grading). It's like learning to cook without ever tasting your food, you have no idea if you're improving or making the same mistakes repeatedly."

Components, all three MISSING:
> "**Internal Scoring Calibration**, your teen learns to evaluate their own work using the exact same criteria AP graders use. They develop the ability to read their essays and predict: 'This is a 4, needs stronger evidence for a 5.' **Performance Forecasting**, before taking any practice exam, your teen predicts their score range. After the exam, they self-grade before seeing official results. **Gap Analysis Mastery**, when predictions don't match results, your teen learns to diagnose exactly what went wrong and how to fix it. No more generic 'study harder', they identify specific skill deficits and address them systematically. It's like developing an internal coach who can provide instant, accurate feedback without waiting for teacher grades."

The four phases, MISSING. **Phase 4 is the strongest single proof point in the mechanism section and appears nowhere in the deck:**
> "**Phase 1: Rubric Internalization.** Your teen practices scoring sample responses until their evaluations match official grades consistently. This develops their internal scoring radar. **Phase 2: Self-Evaluation Practice.** Your teen begins grading their own practice work before checking answers. **Phase 3: Predictive Accuracy.** Your teen starts predicting their performance before attempting practice exams, then compares predictions to results. Over time, their predictions become incredibly accurate. **Phase 4: Real-Time Adjustment.** During actual exams, your teen can monitor their performance and adjust strategy mid-test. They know when to spend more time on an essay that could jump from a 4 to a 5, or when to move on from a question that's already solid."

### 2.17 The demo disarm and the first poll (script L73, L76 to L78) — MISSING

> "Now, I know you haven't been in a history class for 20 years. And I'm not expecting you to remember the French Revolution or the New Deal. But bear with me here, what I'm about to show you will make everything click about why straight-A students struggle on AP exams."

> "Type in chat right now: Can you tell which one is better just by reading them? Type A or B or CAN'T TELL."
> [PAUSE FOR RESPONSES]
> "Most of you typed CAN'T TELL, and that's exactly the problem. **Your teen can't tell either.** Until I show you what I'm about to show you."

The deck's poll is "Which one scored a 5? Type A or B" (line 1963). That is a guessing game. The script's version is a diagnosis, and the payoff line "your teen can't tell either" is the whole reason the demo exists. **This is the highest-value single restore in the audit.**

Also missing, one line, script L96:
> "This is a classroom A. But it's an AP fail."

And script L118:
> "This is what we call a 'generic thesis.' It's safe. It's broad. And it gets zero points."

### 2.18 The post-demo payoff (script L144 to L157) — MISSING ENTIRELY

> "This is what happens when your teen masters AP Insider Intelligence. They don't just know the content. They know what graders want to see. They stop guessing. They stop hoping. They read a prompt and immediately know: what contextualization to include, how to structure their thesis, which evidence counts, what analysis looks like."

> "**The anxiety disappears because the mystery disappears.**"

> "Can you see how that confidence would change everything for your teen? Can you imagine them walking into the exam room KNOWING they're going to score a 5, not hoping, not praying, but KNOWING?"

> "And we just showed you one tiny piece. One rubric criterion for one essay type. Imagine your teen having this level of clarity for DBQs, LEQs, FRQs, and every single question type they'll face."

The deck goes from "that's the invisible scoring gap" straight to "type MIND BLOWN" and then straight to the recap. The meaning-making is gone. "The anxiety disappears because the mystery disappears" is the thesis sentence of the whole webinar and it is not on a slide.

### 2.19 The bridge out of the demo (script L158 to L163) — MISSING

> "Now here's what makes this even more powerful. What we just walked through? That was JUST Mechanism #1. We haven't even talked about Mechanism #2, the Subject-Specific Response Templates that turn this understanding into automatic execution. Or Mechanism #3, the Pre-Grade System that lets your teen predict their score before taking the exam. Those three mechanisms working together? That's when straight-A students become 5-scorers. That's when anxiety becomes confidence."

> "They develop what I call **Grader Vision**, the ability to see exactly what any AP question is really asking for."

Note the script runs the demo *after* all three mechanisms, so this bridge doubles back. The deck keeps that order. Either restore the bridge or reorder so the demo sits inside Mechanism 1. Right now the deck does neither and the demo just ends.

### 2.20 Yes momentum, the three missing rungs (script L170, L171, L174, L182)

> "That your straight-A student has been optimizing for the WRONG scorecard this whole time?"
> "Are you starting to realize that your teen has been studying for the WRONG test? That while they've been perfecting classroom skills, the AP exam has been measuring something completely different?"
> "Wouldn't you agree that if you had this insider knowledge six months ago, everything would be different right now? That instead of feeling uncertain and stressed, you'd be feeling confident and prepared?"
> "The stress disappears. The anxiety vanishes. The financial relief kicks in. The college doors open."

The "six months ago" rung is the regret pivot, and it is the natural on-ramp to a back-to-school booking ask ("you have those six months right now"). It is absent.

### 2.21 Recap items the deck dropped (script L164)

Deck keeps 6 of 11. Missing and worth restoring, claim-stripped:
> "You discovered why expensive tutors and endless practice tests actually make scores worse by reinforcing the wrong approaches."
> "You learned how the Pre-Grade Confidence System eliminates test anxiety by teaching your teen to predict their own scores before taking exams."
> "You saw the difference between families who hope for good scores and families who systematically create them."

---

## 3. IN THE DECK, NOT IN THE SCRIPT — KEEP ALL OF THIS

Sixteen items. Most of this is later and better work.

| Deck lines | What it is | Verdict |
|---|---|---|
| 187 to 244 | **Pop quiz Q1: "the first report card of the year tells you whether your teen is on track"** and its 5-bullet answer | **The best strategic material in either document.** This is the back-to-school thesis. Not in the script, not in V2. Keep and build on |
| 240 | "The first six weeks are the one window to flip from reactive to ahead" | Keep. The urgency mechanism for a seasonal booking ask |
| 399 to 444 | **Q5 answered TRUE** (tuition lever) | Better quiz design than the script's five straight FALSEs. Keep the pattern break |
| 556 to 644 | **"This is not your fault" plus "College Board changed the rules" plus "most AP teachers have never graded a single AP exam"** | Absolution beat, entirely new. Keep. See caution in section 5 |
| 840 to 870 | **Four verbatim parent quote slides** | New, strong texture. **Sourcing unverified**, attributed "Real parent, last month". Verify before ship |
| 908 to 922 | **"Certainty"** named as the single payoff word | Keep. Better than the script's diffuse promise |
| 1209 to 1236 | Two-column **Content Knowledge vs Exam Performance** | Keep, and this is one of the deck's only two non-centred layouts |
| 1631 to 1635 | **"Hope is not a strategy."** | Keep |
| 1641 to 1689 | **Score Forecast Report** artifact plus the "Projected: 5" reveal | Concrete where the script was abstract. Keep. This is a screenshot waiting to happen |
| 1500 to 1506 | "Like running plays in a sport. You don't think. You execute." plus **Week 4 / Week 8 milestones** | Keep |
| 1697 to 1735 | The **Bryce** practice-exam story | Keep the story shape, **change the name.** Bryce is not on the cleared list. Recast as Nabila, Laura or Avery |
| 2586, 2600 | Demo scores changed to **A 2/7** | The deck's A total is arithmetically consistent with its own line items where the script's 3/7 is not. Keep the fix, then fix B, see section 5 |
| 2951 to 2970 | **"Not sell you anything. Build you a plan."** | Keep. This is the pivot John's ruling depends on |
| 2978 to 3025 | **The free AP Game Plan Call frame** plus what the call covers | Keep verbatim |
| 3063 to 3069 | **Seasonal speaker-note variants** for August and September | Keep. One bug: the third variant is labelled AUGUST and duplicates the first label. Should be OCTOBER or later |
| 3071 to 3085 | **"No pressure either way. You leave with a real plan whether or not you ever work with us."** | Keep. Strongest single line in the close |

---

## 4. WHERE THE DECK IS THIN

Ranked by size of the gap between what the script argues and what the deck shows.

1. **The pain section, script L29 to L39.** Eleven paragraphs of dream, wins, trap, second trap, consequence, fear, obstacle and reframe compressed into roughly six thin slides. The deck's entire "I know why you're here" is two sentences: "You've got a feeling your teen isn't getting the support they need. And you don't know what to do about it." The script gives a full portrait. **This is the single thinnest section in the deck relative to source.**

2. **Positioning, script L47, L49, L54.** The deck gives four stat bullets and two "I'm tired of" lines. There is no origin story, no doctorate, no school placements, no evidence of insider access beyond one unbacked line. A stranger has no reason to sit for 45 more minutes.

3. **Mechanism 3.** The deck gives five bullets and a projected score. The script gives three named components and four training phases. Phase 4, real-time mid-exam adjustment, is the most concrete and impressive claim in the mechanism section and it is not in the deck at all.

4. **Mechanism 2's per-subject proof.** Four script paragraphs of genuine specificity (7-paragraph DBQ formula, FRQ sequences, literary analysis frameworks, math process points) become four one-line bullets on a single slide at deck line 1448. This is exactly the beat where a parent decides whether Joe actually knows the subject.

5. **The post-demo payoff.** Fourteen script lines of meaning-making become three slides. The demo lands and then nothing is made of it.

6. **The recap.** Eleven script items become six, and the deck's six are all emotional. None of the three mechanisms is named in the recap, so the parent leaves without a retrievable label for what they just bought into.

7. **The close's "what happens next".** Three bullets at deck line 3007. The script's post-enrollment timeline at L426 to L435 (IMMEDIATELY, WITHIN 24 HOURS, WITHIN 48 HOURS, WEEK 1) is the right shape and should be adapted into "here is exactly what happens on the call and in the 48 hours after".

8. **Yes momentum.** Six rungs where the script has seven, and the deck lost the one rung (regret at "six months ago") that connects the ladder to the seasonal urgency the whole deck is built on.

---

## 5. CLAIM FLAGS — EXCLUDE FROM THE REBUILD

### 5.1 In the SCRIPT, by line number

| Script line | Claim | Status |
|---|---|---|
| 16 | "guaranteed to score a 4 or 5" (inside the FALSE premise) | Safe only as the quiz premise being negated. Never as an assertion |
| 16 | "This gap costs families `$40,000+` in lost college credits every year" | **NOT CLEARED.** Dollar claim |
| 20 | "lack College Board certification" | **BANNED phrasing.** Rewrite to "not certified AP teachers" |
| 20 | "`$125+` per hour" | Unverified market stat. Cut or soften |
| 22 | "competition has increased 300% in five years" | **NOT CLEARED.** Unsupported |
| 22 | "now that AI screens applications" | **NOT CLEARED.** Unsupported |
| 29 | "`$40,000+` in college savings" | **NOT CLEARED** |
| 30 | "to guarantee your teen's AP success" | **BANNED.** Guarantee language |
| 43 | "guaranteeing your teen scores 4s and 5s", "`$40,000+`", "guaranteed" | **BANNED** x3 |
| 44 | "a guaranteed 5", "`$10,000+` in college credit savings" | **BANNED** |
| 48 | "3-word mistake 89% of parents make" | **NOT CLEARED**, and it collides dangerously with our one cleared 89% figure (student scores) |
| 48 | "one mom saved `$64,000`" | **NOT CLEARED.** Unverified student/parent |
| 48 | "turns average students into 5-scorers overnight" | **BANNED.** Result claim |
| 48 | "the exact same advantages as admissions officers' own children" | **NOT CLEARED.** Implies improper insider access |
| 48 | "Why the College Board doesn't want you to know" | **NOT CLEARED.** Conspiracy framing against a named org |
| 48 | "a busy three-sport athlete scored a perfect 5" | **NOT CLEARED.** Unverified student |
| 48 | "guarantees lower scores", "guarantees improvement" | **BANNED** x2 |
| 48 | "families waste `$40,000+`", "saving `$30,000-$50,000`" | **NOT CLEARED** |
| 49 | "over 600 students" | **NOT CLEARED** |
| 49 | "`$2.8 million` in college tuition" | **NOT CLEARED** |
| 49 | "College Board Certified in AP instruction" | **BANNED phrasing.** Must be "certified AP teacher" |
| 49 | "Columbia University, University of Michigan, UCLA, UT Austin" placements | Unverified. Do not use without Joe's written confirmation |
| 49 | "Doctorate in Educational Leadership", "featured as an AP expert" | Verify before use. Probably fine, not on the cleared list |
| 49 | "`$40,000+` in tuition costs" | **NOT CLEARED** |
| 55 | "guarantee your teen scores 4s and 5s on ALL their AP exams in just the next 4-6 months" | **BANNED.** Guaranteed score, on a timeline, on all exams |
| 55 | "college credit savings of `$30,000-$50,000+` near effortlessly" | **NOT CLEARED** |
| 137 | "Full college credit (`$3,000+` value)" | **NOT CLEARED** as stated |
| 162 | "families save `$40,000+` in college tuition" | **NOT CLEARED** |
| 164 | "over 600 students", "`$2.8 million`" | **NOT CLEARED** |
| 194 | "Over 600 students", "95% earn college credit", "150+ perfect 5s", "250+ 4s" | **NOT CLEARED.** The only cleared aggregate is "89% of our students score 4s or 5s versus about 22% nationally", with "results vary", used once |
| 196 | "`$2.8 million` in college tuition" | **NOT CLEARED** |
| 219 | "Test Day Confidence Guarantee" | **BANNED.** Offer section, excluded anyway |
| 239 | "our test prep guarantee" | **BANNED** |
| 345 | "over 600 students", "`$2.8 million`", "`$1,500 to $3,000`" per credit, "worth at least **`$50,000`** in long-term value" | **BANNED.** `$50,000` of value is explicitly on the exclusion list |
| 346 | "worth at least `$25,000`" | **NOT CLEARED** |
| 347 | "**`$11,774`** minimum" | **BANNED.** Explicitly on the exclusion list |
| 357 to 367 | The whole Score Guarantee section | **EXCLUDED by design AND banned** |
| 362 | "we refund **`$800`**. No questions asked." | **BANNED.** Explicitly on the exclusion list |
| 364 | "**You literally can't lose.**" | **BANNED.** Explicitly on the exclusion list |
| 366 | "already helped 600+ families score 4s and 5s" | **NOT CLEARED** |
| 375 | "Once we hit 15, this closes" | Excluded by design. Also unverifiable capacity claim |
| 405 | "`$11,774+` over four years" | **BANNED** |
| 439 | "coaching that guarantees they score 4s and 5s" | **BANNED** |
| 465 | "you get 100% refunded" | **BANNED**, and it contradicts line 362's `$800`. Internal inconsistency |
| 470 to 471 | "600+ students", "95% earn college credit", "150+ perfect 5s" | **NOT CLEARED** |
| 498 | "No score guarantee" | Excluded by design |

**Confirmed absent from the script:** "National AP Scholar" (zero hits), "22%" national comparison (zero hits). The cleared aggregate "89% score 4s or 5s versus about 22% nationally" appears nowhere in the script, so it must be authored fresh in the rebuild, used once, with "results vary".

### 5.2 Already carried INTO the deck — must be removed on rebuild

These are live in the current deck, not merely in the script.

| Deck line | Claim | Action |
|---|---|---|
| 999 to 1005 | "**600+** students coached / **95%** earn college credit / **150+** perfect 5s / **`$2.8 million`** saved in tuition" | **Remove all four.** Replace with the single cleared aggregate |
| 1117 | "Working with 600+ students, I've found three breakthroughs" | Remove the number |
| 832 | "`$95,000` to `$125,000` in scholarship money, gone" | **NOT CLEARED.** Remove |
| 834 | "you could pay `$200,000` in college tuition when the right AP scores could have cut that in half" | **NOT CLEARED.** Remove |
| 2778 | Repeat of "`$95,000` to `$125,000` in scholarships" in the recap | Remove |
| 2945 | "The right AP scores could save your family **`$100,000+`**" | **NOT CLEARED.** Remove |
| 2646 | "**`$3,000` to `$8,000` saved**" as the Essay B payoff | **NOT CLEARED** as a specific figure. Soften to "college credit your family does not pay tuition for" |
| 1703 | Student named "**Bryce**" | **NOT a cleared name.** Only Nabila, Laura, Avery. Recast |
| 1202 | "We've sat in the rooms where **College Board trains graders**" | Adjacent to the banned "College Board certified" positioning. Rewrite as "our coaches have scored AP exams" if and only if that is literally true |
| 574 to 578 | "College Board **changed the rules**. The AP exams are no longer about what your teen **knows**. They're about how your teen **formats their answers**." | Overstatement about a named organization. Soften to "the exam rewards reasoning and structure, and the rubric is where the points live" |
| 846 to 870 | Four parent quotes attributed "Real parent, last month" | Verify sourcing or relabel as composite |
| 440 | "a few strong scores can add up to **meaningful savings**" | Already correctly soft. Keep as the model for all money language |

### 5.3 Arithmetic and factual defects to fix in the rebuild

- **The deck's Essay B total does not add up.** Its own line items are 1 + 1 + 3 + 2 + 1 = **8**, but the final slide (line 2600) says **7 / 7**. The script has the same class of error in reverse: it awards A 0 + 0 + 1 + 1 + 0 = 2 but reports **3 / 7** (line 135), and B 1 + 1 + 3 + 2 + 1 = 8 but reports **6 / 7**.
- **Root cause:** the real APUSH DBQ rubric is 7 points as Thesis 1, Contextualization 1, Evidence 3, Analysis and Reasoning 2, where **complexity is one of the two Analysis points, not a sixth separate criterion.** Both documents double-count it. Fix the line items so they sum, or the one parent in the room who checks will catch it live.
- **Setup vs payoff mismatch:** deck line 1840 says "One scored a 3. One scored a 5", then line 2586 shows Essay A at 2/7 and line 2618 calls it "2 or 3". Pick one.
- **Deck Q2 and Q4 are the same question.** Line 257: "If your teen gets an A in their AP class, they're on track to score a 4 or 5." Line 357: "Your A-student's early A's mean they're on track for a 4 or a 5." Q4's answer block (lines 383 to 397) is **summer-frame residue**: "Three months off, and they reopen the fall textbook cold." That is a summer-slide argument sitting inside a back-to-school deck. Q4 should be replaced, and the two restored script questions (tutors, effort) are the obvious candidates.

---

## 6. EXCLUDED BY DESIGN vs MISSING BY ACCIDENT

### Excluded BY DESIGN, correctly, do not restore
Script lines **187 to 505**, the entire back half:
- Offer introduction and the "Complete ACE System" name reveal (187)
- Components 1 to 4 with dollar values (199 to 287)
- Bonuses 1 to 4 including the 48-hour accelerator (290 to 330)
- Value stack, `$15,550` and `$7,200` (333 to 341)
- Price reveal, `$3,800` / `$2,997` / `$547` (343 to 354)
- Score guarantee and the `$800` refund (357 to 367)
- Scarcity, 15 spots and 48 hours (370 to 384)
- Two paths close (387 to 407)
- The real math, four-year `$15,000` anchor (410 to 423)
- What happens after you enroll (426 to 435)
- Enrollment CTA and final CTA repeat (438 to 446, 474 to 480)
- FAQ, all seven (449 to 471)
- `$97/mo` LITE downsell (483 to 505)

Also excluded by design: everything in `Webinar_Offer.md`. **Flag one conflict:** that file names a **4-step "Comprehensive Score Certainty System"** (Diagnostic, Skill Coaching, Ongoing Support, Exam Readiness) while the deck teaches **3 breakthroughs**. Two different mechanism architectures for the same client. Someone should rule on which is canon before the rebuild, because the booking call will use the 4-step language.

**One recommended exception.** Script lines **188 to 192** sit inside the excluded offer section but are pure narrative, not sale:

> "This system was born from a devastating realization. After working inside the school system for years, I watched the AP prep approach systematically fail brilliant students, not because they weren't smart enough, but because the system itself was broken. I had countless heartbreaking conversations with devastated parents whose straight-A teens scored 2s and 3s, and I realized something shocking: even the teachers and educational experts were ill-equipped to properly support these students. The AP teachers knew their subjects inside and out, but they didn't understand how exams were actually scored. Everyone was working hard, but they were all working with incomplete information. I couldn't stand watching another brilliant teen get crushed by a system that should have lifted them up."

Lift this into positioning (deck section 3), which is currently the deck's second-thinnest section. Stop before "So I spent three years perfecting it" at line 192, and drop the results paragraph at 194 to 196 entirely.

### Missing BY ACCIDENT, restore
These were lost in the January to March V2 compression, not by any ruling. All six are teaching or belief beats, none touch the offer:

1. Pop quiz questions on tutors and on effort (script L20, L25)
2. The full CFA pain block: wins, second trap, consequence cascade, the stated fear, the reframe (L29 to L39)
3. The objection permission block and "how does that sound" (L41, L42)
4. The buyer's-questions agenda and the future-pace ladder (L43, L44)
5. The WHY block and Joe's origin moment (L46, L47)
6. The "you'll discover" curiosity stack (L48), rewritten for claims
7. Roughly half of each mechanism: named components, analogies, phase systems, outcome blocks (L57 to L71)
8. The demo disarm, the CAN'T TELL poll, and the entire post-demo payoff (L73, L76 to L78, L144 to L163)
9. The commitment ask and the three missing yes-momentum rungs (L55, L170, L174, L182)

### Needs a ruling, not a restore
**The attendance bribe** (script L45, the free "AP Success Starter Kit" given at the end). It is a Fladlien stick-strategy staple and the deck has no stick strategy at all beyond "stay with me for 45 minutes". But the deck's close now gives away a free call, and stacking a free kit on top of a free call risks diluting the single ask. Either fold it into the call ("you leave the call with your teen's AP map") or drop it deliberately. Right now it is neither.