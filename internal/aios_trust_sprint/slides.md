---
theme: default
title: The AIOS Trust Sprint
colorSchema: dark
drawings:
  persist: true
transition: slide-left
fonts:
  sans: Inter
---

<!-- slide:cover-01 -->

<div class="ts-bg"></div>

<div class="absolute inset-0 flex flex-col justify-center px-20">
  <div class="ts-eyebrow">15-Minute Sprint Workshop</div>
  <div class="ts-h1 mt-3">The AIOS Trust Sprint</div>
  <div class="ts-sub mt-5 max-w-3xl">Before AIOS goes to clients, it goes through <b style="color:#fff">us</b> and <b style="color:#fff">our team</b>. Can we trust them with it, and is everyone pointed at the highest-leverage thing?</div>
  <div class="ts-meta mt-10">John + co-founder · 2026-06-13 · run it live, draw on it, check things off</div>
</div>

<!--
FRAME. Set the stakes in 20 seconds. This is a fast working session, not a presentation. We will draw on slides 5 and 7. Timer: 15 min total.
-->

---
layout: center
class: text-center
---

<!-- slide:problem-02 -->

<div class="ts-bg"></div>

<div class="ts-eyebrow">The problem we are solving</div>
<div class="ts-h2 mt-4 max-w-4xl mx-auto">How do we trust our own team with AIOS<br/>before we roll it out to everybody else?</div>

<div class="mt-10 max-w-4xl mx-auto">
<v-clicks>

<div class="ts-card text-left mt-3"><span class="t">The team is on the highest-leverage things</span> <span class="d">, not busy-but-not-moving</span></div>
<div class="ts-card text-left mt-3"><span class="t">Clients get their stuff done</span> <span class="d">, without us having to think or worry about it</span></div>
<div class="ts-card text-left mt-3"><span class="t">Zero misallocated team resources</span> <span class="d">, the right people on the right work</span></div>

</v-clicks>
</div>

<!--
FRAME. Read the problem aloud. The three cards are the desired end-state. Click one per beat. This is the lens for the whole sprint.
-->

---

<!-- slide:mission-03 -->

<div class="ts-bg"></div>

<div class="px-16 pt-12">
<div class="ts-eyebrow">Today's mission</div>
<div class="ts-h2 mt-3">Get AIOS to completion , and prove it on ourselves first</div>

<div class="grid grid-cols-2 gap-4 mt-8">
<v-clicks>

