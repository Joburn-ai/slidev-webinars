# §0 -- CONSTRAINTS CAPTURE

**Asked before the roadmap is built. Not after, not during.**

John, 2026-07-28: *"we could also ask about their overall constraints (e.g. time, energy, attention) before the roadmap is created -> it can depend on the industry."*

---

## Why this goes first, and why it is a gate

**A plan that ignores capacity is a plan that produces guilt.** Every roadmap we have ever shipped has assumed the reader has the hours. If they do not, the roadmap is not wrong -- it is unfollowable, which is worse, because unfollowable looks like their failure rather than our mistake.

So the constraint answers do two jobs:

1. **They change what gets built.** Not the diagnosis -- the diagnosis is the diagnosis. **The sequencing, the phase lengths and the DIY-vs-done-with-you split.** Same destination, different route.
2. **They are the honest bound on the promise.** If someone says four hours a week, the roadmap says what four hours a week produces. That is a better asset than one that quietly assumes twenty.

**It is also a qualifier that does not feel like one.** Nobody resents being asked how much time they have. Everybody resents being told they are not a fit.

---

## The three constraints

Attention is the one nobody asks about and it is usually the binding one.

### 1. TIME -- how many hours, realistically

> **"Realistically, how many hours a week can you put into this? Not the number you wish -- the number that survives a bad week."**

| Band | What the roadmap does with it |
|---|---|
| **Under 4** | One lane only. No content engine. Outreach or nothing. Phase lengths double |
| **4 to 8** | One lane plus a light second. The standard shape |
| **8 to 15** | Full shape, both lanes, normal phase lengths |
| **15+** | Full shape compressed. Flag the risk: capacity this high usually means they are the bottleneck for everything else too |

**The wording matters.** "The number that survives a bad week" gets a truthful answer. "How many hours can you commit?" gets an aspiration, and then the roadmap is built on a lie neither party told on purpose.

### 2. ENERGY -- what state are they in

> **"When you sit down to do this, are you starting from full, from tired, or from empty?"**

| State | What the roadmap does with it |
|---|---|
| **Full** | Lead with the hardest, highest-leverage thing |
| **Tired** | Lead with the thing that produces visible proof fastest. **Motivation follows evidence, not the other way round** |
| **Empty** | The first phase is not a growth phase. It is a stabilisation phase. Say so plainly |

**This is the question that decides whether the plan gets started at all**, and the fourth pillar (personal and psychological stability) is why it belongs in a business roadmap rather than feeling like an intrusion.

### 3. ATTENTION -- how fragmented is the day

> **"How much uninterrupted time can you actually get in a row? And what interrupts it?"**

| Shape | What the roadmap does with it |
|---|---|
| **Deep blocks available** (90+ min) | Batch everything. One content session a week, one outreach block a day |
| **Fragmented** (15-30 min slices) | Every task must fit a slice. No task that cannot be finished in one sitting. **This is where most founders actually live and almost no plan is written for it** |
| **Reactive** (client-interrupt driven) | The plan runs on a fixed early block before the interruptions start, and nothing else is assumed |

**Attention is the constraint that silently kills plans.** Someone with fifteen hours a week in six-minute fragments has less usable capacity than someone with six hours in two blocks. Asking about time alone misses this entirely.

---

## Industry variants

The three constraints are constant. **What varies is which one usually binds, and what the interrupt actually is.**

| Industry | Usual binding constraint | The real interrupt | Roadmap adjustment |
|---|---|---|---|
| **Coaching / consulting** | **Attention.** Client calls fragment the day | Client sessions and the admin around them | Fixed pre-client morning block. Never assume afternoons |
| **Agency / done-for-you** | **Energy.** Delivery consumes the same faculty selling needs | Fires, scope creep, team questions | Front-load the week. Assume Thursday and Friday are gone |
| **Education / tutoring** | **Time, and it is seasonal** | The academic calendar. Capacity is not flat across a term | Phase boundaries land on term boundaries, not on calendar months |
| **Course / info product** | **Attention.** The build is infinite and always feels urgent | Their own perfectionism about the product | Cap build time explicitly. The roadmap says stop building on a date |
| **Local / service** | **Time.** Physically on the tools | Jobs, travel between them | Everything asynchronous. Nothing that needs them at a desk |
| **SaaS / product** | **Attention**, split between product and go-to-market | Engineering, support escalations | Separate the two lanes so GTM never competes with a release |

**How to use this.** Do not ask the prospect which industry template applies. Ask the three questions, then let the industry column tell you **which answer to trust least.** A coach who says "attention is fine" is probably wrong about that, and the roadmap should quietly build in the fixed morning block anyway.

---

## Where it goes in the funnel

**Add to the intake, not to the quiz.** The quiz is for capturing curiosity and must stay short. The intake is already ten questions with enforced minimum lengths, and these three belong at the end of it -- after they have described the problem, when they are already being honest.

`quiz-hub/lib/roadmap/intake-questions.ts` already has a `constraints` field marked optional. **Make it three required fields instead of one optional one.**

```
constraint_time      -> band select, 4 options, required
constraint_energy    -> 3 options, required
constraint_attention -> 3 options + "what interrupts it" short text, required
```

**And the roadmap must visibly use them**, or asking was extractive. Slide 5's Snapshot names their constraint back to them in their own words, and the phase timeline at slide 27 is computed from the time band rather than being the same for everyone.

---

## The line that makes it land

On the intake, above the three questions:

> **"These change what we build, not whether we build it. A plan you can't run isn't a plan."**
