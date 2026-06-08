---
theme: default
title: "Brandon × FF · The Path to Cohort 1"
info: |
  brandon launch — the simple critical path.
  90% done. one week to cohort 1. cut through finish-line syndrome.
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: dark
drawings:
  persist: false
transition: fade
mdc: true
fonts:
  sans: Inter
  serif: 'Crimson Pro'
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800'
layout: cover
---

<style>
:root {
  --ff-navy: #0F172A;
  --ff-navy-lt: #1E293B;
  --ff-cream: #FAF8F4;
  --ff-cyan: #22D3EE;
  --ff-cyan-dk: #0891B2;
  --ff-green: #10B981;
  --ff-orange: #F97316;
  --ff-gray: #94A3B8;
  --ff-rule: #334155;
  --ff-text: #E2E8F0;
  --ff-text-mute: #94A3B8;
}

html, body, #app, .slidev-layout {
  background: var(--ff-navy) !important;
  color: var(--ff-text);
  font-family: 'Inter', sans-serif;
}

.slidev-layout {
  padding: 3rem 4rem;
}

h1 {
  font-family: 'Crimson Pro', serif;
  font-weight: 700;
  color: var(--ff-cream);
  letter-spacing: -0.02em;
}

h2, h3 {
  color: var(--ff-cream);
  font-weight: 600;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.15em;
  font-size: 0.75rem;
  color: var(--ff-cyan);
  font-weight: 600;
  margin-bottom: 1rem;
  display: block;
}

.cyan { color: var(--ff-cyan); }
.green { color: var(--ff-green); }
.orange { color: var(--ff-orange); }
.cream { color: var(--ff-cream); }
.mute { color: var(--ff-text-mute); }

.card {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--ff-rule);
  border-radius: 0.5rem;
  padding: 1.5rem;
}

.card-cyan { border-left: 4px solid var(--ff-cyan); }
.card-orange { border-left: 4px solid var(--ff-orange); }
.card-green { border-left: 4px solid var(--ff-green); }

.kicker {
  font-size: 1.1rem;
  color: var(--ff-text-mute);
  line-height: 1.6;
}

.big-stat {
  font-family: 'Crimson Pro', serif;
  font-size: 4rem;
  font-weight: 700;
  color: var(--ff-cyan);
  line-height: 1;
}

.checkmark { color: var(--ff-green); font-weight: 700; margin-right: 0.5rem; }
.arrow { color: var(--ff-orange); font-weight: 700; margin-right: 0.5rem; }

.footer-tag {
  position: absolute;
  bottom: 1.5rem;
  right: 2rem;
  font-size: 0.7rem;
  color: var(--ff-text-mute);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.divider {
  height: 1px;
  background: var(--ff-rule);
  margin: 1.5rem 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

th {
  text-align: left;
  padding: 0.75rem 1rem;
  background: var(--ff-navy-lt);
  border-bottom: 2px solid var(--ff-cyan);
  color: var(--ff-cyan);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.75rem;
}

td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--ff-rule);
  vertical-align: top;
}
</style>

<div class="absolute inset-0 flex flex-col justify-center px-20">

<span class="eyebrow">Brandon × Funnel Futurist</span>

<h1 style="font-size: 4rem; line-height: 1.05;">
The Path to <span class="cyan">Cohort 1</span>.
</h1>

<p class="kicker" style="margin-top: 2rem; max-width: 38rem; font-size: 1.4rem;">
You're <span class="green">90% done</span>. Here's the 10% that's left.
</p>

<p class="kicker" style="margin-top: 1rem; max-width: 38rem;">
This deck is the whole map. 7 slides. Read it in 3 minutes.
</p>

</div>

<div class="footer-tag">2026-05-30 · cohort 1 launches monday</div>

<!--
This is the cure for finish-line syndrome. Brandon is 90% done. The remaining
10% feels like a mountain because the surface area looks huge — actually it's
a handful of moves. We're going to lay them out so he sees the whole path on
one screen.
-->