<div class="ts-card"><span class="n">01</span> <span class="t">Review the cert end-to-end</span><div class="d mt-1">Walk the whole question bank. Does it make sense? Is it clear? (John's main task.)</div></div>
<div class="ts-card"><span class="n">02</span> <span class="t">Build the Typeform</span><div class="d mt-1">Turn the 108-item bank into the live form. (Claude builds it.)</div></div>
<div class="ts-card"><span class="n">03</span> <span class="t">Run the cert as a test</span><div class="d mt-1">John takes it as a candidate, recorded. Find what breaks before anyone else sees it.</div></div>
<div class="ts-card"><span class="n">04</span> <span class="t">Surface the cert gaps</span><div class="d mt-1">Every confusion = a defect logged into the v2.1 fold. The run IS the QC.</div></div>

</v-clicks>
</div>
</div>

<!--
MOVE FAST. One card per beat. This is the AIOS-completion critical path. The validation run (03) is the single highest-leverage QC act.
-->

---
layout: center
class: text-center
---

<!-- slide:three-questions-04 -->

<div class="ts-bg"></div>

<div class="ts-eyebrow">The heart of the sprint , answer these three</div>

<div class="mt-8 max-w-4xl mx-auto text-left">
<v-clicks>

<div class="ts-q mt-4"><span class="num">1.</span>Who is everyone on our team?</div>
<div class="ts-q mt-4"><span class="num">2.</span>What is everybody working on <span style="color:#9db6e0">right now</span>?</div>
<div class="ts-q mt-4"><span class="num">3.</span>What <span style="color:#5fd6b0">should</span> they work on , the most effective use of their time?</div>

</v-clicks>
</div>

<div class="mt-10" v-click>
<span class="ts-pill rose">Challenge the assumption</span>
<div class="ts-sub mt-3 max-w-3xl mx-auto">Where do we <i>think</i> they are on capacity vs. reality? What is the real priority of their focus? Push on it.</div>
</div>

<!--
MOVE FAST. These three questions are the whole evaluation. Reveal one at a time. The last beat is the assumption-challenge, the part most teams skip.
-->

---

<!-- slide:whiteboard-team-05 -->

<div class="ts-bg"></div>

<div class="px-12 pt-6">
<div class="flex items-center justify-between">
<div class="ts-h2">Whiteboard , the team: who's on what?</div>
<span class="ts-pill teal">draw live: pen icon, bottom toolbar</span>
</div>

<div class="grid grid-cols-4 gap-3 mt-5">
  <div class="ts-chip">Justine</div>
  <div class="ts-chip">Keziah</div>
  <div class="ts-chip">Shannon</div>
  <div class="ts-chip">Missy</div>
  <div class="ts-chip">Peter</div>
  <div class="ts-chip">Miles</div>
  <div class="ts-chip">Jaden</div>
  <div class="ts-chip">Ronald</div>
  <div class="ts-chip">Ariel</div>
  <div class="ts-chip cs">Febi<span class="role">client liaison + CS (+ more)</span></div>
  <div class="ts-chip constraint">Salman<span class="role">3rd-party, Phoenix-only = constraint</span></div>
  <div class="ts-chip" style="border-style:dashed;opacity:.6;">+ anyone missing?</div>
</div>

<div class="ts-wb mt-4">Per person, mark it up live: <b style="color:#9db6e0">NOW</b> vs <b style="color:#5fd6b0">SHOULD</b>, tag each acquisition / fulfillment / ops, circle the constraint (Salman), star the highest-leverage move. Every NOW &ne; SHOULD = a reallocation.</div>
</div>

<!--
STOP. This is a whiteboard beat, no v-clicks. Draw the answers in live (drauu persists). Tip from project_management: tag each item acquisition / fulfillment / operations, and watch for the avoidance pattern (lots of building, no acquisition).
-->

---

<!-- slide:trust-gate-06 -->

<div class="ts-bg"></div>

<div class="px-16 pt-12">
<div class="ts-eyebrow">How trust gets earned (not assumed)</div>
<div class="ts-h2 mt-3">Every teammate goes through AIOS themselves</div>

<div class="mt-8 max-w-4xl">
<v-clicks>

<div class="ts-card mt-3"><span class="t">Run the onboarding wizard</span> <span class="d">, the interactive way to actually understand how it all works (role-aware, caveman-clear, no skipped steps)</span></div>
<div class="ts-card mt-3"><span class="t">Set up CODEOWNERS + access</span> <span class="d">, so we get the right access in place and the constitution files are gated</span></div>
<div class="ts-card mt-3"><span class="t">Prove the brain is wired</span> <span class="d">, context loads, F6 check passes, it answers from our real docs</span></div>
<div class="ts-card mt-3"><span class="t">Take the cert</span> <span class="d">, the proof they can be trusted with the keys</span></div>

</v-clicks>
</div>
</div>

<!--
MOVE FAST. This is the answer to "how do we trust them." They earn it by running the same path a client operator will. One card per beat.
-->

---

<!-- slide:whiteboard-track-07 -->

<div class="ts-bg"></div>

<div class="px-12 pt-8">
<div class="flex items-center justify-between">
<div class="ts-h2">Whiteboard , track it, check it off</div>
<span class="ts-pill teal">tick as we go</span>
</div>

<table class="ts-board w-full mt-5" style="border-collapse:collapse;">
<tr><td class="ts-th p-3" style="width:55%">Task / teammate</td><td class="ts-th p-3">Owner</td><td class="ts-th p-3">Done?</td></tr>
<tr class="ts-row"><td>Cert reviewed end-to-end</td><td>John</td><td>&nbsp;</td></tr>
<tr class="ts-row"><td>Typeform built</td><td>Claude</td><td>&nbsp;</td></tr>
<tr class="ts-row"><td>John runs the cert (recorded)</td><td>John</td><td>&nbsp;</td></tr>
<tr class="ts-row"><td>Team mapped (slide 5)</td><td>both</td><td>&nbsp;</td></tr>
<tr class="ts-row"><td>Reallocations decided</td><td>both</td><td>&nbsp;</td></tr>
<tr class="ts-row"><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

<div class="ts-wb mt-3">Are we on track? Anything blocked? Draw a check, circle a blocker.</div>
</div>

<!--
STOP. Whiteboard. Tick the boxes live as you confirm each. Add rows for per-teammate reallocations from slide 5.
-->

---
layout: center
class: text-center
---

<!-- slide:land-08 -->

<div class="ts-bg"></div>

<div class="ts-eyebrow">What we walk away with</div>
<div class="ts-h2 mt-4 max-w-4xl mx-auto">Decisions, owners, and the one next move</div>

<div class="mt-8 max-w-4xl mx-auto text-left">
<v-clicks>

<div class="ts-card mt-3"><span class="t">Who owns what</span> <span class="d">, the reallocations from the team map are decided, not just discussed</span></div>
<div class="ts-card mt-3"><span class="t">AIOS completion path is clear</span> <span class="d">, review -> Typeform -> John's run -> gaps logged</span></div>
<div class="ts-card mt-3"><span class="t">This is Part 1</span> <span class="d">, Part 2 = execute the reallocation + every teammate runs AIOS + the cert</span></div>

</v-clicks>
</div>

<div class="mt-8 ts-foot" v-click>The unlock: a team on the highest-leverage things, that we do not have to worry about.</div>

<!--
LAND. Sequential reveal of the takeaways. End on the identity beat: the unlock line. Hold it 2 seconds. Then go run task 01.
-->
