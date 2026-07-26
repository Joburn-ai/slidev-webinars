---
theme: default
# NOTE: the title is Vue-rendered by Slidev, so it uses a BARE token (no braces).
title: "FF Town Hall · MONTH_YEAR"
info: |
  FF MONTHLY TOWN HALL · standing template.
  The structure never changes. Fill the {{TOKENS}}, present, done.
  Spine: Why we do this · Where we've been · Where we are · Where we're going ·
  Shoutouts + reward · The misses, acknowledged · Close.
  Fill-in SOP: README.md in this folder. ~15 minutes per month.
colorSchema: dark
highlighter: shiki
lineNumbers: false
drawings:
  persist: true
transition: slide-left
fonts:
  sans: Inter
  mono: JetBrains Mono
  weights: '400,500,600,700,800,900'
layout: cover
---

<!-- slide:cover-01 -->

<div class="absolute inset-0 flex flex-col justify-center px-20">
  <div class="flex items-center gap-3">
    <span class="th-diamond"></span>
    <span class="th-eyebrow">Funnel Futurist · all hands · the monthly drumbeat</span>
  </div>
  <h1 class="th-h1 xl mt-5">FF Town Hall</h1>
  <div class="th-cover-month mt-3"><span v-pre>{{MONTH YEAR}}</span></div>
  <div v-click class="th-lead mt-10" style="max-width: 34rem;">This is how we remember what we're doing, and why.</div>
</div>

<div class="th-footer">ff town hall · standing template · the structure never changes</div>

<!--
FRAME. Calm, warm open. Everyone lands, cameras on. One click for the why-line.
BEATS:
  - "Welcome to the town hall. Same structure as every month. That's on purpose."
  - (click) "This is how we remember what we're doing, and why."
TIMING: 30 sec
TRANSITION: straight into the recap. "So. Why do we do this."
-->

---
layout: default
---

<!-- slide:why-vision-mission-02 -->

<div class="px-16 pt-9">

<div class="th-eyebrow">01 · Why we do this <span class="dim">· the two-minute recap, every single month</span></div>

<h2 class="th-h2 mt-2">Where we're going. <span class="th-gold-t">How we get there.</span></h2>

<div class="mt-6 flex flex-col gap-4" style="max-width: 52rem;">
<v-clicks>

<div class="th-card">
  <div class="k">Vision · where we're going</div>
  <div class="v"><span v-pre>{{VISION}}</span></div>
  <div class="s">Big enough that every person's personal vision fits inside it.</div>
</div>

<div class="th-card">
  <div class="k gold">Mission · how we get there</div>
  <div class="v"><span v-pre>{{MISSION}}</span></div>
  <div class="s">What drives when the pain of escaping the current situation subsides.</div>
</div>

</v-clicks>
</div>

</div>

<div class="th-footer">why we do this · vision + mission · never changes</div>

<!--
FRAME. The recap opens EVERY town hall. After a certain point nobody needs new
information; they need to remember the core things. Read both cards out loud, verbatim.
BEATS:
  - (click) Vision. Where we're going.
  - (click) Mission. How we get there.
TIMING: 40 sec
TRANSITION: "And HOW we win matters."
-->

---
layout: default
---

<!-- slide:why-values-03 -->

<div class="px-16 pt-9">

<div class="th-eyebrow">01 · Why we do this <span class="dim">· how we win</span></div>

<h2 class="th-h2 mt-2">It's not just winning. <span class="th-gold-t">How you win matters.</span></h2>

<div class="mt-6 grid grid-cols-3 gap-4">
<v-clicks>

<div class="th-value">
  <div class="n">Internal Mastery</div>
  <div class="d">The craft compounds inside you first. Get better at getting better.</div>
</div>

<div class="th-value">
  <div class="n">Sincere Candor</div>
  <div class="d">Say the true thing, kindly, and say it now. Silence is never agreement.</div>
</div>

<div class="th-value">
  <div class="n">Stewardship &amp; Ownership</div>
  <div class="d">Act like you own it, because you do. Leave everything better than you found it.</div>