---
layout: default
---

<span class="eyebrow">The funnel · one diagram</span>

<h1 style="font-size: 2.6rem; margin-bottom: 2rem;">
This is the <span class="cyan">whole machine</span>.
</h1>

<div style="background: rgba(255,255,255,0.02); border: 1px solid var(--ff-rule); border-radius: 0.5rem; padding: 2rem;">

```mermaid {scale: 0.85}
flowchart TB
    A[Origin Story Sequence<br/>posted on IG Stories]
    B[DMs + Question Sticker Replies]
    C{ManyChat<br/>auto-qualify + tag}
    D[Application Form<br/>= the waitlist]
    E[Mini Sage VSL<br/>indoctrination]
    F[Sales Call w/ Brandon]
    G[Cohort 1<br/>5 founder clients]
    H[More wins → social proof → <br/>Cohort 2 fills faster]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G -.->|feeds| H

    classDef built fill:#10B981,stroke:#0F172A,color:#0F172A,font-weight:bold
    classDef tobuild fill:#F97316,stroke:#0F172A,color:#0F172A,font-weight:bold
    classDef future fill:#1E293B,stroke:#22D3EE,color:#E2E8F0,stroke-dasharray:4
    
    class A,F,G built
    class C,D,E tobuild
    class H future
```

</div>

<p class="kicker" style="margin-top: 1rem; text-align: center;">
<span class="green">■</span> built &nbsp;·&nbsp;
<span class="orange">■</span> to build this week &nbsp;·&nbsp;
<span class="cyan">▢</span> compounding loop
</p>

<div class="footer-tag">7 stages · 5 already in motion</div>

---
layout: default
---

<span class="eyebrow">What's already built ✓</span>

<h1 style="font-size: 2.6rem; margin-bottom: 1.5rem;">
You're not starting from scratch. <span class="green">Most of the work is done.</span>
</h1>

<div class="grid grid-cols-2 gap-4">

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.5rem;"><span class="checkmark">✓</span> Origin Story Sequence</div>
<p style="font-size: 0.9rem; color: var(--ff-text-mute); line-height: 1.5;">
8 IG-story frames in your voice. Two versions (maxxing + wellness). Day-X anchor + Question sticker CTA. Ready to post.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.5rem;"><span class="checkmark">✓</span> VSL Script v1</div>
<p style="font-size: 0.9rem; color: var(--ff-text-mute); line-height: 1.5;">
~7 min, your @beefcakemaxxing essay voice. Ready when you are to record.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.5rem;"><span class="checkmark">✓</span> 28-Email Sequence (draft)</div>
<p style="font-size: 0.9rem; color: var(--ff-text-mute); line-height: 1.5;">
WHISPER 1-5 ready. TEASE + SHOUT draft. We sequence sends, you reply to inbound.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.5rem;"><span class="checkmark">✓</span> Waitlist Landing Page</div>
<p style="font-size: 0.9rem; color: var(--ff-text-mute); line-height: 1.5;">
Copy ready · build in progress. Goes live before TEASE phase opens.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.5rem;"><span class="checkmark">✓</span> MSA + Contract</div>
<p style="font-size: 0.9rem; color: var(--ff-text-mute); line-height: 1.5;">
PandaDoc-ready V2 with Phoenix's revisions. Sign + pay = green light.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.5rem;"><span class="checkmark">✓</span> Audience Verified</div>
<p style="font-size: 0.9rem; color: var(--ff-text-mute); line-height: 1.5;">
40K maxxing + 42K wellness = ~70K unique. Voice locked. Account roles per Phoenix call.
</p>
</div>

</div>

<div class="footer-tag">6 of 9 components shipped</div>

---
layout: default
---

<span class="eyebrow">What's left · the actual finish line</span>

<h1 style="font-size: 2.6rem; margin-bottom: 1.5rem;">
Three things from you. <span class="cyan">Three things from us.</span>
</h1>

