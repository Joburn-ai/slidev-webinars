---
theme: default
title: Slidev Feature Lab
info: Live demo of Slidev's interactive capabilities for FF — Mermaid, charts, live Excalidraw + tldraw, reactive quiz, reactions, self-running AI narration.
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

<div class="absolute inset-0 fl-navy-bg flex flex-col justify-center items-center px-12">

<div class="fl-bar"></div>

<div class="max-w-5xl text-center">

<div class="fl-eyebrow">Funnel Futurist · Live Capability Demo</div>

<h1 style="font-size: 4.5rem; color: white;">Slidev <span class="fl-cyan">Feature Lab</span></h1>

<p style="font-size: 1.4rem; color: rgba(255,255,255,0.85); margin-top: 1.5rem; max-width: 44rem; margin-left:auto; margin-right:auto;">
Every interactive thing Slidev can do — live, on the slide. Click around. Draw. Take the quiz. Let it narrate itself.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
PRESS F FOR FULLSCREEN · ARROWS TO ADVANCE
</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 fl-navy-bg flex flex-col justify-center items-center px-16">

<div class="fl-bar"></div>

<script setup lang="ts">
import { ref } from 'vue'
import { useNav } from '@slidev/client'

const playing = ref(false)
const status = ref('Idle')
const nav = useNav()

function selfRun() {
  if (playing.value) return
  playing.value = true
  status.value = 'Narrating (browser voice)…'
  const text = "Welcome to the Funnel Futurist Feature Lab. What you are hearing is the browser's own voice. In production we swap in an Eleven Labs voiceover. The slides can advance on their own. No presenter. This is a self running webinar."
  try {
    const u = new SpeechSynthesisUtterance(text)
    u.rate = 1.02
    u.onend = () => { status.value = 'Done. Auto-advancing in 2s…'; setTimeout(() => nav.next(), 2000) }
    speechSynthesis.cancel()
    speechSynthesis.speak(u)
  } catch (e) {
    status.value = 'Speech not supported here — but the auto-advance still works.'
    setTimeout(() => nav.next(), 4000)
  }
}
</script>

<div class="max-w-4xl text-center">

<div class="fl-eyebrow" style="color: var(--ff-orange);">The AI VSL concept</div>

<h1 style="font-size: 3.2rem; color: white;">A deck that <span class="fl-cyan">narrates + advances itself</span>.</h1>

<p style="font-size: 1.2rem; color: rgba(255,255,255,0.8); margin-top: 1.25rem; max-width: 40rem; margin-left:auto; margin-right:auto;">
Web Speech API reads the script, then auto-advances. Swap the browser voice for an ElevenLabs MP3 per slide and you have a faceless, self-running webinar or VSL.
</p>

<div class="mt-10">
<button class="fl-quiz-btn" style="background: var(--ff-orange); color: white; border-color: var(--ff-orange);" @click="selfRun">▶ Play self-running narration</button>
</div>

<p style="font-size: 0.95rem; color: rgba(255,255,255,0.55); margin-top: 1.5rem; font-family: monospace;">{{ status }}</p>

</div>

</div>

<!--
Browsers block autoplay audio without a user gesture, so a play button is the honest pattern.
For a true hands-off replay, use slidev-addon-narrator with pre-rendered MP3s + a per-slide timer.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center px-16" style="background: var(--ff-cream);">

<div class="fl-eyebrow">Built-in · Mermaid diagrams</div>

<h2 style="font-size: 2.2rem; margin-bottom: 1rem;">Flowcharts from text. Zero design tools.</h2>

```mermaid {theme: 'neutral', scale: 0.82}
flowchart LR
  A[Cold traffic] --> B{Opt-in?}
  B -->|Yes| C[Webinar reg]
  B -->|No| A
  C --> D[Show up live]
  D --> E{Pop quiz<br/>+ pitch}
  E -->|Buys now| F[Client]
  E -->|Not yet| G[Replay + email]
  G --> E
  F --> H[Advocacy / referral]
```

<p style="font-size: 1rem; color: #475569; margin-top: 1rem;">
Edit the text, the diagram redraws. Also supports sequence, gantt, mindmap, state, ER. Renders to SVG so it exports clean.
</p>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)

const data = ref({ labels: [] as string[], datasets: [] as any[] })
const loaded = ref(false)

onMounted(() => {
  // Simulated "live" series. In production this is a fetch() to Supabase / an API.
  const days = Array.from({ length: 14 }, (_, i) => `D${i + 1}`)
  const spend = days.map((_, i) => 280 + Math.round(Math.sin(i / 2) * 60) + i * 8)
  const leads = days.map((_, i) => 6 + Math.round(Math.cos(i / 2) * 3) + Math.floor(i / 2))
  data.value = {
    labels: days,
    datasets: [
      { label: 'Ad spend ($)', data: spend, borderColor: '#FB923C', backgroundColor: 'rgba(251,146,60,0.1)', tension: 0.4, fill: true },
      { label: 'Leads', data: leads, borderColor: '#22D3EE', backgroundColor: 'rgba(34,211,238,0.1)', tension: 0.4, fill: true, yAxisID: 'y1' },
    ],
  }
  loaded.value = true
})
const opts = {
  responsive: true, maintainAspectRatio: false,
  plugins: { legend: { labels: { font: { size: 13 } } } },
  scales: { y: { position: 'left' }, y1: { position: 'right', grid: { drawOnChartArea: false } } },
}
</script>

