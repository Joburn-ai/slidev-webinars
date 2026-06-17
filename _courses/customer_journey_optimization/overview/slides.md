---
theme: default
title: The 4-Pillar Journey Framework
info: |
  Customer Journey Optimization, Overview deck.
  Internal training format. Built on John's 5-stage spine, the 4 pillars,
  Coleman + Fogg + Heath frameworks, with source-attribution honesty.
  Built 2026-06-17 for FF / Joburn internal team.
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

<!-- slide:cover-01 -->

<div class="cjo-bar"></div>

<div class="absolute inset-0 cjo-dark flex flex-col justify-center items-center px-16">

<div class="cjo-dark-wrap text-center max-w-5xl">

<div class="cjo-eyebrow ondark">Customer Journey Optimization, Overview</div>

<h1 style="font-size: 4.2rem; color: white; letter-spacing: -0.03em;">
The <span style="color:#D4B85A;">4-Pillar</span> Journey Framework
</h1>

<p style="font-size: 1.35rem; color: rgba(255,255,255,0.84); margin-top: 1.6rem; max-width: 44rem; margin-left:auto; margin-right:auto;">
Five stages. Four pillars. Three motions. Built to make journeys that compound, not just convert.
</p>

</div>

<div class="cjo-footer ondark">JOBURN, INTERNAL TRAINING, 2026-06-17</div>

</div>

<!--
COLD OPEN. State the framework by name. The deck teaches a system, not a pitch.
This is internal training format, not a webinar. Pace: slow opening. Hold the
title for 10 seconds. Set the frame: we are going to teach the system that
turns one-time buyers into long-term advocates.
-->

---
layout: default
---

<!-- slide:diagnosis-02 -->

<div class="px-14 py-10">

<div class="cjo-eyebrow">The diagnosis</div>

<h1 class="cjo-h1" style="margin-bottom: 1.2rem;">Why journeys <span class="cjo-rust">leak</span></h1>

<p class="cjo-lead" style="max-width: 52rem;">
Most companies have a few moments without triggers, or actions without tracking. Each missing pillar produces a named failure mode. Find the leak, name the pillar that is missing, fix the structure.
</p>

<div class="grid grid-cols-2 gap-3 mt-7">

<v-clicks>

<div class="cjo-leak">
<div class="ttl">Empathy without triggers</div>
<div class="desc">You know what they need to feel. The moment never fires because nothing in your system is watching for the condition that should fire it.</div>
</div>

<div class="cjo-leak">
<div class="ttl">Triggers without actions</div>
<div class="desc">The system detects the moment. The send queue is empty. The Day 7 check-in never lands because no one wired the surface.</div>
</div>

<div class="cjo-leak">
<div class="ttl">Actions without tracking</div>
<div class="desc">The Day 30 review fires. Nobody knows if it was received, opened, or worked. The journey cannot learn from a moment it cannot measure.</div>
</div>

<div class="cjo-leak">
<div class="ttl">Tracking without empathy</div>
<div class="desc">The dashboard is full. The moments score high on completion and low on meaning. The relationship dies politely on schedule.</div>
</div>

</v-clicks>

</div>

</div>

<!--
DIAGNOSTIC FRAME. Each leak corresponds to a missing pillar. The lesson is
structural, not motivational. Four v-clicks, one beat each, one per missing
pillar. Set up the framework reveal.
-->

---
layout: default
---

<!-- slide:double-bowtie-03 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">The macro frame</div>

<h2 class="cjo-h2">Every business runs <span class="cjo-teal">two bowties</span> in parallel</h2>

<p class="cjo-lead" style="margin-top: 0.6rem; max-width: 52rem;">
The customer bowtie buys, retains, expands. The talent bowtie hires, ramps, places, advocates. Most founders only see the first one. The leak in the second one is invisible until headcount stops scaling.
</p>

<div class="cjo-mermaid-wrap" style="margin-top: 1rem; max-height: 22rem;">

```mermaid
flowchart LR
    classDef stage fill:#1E3A5F,color:#fff,stroke:#D4B85A,stroke-width:2px
    classDef cust fill:#2E8B8B,color:#fff,stroke:#1E3A5F,stroke-width:1px
    classDef tal fill:#D4B85A,color:#1E3A5F,stroke:#1E3A5F,stroke-width:1px
    classDef hub fill:#FAFAF5,color:#1E3A5F,stroke:#94463B,stroke-width:2px

    A[Customer<br/>acquired]:::cust --> B[Customer<br/>retained]:::cust --> C[Customer<br/>expanded]:::cust
    D[Talent<br/>acquired]:::tal --> E[Talent<br/>ramped]:::tal --> F[Talent<br/>placed and advocates]:::tal
    C --> Z[The business<br/>that compounds]:::hub
    F --> Z
```

</div>

</div>

<!--
DOUBLE BOWTIE. The visual sets up the macro frame. The 4 pillars and the
5-stage spine apply to BOTH bowties. We teach the customer side in this deck;
the talent side is the cyborgtalent worked example later.
-->

---
layout: default
---

<!-- slide:five-stage-spine-04 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">The structure</div>

<h2 class="cjo-h2">The <span class="cjo-gold">5-stage spine</span> every journey runs on</h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 50rem;">
Stages run in order. You cannot Stage 5 your way out of a broken Stage 2. If retention leaks at Day 30, the fix lives in stages 2 or 3, not in adding more advocacy mechanics at the end.
</p>

<div class="grid grid-cols-5 gap-2 mt-7">

<v-clicks>

<div class="cjo-stage">
<span class="num">STAGE 1</span>
Commit, Payment
</div>

<div class="cjo-stage">
<span class="num">STAGE 2</span>
Onboarding, Orientation
</div>

<div class="cjo-stage">
<span class="num">STAGE 3</span>
Activation
</div>

<div class="cjo-stage">
<span class="num">STAGE 4</span>
Customer Success
</div>

<div class="cjo-stage gold">
<span class="num">STAGE 5</span>
Ascension, Advocacy
</div>

</v-clicks>

</div>

<div class="grid grid-cols-5 gap-2 mt-3 cjo-meta" style="text-align:center;">
<div>Coleman: Admit</div>
<div>Affirm + Activate</div>
<div>Acclimate</div>
<div>Accomplish</div>
<div>Adopt + Advocate</div>
</div>

<div class="cjo-callout" style="margin-top: 1.6rem;">
<span class="lab">The locked sequencing rule</span>
Run the stages in order. Diagnose leaks by working backward from the visible failure to the missing structure.
</div>

</div>

<!--
THE SPINE. Five v-clicks, one per stage. The Coleman row underneath shows the
8 phases collapsing into our 5 stages. The callout locks the rule.
-->

---
layout: default
---

<!-- slide:bookends-05 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">The bookends</div>

<h2 class="cjo-h2">Stage 0 and Stage 6, the <span class="cjo-rust">moments most teams skip</span></h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
The spine assumes the relationship starts at Stage 1 and ends at Stage 5. Real engagements start before the contract is signed and continue after it closes. Without bookends, the front and back leak.
</p>

<div class="grid grid-cols-2 gap-5 mt-7">

<v-clicks>

<div class="cjo-bookend">
<span class="lab">Stage 0, Sales to CS handoff</span>
<div class="ttl">Context survives the transition</div>
<div class="d">Every promise the closer made gets captured before the handshake dries. Three-way intro call inside 72 hours. The buyer never has to re-explain themselves on Day 1.</div>
</div>

<div class="cjo-bookend">
<span class="lab">Stage 6, Exit Journey</span>
<div class="ttl">The relationship continues past the contract</div>
<div class="d">Cancel ritual within 48 hours, no save attempt. Exit interview. 30 / 60 / 90 day win-back ladder. Alumni nurture. Re-acquisition rates from alumni run 3 to 5 times cold cohorts.</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.5rem;">
<span class="lab">Why the bookends are load bearing</span>
Honest exit interviews surface the real breakage in stages 2 to 4 that no satisfaction survey will catch. The bookends pay for themselves twice.
</div>

