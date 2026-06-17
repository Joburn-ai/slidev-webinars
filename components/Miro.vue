<script setup>
// Reusable Miro live-embed for any Slidev deck.
// Usage:  <Miro board="uXjVGAJoXLw=" />
//         <Miro board="https://miro.com/app/board/uXjVGAJoXLw=/" title="The Bowtie" />
//         <Miro board="uXjVGAJoXLw=" moveToWidget="3458764..." aspect="16 / 10" />
// The board must be shared "anyone with the link" for it to render. No API key needed.
import { computed } from 'vue'

const props = defineProps({
  board:        { type: String, required: true },   // board id OR full miro url
  title:        { type: String, default: 'Miro board' },
  // view_only_without_ui = cleanest for slides; view_only keeps Miro's chrome; edit = interactive
  mode:         { type: String, default: 'view_only_without_ui' },
  aspect:       { type: String, default: '16 / 9' },
  moveToWidget: { type: String, default: '' },        // optional: focus a specific frame/widget id
})

const boardId = computed(() => {
  const m = String(props.board).match(/board\/([^/?#]+)/)
  return m ? m[1] : props.board
})

const src = computed(() => {
  const p = new URLSearchParams({ embedMode: props.mode })
  if (props.moveToWidget) p.set('moveToWidget', props.moveToWidget)
  return `https://miro.com/app/live-embed/${boardId.value}/?${p.toString()}`
})
</script>

<template>
  <div class="miro-embed" :style="{ aspectRatio: aspect }">
    <iframe
      :src="src"
      :title="title"
      frameborder="0"
      scrolling="no"
      allow="fullscreen; clipboard-read; clipboard-write"
      allowfullscreen
    />
    <!-- atomic-era registration ticks -->
    <span class="t tl" /><span class="t tr" /><span class="t bl" /><span class="t br" />
  </div>
</template>

<style scoped>
.miro-embed {
  position: relative;
  width: 100%;
  max-height: 78vh;
  margin: 0 auto;
  background: #0e1c2b;
  border: 1px solid rgba(181, 133, 42, 0.42);
  box-shadow: 0 10px 40px rgba(14, 28, 43, 0.18);
}
.miro-embed iframe { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
.miro-embed .t { position: absolute; width: 14px; height: 14px; border: 1.5px solid #B5852A; z-index: 2; pointer-events: none; }
.miro-embed .tl { top: -1px; left: -1px; border-right: 0; border-bottom: 0; }
.miro-embed .tr { top: -1px; right: -1px; border-left: 0; border-bottom: 0; }
.miro-embed .bl { bottom: -1px; left: -1px; border-right: 0; border-top: 0; }
.miro-embed .br { bottom: -1px; right: -1px; border-left: 0; border-top: 0; }
</style>
