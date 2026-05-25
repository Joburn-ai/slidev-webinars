---
theme: default
title: The 2026 BS/MD Admissions Architecture
info: |
  Coach Jo (Gifted Gabber) BS/MD Parent Masterclass.
  Wed 2026-05-27, 9pm ET. Coach Jo on camera, live.
  10-slide showcase sample. v3 short script source (45-min target).
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: Inter
  serif: Inter
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
---

<style>
:root {
  --brand-primary: #422C76;
  --brand-secondary: #FEBC11;
  --brand-coral: #EE7962;
  --brand-mint: #95D1C9;
  --brand-light: #EFEEED;
  --brand-dark: #1a0f2e;
  --brand-cream: #fafaf7;
}

.slidev-layout {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--brand-cream);
  color: var(--brand-dark);
}

.slidev-layout h1 {
  font-size: 4.5rem;
  font-weight: 900;
  color: var(--brand-primary);
  letter-spacing: -0.03em;
  line-height: 1.05;
  margin-bottom: 1.5rem;
}

.slidev-layout h2 {
  font-size: 3rem;
  font-weight: 800;
  color: var(--brand-primary);
  letter-spacing: -0.02em;
  margin-bottom: 1.25rem;
}

.slidev-layout p, .slidev-layout li {
  font-size: 1.5rem;
  line-height: 1.55;
  color: var(--brand-dark);
}

.slidev-layout li {
  margin-bottom: 0.75rem;
}

.slidev-layout strong {
  color: var(--brand-primary);
  font-weight: 700;
}

.slidev-vclick-hidden {
  opacity: 0 !important;
}

.slidev-vclick-target {
  transition: opacity 200ms ease;
}

.gold {
  color: var(--brand-secondary);
  font-weight: 800;
}
.purple {
  color: var(--brand-primary);
}
.coral {
  color: var(--brand-coral);
}
.mint {
  color: var(--brand-mint);
}
.frosted {
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(66, 44, 118, 0.12);
  border-radius: 20px;
  padding: 3rem 4rem;
  box-shadow: 0 20px 60px -10px rgba(66, 44, 118, 0.25);
}

.frosted-dark {
  background: rgba(26, 15, 46, 0.78);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(254, 188, 17, 0.22);
  border-radius: 20px;
  padding: 3rem 4rem;
  color: white;
}