</div>

<!--
BOOKENDS. Stage 0 and Stage 6 added in v1.1. Two v-clicks, one per bookend.
Speaker note: most teams design 1-5 and silently break 0 and 6.
-->

---
layout: default
---

<!-- slide:motion-types-06 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow gold">v1.3 framing, new this cycle</div>

<h2 class="cjo-h2">The journey <span class="cjo-gold">forks by motion type</span></h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
The 5-stage spine stays. The default triggers, action surfaces, and channels change based on how the deal moves through the cycle. Pick the motion before you pick the moments.
</p>

<div class="grid grid-cols-3 gap-3 mt-6">

<v-clicks>

<div class="cjo-motion led-p">
<div class="mt">Product led</div>
<div class="ttl">PLG</div>
<div class="desc">User discovers, activates, buys themselves. Stage 1 commit is in-app, not a closing call. Activation is product driven. Default for SaaS, low-ticket subscription, B2C apps.</div>
</div>

<div class="cjo-motion led-s">
<div class="mt gold">Sales led</div>
<div class="ttl">SLG</div>
<div class="desc">Sales team drives the cycle. Stage 1 commit is the close call. Heavy Coleman Affirm requirement post-close. Default for coaches, consultants, agencies, high-ticket B2B, enterprise.</div>
</div>

<div class="cjo-motion led-m">
<div class="mt rust">Marketing led</div>
<div class="ttl">MLG</div>
<div class="desc">Marketing drives the cycle with sales support. Stage 1 commit is form driven with sales triage. Lead nurture is dominant. Default for hybrid B2B mid-market, content-driven funnels.</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.4rem;">
<span class="lab">Implication for the master flow</span>
Same 5 stages. Three different default templates. The Master Flow table forks by motion. We show all three so the operator picks the right one for their cycle.
</div>

</div>

<!--
MOTION TYPES. New v1.3 framing. Three v-clicks. Lock the language: PLG, SLG,
MLG. The slide is the bridge between "the spine is universal" (stages don't
change) and "the execution is context dependent" (everything else does).
-->

---
layout: default
---

<!-- slide:pillar-1-07 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">Pillar 1 of 4</div>

<h2 class="cjo-h2"><span class="cjo-gold">Key Moments.</span> What do we want them to feel?</h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
The user does not remember features. They remember moments. Empathy mapping is the design lens that prevents technically correct but emotionally cold journeys.
</p>

<div class="grid grid-cols-3 gap-3 mt-6">

<v-clicks>

<div class="cjo-card">
<div class="n">THINK / FEEL / SAY</div>
<div class="t">The human state</div>
<div class="d">What is going through their head? What is the dominant emotion? What would they say out loud to a peer right now?</div>
</div>

<div class="cjo-card">
<div class="n">DO / HEAR / SEE</div>
<div class="t">The context</div>
<div class="d">What action are they taking? What are they hearing from people around them? What are they looking at on screen?</div>
</div>

<div class="cjo-card">
<div class="n">PAIN / GAIN / DOPAMINE</div>
<div class="t">The curve</div>
<div class="d">What is the dominant friction? What would feel like a win? Where are they on the dopamine curve, peak, collapse, neutral, high?</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.5rem;">
<span class="lab">First person line per moment</span>
For each moment, write one sentence in the user voice. I just signed and I am wondering if I made a mistake. That sentence surfaces design gaps faster than any framework discussion.
</div>

</div>

<!--
PILLAR 1. Empathy mapping is the load-bearing skill. Three v-clicks group
the 9 empathy-map dimensions into bundles that fit the slide. Speaker note:
the dopamine state is the most important dimension; map every transition
against the curve.
-->

---
layout: default
---

<!-- slide:pillar-2-08 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">Pillar 2 of 4</div>

<h2 class="cjo-h2"><span class="cjo-teal">Triggers.</span> What fires each moment?</h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
Every moment has exactly one trigger. Default to the lowest friction type that produces the right semantic. Event beats time beats state beats manual.
</p>

<div class="grid grid-cols-4 gap-3 mt-7">

<v-clicks>

<div class="cjo-pillar p2">
<div class="lab">Type 1</div>
<div class="ttl">Event based</div>
<div class="desc">A specific event lands in the database. Contract signed, first login, first deliverable shipped, payment posted.</div>
</div>

<div class="cjo-pillar p2">
<div class="lab">Type 2</div>
<div class="ttl">Time based</div>
<div class="desc">Day N relative to an anchor. Day 7 check-in. Day 30 review. Day 100 celebration. One canonical anchor per engagement.</div>
</div>

<div class="cjo-pillar p2">
<div class="lab">Type 3</div>
<div class="ttl">State based</div>
<div class="desc">A composite condition crosses a threshold. Health score yellow, goal-met flag flips, churn-risk above 0.6.</div>
</div>

<div class="cjo-pillar p2">
<div class="lab">Type 4</div>
<div class="ttl">Manual</div>
<div class="desc">A human deliberately fires the moment. Named owner, named SLA, audit row. A smell if it scales.</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.4rem;">
<span class="lab">The cascade</span>
Event beats time beats state beats manual. Each step down loses fidelity and gains operational cost. Manual without an owner is a journey that decays the moment the named human takes a vacation.
</div>

</div>

<!--
PILLAR 2. Four trigger types. Four v-clicks, one per type. The cascade is the
load-bearing principle: lowest friction trigger that produces the right
semantic. Speaker: walk through the failure modes briefly if time allows.
-->

---
layout: default
---

<!-- slide:pillar-3-09 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">Pillar 3 of 4</div>

<h2 class="cjo-h2"><span class="cjo-rust">Actions.</span> Where does the moment ship from?</h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
Each action surface has its emotional weight. The right surface depends on what the moment is doing. Physical mail signals care that an email cannot. A 90 second Loom outperforms a 1500 word email for an Affirm moment.
</p>

<div class="mt-6">

<table class="cjo-table">
<thead>
<tr>
<th>Surface</th>
<th>What it does</th>
<th>When to use it</th>
</tr>
</thead>
<tbody>
<tr><td>Physical mail</td><td>Handwritten note, certificate, welcome artifact</td><td>Stage 1 Admit, Stage 4 Accomplish certificate. Unbypassable.</td></tr>
<tr><td>Loom video</td><td>Personalized 90 sec founder video</td><td>Stage 2 Affirm. Day 30 / 60 / 90 milestone. Recorded once per cohort, sent automatically.</td></tr>
<tr><td>Live call</td><td>24 hour welcome call, kickoff, milestone review</td><td>Stage 1 / 2 / 4 high-stakes moments. Voice and tone matter.</td></tr>
<tr><td>Email</td><td>Cadence touchpoints, milestone announcements</td><td>Stage 2 to 4 recurring digests, structured stage transitions.</td></tr>
<tr><td>SMS</td><td>Time sensitive nudges, confirmations</td><td>Stage 1 confirmations, Stage 4 reminders. Use sparingly.</td></tr>
<tr><td>Slack / community</td><td>Cohort recognition, tribal identity</td><td>Stage 3 / 4 peer recognition, identity reinforcement.</td></tr>
<tr><td>In-app prompt</td><td>Product-led activation nudges</td><td>PLG motion Stage 2 / 3. Replaces kickoff call.</td></tr>
<tr><td>Dashboard</td><td>Owned, internal-facing progress surface</td><td>Stage 4 measurement, founder visibility into outcomes.</td></tr>
</tbody>
</table>

</div>

</div>

<!--
PILLAR 3. The action surfaces. Static table, no v-clicks (already dense). The
table is the reference; speaker walks through 2-3 rows of greatest interest.
-->

---
layout: default
---

<!-- slide:pillar-4-10 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">Pillar 4 of 4</div>