</div>

</v-clicks>
</div>

<div v-click class="th-meta mt-6"><span v-pre>{{VALUES_LOCKED_LIST}}</span> · replace this token with the sitting-locked 3 to 5 values, then never touch this slide again</div>

</div>

<div class="th-footer">why we do this · values · never changes</div>

<!--
FRAME. One value per click, one breath each. These are the current live three;
the sitting locks the canonical list, then this slide is frozen.
BEATS:
  - (click) Internal Mastery.
  - (click) Sincere Candor.
  - (click) Stewardship and Ownership.
TIMING: 40 sec
TRANSITION: "And the last piece of the why: how this whole system works."
-->

---
layout: center
class: text-center
---

<!-- slide:why-self-improving-04 -->

<div style="max-width: 50rem;" class="mx-auto">

<div class="th-eyebrow gold">01 · Why we do this <span class="dim">· the promise</span></div>

<div class="th-h1 mt-5">This system <span class="th-gold-t">self-improves</span><br>as long as we stick to it.</div>

<v-click>

<div class="th-lead mt-8">We set targets. We miss some. That is the system working, not failing.</div>

</v-click>

<v-click>

<div class="th-callout mt-6">A miss just means: <b>okay, what do we have to do.</b></div>

</v-click>

</div>

<div class="th-footer">why we do this · targets doctrine · never changes</div>

<!--
FRAME. The targets doctrine, stated plainly so misses never become fear or theater.
BEATS:
  - The system self-improves as long as we stick to it.
  - (click) Targets get missed. That's the system working.
  - (click) A miss just means: okay, what do we have to do.
TIMING: 40 sec. That closes the 2-minute recap.
TRANSITION: "So. Last month."
-->

---
layout: center
---

<!-- slide:divider-been-05 -->

<div class="th-ghostnum">02</div>

<div class="relative z-1 text-center">
  <div class="th-eyebrow">Section 02</div>
  <div class="th-h1 mt-3">Where we've been</div>
  <div v-click class="th-lead mt-5"><span v-pre>{{LAST MONTH}}</span>, honestly. Planned against actual.</div>
</div>

<div class="th-footer">where we've been</div>

<!--
FRAME. Section turn. Slow down for half a beat.
TIMING: 10 sec
TRANSITION: "Here's the scoreboard."
-->

---
layout: default
---

<!-- slide:been-planned-actual-06 -->

<div class="px-16 pt-9">

<div class="th-eyebrow">02 · Where we've been <span class="dim">· the scoreboard</span></div>

<h2 class="th-h2 mt-2">What we planned. <span class="th-teal-t">What actually happened.</span></h2>

<div v-click class="mt-6" style="max-width: 54rem;">
<table class="th-table" v-pre>
<thead>
<tr><th>Objective</th><th>Planned</th><th>Actual</th></tr>
</thead>
<tbody>
<tr><td>{{OBJ_1_NAME}}</td><td>{{OBJ_1_PLANNED}}</td><td>{{OBJ_1_ACTUAL}}</td></tr>
<tr><td>{{OBJ_2_NAME}}</td><td>{{OBJ_2_PLANNED}}</td><td>{{OBJ_2_ACTUAL}}</td></tr>
<tr><td>{{OBJ_3_NAME}}</td><td>{{OBJ_3_PLANNED}}</td><td>{{OBJ_3_ACTUAL}}</td></tr>
<tr><td>{{OBJ_4_NAME}}</td><td>{{OBJ_4_PLANNED}}</td><td>{{OBJ_4_ACTUAL}}</td></tr>
</tbody>
</table>
</div>

<div v-click class="th-lead mt-6">One line on the month: <span class="th-gold-t font-bold" v-pre>{{LAST_MONTH_VERDICT}}</span></div>

</div>

<div class="th-footer">where we've been · planned vs actual</div>

<!--
MOVE FAST. Numbers first, no editorializing row by row. The verdict line lands last.
BEATS:
  - (click) The table. Read the gaps out loud where they exist. No blame register.
  - (click) The one-line verdict on the month.
