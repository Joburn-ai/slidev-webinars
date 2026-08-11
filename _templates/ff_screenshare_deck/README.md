# FF SCREEN-SHARE DECK — the approved template

**Use this for any VSL, training or walkthrough John records by screen-sharing a deck.**
Proven on the Constraint Roadmap VSL: 106 slides, 86% of slides carrying a real visual,
live at **roadmap-vsl-v8.vercel.app**. John, 2026-08-11: *"this is much much much much better."*

## Start a new deck

```bash
cp -r _templates/ff_screenshare_deck <lane>/<deck_name>
# style.css already imports the frozen system; add only deck-specific rules under it
npx slidev <lane>/<deck_name>/slides.md --port 31xx
```

## The register

**Indirect training, not a talking-head support deck.** It should read like someone showing you
their actual working surface. John: *"for most people they would do talking head, but for us we're
gonna make it almost an indirect training in a way."*

## The five rules that make it work

**1. 🔴 A visual on every slide — the target is ≥85%, and the gate is ≤5% bare.**
Measured from our own Fladlien swipe: 4.2 image objects per page, 2% of pages bare.
**But the rule is FRAME, not IMAGE** — `roadmap_thesis` ships ONE image across 145 slides and reads
finished, because every slide is a framed card, a lit stat or a contrast block. What fails is an
unframed sentence floating on a ground.

**2. Fast pace: 12–18 spoken words per slide.** More slides, fewer words each. A ≤7-word headline.

**3. 🔴 Motion is a KEYSTROKE, and that changes the rule.** In a screen share every click is
something John must hit on beat while reading. A late click needs a jump cut; a slide change trims
clean. **So: new slide wherever content REPLACES content. v-clicks ONLY where content ACCUMULATES.**
Cap total interactions near one per slide. The approved deck runs ~37 clicks across 106 slides.

**4. Write the `_VISUAL_MAP` BEFORE the slides.** One row per slide: spoken line · ≤7-word headline ·
treatment · exact asset path or `NEW:` · tempo · click count. Alternate treatments, never the same
three in a row, alternate image left/right. **This table is the difference between a deck that reads
finished and one that reads improvised.**

**5. Gather before you generate.** `ls -R public/` first. Real screenshots and real photos outrank
generated art every time. Pass the FF palette IN to any generator — its house fallback is a doc
green that creates a competing brand.

## Before it ships
- **Render every slide and LOOK at the screenshots.** Assertions have passed over a clipped
  headline, a painted checkerboard and a half-empty frame — three times in one day.
- **Deploy check:** Slidev emits Netlify `_redirects`, NOT a Vercel rewrite. Copy `vercel.json` into
  the build output or every deep link 404s while still rendering. And register the URL as a project
  **domain**, not just an alias, or `all_except_custom_domains` SSO puts it behind auth.