.section-gradient {
  background: linear-gradient(135deg, var(--brand-primary) 0%, #5b3da3 50%, #422C76 100%);
  color: white;
}

.amber-stripe {
  background: var(--brand-secondary);
  height: 8px;
  width: 100%;
}

.outcome-card {
  background: white;
  border-radius: 16px;
  padding: 2rem 1.5rem;
  border: 1px solid rgba(66, 44, 118, 0.10);
  box-shadow: 0 8px 24px -8px rgba(66, 44, 118, 0.18);
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.outcome-name {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--brand-primary);
  margin-bottom: 0.5rem;
}

.outcome-detail {
  font-size: 1rem;
  color: #444;
  line-height: 1.45;
}

.outcome-tag {
  display: inline-block;
  background: var(--brand-secondary);
  color: var(--brand-dark);
  font-size: 0.75rem;
  font-weight: 800;
  padding: 0.3rem 0.7rem;
  border-radius: 6px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-top: 0.75rem;
  align-self: flex-start;
}
</style>

<div class="absolute inset-0 section-gradient flex flex-col justify-center items-center px-12 text-white">
  <div class="absolute top-0 left-0 right-0 amber-stripe"></div>

  <div class="frosted-dark max-w-5xl">
    <div class="text-sm uppercase tracking-widest mb-6" style="color: var(--brand-secondary); font-weight: 800; letter-spacing: 0.3em;">
      Gifted Gabber · BS/MD Parent Masterclass
    </div>

    <h1 class="text-white" style="font-size: 4rem; line-height: 1.1; color: white;">
      The 2026 BS/MD <br/>Admissions Architecture
    </h1>

    <p class="text-2xl mt-6 mb-8" style="color: rgba(255,255,255,0.92); font-weight: 400; line-height: 1.4;">
      Why <strong style="color: var(--brand-secondary);">Perfect Grades + 1560 SAT + 500 Hospital Hours</strong> Is the #1 Cause of BS/MD Rejection in 2026.
    </p>

    <div class="text-lg mt-12" style="color: rgba(255,255,255,0.7);">
      with <strong style="color: white;">Coach Jo</strong> · Wednesday, May 27 · 9:00 PM ET
    </div>
  </div>

  <div class="absolute bottom-6 left-0 right-0 text-center text-xs" style="color: rgba(255,255,255,0.4); letter-spacing: 0.15em;">
    LIVE WEBINAR · RECURRING WEEKLY WEDNESDAYS
  </div>
</div>

---
layout: default
---

<!-- slide:diagnostic-q1-2 -->

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--brand-cream);">

  <div class="text-sm uppercase mb-8" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
    Quick gut check · Question 1
  </div>

  <h1 class="text-center" style="font-size: 3.5rem; max-width: 1100px; line-height: 1.15;">
    A 1560 SAT is your child's <span class="purple">strongest</span> <br/>BS/MD application asset.
  </h1>

  <div class="mt-12 flex gap-6" v-click>
    <div style="background: white; border: 3px solid var(--brand-primary); padding: 1.5rem 3rem; border-radius: 12px; font-size: 2rem; font-weight: 800; color: var(--brand-primary);">
      TRUE
    </div>
    <div style="background: var(--brand-coral); padding: 1.5rem 3rem; border-radius: 12px; font-size: 2rem; font-weight: 900; color: white; box-shadow: 0 12px 30px -8px rgba(238, 121, 98, 0.5);">
      FALSE
    </div>
  </div>

  <div class="mt-10 max-w-3xl text-center" v-click>
    <p class="text-2xl" style="color: var(--brand-dark); font-weight: 500;">
      Most NJMS applicants now score above 1500. <br/>
      <span class="gold">The score is the entry fee.</span> Not the asset.
    </p>
  </div>
</div>

---
layout: default
---

<!-- slide:proof-stack-3 -->

<div class="absolute inset-0 px-16 py-12" style="background: var(--brand-cream);">

  <div class="text-center mb-10">
    <div class="text-sm uppercase mb-4" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
      Three recent Gifted Gabber families
    </div>
    <h2 style="font-size: 2.5rem;">
      Different students. Different programs. <br/>
      <span class="purple">Same architecture.</span>
    </h2>
  </div>

  <div class="grid grid-cols-3 gap-6 max-w-6xl mx-auto mt-10">

    <div class="outcome-card" v-click>
      <div>
        <div class="outcome-name">Diya Menon</div>
        <div class="outcome-detail">
          Full ride to <strong>seven BS/MD colleges</strong>.
        </div>
      </div>
      <div class="outcome-tag">7 admits · full ride</div>
    </div>

    <div class="outcome-card" v-click>
      <div>
        <div class="outcome-name">Taksh</div>
        <div class="outcome-detail">
          Accepted to <strong>four BS/MD programs</strong> with scholarships. <strong>One full ride.</strong>
        </div>
      </div>
      <div class="outcome-tag">4 admits · 1 full ride</div>
    </div>

    <div class="outcome-card" v-click>
      <div>
        <div class="outcome-name">Diya Patel</div>
        <div class="outcome-detail">
          Stanford. FAU with scholarships. <strong>Full tuition</strong> to Davidson Scholar Program.
        </div>
      </div>
      <div class="outcome-tag">Stanford · Davidson Scholar</div>
    </div>
  </div>

  <div class="mt-12 text-center max-w-4xl mx-auto" v-click>
    <p class="text-xl" style="color: #555; font-style: italic;">
      Plus over <strong style="color: var(--brand-primary);">$15M in merit aid</strong> placed across Brown PLME, Stony Brook Scholars for Medicine, NJMS, Drexel, Pitt GAP, and Rice/Baylor.
    </p>
  </div>
</div>

---
layout: default
---

<!-- slide:ivy-selectivity-4 -->