TIMING: 60 sec
TRANSITION: "Here's how the month actually moved."
-->

---
layout: default
---

<!-- slide:been-timeline-07 -->

<div class="px-16 pt-8">

<div class="th-eyebrow">02 · Where we've been <span class="dim">· the shape of the month</span></div>

<h2 class="th-h2 mt-2">The month in four beats.</h2>

<div v-click class="flex justify-center mt-4">

```mermaid {scale: 0.62}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#F7F5EE','lineColor':'#4FBDBD','cScale0':'#14304F','cScale1':'#2E8B8B','cScale2':'#8a701f','cScale3':'#94463B','cScaleLabel0':'#F7F5EE','cScaleLabel1':'#F7F5EE','cScaleLabel2':'#F7F5EE','cScaleLabel3':'#F7F5EE'}}}%%
timeline
    title LAST_MONTH_NAME
    Week 1 : W1_HEADLINE
    Week 2 : W2_HEADLINE
    Week 3 : W3_HEADLINE
    Week 4 : W4_HEADLINE
```

</div>

</div>

<div class="th-footer">where we've been · timeline</div>

<!--
ZOOM. One headline per week; the visual carries it. NOTE: tokens inside the Mermaid
block are bare CAPS (no curly braces; braces break the diagram parser). Replace
LAST_MONTH_NAME + W1..W4_HEADLINE when filling in.
TIMING: 40 sec
TRANSITION: "Which brings us to today."
-->

---
layout: center
---

<!-- slide:divider-now-08 -->

<div class="th-ghostnum">03</div>

<div class="relative z-1 px-16" style="max-width: 58rem;">
  <div class="th-eyebrow">Section 03</div>
  <div class="th-h1 mt-3">Where we are</div>
  <div class="th-lead mt-4">Five departments. One slide each. Ninety seconds each. Same format every month.</div>

<div v-click class="mt-7 flex gap-3 flex-wrap">
  <span class="th-chip">Objective + definition of done</span>
  <span class="th-chip gold">3 numbers · planned / actual / next target</span>
  <span class="th-chip rust">One win · one miss · one ask</span>
</div>

</div>

<div class="th-footer">where we are · the 90-second format</div>

<!--
FRAME. Set the rule before the first report so the rhythm holds.
BEATS:
  - Five departments, 90 seconds each.
  - (click) The locked format: objective + DoD, three numbers, win-miss-ask. No slideware beyond this.
TIMING: 20 sec
TRANSITION: "Acquisition, you're up."
-->

---
layout: default
---

<!-- slide:dept-1-acquisition-09 -->

<div class="px-14 pt-7">

<div class="th-eyebrow">Where we are · dept 1 of 5 · <span v-pre>{{ACQ_OWNER}}</span> reporting</div>

<h2 class="th-h2 mt-1">Acquisition <span class="th-teal-t">/ Pipeline</span></h2>

<div class="th-obj mt-4">
  <div class="row"><span class="k">Objective</span><span v-pre>{{ACQ_OBJECTIVE}}</span></div>
  <div class="row"><span class="k">Done when</span><span v-pre>{{ACQ_DOD}}</span></div>
</div>

<div v-click class="grid grid-cols-3 gap-4 mt-4">
  <div class="th-stat"><div class="lbl">Planned</div><div class="val teal" v-pre>{{ACQ_PLANNED}}</div></div>
  <div class="th-stat"><div class="lbl">Actual</div><div class="val gold" v-pre>{{ACQ_ACTUAL}}</div></div>
  <div class="th-stat"><div class="lbl">Next target</div><div class="val" v-pre>{{ACQ_NEXT_TARGET}}</div></div>
</div>

<div v-click class="mt-4 flex flex-col gap-2">
  <div class="th-row win"><span class="tag">Win</span><span v-pre>{{ACQ_WIN}}</span></div>
  <div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{ACQ_MISS}}</span></div>
  <div class="th-row ask"><span class="tag">Ask</span><span v-pre>{{ACQ_ASK}}</span></div>
</div>

</div>