<h2 class="cjo-h2"><span class="cjo-teal">Tracking.</span> How do we know it landed?</h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
Every moment writes a tracking event. Every event feeds a dashboard. Every dashboard feeds a calibration loop. Without this loop, the journey cannot learn.
</p>

<div class="grid grid-cols-2 gap-4 mt-6">

<div>

<div class="cjo-eyebrow" style="margin-bottom: 0.4rem;">The schema</div>

<div class="cjo-code">
<span class="c">-- One canonical events table</span><br/>
<span class="k">CREATE TABLE</span> journey_events (<br/>
&nbsp;&nbsp;id <span class="k">uuid</span> PRIMARY KEY,<br/>
&nbsp;&nbsp;engagement_id <span class="k">uuid</span> NOT NULL,<br/>
&nbsp;&nbsp;stage <span class="k">text</span> NOT NULL,<br/>
&nbsp;&nbsp;moment_id <span class="k">text</span> NOT NULL,<br/>
&nbsp;&nbsp;track <span class="k">text</span> NOT NULL,<br/>
&nbsp;&nbsp;fired_at <span class="k">timestamptz</span> NOT NULL,<br/>
&nbsp;&nbsp;delivered_at <span class="k">timestamptz</span>,<br/>
&nbsp;&nbsp;acknowledged_at <span class="k">timestamptz</span>,<br/>
&nbsp;&nbsp;status <span class="k">text</span> NOT NULL,<br/>
&nbsp;&nbsp;trigger_type <span class="k">text</span> NOT NULL,<br/>
&nbsp;&nbsp;action_surface <span class="k">text</span> NOT NULL,<br/>
&nbsp;&nbsp;cost_usd <span class="k">numeric</span>,<br/>
&nbsp;&nbsp;metadata <span class="k">jsonb</span><br/>
);
</div>

</div>

<div class="flex flex-col gap-3">

<v-clicks>

<div class="cjo-card accent">
<div class="t">v_journey_health</div>
<div class="d">Per-engagement composite. Stage completion, days since last event, acknowledged-vs-dispatched ratio, goal-met flag.</div>
</div>

<div class="cjo-card accent">
<div class="t">v_advocate_unlock</div>
<div class="d">Boolean per engagement. True only when goal_met = true AND accomplish_celebrated_at IS NOT NULL. The Advocate-ask gate.</div>
</div>

<div class="cjo-card accent">
<div class="t">v_cohort_progression</div>
<div class="d">Cohort-level rollup. Powers the wins-of-the-week post, the cohort-call agenda, the tribal-recognition surface.</div>
</div>

</v-clicks>

</div>

</div>

</div>

<!--
PILLAR 4. Schema on the left, computed views on the right. Three v-clicks
reveal the three views. The advocate-unlock view is the load-bearing one,
the gate between Stage 4 and Stage 5.
-->

---
layout: default
---

<!-- slide:pillars-aligned-11 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">The 4 pillars in alignment</div>

<h2 class="cjo-h2">One complete moment: the <span class="cjo-gold">Day 1 founder note</span></h2>

<div class="grid grid-cols-2 gap-4 mt-5">

<div class="flex flex-col gap-2">

<div class="cjo-mchip">
<div class="lab">Pillar 1, Key Moment</div>
<div class="v">Day 1 dopamine peak catch. Founder writes a personal note that arrives same-day, references the stated 100-day goal.</div>
</div>

<div class="cjo-mchip">
<div class="lab">Pillar 2, Trigger</div>
<div class="v">Event based. contract_signed_at IS NOT NULL AND day1_note_sent_at IS NULL. Fires within 2 hours.</div>
</div>

<div class="cjo-mchip">
<div class="lab">Pillar 3, Action</div>
<div class="v">Handwrytten API via Make scenario. Founder-personal carve-out for top 1 to 3 notes per week. Cost ~5 USD per note.</div>
</div>

<div class="cjo-mchip">
<div class="lab">Pillar 4, Tracking</div>
<div class="v">journey_events row at dispatch. Status update at vendor mail_delivered webhook. Failure alert to ops Slack if 7 days silent.</div>
</div>

</div>

<div class="cjo-code">
<span class="k">moment_id:</span> day1_founder_handwritten_note<br/>
<span class="k">stage:</span> 1_commit<br/>
<span class="k">track:</span> founder<br/>
<span class="k">trigger:</span><br/>
&nbsp;&nbsp;<span class="k">type:</span> event-based<br/>
&nbsp;&nbsp;<span class="k">condition:</span> <span class="s">"contract_signed_at NOT NULL"</span><br/>
&nbsp;&nbsp;<span class="k">expected_latency_hours:</span> 2<br/>
<span class="k">action:</span><br/>
&nbsp;&nbsp;<span class="k">surface:</span> handwrytten_api<br/>
&nbsp;&nbsp;<span class="k">via:</span> make_scenario <span class="s">"ct-day1"</span><br/>
&nbsp;&nbsp;<span class="k">cost_usd:</span> 5.00<br/>
<span class="k">voice_lock:</span><br/>
&nbsp;&nbsp;<span class="k">ref:</span> <span class="s">"voice_dna_v1.md"</span><br/>
&nbsp;&nbsp;<span class="k">voice_qc_skill:</span> voice_qc<br/>
<span class="k">tracking:</span><br/>
&nbsp;&nbsp;<span class="k">fire_event:</span> <span class="s">"INSERT journey_events..."</span><br/>
&nbsp;&nbsp;<span class="k">success_event:</span> <span class="s">"webhook mail_delivered"</span><br/>
&nbsp;&nbsp;<span class="k">failure_alert:</span> <span class="s">"slack ops if 7d silent"</span><br/>
<span class="k">fallback:</span> <span class="s">"founder writes personally"</span>
</div>

</div>

</div>

<!--
PILLARS ALIGNED. One worked moment with all 4 pillars filled in. Left side is
the human-readable explanation, right side is the YAML manifest that the
implementation team gets. This is the deliverable target: 80 percent
executable infrastructure, 20 percent strategic prose.
-->

---
layout: default
---

<!-- slide:empathy-dopamine-12 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">The empathy overlay</div>

<h2 class="cjo-h2">Map every transition against the <span class="cjo-gold">dopamine curve</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
Coleman's whole framework rests on the dopamine asymmetry. The seller exits high. The buyer collapses inside 48 hours. The gaps between states are where the load-bearing moments live.
</p>

<div class="cjo-mermaid-wrap" style="margin-top: 1rem; max-height: 18rem;">

```mermaid
flowchart LR
    classDef high fill:#2E8B8B,color:#fff,stroke:#1E3A5F
    classDef collapse fill:#94463B,color:#fff,stroke:#1E3A5F
    classDef neutral fill:#cbd5e1,color:#1E3A5F,stroke:#51688a
    classDef peak fill:#D4B85A,color:#1E3A5F,stroke:#1E3A5F

    P1[Pre-buy<br/>curiosity]:::neutral --> P2[Commit<br/>dopamine peak]:::high
    P2 --> P3[Hour 2-48<br/>collapse window]:::collapse
    P3 --> P4[Day 7<br/>ability building]:::neutral
    P4 --> P5[Day 30<br/>first small win]:::peak
    P5 --> P6[Day 60<br/>midpoint doubt]:::collapse
    P6 --> P7[Day 100<br/>goal achieved]:::peak
    P7 --> P8[Day 100+<br/>advocacy]:::high
```

</div>

<div class="grid grid-cols-4 gap-3 mt-4">

<div><span class="cjo-dopa peak">PEAK</span> Stage 1 commit, Stage 4 win.</div>
<div><span class="cjo-dopa collapse">COLLAPSE</span> Affirm window, Day 60 midpoint.</div>
<div><span class="cjo-dopa neutral">NEUTRAL</span> Pre-buy, Day 7 ability build.</div>
<div><span class="cjo-dopa high">HIGH</span> Day 100+ advocate willing.</div>

</div>

</div>

