---
theme: default
title: Miro × Slidev — Live Embed
colorSchema: light
highlighter: shiki
transition: slide-left
fonts:
  sans: Inter
  mono: JetBrains Mono
layout: cover
---

# Miro × Slidev

Live, pannable Miro boards — dropped straight into any deck.

<div class="text-sm opacity-60 mt-4 font-mono">No API key. No MCP. Just a shared board link.</div>

---

## How to use it (one line)

The global `<Miro>` component lives in `components/Miro.vue` — auto-available in **every** deck.

```md
<Miro board="uXjVGAJoXLw=" />
```

Or paste the full board URL — it parses the ID for you:

```md
<Miro board="https://miro.com/app/board/uXjVGAJoXLw=/" title="The Bowtie" />
```

Options: `mode` (`view_only_without_ui` · `view_only` · `edit`) · `aspect` (`16 / 9`) · `moveToWidget` (focus one frame).

---
layout: center
---

## Live board

<Miro board="uXjVGAJoXLw=" title="Demo board" />

<div class="text-xs opacity-50 mt-3 text-center font-mono">
If this shows a "private board" screen, the board isn't shared yet — see the next slide.
</div>

---

## Setup — 30 seconds, no credentials

**To embed a board (all you need):**
1. Open the board in Miro → **Share** (top right).
2. Set access to **"Anyone with the link"** → *Can view*.
3. Copy the link → drop the ID into `<Miro board="..." />`. Done.

**Optional — programmatic control** (only if you want Claude to *read/build* boards):
- Get a token at **miro.com → your app in Developer settings → "Install app and get OAuth token."**
- Drop it in `.env` as `MIRO_ACCESS_TOKEN`. *Not needed for embedding.*

<div class="text-sm opacity-60 mt-6 font-mono">Run this deck:  pnpm exec slidev _demo/miro_embed_2026_06_17/slides.md --open</div>