<div class="th-footer">where we are · acquisition / pipeline · 90 seconds</div>

<!--
MOVE FAST. The owner talks, the slide keeps them honest. 90 seconds hard.
BEATS:
  - Objective + done-when, one breath.
  - (click) The three numbers. Planned, actual, next.
  - (click) One win, one miss, one ask. The ask names WHO it's for.
TIMING: 90 sec
TRANSITION: "Delivery."
-->

---
layout: default
---

<!-- slide:dept-2-delivery-10 -->

<div class="px-14 pt-7">

<div class="th-eyebrow">Where we are · dept 2 of 5 · <span v-pre>{{DEL_OWNER}}</span> reporting</div>

<h2 class="th-h2 mt-1">Delivery <span class="th-gold-t">/ Client Work</span></h2>

<div class="th-obj mt-4">
  <div class="row"><span class="k">Objective</span><span v-pre>{{DEL_OBJECTIVE}}</span></div>
  <div class="row"><span class="k">Done when</span><span v-pre>{{DEL_DOD}}</span></div>
</div>

<div v-click class="grid grid-cols-3 gap-4 mt-4">
  <div class="th-stat"><div class="lbl">Planned</div><div class="val teal" v-pre>{{DEL_PLANNED}}</div></div>
  <div class="th-stat"><div class="lbl">Actual</div><div class="val gold" v-pre>{{DEL_ACTUAL}}</div></div>
  <div class="th-stat"><div class="lbl">Next target</div><div class="val" v-pre>{{DEL_NEXT_TARGET}}</div></div>
</div>

<div v-click class="mt-4 flex flex-col gap-2">
  <div class="th-row win"><span class="tag">Win</span><span v-pre>{{DEL_WIN}}</span></div>
  <div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{DEL_MISS}}</span></div>
  <div class="th-row ask"><span class="tag">Ask</span><span v-pre>{{DEL_ASK}}</span></div>
</div>

</div>

<div class="th-footer">where we are · delivery / client work · 90 seconds</div>

<!--
MOVE FAST. Same rhythm as the last report. 90 seconds hard.
TIMING: 90 sec
TRANSITION: "Systems."
-->

---
layout: default
---

<!-- slide:dept-3-systems-11 -->

<div class="px-14 pt-7">

<div class="th-eyebrow">Where we are · dept 3 of 5 · <span v-pre>{{SYS_OWNER}}</span> reporting</div>

<h2 class="th-h2 mt-1">Systems <span class="th-teal-t">/ AIOS</span></h2>

<div class="th-obj mt-4">
  <div class="row"><span class="k">Objective</span><span v-pre>{{SYS_OBJECTIVE}}</span></div>
  <div class="row"><span class="k">Done when</span><span v-pre>{{SYS_DOD}}</span></div>
</div>

<div v-click class="grid grid-cols-3 gap-4 mt-4">
  <div class="th-stat"><div class="lbl">Planned</div><div class="val teal" v-pre>{{SYS_PLANNED}}</div></div>
  <div class="th-stat"><div class="lbl">Actual</div><div class="val gold" v-pre>{{SYS_ACTUAL}}</div></div>
  <div class="th-stat"><div class="lbl">Next target</div><div class="val" v-pre>{{SYS_NEXT_TARGET}}</div></div>
</div>

<div v-click class="mt-4 flex flex-col gap-2">
  <div class="th-row win"><span class="tag">Win</span><span v-pre>{{SYS_WIN}}</span></div>
  <div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{SYS_MISS}}</span></div>
  <div class="th-row ask"><span class="tag">Ask</span><span v-pre>{{SYS_ASK}}</span></div>
</div>

</div>

<div class="th-footer">where we are · systems / aios · 90 seconds</div>

<!--
MOVE FAST. Same rhythm. 90 seconds hard.
TIMING: 90 sec
TRANSITION: "Team ops."
-->

---
layout: default
---

<!-- slide:dept-4-teamops-12 -->

<div class="px-14 pt-7">