<!--
DOPAMINE OVERLAY. The map is the second view of the journey. Where the chart
goes red is where the moments must catch them. Speaker: walk through the
hour-2-to-48 collapse window and the Day 60 midpoint doubt as the two most
common failure points.
-->

---
layout: default
---

<!-- slide:hero-journey-flow-13 -->

<div class="px-12 py-6">

<div class="cjo-eyebrow gold">HERO VISUAL</div>

<h2 class="cjo-h2">The full journey, all <span class="cjo-gold">4 pillars across all 5 stages</span></h2>

<div class="cjo-mermaid-wrap" style="margin-top: 0.8rem; max-height: 27rem;">

```mermaid
flowchart TD
    classDef stage fill:#1E3A5F,color:#fff,stroke:#fff,stroke-width:2px
    classDef moment fill:#FAFAF5,color:#1E3A5F,stroke:#2E8B8B,stroke-width:2px
    classDef trigger fill:#F4EEDC,color:#1E3A5F,stroke:#D4B85A,stroke-width:1px,stroke-dasharray: 5 5
    classDef track fill:#fff,color:#51688a,stroke:#94a3b8,stroke-width:1px

    subgraph S1["Stage 1 Commit"]
        T1[Contract signed]:::trigger --> M1[Day 1 handwritten note]:::moment
        T1 --> M2[24h personalized call]:::moment
        M1 --> TR1[(events: dispatched to delivered)]:::track
        M2 --> TR2[(call_logs: completed)]:::track
    end

    subgraph S2["Stage 2 Onboarding"]
        TR1 --> T2[Day 2 cron]:::trigger
        T2 --> M3[Affirm Loom from founder]:::moment
        M3 --> M4[Day 7 joint kickoff]:::moment
        M4 --> TR3[(kickoff_completed_at)]:::track
    end

    subgraph S3["Stage 3 Activation"]
        TR3 --> T3[Daily checkin habit]:::trigger
        T3 --> M5[Cohort surface posts]:::moment
        T3 --> M6[Manager check-in D7 D14]:::moment
        M5 --> TR4[(daily_checkins)]:::track
        M6 --> TR5[(manager_feedback)]:::track
    end

    subgraph S4["Stage 4 Success"]
        TR4 --> T4[Day 30 60 90 cron]:::trigger
        T4 --> M7[Measured-progress doc]:::moment
        M7 --> M8[Accomplish celebration]:::moment
        M8 --> TR6[(goal_met flag = true)]:::track
    end

    subgraph S5["Stage 5 Ascension"]
        TR6 --> T5[goal_met gate]:::trigger
        T5 --> M9[Adopt scope expansion]:::moment
        T5 --> M10[Advocate ask]:::moment
        M9 --> TR7[(account_expansion)]:::track
        M10 --> TR7
    end

    S1 -.-> S2
    S2 -.-> S3
    S3 -.-> S4
    S4 -.-> S5
```

</div>

</div>

<!--
HERO VISUAL ONE. The full flowchart. 5 swimlanes. Moments as nodes, triggers
as dashed conditions, tracking as side notes. This is the chart we walk
clients through in the workshop. No v-clicks; the chart is the moment.
-->

---
layout: default
---

<!-- slide:master-flow-table-14 -->

<div class="px-12 py-7">

<div class="cjo-eyebrow">The Master Flow, scaffolded onto our spine</div>

<h2 class="cjo-h2">Stage by stage, all four pillars in one row</h2>

<div class="mt-5">

<table class="cjo-table">
<thead>
<tr>
<th>Stage</th>
<th>Trigger</th>
<th>Action</th>
<th>Timing</th>
<th>Channel</th>
<th>Tracking</th>
<th>Motion variant</th>
</tr>
</thead>
<tbody>
<tr><td>1 Commit</td><td>contract_signed</td><td>Handwritten note + 24h call</td><td>0-24 h</td><td>Mail + phone</td><td>events row + call_log</td><td>PLG: in-app welcome</td></tr>
<tr><td>2 Onboard</td><td>Day 2 cron</td><td>Affirm Loom + joint kickoff</td><td>2-7 d</td><td>Loom + video call</td><td>kickoff_completed_at</td><td>PLG: product tour</td></tr>
<tr><td>3 Activate</td><td>first_meaningful_action</td><td>Cohort posts + manager check-in</td><td>7-30 d</td><td>Slack + call</td><td>daily_checkins</td><td>PLG: in-app nudges</td></tr>
<tr><td>4 Success</td><td>Day 30 / 60 / 90 cron</td><td>Measured-progress review + celebration</td><td>30-100 d</td><td>Doc + Loom + call</td><td>goal_met flag</td><td>PLG: usage milestones</td></tr>
<tr><td>5 Ascend</td><td>goal_met = true</td><td>Scope expansion + advocate ask</td><td>100 d +</td><td>Call + case study</td><td>account_expansion</td><td>PLG: tier upgrade prompt</td></tr>
</tbody>
</table>

</div>

<div class="cjo-callout" style="margin-top: 1rem;">
<span class="lab">How to read this</span>
The first 6 columns are the default Sales-led template. The Motion variant column shows the PLG fork. Same stage, different surface. Same physics, different execution.
</div>

</div>

<!--
MASTER FLOW. The reference table. Pull from the mega doc, scaffolded onto
our 5-stage spine. The motion variant column shows the PLG fork. Speaker:
walk one row, then point at the variant column for the contrast.
-->

---
layout: default
---

<!-- slide:tool-tier-15 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">Tool-tier adaptation</div>

<h2 class="cjo-h2">The same moment, <span class="cjo-gold">three different stacks</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
Constraints set the tier. Budget, existing stack, team capacity, engagement count, latency. Mix tiers freely within one journey. The Day 1 note can be Tier 1, the Day 60 review Tier 3.
</p>

<div class="grid grid-cols-3 gap-3 mt-6">

<v-clicks>

<div class="cjo-tier t1">
<div class="tl">Tier 1</div>
<div class="nm">Bootstrap, DIY</div>
<div class="pr">~50 USD per engagement</div>
<div class="desc">Founder writes the Day 1 note. Google Sheets tracks moments. Gmail + Calendly + Loom-recorded-once. 1 to 5 engagements per month.</div>
</div>

<div class="cjo-tier t2">
<div class="tl">Tier 2</div>
<div class="nm">Solo founder, small agency</div>
<div class="pr">~200 to 700 USD per engagement</div>
<div class="desc">Scribeless robot-pen. Airtable or Notion CRM. Resend email. Make scenarios for cross-system. 5 to 20 engagements per month.</div>
</div>

<div class="cjo-tier t3">
<div class="tl">Tier 3</div>
<div class="nm">Pro agency, scaled</div>
<div class="pr">~700 to 1,500 USD per engagement</div>
<div class="desc">Handwrytten API. GHL workflows. Postgres journey_events. Make scenarios. Edge functions for goal-met flag. 20+ engagements per month.</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.4rem;">
<span class="lab">The DIY-always-works fallback</span>
Every prescribed surface has a DIY fallback. Even at Tier 3, the founder personally writes the Day 1 note for the top 10 accounts. Coleman's pattern, not a downgrade.
</div>

</div>

<!--
TOOL TIERS. Three v-clicks, one per tier. The fallback callout is important:
even at Tier 3, the founder-touch on top accounts is a feature, not a
fallback. Speaker: walk through which moments stay Tier 1 forever (the Day
1 founder note for high-stakes accounts).
-->

---
layout: default
---

<!-- slide:frameworks-attribution-16 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Frameworks layered, attribution honest</div>

<h2 class="cjo-h2">What is <span class="cjo-teal">theirs</span>, what is <span class="cjo-gold">ours</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
We stand on three load-bearing thinkers and we name them. We also name where our framework extends theirs. The lineage is owned, not laundered.
</p>

<div class="grid grid-cols-2 gap-3 mt-5">

<v-clicks>