<div class="absolute inset-0 section-gradient flex flex-col justify-center px-16 text-white">

  <div class="max-w-5xl mx-auto text-center">

    <div class="text-sm uppercase mb-6" style="color: var(--brand-secondary); letter-spacing: 0.3em; font-weight: 800;">
      The 2026 Admissions Shift
    </div>

    <h2 class="text-white" style="font-size: 3.5rem; color: white;">
      Ivy-level selectivity. <br/>
      <span style="color: var(--brand-secondary);">Without the Ivy name.</span>
    </h2>

    <div class="grid grid-cols-3 gap-8 mt-16">
      <div v-click style="background: rgba(255,255,255,0.06); border: 1px solid rgba(254, 188, 17, 0.25); border-radius: 12px; padding: 2rem;">
        <div style="font-size: 4rem; font-weight: 900; color: var(--brand-secondary); line-height: 1;">~3,000</div>
        <div class="mt-3 text-base" style="color: rgba(255,255,255,0.85);">applications to NJMS</div>
      </div>
      <div v-click style="background: rgba(255,255,255,0.06); border: 1px solid rgba(254, 188, 17, 0.25); border-radius: 12px; padding: 2rem;">
        <div style="font-size: 4rem; font-weight: 900; color: var(--brand-secondary); line-height: 1;">25</div>
        <div class="mt-3 text-base" style="color: rgba(255,255,255,0.85);">seats available</div>
      </div>
      <div v-click style="background: rgba(255,255,255,0.06); border: 1px solid rgba(254, 188, 17, 0.25); border-radius: 12px; padding: 2rem;">
        <div style="font-size: 4rem; font-weight: 900; color: var(--brand-secondary); line-height: 1;">1-2%</div>
        <div class="mt-3 text-base" style="color: rgba(255,255,255,0.85);">effective rate <em>inside qualified pool</em></div>
      </div>
    </div>

    <p class="text-xl mt-14" style="color: rgba(255,255,255,0.85); font-weight: 400; max-width: 800px; margin-left: auto; margin-right: auto;" v-click>
      Every elite BS/MD program now operates at Ivy-level selectivity. <br/>
      And the qualified pool is full of perfect templates.
    </p>
  </div>
</div>

---
layout: default
---

<!-- slide:another-path-5 -->

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--brand-cream);">

  <div class="amber-stripe" style="position: absolute; top: 0; left: 0;"></div>

  <div class="max-w-4xl text-center">

    <div class="text-sm uppercase mb-6" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
      Here's the part nobody is telling you
    </div>

    <h1 style="font-size: 3.8rem; line-height: 1.1;">
      There is <span class="gold">another path</span>.
    </h1>

    <p class="text-2xl mt-10 mb-4" style="color: #333; font-weight: 500; line-height: 1.5;" v-click>
      Diya, Taksh, and Diya Patel didn't run the same path <em>harder</em>.
    </p>

    <p class="text-2xl mt-4" style="color: var(--brand-primary); font-weight: 700; line-height: 1.4;" v-click>
      They ran a <strong style="color: var(--brand-coral);">different path entirely</strong>.
    </p>

    <div class="mt-16 inline-block" style="background: white; border: 2px solid var(--brand-primary); border-radius: 12px; padding: 1.5rem 2.5rem;" v-click>
      <p class="text-lg" style="color: var(--brand-primary); font-weight: 600; margin: 0;">
        Built around what BS/MD committees <em>actually need</em>.
      </p>
    </div>
  </div>
</div>

---
layout: default
---

<!-- slide:mechanism-1-spike-6 -->