<div class="th-eyebrow">Where we are · dept 4 of 5 · <span v-pre>{{TOPS_OWNER}}</span> reporting</div>

<h2 class="th-h2 mt-1">Team Ops <span class="th-gold-t">/ VA</span></h2>

<div class="th-obj mt-4">
  <div class="row"><span class="k">Objective</span><span v-pre>{{TOPS_OBJECTIVE}}</span></div>
  <div class="row"><span class="k">Done when</span><span v-pre>{{TOPS_DOD}}</span></div>
</div>

<div v-click class="grid grid-cols-3 gap-4 mt-4">
  <div class="th-stat"><div class="lbl">Planned</div><div class="val teal" v-pre>{{TOPS_PLANNED}}</div></div>
  <div class="th-stat"><div class="lbl">Actual</div><div class="val gold" v-pre>{{TOPS_ACTUAL}}</div></div>
  <div class="th-stat"><div class="lbl">Next target</div><div class="val" v-pre>{{TOPS_NEXT_TARGET}}</div></div>
</div>

<div v-click class="mt-4 flex flex-col gap-2">
  <div class="th-row win"><span class="tag">Win</span><span v-pre>{{TOPS_WIN}}</span></div>
  <div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{TOPS_MISS}}</span></div>
  <div class="th-row ask"><span class="tag">Ask</span><span v-pre>{{TOPS_ASK}}</span></div>
</div>

</div>

<div class="th-footer">where we are · team ops / va · 90 seconds</div>

<!--
MOVE FAST. Same rhythm. 90 seconds hard.
TIMING: 90 sec
TRANSITION: "Finance closes the round."
-->

---
layout: default
---

<!-- slide:dept-5-finance-13 -->

<div class="px-14 pt-7">

<div class="th-eyebrow">Where we are · dept 5 of 5 · <span v-pre>{{FIN_OWNER}}</span> reporting</div>

<h2 class="th-h2 mt-1">Finance <span class="th-teal-t">/ Ops</span></h2>

<div class="th-obj mt-4">
  <div class="row"><span class="k">Objective</span><span v-pre>{{FIN_OBJECTIVE}}</span></div>
  <div class="row"><span class="k">Done when</span><span v-pre>{{FIN_DOD}}</span></div>
</div>

<div v-click class="grid grid-cols-3 gap-4 mt-4">
  <div class="th-stat"><div class="lbl">Planned</div><div class="val teal" v-pre>{{FIN_PLANNED}}</div></div>
  <div class="th-stat"><div class="lbl">Actual</div><div class="val gold" v-pre>{{FIN_ACTUAL}}</div></div>
  <div class="th-stat"><div class="lbl">Next target</div><div class="val" v-pre>{{FIN_NEXT_TARGET}}</div></div>
</div>

<div v-click class="mt-4 flex flex-col gap-2">
  <div class="th-row win"><span class="tag">Win</span><span v-pre>{{FIN_WIN}}</span></div>
  <div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{FIN_MISS}}</span></div>
  <div class="th-row ask"><span class="tag">Ask</span><span v-pre>{{FIN_ASK}}</span></div>
</div>

</div>

<div class="th-footer">where we are · finance / ops · 90 seconds</div>

<!--
MOVE FAST. Only share what the whole team should see; detail lives in the finance lane.
TIMING: 90 sec
TRANSITION: "That's today. Now, forward."
-->

---
layout: center
---

<!-- slide:divider-going-14 -->

<div class="th-ghostnum">04</div>

<div class="relative z-1 text-center">
  <div class="th-eyebrow">Section 04</div>
  <div class="th-h1 mt-3">Where we're going</div>
  <div v-click class="th-lead mt-5">One goal for <span v-pre>{{NEXT MONTH}}</span>, tied to the quarter.</div>
</div>

<div class="th-footer">where we're going</div>

<!--
FRAME. Section turn. Lift the energy; this is the part people leave with.
TIMING: 10 sec
TRANSITION: "Here it is."
-->

---
layout: default
---

<!-- slide:going-goal-15 -->

<div class="px-16 pt-10">