<div class="cjo-attrib">
<div class="who">Joey Coleman</div>
<div class="what">First 100 Days framework, 8 phases</div>
<div class="desc">Assess, Admit, Affirm, Activate, Acclimate, Accomplish, Adopt, Advocate. Owns the dopamine-asymmetry physics and the first-date-parents principle.</div>
<div class="ours">OUR EXTENSION, Accomplish-gate on goal_met flag (programmatic Advocate-ask tripwire)</div>
</div>

<div class="cjo-attrib">
<div class="who">BJ Fogg</div>
<div class="what">Two distinct models, two distinct jobs</div>
<div class="desc">B=MAP (Motivation + Ability + Prompt) fires a single behavior at a single moment. Tiny Habits (anchor + tiny behavior + celebration) installs a recurring habit. Most write-ups blur them, we do not.</div>
<div class="ours">OUR DISCIPLINE, separate use for Stage 3 prompts vs Acclimate-window habits</div>
</div>

<div class="cjo-attrib">
<div class="who">Chip and Dan Heath</div>
<div class="what">Power of Moments, 4 ingredients</div>
<div class="desc">Elevation, Insight, Pride, Connection. The Heaths define what makes a moment memorable. They do not prescribe a numeric scoring system.</div>
<div class="ours">OUR HEURISTIC, the 2 / 3 / 4 ingredient threshold triage is ours, built on Heath's ingredients</div>
</div>

<div class="cjo-attrib">
<div class="who">Russell Brunson + John</div>
<div class="what">Ascension language, contextual rejection</div>
<div class="desc">Stage 5 Ascension borrows Brunson's direct-response language on top of Coleman's Adopt. We also contextually reject Hooked-Model variable-reward in B2B paying-buyer settings, not as universal ethics.</div>
<div class="ours">OUR FRAMING, layered language + named exclusion lines</div>
</div>

</v-clicks>

</div>

</div>

<!--
FRAMEWORKS LAYERED. Four v-clicks. Each card shows WHO owns the original
framework and WHERE we extend it. This is the attribution-honesty slide. We
do not pretend Coleman invented the Accomplish-gate flag. We do not pretend
Heath invented the 2/3/4 score. We name our extensions explicitly.
-->

---
layout: default
---

<!-- slide:anti-patterns-17 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow rust">Anti-patterns to reject on sight</div>

<h2 class="cjo-h2">Future feature proposals that hit any of these get <span class="cjo-rust">killed</span>, not considered</h2>

<div class="grid grid-cols-1 gap-2 mt-5">

<div class="cjo-anti"><span class="x">x</span> Pull-to-refresh randomness, variable-reward mechanics. Contextual rejection in B2B paying-buyer settings.</div>
<div class="cjo-anti"><span class="x">x</span> Streak punishment, loss-aversion mechanics. Engineers compulsion through fear.</div>
<div class="cjo-anti"><span class="x">x</span> Cheap branded swag. Pens, mugs, tote bags. Serves the seller, not the recipient.</div>
<div class="cjo-anti"><span class="x">x</span> Premature referral asks at Day 30 / 60 calendar trigger. First-date-parents damage.</div>
<div class="cjo-anti"><span class="x">x</span> Vague satisfaction surveys at milestone points. Doesn't measure the stated goal.</div>
<div class="cjo-anti"><span class="x">x</span> Generic welcome email with company history + product features.</div>
<div class="cjo-anti"><span class="x">x</span> Engagement metrics dashboards optimized for time-on-platform.</div>
<div class="cjo-anti"><span class="x">x</span> Replacing the Day 1 handwritten note with email for efficiency.</div>
<div class="cjo-anti"><span class="x">x</span> Message overload, channel collision. 10 messages across 4 senders in one day.</div>

</div>

</div>

<!--
ANTI PATTERNS. The 9-row catalog. No v-clicks, the density is the point.
Speaker: read 3 to 5 out loud, point at the ones the team has actually
shipped recently, agree to kill them. The slide is the audit.
-->

---
layout: default
---

<!-- slide:database-reactivation-18 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow gold">v1.3 framing, new this cycle</div>

<h2 class="cjo-h2">Database Reactivation is a <span class="cjo-gold">standalone moment class</span></h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
Most teams treat reactivation as an email sequence. Wrong frame. Reactivation is the 5-stage journey applied in reverse to a cold contact who once raised their hand. Same physics, different anchor.
</p>

<div class="grid grid-cols-2 gap-4 mt-6">

<v-clicks>

<div class="cjo-card accent">
<div class="t">The reframe</div>
<div class="d">A dormant lead is not a new lead. They committed once. They paused. The Affirm-window for a reactivation is the first 48 hours after they re-engage, not after they first signed.</div>
</div>

<div class="cjo-card accent">
<div class="t">The trigger surface</div>
<div class="d">State-based on engagement_score crossing a threshold (last-touch + opens + intent signals). Not time-based. Reactivation that fires on a calendar is a campaign. Reactivation that fires on a signal is a relationship.</div>
</div>

<div class="cjo-card accent">
<div class="t">The anchor moment</div>
<div class="d">A founder-named human note that references something specific from the original engagement. We made the change you said we needed. No pitch. The note IS the moment.</div>
</div>

<div class="cjo-card accent">
<div class="t">The Accomplish gate</div>
<div class="d">Same rule. No advocate ask until the reactivated relationship hits a renewed goal-met state. Reactivation is not a license to skip stages.</div>
</div>

</v-clicks>

</div>

</div>

<!--
DATABASE REACTIVATION. New v1.3 framing. Four v-clicks. The reframe is the
load-bearing beat: reactivation IS a journey, not a campaign. Speaker: tie
this to the SupportED reactivation SOP and the agency Reactivation & Launch
SOP that already exists.
-->

---
layout: default
---

<!-- slide:art-of-follow-up-19 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow gold">v1.3 framing, new this cycle</div>

<h2 class="cjo-h2">The Art of the Follow Up, a <span class="cjo-gold">10 day cadence</span></h2>

<p class="cjo-lead" style="margin-top: 0.5rem; max-width: 52rem;">
For any high-intent contact who paused (booked a call and ghosted, started a trial and went silent, signed an MSA and stalled), run this 10-day cadence. Built for warmth, not pressure. Each touch has its own job.
</p>

<div class="grid grid-cols-5 gap-2 mt-6">

<v-clicks>

<div class="cjo-card"><div class="n">D 0</div><div class="t">Re-anchor</div><div class="d">Reference the exact stated outcome. No new pitch.</div></div>
<div class="cjo-card"><div class="n">D 1</div><div class="t">Pattern-match</div><div class="d">Show a peer with their same situation. Outcome, not feature.</div></div>
<div class="cjo-card"><div class="n">D 3</div><div class="t">Friction-find</div><div class="d">Ask one question. What is in the way right now?</div></div>
<div class="cjo-card"><div class="n">D 5</div><div class="t">Loom check</div><div class="d">90 sec personal video. Named. Specific.</div></div>
<div class="cjo-card"><div class="n">D 7</div><div class="t">Door-open</div><div class="d">If now is not it, here is when. Soft.</div></div>

</v-clicks>

</div>

<div class="grid grid-cols-5 gap-2 mt-3">

<v-clicks>

<div class="cjo-card"><div class="n">D 8</div><div class="t">Story drop</div><div class="d">One short case study, same vertical.</div></div>
<div class="cjo-card"><div class="n">D 9</div><div class="t">Honest pause</div><div class="d">If silent, name it. No guilt-trip.</div></div>
<div class="cjo-card"><div class="n">D 10</div><div class="t">Close-loop</div><div class="d">Final note. Door stays open. Move to nurture list.</div></div>
<div class="cjo-card" style="grid-column: span 2;"><div class="n">RULE</div><div class="t">Every touch carries one job</div><div class="d">No mega-mails. No 4-stack subject lines. Quiet, warm, ownership.</div></div>

</v-clicks>

</div>

</div>