<div class="fl-eyebrow">Charts + live data</div>

<h2 style="font-size: 2.1rem; margin-bottom: 0.5rem;">Real data, rendered at open-time.</h2>

<p style="font-size: 1rem; color: #475569; margin-bottom: 1.25rem; max-width: 42rem; text-align: center;">
This is Chart.js inside the slide. Swap the simulated series for a <code>fetch()</code> to Supabase and the deck shows current numbers every time a client opens it.
</p>

<div style="width: 760px; height: 340px; background: white; border-radius: 16px; padding: 1.25rem; box-shadow: 0 12px 30px -12px rgba(15,23,42,0.25);">
<Line v-if="loaded" :data="data" :options="opts" />
</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col px-10 py-8" style="background: var(--ff-cream);">

<div class="text-center mb-3">
<div class="fl-eyebrow">Live embed · Excalidraw</div>
<h2 style="font-size: 1.9rem;">Draw on a real Excalidraw board, live.</h2>
</div>

<div style="flex: 1; border-radius: 14px; overflow: hidden; border: 2px solid rgba(15,23,42,0.1); box-shadow: 0 12px 30px -12px rgba(15,23,42,0.25);">
<iframe src="https://excalidraw.com" style="width: 100%; height: 100%; border: 0;" allow="clipboard-read; clipboard-write"></iframe>
</div>

<p style="font-size: 0.85rem; color: #64748b; margin-top: 0.6rem; text-align: center;">
Fully interactive — draw right now. For finished slides, the <code>slidev-addon-excalidraw</code> renders a saved <code>.excalidraw</code> file as crisp SVG.
</p>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col px-10 py-8" style="background: var(--ff-cream);">

<div class="text-center mb-3">
<div class="fl-eyebrow">Live embed · tldraw</div>
<h2 style="font-size: 1.9rem;">Or a tldraw whiteboard.</h2>
</div>

<div style="flex: 1; border-radius: 14px; overflow: hidden; border: 2px solid rgba(15,23,42,0.1); box-shadow: 0 12px 30px -12px rgba(15,23,42,0.25);">
<iframe src="https://www.tldraw.com" style="width: 100%; height: 100%; border: 0;"></iframe>
</div>

<p style="font-size: 0.85rem; color: #64748b; margin-top: 0.6rem; text-align: center;">
Live whiteboarding for workshops. (If this panel is blank, tldraw is blocking the embed — use the <code>slidev-addon-tldraw</code> addon instead, which renders inline.)
</p>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<script setup lang="ts">
import { ref } from 'vue'
const answered = ref(false)
const picked = ref('')
const tallyT = ref(38)
const tallyF = ref(124)
function pick(ans: string) {
  if (answered.value) return
  picked.value = ans
  answered.value = true
  if (ans === 'T') tallyT.value++; else tallyF.value++
}
</script>

<div class="fl-eyebrow">Reactive quiz · Hannah's pop-quiz hook</div>

<h2 style="font-size: 2rem; max-width: 50rem; text-align: center; margin-bottom: 0.5rem;">
A 1560 SAT is your child's <span class="fl-cyan">strongest</span> BS/MD asset.
</h2>
<p style="color: #64748b; margin-bottom: 1.5rem;">True or false? Click one.</p>

<div class="flex gap-6">
<button class="fl-quiz-btn" :class="{ 'fl-quiz-wrong': answered && picked==='T', 'opacity-50': answered && picked!=='T' }" @click="pick('T')">TRUE</button>
<button class="fl-quiz-btn" :class="{ 'fl-quiz-correct': answered && picked==='F', 'opacity-50': answered && picked!=='F' }" @click="pick('F')">FALSE</button>
</div>

<div v-if="answered" class="mt-8 text-center" style="max-width: 40rem;">
<p style="font-size: 1.15rem; font-weight: 600;">
<span v-if="picked==='F'" class="fl-green">Correct.</span>
<span v-else class="fl-orange">Not quite.</span>
Most NJMS applicants now score above 1500 — the score is the entry fee, not the asset.
</p>
<div class="flex gap-8 justify-center mt-4" style="font-family: monospace; color: #475569;">
<div>TRUE: {{ tallyT }}</div>
<div>FALSE: {{ tallyF }}</div>
</div>
<p style="font-size:0.8rem; color:#94a3b8; margin-top:0.5rem;">Self-contained reactive widget — no server. (For real audience polling, see the interaction slide.)</p>
</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream); overflow: hidden;">

<script setup lang="ts">
import { ref } from 'vue'
const floats = ref<{ id: number, emoji: string, left: number }[]>([])
let id = 0
function react(emoji: string) {
  const left = 30 + Math.random() * 40
  const fid = id++
  floats.value.push({ id: fid, emoji, left })
  setTimeout(() => { floats.value = floats.value.filter(f => f.id !== fid) }, 2200)
}
</script>