<div class="th-eyebrow gold">04 · Where we're going <span class="dim">· the month's job</span></div>

<div class="th-h1 mt-4" style="max-width: 54rem;"><span class="th-gold-t" v-pre>{{NEXT_MONTH_GOAL}}</span></div>

<v-click>

<div class="th-obj mt-8" style="max-width: 52rem;">
  <div class="row"><span class="k">Serves</span><span v-pre>{{QUARTER_TARGET}}</span></div>
  <div class="row"><span class="k">Done when</span><span v-pre>{{NEXT_MONTH_DOD}}</span></div>
</div>

</v-click>

</div>

<div class="th-footer">where we're going · next month's goal</div>

<!--
FRAME then LAND. The goal in one sentence, big type. Then anchor it to the quarter
so nobody mistakes a month goal for a floating wish.
BEATS:
  - The goal. Read it slowly.
  - (click) What quarter target it serves + the definition of done.
TIMING: 45 sec
TRANSITION: "On the calendar, it looks like this."
-->

---
layout: default
---

<!-- slide:going-roadmap-16 -->

<div class="px-16 pt-8">

<div class="th-eyebrow gold">04 · Where we're going <span class="dim">· the month inside the quarter</span></div>

<h2 class="th-h2 mt-2">The road, drawn.</h2>

<div v-click class="flex justify-center mt-4">

```mermaid {scale: 0.68}
%%{init: {'theme':'dark','themeVariables':{'taskBkgColor':'#2E8B8B','taskBorderColor':'#4FBDBD','taskTextLightColor':'#F7F5EE','taskTextDarkColor':'#0A1524','activeTaskBkgColor':'#E2C25C','activeTaskBorderColor':'#E2C25C','titleColor':'#F7F5EE','textColor':'#C9D4E4','sectionBkgColor':'rgba(255,255,255,0.04)','altSectionBkgColor':'rgba(255,255,255,0.01)','gridColor':'#3B516E','todayLineColor':'#E0755C'},'gantt':{'barHeight':30,'fontSize':15,'sectionFontSize':14,'gridLineStartPadding':8}}}%%
gantt
    title QUARTER_NAME
    dateFormat YYYY-MM-DD
    axisFormat %b %d
    %% EDIT DATES MONTHLY: keep real dates here; the gantt parser needs them.
    section Quarter target
    QUARTER_TARGET_LABEL          :q1, 2026-08-01, 92d
    section This month
    NEXT_MONTH_GOAL_LABEL         :active, m1, 2026-08-03, 26d
    MILESTONE_1_LABEL             :milestone, ms1, 2026-08-14, 1d
    MILESTONE_2_LABEL             :milestone, ms2, 2026-08-28, 1d
```

</div>

</div>

<div class="th-footer">where we're going · roadmap</div>

<!--
ZOOM. Point at the bar, not the audience. The month is a bar inside the quarter's bar.
NOTE: tokens inside the Mermaid block are bare CAPS (no curly braces) and the DATES
must stay real calendar dates or the gantt parser errors. Edit both monthly.
TIMING: 40 sec
TRANSITION: "Before we close the loop: the good stuff."
-->

---
layout: default
---

<!-- slide:shoutouts-17 -->

<div class="px-16 pt-9">

<div class="th-eyebrow gold">05 · Shoutouts</div>

<h2 class="th-h2 mt-2">Celebrated <span class="th-gold-t">by name.</span></h2>

<div class="mt-7 flex flex-col gap-8">
<v-clicks>

<div>
  <div class="th-name"><span v-pre>{{SHOUTOUT_1_NAME}}</span></div>
  <div class="th-lead mt-2"><span v-pre>{{SHOUTOUT_1_WHAT}}</span> <span class="th-mute-t">· killer work here.</span></div>
</div>

<div>
  <div class="th-name"><span v-pre>{{SHOUTOUT_2_NAME}}</span></div>
  <div class="th-lead mt-2"><span v-pre>{{SHOUTOUT_2_WHAT}}</span> <span class="th-mute-t">· killer work here.</span></div>
</div>

</v-clicks>
</div>