<div class="grid grid-cols-2 gap-6">

<div>
<h3 style="color: var(--ff-orange); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">
Brandon (you)
</h3>

<div class="card card-orange" style="margin-bottom: 0.75rem;">
<div style="font-weight: 700; margin-bottom: 0.25rem;"><span class="arrow">1.</span> Finish offer ramp-up docs</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute);">You're close. Get them done today/tomorrow.</p>
</div>

<div class="card card-orange" style="margin-bottom: 0.75rem;">
<div style="font-weight: 700; margin-bottom: 0.25rem;"><span class="arrow">2.</span> Post the Origin Story Sequence</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute);">8 IG stories. Version A on @beefcakemaxxing. Today or tomorrow.</p>
</div>

<div class="card card-orange">
<div style="font-weight: 700; margin-bottom: 0.25rem;"><span class="arrow">3.</span> Reply warm to inbound</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute);">Don't sell. Just sort. ManyChat picks up the heavy lifting.</p>
</div>
</div>

<div>
<h3 style="color: var(--ff-cyan); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">
Funnel Futurist (us)
</h3>

<div class="card card-cyan" style="margin-bottom: 0.75rem;">
<div style="font-weight: 700; margin-bottom: 0.25rem;"><span class="arrow">1.</span> ManyChat flows</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute);">Auto-qualify story replies, tag by intent, route to application form. Built before stories go live.</p>
</div>

<div class="card card-cyan" style="margin-bottom: 0.75rem;">
<div style="font-weight: 700; margin-bottom: 0.25rem;"><span class="arrow">2.</span> Application form</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute);">10-Q form = the waitlist. Funnels every reply into one sortable list.</p>
</div>

<div class="card card-cyan">
<div style="font-weight: 700; margin-bottom: 0.25rem;"><span class="arrow">3.</span> Mini Sage VSL</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute);">3-5 min, your voice. "When you join, here's what happens." John records right after your offer docs land.</p>
</div>
</div>

</div>

<div class="footer-tag">6 items · ~5 working days · then we launch</div>

---
layout: default
---

<span class="eyebrow">This week · the critical path</span>

<h1 style="font-size: 2.4rem; margin-bottom: 1.5rem;">
Day by day. <span class="cyan">No mystery.</span>
</h1>

<table>
<thead>
<tr>
<th style="width: 18%;">Day</th>
<th style="width: 41%;">Brandon</th>
<th style="width: 41%;">Funnel Futurist</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong class="cream">Sat May 30</strong><br/><span class="mute" style="font-size: 0.8rem;">today</span></td>
<td>Finish offer ramp-up docs · review Origin sequence</td>
<td>Build ManyChat flows · stub application form</td>
</tr>
<tr>
<td><strong class="cream">Sun May 31</strong></td>
<td>Post Origin Story Sequence · reply to early DMs</td>
<td>ManyChat live · application form live · capture early data</td>
</tr>
<tr>
<td><strong class="cream">Mon Jun 1</strong><br/><span class="orange" style="font-size: 0.8rem;">launch day</span></td>
<td>WHISPER content cadence starts · DMs all day</td>
<td>WHISPER Email 1 sends · monitor + analyze engagement</td>
</tr>
<tr>
<td><strong class="cream">Tue-Wed Jun 2-3</strong></td>
<td>Reply to inbound · record Mini Sage VSL with John</td>
<td>Mini VSL produced + deployed · ManyChat routes warm leads to it</td>
</tr>
<tr>
<td><strong class="cream">Thu-Sun Jun 4-7</strong></td>
<td>Continue WHISPER posts · warm DM follow-up</td>
<td>Analyze qualitative data · refine VSL v2 prep · waitlist opens Jun 8</td>
</tr>
<tr>
<td><strong class="cream">Mon Jun 22</strong><br/><span class="green" style="font-size: 0.8rem;">cohort 1 day 1</span></td>
<td>Run Execution Launch Calls with 5 founder clients</td>
<td>Onboarding sequences fire · we monitor delivery + retention</td>
</tr>
</tbody>
</table>