<!--
ART OF FOLLOW UP. 8 cadence touches across 10 days plus the rule card.
v-clicks reveal them in two rows. The whole sequence is one moment class,
not 8 separate moments. Speaker: read 3 touches aloud, name the job each
does, lock in the rule.
-->

---
layout: default
---

<!-- slide:industry-matrix-20 -->

<div class="px-12 py-7">

<div class="cjo-eyebrow gold">HERO VISUAL TWO</div>

<h2 class="cjo-h2">Five industries, <span class="cjo-gold">five different defaults</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
Same 5-stage spine. The Day 1 ritual, the cohort surface, the Advocate ask, the tracking surface all fork by industry. Lock the industry before designing the moments.
</p>

<div class="grid grid-cols-5 gap-2 mt-5">

<div class="cjo-ind coach">
<div class="nm">Coach / Agency</div>
<div class="ttl">Sales led</div>
<div class="d">Day 1 founder note + 24h call. Cohort Slack. Advocate ask at goal_met. Postgres tracking.</div>
</div>

<div class="cjo-ind real">
<div class="nm">Real Estate</div>
<div class="ttl">Sales led</div>
<div class="d">Closing-day gift + 30d check. Repeat-buyer registry. Advocate ask post-close. CRM tracking.</div>
</div>

<div class="cjo-ind trade">
<div class="nm">Local Trade</div>
<div class="ttl">Marketing led</div>
<div class="d">Same-day follow-up + 90d return-visit nudge. Neighborhood referrals. NPS at job close.</div>
</div>

<div class="cjo-ind ent">
<div class="nm">Enterprise B2B</div>
<div class="ttl">Sales led, multi-stake</div>
<div class="d">QBR cadence + champion + sponsor + IT touches. Renewal window opens at Day 60. Salesforce.</div>
</div>

<div class="cjo-ind saas">
<div class="nm">SaaS / B2C</div>
<div class="ttl">Product led</div>
<div class="d">In-app welcome + activation gates. Cohort by usage tier. Auto-referral after first-value. Mixpanel + DB.</div>
</div>

</div>

<div class="mt-5">

<table class="cjo-table">
<thead>
<tr>
<th>Industry</th>
<th>Day 1 ritual</th>
<th>Cohort recognition</th>
<th>Advocate ask</th>
<th>Tracking surface</th>
</tr>
</thead>
<tbody>
<tr><td>Coach / Agency</td><td>Founder note + welcome call</td><td>Private Slack channel</td><td>Goal-met flag, case study request</td><td>Postgres journey_events</td></tr>
<tr><td>Real Estate</td><td>Closing-day artifact (housewarming)</td><td>Referral program + repeat ladder</td><td>Post-close handshake at month 1</td><td>CRM tags + repeat-buyer flag</td></tr>
<tr><td>Local Trade</td><td>Same-day SMS thank-you</td><td>Neighborhood network of homes serviced</td><td>NPS at job close + 90d return nudge</td><td>Jobber / Housecall Pro</td></tr>
<tr><td>Enterprise B2B</td><td>3-way exec intro + handoff dossier</td><td>Customer council, exec-tier roundtable</td><td>QBR-gated, sponsor-validated</td><td>Salesforce + Gainsight</td></tr>
<tr><td>SaaS / B2C</td><td>In-app welcome + founder Loom</td><td>In-app feed + referral codes</td><td>First-value-delivered in-app prompt</td><td>Mixpanel + Postgres events</td></tr>
</tbody>
</table>

</div>

</div>

<!--
INDUSTRY MATRIX. Hero visual two. Top row of 5 tiles = the strategic frame
per industry. Bottom row = the 4-column adaptation matrix. The slide is
information-dense by design. Speaker: pick the audience's industry, walk
that ONE row, contrast with one neighbor.
-->

---
layout: default
---

<!-- slide:worked-cyborgtalent-21 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Worked example, dual-track placement</div>

<h2 class="cjo-h2">cyborgtalent, the <span class="cjo-gold">canonical reference</span></h2>

<div class="grid grid-cols-2 gap-4 mt-5">

<div class="cjo-card accent">
<div class="t">The setup</div>
<div class="d">cyborgtalent places AI-trained operators (cyborgs) into founders' companies. The founder is the buyer. The operator is the user. Both must be retained.</div>
</div>

<div class="cjo-card accent">
<div class="t">The economics</div>
<div class="d">~1,065 USD vendor + ~800 USD labor = ~1,865 USD per placement, 100-day window. Baseline LTV 9,600. Treated LTV 24,000. LTV-delta ratio 7.7 times. The moments are pulling their weight.</div>
</div>

<div class="cjo-card accent">
<div class="t">Founder track</div>
<div class="d">Day 1 handwritten note from John. Day 2-3 Affirm Loom. Day 7 joint kickoff. Day 30 / 60 / 90 measured-progress reviews. Day 100 Accomplish celebration. Then the Advocate ask, gated.</div>
</div>

<div class="cjo-card accent">
<div class="t">Operator track</div>
<div class="d">24h welcome call from senior operator. Embossed Operator Charter booklet. Weekly Cyborg Cohort call. First-week pride moment in internal Slack. Identity-ladder progression to senior cyborg.</div>
</div>

</div>

<div class="cjo-callout" style="margin-top: 1.5rem;">
<span class="lab">The lesson the worked example proves</span>
Dual-track journeys are not double-cost journeys. The shared moments (joint kickoff, measured-progress review) serve both audiences. The split moments (founder Affirm Loom, operator Charter) serve each precisely. Cost stays inside the 500 to 1,200 band per side.
</div>

</div>

<!--
WORKED EXAMPLE ONE. cyborgtalent. The canonical doc is at
00_Foundations/cyborgtalent_moments_architecture_2026_06_14.md. This slide is
the compression. Speaker: walk the LTV-delta math out loud, then the
dual-track principle.
-->

---
layout: default
---

<!-- slide:worked-saas-22 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Worked example, product-led motion</div>

<h2 class="cjo-h2">SaaS trial to paid, <span class="cjo-gold">5 USD per trial</span> economics</h2>

<div class="grid grid-cols-2 gap-4 mt-5">

<div>

<div class="cjo-card accent">
<div class="t">The constraint</div>
<div class="d">500 trials per month. No founder time per user. Activation must happen in-app within 7 days or churn risk skyrockets.</div>
</div>

<div class="cjo-card accent" style="margin-top: 0.7rem;">
<div class="t">What changes</div>
<div class="d">Action surfaces shift from physical to digital. In-app welcome replaces mail. Behavioral-trigger emails replace calls. Recorded-once founder Loom serves every new user. Spend per trial 5 to 50 USD vs 500 to 1,200 high-touch.</div>
</div>

</div>

<div>

<div class="cjo-card accent">
<div class="t">What stays the same</div>
<div class="d">Day 0 measurable goal capture (in signup flow). Affirm window inside 48 hours (welcome email + in-app nudge + Loom). Accomplish-gate on Advocate ask. All 9 anti-patterns hold.</div>
</div>

<div class="cjo-card accent" style="margin-top: 0.7rem;">
<div class="t">The economics</div>
<div class="d">Infrastructure cost is fixed, not per-trial. Same welcome email serves 10 or 10,000 trials. Same founder Loom plays for the next 18 months. The math compounds as the cohort grows.</div>
</div>

</div>

</div>

<div class="cjo-callout" style="margin-top: 1.4rem;">
<span class="lab">The lesson the SaaS example proves</span>
The principles are universal. The surfaces adapt. Coleman's dopamine asymmetry hits a 19 USD subscription the same way it hits a 50,000 USD engagement. Magnitude differs. Shape does not.
</div>

</div>

<!--
WORKED EXAMPLE TWO. SaaS. From the v1.2 saas_b2c_adaptation_guide.md. Four
cards in 2x2. Speaker: walk the constraint, name what changes, name what
stays. The universal-physics-with-adapted-surfaces beat is the lesson.
-->

---
layout: default
---

