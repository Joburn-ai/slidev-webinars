---
theme: default
colorSchema: light
title: "SupportED Tutoring | The Back-to-School Game Plan"
info: |
  THE BACK-TO-SCHOOL GAME PLAN — live webinar deck. Wed 26 Aug 2026, 8:00 PM ET.

  🔴 HOW TO USE IT: every spoken beat lives in the SPEAKER NOTES of the slide it belongs to.
  Open presenter mode (press P) and read the notes. The visible slide always carries the
  short form; the notes carry the full line. A slide is a picture, not a script.

  🔴 STRUCTURE: this file is the SPINE only — frontmatter, section dividers, and src
  includes. No slide content lives here. Each of the 8 sections is its own file under
  sections/, so two people can work on two sections without touching the same file.

  SCRIPT:  06_Clients/supported/strategy/webinar_script_2026_08_10/Full_Script_Jan_26_.md
  DESIGN:  style.css — the .sp-* system, lifted from internal/roadmap_vsl_2026_08_05.
  GATE:    scripts/deck_gate.py — run it before every deploy. It fails the build on a
           bare-slide ratio, a layout run, a missing note or an uncleared claim.

  🔴 CLAIM RULES HELD: "89% score 4s or 5s vs about 22% nationally" used ONCE, with
  "results vary". Named students NABILA, LAURA, AVERY only. "Certified AP teacher",
  never "College Board certified". No National AP Scholar. No absolute claims.
  No em-dash character anywhere.
transition: none
clickAnimation: fade-in up
fonts:
  provider: none
mdc: true
drawings:
  persist: false
layout: cover
class: text-center bleed
---

<!-- slide:000 — HOLDING SLIDE. Runs on the loop before the room fills. -->

<img class="sp-bleed" src="/images/concept/c04_parent_at_kitchen_table.png" alt="A parent at a kitchen table in the evening, laptop open" />
<div class="sp-scrim-b"></div>

<div class="relative h-full flex flex-col items-center justify-center">

<img src="/images/supported-logo.png" alt="SupportED Tutoring" class="w-36 mb-6 opacity-95" />

<div class="sp-h1 sp-onimg mx-auto">The Back-to-School Game Plan</div>

<div class="sp-say sp-onimg mt-4 mx-auto" style="color:#D8BC77;">How to turn a 3 into a 5 on the AP exam</div>

<div class="sp-cover-host mt-8">
  <img class="sp-portrait round" src="/images/dr-joe.jpg" alt="Dr Joe Sebestyen" />
  <div class="text-left">
    <div class="sp-name sp-onimg">Dr. Joe Sebestyen</div>
    <div class="sp-role" style="color:#D8BC77;">Doctorate in Educational Leadership</div>
  </div>
</div>

<div class="sp-sub sp-onimg mt-8 mx-auto" style="opacity:0.75;">Starting in 2 minutes</div>

</div>

<!--
🔴 HOLDING SLIDE. Music up, camera off. Do not start on this slide — advance once, then
go live. Nothing is spoken here.

🔴 THE OUTCOME LINE IS A LIVE DECISION. John, 2026-08-15: "the back to school game plan
that GUARANTEES a five on the AP exam. We just want the outcome very, very clear."
This currently reads "How to turn a 3 into a 5 on the AP exam", which states the outcome
without promising it. See the note at the top of slides.md before changing it.

Joe's face is on the cover per the same review, so the room knows who is talking before
he opens his mouth.
-->

---
src: ./sections/00_hold.md
---

---
layout: center
class: nomark night
---

<!-- divider:S1 -->

<div class="text-center">
<div class="sp-kicker">Section 1</div>
<div class="sp-h1 sp-onimg mx-auto">Pop Quiz</div>
<div class="sp-rule"></div>
<div class="sp-sub sp-onimg mx-auto">Five statements. Two of them will surprise you.</div>
</div>

<!--
DIVIDER. Half a beat. "Before anything else, a pop quiz." Then move.
-->

---
src: ./sections/01_quiz.md
---

---
layout: center
class: nomark ink
---

<!-- divider:S2 -->

<div class="text-center">
<div class="sp-kicker">Section 2</div>
<div class="sp-h1 sp-onimg mx-auto">What Is Really Going On</div>
<div class="sp-rule"></div>
<div class="sp-sub sp-onimg mx-auto">This part is not about your teen. It is about a system that changed.</div>
</div>

<!--
DIVIDER. Drop the energy here. The quiz was fast and loud; this is slow and quiet.
The tempo change IS the transition.
-->

---
src: ./sections/02_pain.md
---

---
layout: center
class: nomark night
---

<!-- divider:S3 -->

<div class="text-center">
<div class="sp-kicker">Section 3</div>
<div class="sp-h1 sp-onimg mx-auto">Who Is Talking</div>
<div class="sp-rule"></div>
<div class="sp-sub sp-onimg mx-auto">Fair question. Short answer.</div>
</div>

<!--
DIVIDER. Keep this genuinely short. Credibility earns the next section, it is not the show.
-->

---
src: ./sections/03_positioning.md
---

---
layout: center
class: nomark night
---

<!-- divider:S4 -->

<div class="text-center">
<div class="sp-kicker">Section 4</div>
<div class="sp-h1 sp-onimg mx-auto">The 3 Breakthroughs</div>
<div class="sp-rule"></div>
<div class="sp-sub sp-onimg mx-auto">That separate a 5 from a 3.</div>
</div>

<!--
DIVIDER. This is the teaching spine of the whole webinar. Signal it.
"Three things. Write them down."
-->

---
src: ./sections/04_mechanisms.md
---

---
layout: center
class: nomark sun
---

<!-- divider:S5 -->

<div class="text-center">
<div class="sp-kicker">Section 5</div>
<div class="sp-h1 sp-onimg mx-auto">Let's Do This Together</div>
<div class="sp-rule"></div>
<div class="sp-sub sp-onimg mx-auto">Two real essays. You grade them. Live.</div>
</div>

<!--
DIVIDER. Gold ground, used exactly three times in the deck, and this is the one that
matters most. Interaction starts here. "Grab your pen."
-->

---
src: ./sections/05_demonstration.md
---

---
layout: center
class: nomark night
---

<!-- divider:S6 -->

<div class="text-center">
<div class="sp-kicker">Section 6</div>
<div class="sp-h1 sp-onimg mx-auto">Let's Lock In What Just Happened</div>
<div class="sp-rule"></div>
</div>

<!--
DIVIDER. Recap. Short, fast, no new information.
-->

---
src: ./sections/06_recap.md
---

---
src: ./sections/07_momentum.md
---

---
layout: center
class: nomark sun
---

<!-- divider:S8 -->

<div class="text-center">
<div class="sp-kicker">Section 8</div>
<div class="sp-h1 sp-onimg mx-auto">The Back-to-School Game Plan</div>
<div class="sp-rule"></div>
<div class="sp-sub sp-onimg mx-auto">What we build with you, and how to get it.</div>
</div>

<!--
DIVIDER. The turn. Everything before this was teaching; everything after is the ask.
Do not rush it and do not apologise for it.
-->

---
src: ./sections/08_close.md
---