<div class="fl-eyebrow">Reactions</div>
<h2 style="font-size: 2rem; margin-bottom: 0.5rem;">Tap a reaction. Watch it float.</h2>
<p style="color:#64748b; margin-bottom: 2rem; max-width: 40rem; text-align:center;">This is the self-contained version. The live-audience version streams taps from everyone's phones onto your screen.</p>

<div class="flex gap-8">
<span class="fl-react-btn" @click="react('🔥')">🔥</span>
<span class="fl-react-btn" @click="react('❤️')">❤️</span>
<span class="fl-react-btn" @click="react('👏')">👏</span>
<span class="fl-react-btn" @click="react('🤯')">🤯</span>
<span class="fl-react-btn" @click="react('💰')">💰</span>
</div>

<div v-for="f in floats" :key="f.id" class="fl-float" :style="{ left: f.left + '%' }">{{ f.emoji }}</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 fl-navy-bg flex flex-col justify-center px-16">

<div class="fl-bar"></div>

<div class="max-w-5xl mx-auto w-full">

<div class="fl-eyebrow" style="color: var(--ff-orange);">The question you actually asked</div>
<h2 style="font-size: 2.2rem; color: white; margin-bottom: 1.5rem;">How does audience interaction work?</h2>

<div class="grid grid-cols-2 gap-5">

<div class="fl-card">
<span class="fl-tag" style="background: var(--ff-cyan);">Live polls / quizzes / reactions</span>
<p style="margin-top: 0.75rem; font-size: 0.98rem; color: #334155; line-height: 1.5;">
You run the deck on a <strong>server</strong> (not static). A slide shows a <strong>QR / short URL</strong>. The audience opens it on their phones, taps answers, and their responses <strong>stream back onto your screen live</strong>. Needs <code>slidev-polls</code> / <code>slidev-addon-slide-quiz</code> / <code>-reaction</code> running on a host.
</p>
</div>

<div class="fl-card">
<span class="fl-tag" style="background: var(--ff-green);">Recorded / one-way (YouTube, webinar)</span>
<p style="margin-top: 0.75rem; font-size: 0.98rem; color: #334155; line-height: 1.5;">
No phones needed. Two options: <strong>(a)</strong> self-contained reactive widgets <em>you</em> click (like the quiz + reactions you just used), or <strong>(b)</strong> the platform chat — slides prompt <em>"type T or F in the chat"</em> and you read it out. This is Hannah's model.
</p>
</div>

</div>

<p style="color: rgba(255,255,255,0.8); font-size: 1.05rem; margin-top: 1.5rem; text-align:center;">
Short version: <span class="fl-cyan">live = phones + a running server</span>. <span class="fl-green">Recorded = reactive widgets or the chat.</span> For our webinars we use the chat; for YouTube + courses we use widgets.
</p>

</div>

</div>

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="fl-eyebrow">What's live here vs what needs a server</div>

<div class="fl-card" style="max-width: 52rem; width: 100%;">

<div class="grid grid-cols-2 gap-x-8 gap-y-2" style="font-size: 1rem;">
<div>✅ Mermaid diagrams</div><div style="color:#64748b;">static, exports clean</div>
<div>✅ Charts (Chart.js)</div><div style="color:#64748b;">static; can fetch live data</div>
<div>✅ Live Excalidraw / tldraw</div><div style="color:#64748b;">iframe embed</div>
<div>✅ Reactive quiz + reactions</div><div style="color:#64748b;">self-contained Vue</div>
<div>✅ Self-running narration</div><div style="color:#64748b;">Web Speech / ElevenLabs MP3</div>
<div>✅ Pen / drawing</div><div style="color:#64748b;">built-in (pencil icon)</div>
<div>⚙️ Live audience polls</div><div style="color:#64748b;">needs running server</div>
<div>⚙️ Multi-viewer sync</div><div style="color:#64748b;">needs running server</div>
</div>

</div>

<p style="font-size: 1rem; color: #475569; margin-top: 1.5rem; max-width: 42rem; text-align:center;">
Everything with ✅ works on a plain Vercel deploy like this one. Only true live-audience features need the dev server running.
</p>

</div>

---
layout: cover
---

<div class="absolute inset-0 fl-navy-bg flex flex-col justify-center items-center px-16">

<div class="fl-bar"></div>

<div class="text-center max-w-3xl">
<div class="fl-eyebrow" style="color: var(--ff-orange);">Feature Lab</div>
<h1 style="font-size: 3rem; color: white;">All of it. <span class="fl-cyan">One markdown file.</span></h1>
<p style="font-size: 1.1rem; color: rgba(255,255,255,0.8); margin-top: 1.25rem;">
Webinars, courses, YouTube, portal walkthroughs, live client reports. Same engine, infinite range.
</p>
</div>

<div class="absolute bottom-6 left-0 right-0 text-center" style="color: rgba(255,255,255,0.35); font-size: 0.7rem; letter-spacing: 0.2em;">
FUNNEL FUTURIST · SLIDEV FEATURE LAB
</div>

</div>