<!-- slide:thought-experiments-23 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Thought experiments, stress-test any design</div>

<h2 class="cjo-h2">12 mental moves to land on <span class="cjo-gold">great moments</span></h2>

<div class="grid grid-cols-4 gap-2 mt-5">

<div class="cjo-te"><span class="n">01</span>Pre-mortem the relationship</div>
<div class="cjo-te"><span class="n">02</span>The phone call they don't make</div>
<div class="cjo-te"><span class="n">03</span>The brag they want to make</div>
<div class="cjo-te"><span class="n">04</span>Strip the rewards</div>
<div class="cjo-te"><span class="n">05</span>Find the dopamine collapse</div>
<div class="cjo-te"><span class="n">06</span>Peer-comparison test</div>
<div class="cjo-te"><span class="n">07</span>Reverse the ask</div>
<div class="cjo-te"><span class="n">08</span>5-year-old test</div>
<div class="cjo-te"><span class="n">09</span>Lifeboat test</div>
<div class="cjo-te"><span class="n">10</span>Third-rail test</div>
<div class="cjo-te"><span class="n">11</span>Repeat-customer letter</div>
<div class="cjo-te"><span class="n">12</span>Retroactive consent test</div>

</div>

<div class="grid grid-cols-3 gap-3 mt-5">

<v-clicks>

<div class="cjo-card">
<div class="n">01 PRE-MORTEM</div>
<div class="t">Write the breakup message</div>
<div class="d">Imagine the customer is sending a breakup message 6 months from now. What did you miss in Stage 2-4? Which moment, if engineered, would have caught it?</div>
</div>

<div class="cjo-card">
<div class="n">03 THE BRAG</div>
<div class="t">Write their LinkedIn post</div>
<div class="d">If they were proud at Day 100, what is in that post? Reverse-engineer the moments that make that brag true. Build toward THAT, not generic milestones.</div>
</div>

<div class="cjo-card">
<div class="n">05 DOPAMINE COLLAPSE</div>
<div class="t">Find the cheap save</div>
<div class="d">At each stage transition, identify where the emotional state probably drops. What touchpoint, costing 5 to 50 USD, would close THAT gap?</div>
</div>

</v-clicks>

</div>

</div>

<!--
THOUGHT EXPERIMENTS. 12-card grid up top. Three expanded cards below (clicks
reveal one at a time). These are the mental moves to land great moments.
Speaker: pick one, run it live with the audience on their actual journey.
-->

---
layout: default
---

<!-- slide:workshop-format-24 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Workshop format</div>

<h2 class="cjo-h2">90 minutes, <span class="cjo-gold">5 blocks</span>, with a runnable manifest at the end</h2>

<div class="grid grid-cols-5 gap-2 mt-6">

<v-clicks>

<div class="cjo-block">
<span class="num">BLOCK 1</span>
<div class="ttl">Empathy walk</div>
<div class="tm">15 min</div>
</div>

<div class="cjo-block">
<span class="num">BLOCK 2</span>
<div class="ttl">4-pillar audit</div>
<div class="tm">20 min</div>
</div>

<div class="cjo-block">
<span class="num">BLOCK 3</span>
<div class="ttl">Options exploration</div>
<div class="tm">20 min</div>
</div>

<div class="cjo-block">
<span class="num">BLOCK 4</span>
<div class="ttl">Flow chart co-create</div>
<div class="tm">20 min</div>
</div>

<div class="cjo-block">
<span class="num">BLOCK 5</span>
<div class="ttl">Output + next steps</div>
<div class="tm">15 min</div>
</div>

</v-clicks>

</div>

<div class="grid grid-cols-2 gap-4 mt-6">

<div class="cjo-card">
<div class="n">PRE-WORKSHOP, ASYNC</div>
<div class="t">15 min intake from the client</div>
<div class="d">Constraint discovery (budget, stack, capacity, count, latency). Current-state audit. Engagement context (buyer, user, stated 100-day goal).</div>
</div>

<div class="cjo-card">
<div class="n">POST-WORKSHOP, 24 H</div>
<div class="t">Runnable deliverable</div>
<div class="d">Filled-in journey design doc + Mermaid flow chart + per-moment YAML manifest catalog + tier-adapted tool recs + 3-week implementation roadmap.</div>
</div>

</div>

</div>

<!--
WORKSHOP FORMAT. Five v-clicks across the blocks. Then the pre and post
wrappers as static cards. Speaker: this is what we sell to clients. 90 min
of facilitated work. Output is runnable infrastructure, not a strategy doc.
-->

---
layout: default
---

<!-- slide:context-doc-prompt-25 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">The reusable artifact</div>

<h2 class="cjo-h2">The context-doc prompt, <span class="cjo-gold">paste and run</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
Hand this prompt + the client engagement context to the customer_journey_optimizer skill and you get back a 5-stage moments map with per-moment YAML manifests. The prompt is the reusable interface.
</p>

<div class="cjo-code" style="margin-top: 1rem; font-size: 0.78rem;">
<span class="c"># Context-doc prompt</span><br/>
<br/>
<span class="k">CLIENT:</span> {client_slug}<br/>
<span class="k">MOTION:</span> {product_led | sales_led | marketing_led}<br/>
<span class="k">INDUSTRY:</span> {coach | real_estate | trade | enterprise_b2b | saas}<br/>
<span class="k">BUYER:</span> {persona, ICP-locked, one paragraph}<br/>
<span class="k">USER:</span> {persona, separate or same as buyer}<br/>
<span class="k">STATED_DAY_100_GOAL:</span> {one measurable sentence}<br/>
<span class="k">TIER_BUDGET:</span> {tier_1 | tier_2 | tier_3, per-engagement spend cap}<br/>
<span class="k">EXISTING_STACK:</span> {CRM, email, comm channels}<br/>
<span class="k">ENGAGEMENT_COUNT_PER_MONTH:</span> {1-5 | 5-20 | 20+}<br/>
<br/>
<span class="c"># Skill activates and produces:</span><br/>
<span class="c"># 1. Engagement snapshot with ICP lock</span><br/>
<span class="c"># 2. 5-stage moments map (founder + user tracks)</span><br/>
<span class="c"># 3. Per-moment YAML manifest catalog</span><br/>
<span class="c"># 4. Tracking architecture + goal-met flag spec</span><br/>
<span class="c"># 5. Trigger wiring plan + anti-pattern audit</span><br/>
<span class="c"># 6. Vendor + cost choices for the matched tier</span><br/>
<span class="c"># 7. Open decisions surfaced for John</span>
</div>

</div>

<!--
CONTEXT DOC PROMPT. The reusable artifact. Show the actual structure of the
input. Speaker: this is how we go from a sales call to a runnable journey
design in one workflow run. Live demo if time.
-->

---
layout: default
---

<!-- slide:cost-discipline-26 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Cost discipline + journey economics</div>

<h2 class="cjo-h2">Per-engagement spend, <span class="cjo-gold">500 to 1,200 USD</span> band</h2>

<div class="grid grid-cols-2 gap-4 mt-5">

<div>

<table class="cjo-table">
<thead>
<tr><th>Stage</th><th>Spend band (vendor)</th><th>What it buys</th></tr>
</thead>
<tbody>
<tr><td>1 Commit</td><td>5 to 20</td><td>Day 1 note + 24h call</td></tr>
<tr><td>2 Onboard</td><td>50 to 200</td><td>Welcome artifact + kickoff</td></tr>
<tr><td>3 Activate</td><td>100 to 300</td><td>Cohort calls + check-ins</td></tr>
<tr><td>4 Success</td><td>300 to 500</td><td>Measured reviews + celebration</td></tr>
<tr><td>5 Ascend</td><td>0 to 50</td><td>Gated, low-cost ask</td></tr>
</tbody>
</table>

</div>

<div>

<div class="cjo-eyebrow" style="margin-bottom: 0.5rem;">The LTV-delta formula</div>