<div class="absolute inset-0 px-16 py-14" style="background: var(--brand-cream);">

  <div class="max-w-6xl mx-auto">

    <div class="text-sm uppercase mb-3" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
      Mechanism 1 · The Medical Spike
    </div>

    <h2 style="font-size: 2.8rem; margin-bottom: 2rem;">
      A singular, polarizing thesis. <br/>
      Built in a <span class="gold">90-day window</span>.
    </h2>

    <p class="text-xl mb-10" style="color: #444; max-width: 900px;">
      Not a generic "medical interest" essay. <strong>A specific thesis</strong> the student can defend, present, and build proof assets around.
    </p>

    <div class="grid grid-cols-3 gap-5 mt-10">

      <div v-click style="background: white; border-left: 5px solid var(--brand-primary); border-radius: 0 12px 12px 0; padding: 1.75rem; box-shadow: 0 4px 16px -4px rgba(66, 44, 118, 0.15);">
        <div class="text-sm font-bold uppercase mb-2" style="color: var(--brand-primary); letter-spacing: 0.1em;">Diya Menon</div>
        <div class="text-lg" style="color: var(--brand-dark); font-weight: 600; line-height: 1.3;">Healthcare access in underserved Indian-American communities.</div>
      </div>

      <div v-click style="background: white; border-left: 5px solid var(--brand-coral); border-radius: 0 12px 12px 0; padding: 1.75rem; box-shadow: 0 4px 16px -4px rgba(238, 121, 98, 0.15);">
        <div class="text-sm font-bold uppercase mb-2" style="color: var(--brand-coral); letter-spacing: 0.1em;">Taksh</div>
        <div class="text-lg" style="color: var(--brand-dark); font-weight: 600; line-height: 1.3;">AI-assisted differential diagnosis.</div>
      </div>

      <div v-click style="background: white; border-left: 5px solid var(--brand-secondary); border-radius: 0 12px 12px 0; padding: 1.75rem; box-shadow: 0 4px 16px -4px rgba(254, 188, 17, 0.18);">
        <div class="text-sm font-bold uppercase mb-2" style="color: #B8870D; letter-spacing: 0.1em;">Diya Patel</div>
        <div class="text-lg" style="color: var(--brand-dark); font-weight: 600; line-height: 1.3;">Rural pediatric care infrastructure.</div>
      </div>
    </div>

    <div class="mt-12 text-center" v-click>
      <p class="text-xl" style="color: var(--brand-primary); font-weight: 700;">
        Three different theses. Three sets of proof assets. <br/>Three students who stopped being applicants and started being <em>acquired</em>.
      </p>
    </div>
  </div>
</div>

---
layout: default
---

<!-- slide:demo-side-by-side-7 -->

<div class="absolute inset-0 px-12 py-10" style="background: var(--brand-cream);">

  <div class="text-center mb-8">
    <div class="text-sm uppercase mb-3" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
      The demonstration
    </div>
    <h2 style="font-size: 2.4rem;">Two applicants. Side by side.</h2>
  </div>

  <div class="grid grid-cols-2 gap-6 max-w-6xl mx-auto">

    <div style="background: white; border-radius: 16px; padding: 2rem; border: 1px solid rgba(0,0,0,0.06); box-shadow: 0 8px 24px -8px rgba(0,0,0,0.1);">
      <div style="background: var(--brand-light); padding: 0.5rem 1rem; border-radius: 6px; display: inline-block; font-size: 0.85rem; font-weight: 700; color: #666; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.2rem;">
        Applicant A · The Polished Pre-Med
      </div>
      <ul class="text-base" style="list-style: none; padding: 0; margin: 0; color: #333; line-height: 1.7;">
        <li>· <strong>GPA</strong> 4.0 unweighted</li>
        <li>· <strong>SAT</strong> 1560</li>
        <li>· <strong>APs</strong> All 5s</li>
        <li>· <strong>Hospital volunteer</strong> 500 hrs</li>
        <li>· <strong>Research assistant</strong> Local lab</li>
        <li>· <strong>HOSA</strong> Chapter president</li>
        <li>· <strong>Conferences</strong> Three medical leadership</li>
      </ul>
      <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 2px solid var(--brand-coral);">
        <div style="font-size: 1.5rem; font-weight: 900; color: var(--brand-coral);">REJECTED</div>
        <div style="font-size: 0.9rem; color: #666; margin-top: 0.3rem;">from every BS/MD program he applied to</div>
      </div>
    </div>

    <div style="background: white; border-radius: 16px; padding: 2rem; border: 2px solid var(--brand-primary); box-shadow: 0 16px 40px -8px rgba(66, 44, 118, 0.3);" v-click>
      <div style="background: var(--brand-primary); padding: 0.5rem 1rem; border-radius: 6px; display: inline-block; font-size: 0.85rem; font-weight: 700; color: white; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.2rem;">
        Applicant B · Maya · Real Gifted Gabber Student
      </div>
      <ul class="text-base" style="list-style: none; padding: 0; margin: 0; color: #333; line-height: 1.7;">
        <li>· <strong>GPA</strong> 3.85 unweighted</li>
        <li>· <strong>SAT</strong> 1490 (single sitting)</li>
        <li>· <strong>APs</strong> 9 total · mix of sciences + humanities</li>
        <li>· <strong>Clinical exposure</strong> Zero</li>
        <li>· <strong>One Medical Spike:</strong> Healthcare policy for rural seniors</li>
        <li>· Built over <strong>12 weeks</strong> the summer before senior year</li>
        <li>· One policy brief · Two conference talks · One named cohort</li>
      </ul>
      <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 2px solid var(--brand-secondary);">
        <div style="font-size: 1.5rem; font-weight: 900; color: var(--brand-primary);">ACQUIRED</div>
        <div style="font-size: 0.9rem; color: #666; margin-top: 0.3rem;">top-tier BS/MD admit. Over five 4.0/1560+ students from her own high school.</div>
      </div>
    </div>
  </div>

  <p class="text-center mt-8" style="font-size: 1.2rem; color: var(--brand-primary); font-weight: 600;" v-click>
    That is not luck. <span class="gold">That is architecture.</span>
  </p>