<div class="footer-tag">9 working days to first founder client</div>

---
layout: default
---

<span class="eyebrow">After cohort 1 · the compounding loop</span>

<h1 style="font-size: 2.6rem; margin-bottom: 1.5rem;">
The hard part is <span class="orange">launch one</span>.<br/>
After that, <span class="green">it gets easier</span>.
</h1>

<div class="grid grid-cols-2 gap-8" style="margin-top: 2rem;">

<div>
<p class="kicker" style="margin-bottom: 1.5rem;">
Every cohort feeds the next. The work compounds:
</p>

<div style="font-size: 1rem; line-height: 2;">
<div><span class="green">→</span> <strong class="cream">Cohort 1 wins</strong> become testimonials</div>
<div><span class="green">→</span> <strong class="cream">Testimonials</strong> unlock the Social Proof sequence</div>
<div><span class="green">→</span> <strong class="cream">Social Proof</strong> shortens the cohort 2 sales cycle</div>
<div><span class="green">→</span> <strong class="cream">Shorter cycle</strong> means higher close rate</div>
<div><span class="green">→</span> <strong class="cream">Higher close rate</strong> means cohort 3 sells out before WHISPER ends</div>
</div>
</div>

<div class="card card-cyan">
<h3 style="color: var(--ff-cyan); margin-bottom: 1rem;">The math</h3>
<table style="font-size: 0.9rem;">
<tr><td style="padding: 0.4rem 0;">Cohort 1 (Jun-Sep)</td><td style="text-align: right;"><strong>5 × $3K = $15K</strong></td></tr>
<tr><td style="padding: 0.4rem 0;">Cohort 2 (Sep-Dec)</td><td style="text-align: right;"><strong>8 × $3.5K = $28K</strong></td></tr>
<tr><td style="padding: 0.4rem 0;">Cohort 3 (Dec-Mar)</td><td style="text-align: right;"><strong>12 × $4K = $48K</strong></td></tr>
<tr style="border-top: 1px solid var(--ff-rule);"><td style="padding: 0.6rem 0;"><strong class="cyan">9 months total</strong></td><td style="text-align: right;"><strong class="cyan">$91K</strong></td></tr>
</table>
<p style="font-size: 0.75rem; color: var(--ff-text-mute); margin-top: 0.75rem; line-height: 1.4;">
Conservative. Each cohort can run higher pricing as social proof accumulates. Numbers above assume modest growth, no ads.
</p>
</div>

</div>

<div class="footer-tag">launch one · then the system runs</div>

---
layout: cover
class: text-center
---

<div class="absolute inset-0 flex flex-col justify-center px-20 text-center">

<span class="eyebrow" style="margin: 0 auto;">One question</span>

<h1 style="font-size: 3.6rem; line-height: 1.1; margin: 2rem 0;">
What's <span class="orange">blocking you</span> right now?
</h1>

<p class="kicker" style="max-width: 36rem; margin: 0 auto; font-size: 1.2rem;">
Not the whole launch. Just the <span class="cyan">next thing on your list</span>.
</p>

<p class="kicker" style="max-width: 36rem; margin: 1.5rem auto 0; font-size: 1rem;">
Drop it in your launch Slack channel. We'll move it within 4 hours.
</p>

<div style="margin-top: 4rem;">
<p style="font-size: 0.9rem; color: var(--ff-text-mute);">
You're <span class="green">90% done</span>. Don't let the last 10% feel like 90.
</p>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); margin-top: 0.5rem;">
Cohort 1 starts <strong class="cyan">Mon Jun 22</strong>. Three weeks from today.
</p>
</div>

</div>

<div class="footer-tag">brandon × funnel futurist · the simplest version of this</div>