<div class="cjo-code" style="font-size: 0.85rem;">
<span class="c">// per engagement type, one row per quarter</span><br/>
<br/>
LTV_delta = <br/>
&nbsp;&nbsp;(LTV_treated - LTV_baseline)<br/>
&nbsp;&nbsp;/ moment_spend_per_engagement
</div>

<div class="cjo-callout" style="margin-top: 1rem;">
<span class="lab">The thresholds</span>
Ratio under 3 times suggests the moments are not pulling their weight. Re-run calibration. Ratio above 10 times suggests under-investment. Widen the band.
</div>

</div>

</div>

<div class="cjo-callout" style="margin-top: 1.2rem;">
<span class="lab">Loaded-cost honesty</span>
The 5 USD Day 1 note vendor pass-through is real cost 25.83 USD with 5 minutes founder review at 250 USD per hour. The cost band assumes fully-loaded math. The YAML manifest cost_usd field is vendor-only.
</div>

</div>

<!--
COST DISCIPLINE. Left = the spend bands per stage. Right = the LTV-delta
formula and the thresholds. Bottom callout = the loaded-cost honesty rule.
Speaker: walk the cyborgtalent row from the previous slide (1,865 / 14,400
= 7.7x). The ratio is the test.
-->

---
layout: default
---

<!-- slide:self-application-27 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow">Self-application discipline</div>

<h2 class="cjo-h2">We use the framework on <span class="cjo-gold">ourselves first</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
Five FF and Joburn journey types run today. None are mapped explicitly. We apply this skill to each as a self-audit. The outputs become both operational improvement and the canonical worked-example library.
</p>

<div class="grid grid-cols-5 gap-2 mt-6">

<v-clicks>

<div class="cjo-card">
<div class="n">01</div>
<div class="t">Client engagement</div>
<div class="d">offer_ramp_up Phase 1-4 detailing</div>
</div>

<div class="cjo-card">
<div class="n">02</div>
<div class="t">Operator placement</div>
<div class="d">cyborgtalent, mapped, canonical</div>
</div>

<div class="cjo-card">
<div class="n">03</div>
<div class="t">Cert candidate</div>
<div class="d">cert_forge intake to issuance to alumni</div>
</div>

<div class="cjo-card">
<div class="n">04</div>
<div class="t">Internal team hire</div>
<div class="d">Joburn team member ramp arc</div>
</div>

<div class="cjo-card">
<div class="n">05</div>
<div class="t">Audience growth</div>
<div class="d">Joburn brain to audience to operator pipeline</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.4rem;">
<span class="lab">Why we eat our own dog food</span>
We sell the framework by showing we use it on ourselves. Each self-applied journey is a worked example. Each calibrates the framework against real-world data. The credibility is structural.
</div>

</div>

<!--
SELF APPLICATION. Five v-clicks for the five journey types. The
cyborgtalent one is already mapped (canonical worked example). The other
four are pending. Speaker: name which one we tackle next.
-->

---
layout: default
---

<!-- slide:whats-next-28 -->

<div class="px-14 py-7">

<div class="cjo-eyebrow gold">What's next, v1.3 framing</div>

<h2 class="cjo-h2">Customer Journey in a Box, <span class="cjo-gold">the productized asset</span></h2>

<p class="cjo-lead" style="margin-top: 0.4rem; max-width: 52rem;">
After this deck validates the framing, the next build is the productized version. GHL-importable template bundle, industry adaptation tables, per-step tier alternatives, fed through AIOS as a workshop deliverable.
</p>

<div class="grid grid-cols-2 gap-4 mt-6">

<v-clicks>

<div class="cjo-card accent">
<div class="t">The bundle</div>
<div class="d">GHL workflow JSON exports per industry x motion type. Pre-built triggers, action surfaces, tracking tags. Operator imports, swaps the variables, ships in days.</div>
</div>

<div class="cjo-card accent">
<div class="t">The industry adaptation tables</div>
<div class="d">For each of the 5 industries, the per-stage moment defaults, the cohort surface defaults, the Advocate-ask defaults. Five rows times five stages times four pillars.</div>
</div>

<div class="cjo-card accent">
<div class="t">The technical trigger maps</div>
<div class="d">Per-step manual / mid / pro alternative solutions. The Tier 1 fallback for every Tier 3 prescription. The operator picks the tier the client lives in.</div>
</div>

<div class="cjo-card accent">
<div class="t">Powered by RAG</div>
<div class="d">Pulls canon language from copy-brain at build time. Feels rich without exposing the SOP layer or the internal vocabulary. Living asset, not a one-time write.</div>
</div>

</v-clicks>

</div>

</div>

<!--
WHAT'S NEXT. The product layer. Four v-clicks. Speaker: this Slidev validates
the framing. After it ships, we build the productized version. ~6-10 hr next
session.
-->

---
layout: default
---

<!-- slide:next-steps-29 -->

<div class="px-14 py-8">

<div class="cjo-eyebrow">How to apply this on Monday</div>

<h2 class="cjo-h2">Three concrete next steps</h2>

<div class="grid grid-cols-3 gap-4 mt-7">

<v-clicks>

<div class="cjo-card accent">
<div class="n">STEP 01</div>
<div class="t">Pick one client</div>
<div class="d">Pick the client whose journey is leaking the most visible money. Run the 4-pillar audit on their last 5 engagements. Surface the missing pillar.</div>
</div>

<div class="cjo-card accent">
<div class="n">STEP 02</div>
<div class="t">Map one journey</div>
<div class="d">Load the customer_journey_optimizer skill. Feed it the context-doc prompt with their motion, industry, ICP lock, stated goal, tier. Generate the YAML manifest catalog.</div>
</div>

<div class="cjo-card accent">
<div class="n">STEP 03</div>
<div class="t">Ship one moment</div>
<div class="d">Pick the highest-stakes moment that currently does not exist. Wire all 4 pillars. Trigger, action, tracking, voice lock. Ship it inside 7 days. Calibrate.</div>
</div>

</v-clicks>

</div>

<div class="cjo-callout" style="margin-top: 1.8rem;">
<span class="lab">The compounding move</span>
The framework is not earned by understanding it. It is earned by shipping one moment, watching the tracking surface light up, calibrating, then shipping the next one. The journey that compounds is the journey that learns.
</div>

</div>

<!--
NEXT STEPS. Three v-clicks. Each one is actionable inside the week. Speaker:
end on the compounding-move callout. The framework rewards the operator who
ships, not the operator who reads.
-->

---
layout: cover
---

<!-- slide:closing-litmus-30 -->

<div class="cjo-bar"></div>

<div class="absolute inset-0 cjo-dark flex flex-col justify-center items-center px-16">

<div class="cjo-dark-wrap text-center max-w-5xl">

<div class="cjo-eyebrow ondark">The litmus test</div>

<div class="cjo-litmus" style="background: rgba(255,255,255,0.06); border-color: #D4B85A;">

<div class="q" style="color: #D4B85A;">Ask this on every journey design before shipping</div>

<div class="a" style="color: #fff; font-size: 1.75rem;">
Does this journey have <span style="color:#D4B85A;">all 4 pillars</span><br/>
at <span style="color:#D4B85A;">every stage</span>?
</div>

<p style="color: rgba(255,255,255,0.78); font-size: 1.05rem; line-height: 1.5; margin-top: 1.4rem;">
Key Moments. Triggers. Actions. Tracking. At Stage 0, 1, 2, 3, 4, 5, 6. If any cell in that grid is empty, the journey has a structural leak. Find it. Fill it. Ship the next moment.
</p>

</div>

</div>

<div class="cjo-footer ondark">JOBURN, INTERNAL TRAINING, 2026-06-17, END OF DECK</div>

</div>

<!--
CLOSING LITMUS. The single test that closes the deck. Five-by-seven grid of
pillars by stages. Every cell filled or named missing. Speaker: hold this
slide. The litmus is what they take with them.
-->
