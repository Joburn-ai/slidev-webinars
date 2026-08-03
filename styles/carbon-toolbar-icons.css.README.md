
---

## 🔴 THE INVISIBLE-RENDER LAW (locked 2026-08-03, after the toolbar shipped blank FOUR times)

**Applies to every slide deck, every SAGE VSL, every webinar, every 400-slide-hack build, and
every diagram we program directly into Slidev.**

### What happened
`styles/carbon-toolbar-icons.css` set **only** `mask-image`. A mask icon is painted by masking
the element's **background**, so with no `width`, `height` or `background-color` every icon
computed to `0x0` and `transparent`. **All 50 masks were correct and all 50 were invisible.**

### Why it survived three previous fixes
**Because the documented verification was wrong.** It asserted `maskImage !== 'none'` -- the one
property that was never broken. It passed every time, on a completely blank toolbar. The
operator reported "10/10 icons resolving" on a deck John could see was blank.

> ### THE LAW
> **Verify the property that determines VISIBILITY, not the property you changed.**
>
> For anything mask-based that means **area AND a non-transparent paint source AND the mask.**
> For anything rendered at runtime it means **look at the rendered pixels.**

### Two failure modes this generalises to, both hit on the same deck
1. **Mask-based icons** -- valid asset, zero box, no paint source. Invisible.
2. **Runtime-rendered diagrams** (inline Mermaid) -- Slidev creates `<div class="mermaid"></div>`
   and the renderer never fills it. **No console error, no failed request, valid source.** The
   slide looks finished in the markdown and is empty on screen.

### 🔴 SO: ANY DIAGRAM PROGRAMMED DIRECTLY INTO SLIDEV MUST BE SCREENSHOT-VERIFIED
**John asked whether an inline chart is unverifiable because you cannot see it. It is NOT
unverifiable -- Playwright can screenshot it, and that is exactly what must happen.** The
failure was never a missing capability; it was skipping the visual check.

**Required before any deck with diagrams ships:**
```
1. Build and serve (or deploy) the deck.
2. For EVERY diagram slide, navigate to it and screenshot it.
   Slidev keeps all slides mounted, so `document.querySelector('.slidev-layout')` returns
   SLIDE 1, not the active one. Select the visible slide:
     [...document.querySelectorAll('.slidev-layout')]
       .find(e => e.offsetParent !== null && e.getBoundingClientRect().width > 100)
3. Assert the diagram actually produced geometry, not just a container:
     el.querySelectorAll('svg .node').length > 0        // Mermaid rendered nodes
   An empty `<div class="mermaid"></div>` is the tell.
4. LOOK AT THE SCREENSHOT. Overlapping nodes, clipped labels, a connector routed through a
   box and a caption sitting on a shape are all invisible to a DOM assertion.
```

**Preferred delivery for our decks: author in Mermaid, render with the Mermaid CLI, embed the
PNG.** Not because inline cannot be verified, but because pre-rendering means every diagram is
looked at by construction, the aspect ratio is ours to choose, and the deck cannot lose its
diagrams to a version bump. Inline stays legal **only with the screenshot pass above.**

### The toolbar check that actually works
```js
// Slidev's toolbar is opacity-0 until hover. Force it visible or you screenshot nothing.
const bar = [...document.querySelectorAll('div')].find(d =>
  /absolute bottom-0 left-0/.test(d.className.toString()) &&
  d.querySelectorAll('[class*="i-carbon"]').length >= 4);
bar.style.opacity = '1';

const icons = [...document.querySelectorAll('[class*="i-carbon"]')]
  .filter(e => e.offsetParent !== null);        // skip icons inside closed modals
const broken = icons.filter(e => {
  const s = getComputedStyle(e), r = e.getBoundingClientRect();
  const mask = s.maskImage !== 'none' ? s.maskImage : s.webkitMaskImage;
  const painted = !/rgba\(0,\s*0,\s*0,\s*0\)|transparent/.test(s.backgroundColor);
  return !(r.width > 0 && r.height > 0 && painted && mask && mask !== 'none');
});
// broken.length must be 0. Expect 8 visible on a normal slide.
```
