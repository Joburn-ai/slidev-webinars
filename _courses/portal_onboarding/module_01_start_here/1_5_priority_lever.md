---
theme: default
title: How the Priority Lever Works
info: |
  Portal Onboarding · Module 1 Start Here · Lesson 1.5
  Template deck for the ramp. Showcases v-mark (programmatic circle/underline/
  strike), v-click staged reveal, and a click-by-click "draws itself" diagram.
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  persist: true
transition: slide-left
mdc: true
fonts:
  sans: Inter
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-12">

<div class="ff-bar"></div>

<div class="max-w-5xl text-center">

<div class="ff-eyebrow">Start Here · Lesson 1.5</div>

<h1 style="font-size: 4rem; color: white;">
How the <span class="ff-cyan">Priority Lever</span> works
</h1>

<p style="font-size: 1.4rem; color: rgba(255,255,255,0.85); margin-top: 1.5rem; max-width: 44rem; margin-left:auto; margin-right:auto;">
The single move that, pulled hard this month, makes everything else easier or unnecessary.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
JOHN COBURN · FUNNEL FUTURIST
</div>

</div>

<!--
Open on the mechanism by name. This is the engine of the whole offer. Slow down.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">What&apos;s wrong with this picture?</div>

<h1 style="font-size: 5rem; margin-bottom: 1rem;">
<span v-mark.strike-through.red="2">Priorities</span>
</h1>

<p v-click="1" style="font-size: 1.2rem; color:#64748b; margin-bottom: 2rem;">
*staring at the word for a beat*
</p>

<h1 v-click="3" style="font-size: 4.5rem; margin-top: 1rem;">
<span v-mark.circle.cyan="4">Priority.</span>
</h1>

<p v-click="5" style="font-size: 1.3rem; margin-top: 2rem; max-width: 44rem; text-align:center; font-weight:500;">
From Latin <em>prior</em> &mdash; what comes before. It entered English around 1450 and stayed singular for <strong>five hundred years</strong>. The plural &ldquo;priorities&rdquo; didn&apos;t enter common usage until the mid-twentieth century. Convenient timing.
</p>

<p v-click="6" style="font-size: 1.5rem; margin-top: 1.5rem; max-width: 40rem; text-align:center; font-weight:700; color:var(--ff-navy);">
You can&apos;t have <span class="ff-orange">multiple</span> most importants.<br/>You can only have <span class="ff-cyan">one</span>.
</p>

</div>

<!--
TONGUE-IN-CHEEK opener.
Click 1: pause beat ("staring at the word").
Click 2: v-mark strike-through on "Priorities".
Click 3: "Priority." (singular) clicks in.
Click 4: v-mark circle on "Priority".
Click 5: etymology punchline (1450, 500 years singular, 20th century plural).
Click 6: the logical kicker — most importants is a contradiction.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-20" style="background: var(--ff-cream);">

<div class="ff-eyebrow">The definition</div>

<h2 style="font-size: 2.2rem; max-width: 50rem; text-align:center; line-height:1.3;">
Your Priority Lever is the single move that, pulled hard this month,<br/>
makes everything else <span v-mark.underline.cyan="1">easier or unnecessary</span>.
</h2>

<p v-click="2" style="font-size: 1.3rem; margin-top: 2.5rem; max-width: 42rem; text-align:center; font-weight:500;">
That&apos;s the test. Not what&apos;s urgent. Not what&apos;s loudest. The one thing that, if it moves, shrinks the rest of your list.
</p>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Every week, the same move</div>

<h2 style="font-size: 2rem; margin-bottom: 2rem;">You bring three things. We pick one.</h2>

<div class="grid grid-cols-3 gap-5 max-w-5xl mx-auto w-full" style="min-height: 130px;">

<div v-click="1" class="lever-tile" :class="$clicks >= 4 ? 'parked' : ''">
<span v-mark.crossed-off.red="4">Run more ads</span>
</div>

<div v-click="2" class="lever-tile" :class="$clicks >= 4 ? 'chosen' : ''">
<span v-mark.circle.cyan="4">Fix the offer</span>
</div>

<div v-click="3" class="lever-tile" :class="$clicks >= 4 ? 'parked' : ''">
<span v-mark.crossed-off.red="4">New funnel build</span>
</div>

</div>

<p v-click="5" style="font-size: 1.25rem; margin-top: 2.5rem; max-width: 44rem; margin-left:auto; margin-right:auto; text-align:center; font-weight:600;">
One lever, chosen from your real numbers. The other two get parked. <span class="ff-orange" style="font-weight:800;">That&apos;s the whole methodology.</span>
</p>

</div>

<!--
THE SHOWCASE: the diagram assembles click by click. Three options fade in
(clicks 1-3). On click 4, the chosen one gets a hand-drawn circle and the other
two get crossed off and dimmed, all programmatic. This is "draw without drawing."
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">Why most operators never find it</div>

<h2 style="font-size: 2.6rem; color: white; line-height:1.3;">
They spread across ten half-efforts<br/>and call it <span v-mark.circle.orange="1">being busy</span>.
</h2>

<p v-click="2" style="font-size: 1.3rem; color: rgba(255,255,255,0.85); margin-top: 2.5rem; line-height:1.5;">
Busy feels like progress. It isn&apos;t. Every week becomes a different scattered push, and twelve months later they&apos;re running the post-mortem on a quarter that never had a chance.
</p>

</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Two things to do with this</div>

<div class="space-y-4 mt-2 max-w-4xl mx-auto w-full">

<div v-click class="ff-card" style="display:flex; align-items:flex-start; gap:1.25rem;">
<span style="font-size:1.8rem;" class="ff-cyan">1</span>
<p style="margin:0; font-size:1.2rem;">When you bring three ideas, expect us to pick one and park two. That&apos;s not us ignoring you. <strong>That&apos;s the method working.</strong></p>
</div>

<div v-click class="ff-card" style="display:flex; align-items:flex-start; gap:1.25rem;">
<span style="font-size:1.8rem;" class="ff-green">2</span>
<p style="margin:0; font-size:1.2rem;">When the lever is named, judge yourself on one question: <strong>did I actually pull it</strong>, or did I go looking for permission to keep doing what I was already doing?</p>
</div>

</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">If you remember one thing</div>

<h1 style="font-size: 3.4rem; color: white; line-height:1.2;">
Get clear on the lever.<br/>
<span class="ff-cyan">Then pull it.</span>
</h1>

<p v-click style="font-size: 1.25rem; color: rgba(255,255,255,0.85); margin-top: 2.5rem; max-width: 42rem; margin-left:auto; margin-right:auto;">
Everything else in this portal exists to serve those two moves. This is the operating system the full Funnel Futurist install runs on, sized for one operator.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
JOHN COBURN · FUNNEL FUTURIST · PORTAL ONBOARDING
</div>

</div>