</div>

---
layout: default
---

<!-- slide:offer-clarity-call-8 -->

<div class="absolute inset-0 flex flex-col justify-center px-16" style="background: var(--brand-cream);">

  <div class="max-w-5xl mx-auto">

    <div class="text-center mb-10">
      <div class="text-sm uppercase mb-4" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
        Tonight's actual offer
      </div>
      <h1 style="font-size: 4rem;">$100. <span class="gold">Refundable.</span></h1>
      <p class="text-2xl mt-2" style="color: var(--brand-dark);">
        Thirty minutes. With me. One on one.
      </p>
    </div>

    <div class="grid grid-cols-3 gap-5 mt-12">

      <div style="background: white; border-radius: 12px; padding: 1.75rem; border: 1px solid rgba(66, 44, 118, 0.12);" v-click>
        <div style="font-size: 2.5rem; line-height: 1; margin-bottom: 0.5rem;">1</div>
        <div style="font-weight: 700; color: var(--brand-primary); margin-bottom: 0.5rem;">Where your child stands</div>
        <div class="text-sm" style="color: #555; line-height: 1.4;">Current position in the qualified pool relative to your target programs' institutional needs.</div>
      </div>

      <div style="background: white; border-radius: 12px; padding: 1.75rem; border: 1px solid rgba(66, 44, 118, 0.12);" v-click>
        <div style="font-size: 2.5rem; line-height: 1; margin-bottom: 0.5rem;">2</div>
        <div style="font-weight: 700; color: var(--brand-primary); margin-bottom: 0.5rem;">The Spike thesis</div>
        <div class="text-sm" style="color: #555; line-height: 1.4;">The Medical Spike we'd build first. With the 90-day calendar.</div>
      </div>

      <div style="background: white; border-radius: 12px; padding: 1.75rem; border: 1px solid rgba(66, 44, 118, 0.12);" v-click>
        <div style="font-size: 2.5rem; line-height: 1; margin-bottom: 0.5rem;">3</div>
        <div style="font-weight: 700; color: var(--brand-primary); margin-bottom: 0.5rem;">Honest fit check</div>
        <div class="text-sm" style="color: #555; line-height: 1.4;">Whether Gifted Gabber is the right fit. If not, I tell you that.</div>
      </div>
    </div>

    <div class="mt-12 text-center" v-click>
      <div style="display: inline-block; background: var(--brand-secondary); color: var(--brand-dark); padding: 1.25rem 3rem; border-radius: 12px; font-size: 1.4rem; font-weight: 900; box-shadow: 0 12px 30px -8px rgba(254, 188, 17, 0.5);">
        BOOK YOUR CLARITY CALL →
      </div>
      <div class="mt-3 text-sm" style="color: #666; font-family: monospace;">
        calendly.com/gg-counseling/clarity-call-with-head-of-counseling
      </div>
    </div>
  </div>