</div>

<div class="th-footer">shoutouts · wins have names</div>

<!--
LAND. Names in big gold type. Pause after each; let the room react. Applause is allowed.
BEATS:
  - (click) Name one + the specific thing they did.
  - (click) Name two + the specific thing they did.
TIMING: 60 sec
TRANSITION: "And because the team won, the team gets the reward."
-->

---
layout: center
class: text-center
---

<!-- slide:reward-18 -->

<div style="max-width: 46rem;" class="mx-auto">

<div class="th-eyebrow gold">05 · The team reward</div>

<v-click>

<div class="th-heroCard mt-7">
  <div class="k">Earned this month</div>
  <div class="v"><span v-pre>{{TEAM_REWARD}}</span></div>
</div>

</v-click>

<div v-click class="th-lead mt-7">Won together. Enjoyed together.</div>

</div>

<div class="th-footer">shoutouts · team reward</div>

<!--
LAND. Keep it fun. The reward is the team's, not a bonus scheme.
TIMING: 30 sec
TRANSITION: "Now the honest part."
-->

---
layout: default
---

<!-- slide:misses-19 -->

<div class="px-16 pt-8">

<div class="th-eyebrow rust">06 · The misses, acknowledged</div>

<h2 class="th-h2 mt-2">What we said we'd do, <span class="th-rust-t">and didn't.</span></h2>

<div class="mt-5 flex flex-col gap-2" style="max-width: 52rem;">
<v-clicks>

<div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{MISS_1}}</span></div>

<div class="th-row miss"><span class="tag">Miss</span><span v-pre>{{MISS_2}}</span></div>

</v-clicks>
</div>

<v-click>

<div class="th-heroCard rustline mt-6" style="max-width: 52rem;">
  <div class="k">The system change we're making</div>
  <div class="v"><span v-pre>{{SYSTEM_CHANGE}}</span></div>
</div>

</v-click>

<div v-click class="th-lead mt-5">No blame. No theater. A miss just means: okay, what do we have to do.</div>

</div>

<div class="th-footer">the misses · acknowledged, then answered</div>

<!--
FRAME. Honest register, level voice. Own the misses as the company's, not a person's.
BEATS:
  - (click) Miss one, plainly.
  - (click) Miss two, plainly.
  - (click) The system change. This is the payoff: a miss produces a fix, every time.
  - (click) Restate the doctrine line.
TIMING: 90 sec
TRANSITION: "Which leaves one thing."
-->

---
layout: center
class: text-center
---

<!-- slide:close-one-thing-20 -->

<div style="max-width: 52rem;" class="mx-auto">

<div class="th-eyebrow gold">07 · Close</div>

<div class="th-lead mt-5">If we do nothing else in <span v-pre>{{NEXT MONTH}}</span>, we do this:</div>

<v-click>

<div class="th-h1 xl mt-6"><span class="th-gold-t" v-pre>{{ONE_THING}}</span></div>

</v-click>

</div>

<div class="th-footer">close · the one thing</div>

<!--
LAND. The single takeaway. Say it, click it, let it sit for two full seconds.
TIMING: 30 sec
TRANSITION: "Same time next month."
-->

---
layout: center
class: text-center
---

<!-- slide:close-next-date-21 -->

<div class="mx-auto">

<div class="flex items-center justify-center gap-3">
  <span class="th-diamond"></span>
  <span class="th-eyebrow">See you next month</span>
</div>

<div class="th-h1 mt-5">Next town hall</div>

<div class="th-cover-month mt-4"><span v-pre>{{NEXT_TOWNHALL_DATE}}</span></div>

<v-click>

<div class="th-lead mt-9">Same structure. New numbers. That's the point.</div>

</v-click>

</div>

<div class="th-footer">ff town hall · standing template · the structure never changes</div>

<!--
LAND. Eye-contact close. Date on screen, one click for the closing line, done.
BEATS:
  - Next town hall date.
  - (click) "Same structure. New numbers. That's the point."
TIMING: 20 sec. Total runtime target: about 20 minutes.
-->