</div>

---
layout: default
---

<!-- slide:two-types-parents-9 -->

<div class="absolute inset-0 px-12 py-10" style="background: var(--brand-cream);">

  <div class="text-center mb-8">
    <div class="text-sm uppercase mb-3" style="color: var(--brand-coral); letter-spacing: 0.3em; font-weight: 800;">
      The decision in plain language
    </div>
    <h2 style="font-size: 2.6rem;">There are <span class="purple">two types of parents</span> on this call.</h2>
  </div>

  <div class="grid grid-cols-2 gap-6 max-w-6xl mx-auto mt-10">

    <div style="background: white; border-radius: 16px; padding: 2.5rem; border: 1px solid rgba(0,0,0,0.06); opacity: 0.7;">
      <div style="background: var(--brand-light); padding: 0.5rem 1rem; border-radius: 6px; display: inline-block; font-size: 0.85rem; font-weight: 700; color: #666; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 1.5rem;">
        Type One · The Waiter
      </div>
      <p class="text-lg" style="color: #444; line-height: 1.6; font-weight: 500;">
        Goes back to the 500-hour grind. To the polished essays. To the boutique consultancy. To the hope that one more semester will be enough.
      </p>
      <p class="text-lg mt-4" style="color: #444; line-height: 1.6; font-weight: 500;">
        That parent already knows what their December 15 looks like.
      </p>
    </div>

    <div style="background: white; border-radius: 16px; padding: 2.5rem; border: 3px solid var(--brand-primary); box-shadow: 0 16px 40px -8px rgba(66, 44, 118, 0.3);" v-click>
      <div style="background: var(--brand-primary); padding: 0.5rem 1rem; border-radius: 6px; display: inline-block; font-size: 0.85rem; font-weight: 700; color: white; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 1.5rem;">
        Type Two · The Architect
      </div>
      <p class="text-lg" style="color: var(--brand-dark); line-height: 1.6; font-weight: 600;">
        Books the thirty minutes. Hears the diagnosis. Runs the build. Positions the asset.
      </p>
      <p class="text-lg mt-4" style="color: var(--brand-dark); line-height: 1.6; font-weight: 600;">
        Doesn't know if their child gets the seat. <strong>Nobody does.</strong> What they know is that the architecture will be built right.
      </p>
    </div>
  </div>

  <p class="text-center mt-10" style="font-size: 1.6rem; color: var(--brand-primary); font-weight: 800;" v-click>
    Which type are you?
  </p>
</div>

---
layout: end
---

<!-- slide:close-identity-10 -->

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--brand-dark);">

  <div class="amber-stripe" style="position: absolute; top: 0; left: 0;"></div>

  <div class="text-center max-w-4xl">

    <div class="text-sm uppercase mb-6" style="color: var(--brand-secondary); letter-spacing: 0.3em; font-weight: 800;">
      Make this decision on identity. Not on price.
    </div>

    <h1 style="font-size: 4rem; color: white; line-height: 1.15;">
      Architect <br/>the next 90 days.
    </h1>

    <p class="text-2xl mt-6" style="color: rgba(255,255,255,0.6); font-weight: 400;">
      Or wait for the letter.
    </p>

    <div class="mt-16" v-click>
      <div style="display: inline-block; background: var(--brand-secondary); color: var(--brand-dark); padding: 1.25rem 3.5rem; border-radius: 12px; font-size: 1.5rem; font-weight: 900; box-shadow: 0 16px 40px -8px rgba(254, 188, 17, 0.5);">
        Your call.
      </div>
    </div>
  </div>

  <div class="absolute bottom-8 left-0 right-0 text-center text-xs" style="color: rgba(255,255,255,0.3); letter-spacing: 0.15em;">
    GIFTED GABBER · COACH JO · BS/MD ADMISSIONS ARCHITECTURE
  </div>
</div>
