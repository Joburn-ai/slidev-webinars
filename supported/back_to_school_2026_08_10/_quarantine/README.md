# QUARANTINE — do not put these back in the deck

## joe-conf.AI-GENERATED.png

🔴 **This is an AI-generated image of a real person.** It was live on the deck's authority
slide (Section 3, "I am Dr. Joe Sebestyen") presented as a photograph of him speaking at a
conference.

Evidence, measured 2026-08-15:

| Check | Result |
|---|---|
| XMP `DigitalSourceType` | `http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia` |
| XMP `Credit` | `Google AI` |
| Visible watermark | Google Gemini four-point sparkle, bottom-right corner |

`trainedAlgorithmicMedia` is the IPTC standard value meaning the asset was created by a
generative model.

**Why it cannot ship:** it fabricates a real, named person at a named event ("GLOBAL
INNOVATION SUMMIT"), on the one slide whose entire job is establishing that he is credible.
If a single parent reverse-images it or spots the sparkle, the proof stack collapses at
exactly the moment it matters most.

**What to do instead:** use a real photograph. `public/images/dr-joe.jpg` is a genuine
headshot and carries no AI provenance markers. If a stage/teaching shot is wanted, get a
real one from Joe.

`scripts/deck_gate.py` now fails the build on any image carrying AI-provenance metadata.

---

## 🔴 Why this folder is NOT under public/

It was, briefly. Slidev copies everything in `public/` into `dist/`, so the quarantined
AI-generated photo was being published to the deployed site — reachable by URL, on the
public web, still carrying its Gemini watermark and its `trainedAlgorithmicMedia` XMP.

Caught 2026-08-15 by listing `dist/` before the first Vercel deploy.

**Quarantine means removed from the build, not renamed inside it.** Anything in here stays
outside `public/`.

---

## reviews_band_456.png

🔴 **Removed 2026-08-16. We cannot 100% stand behind the number.**

John: *"I would take out the 456 reviews because I don't know if that's true. We have pages
with a ton of testimonials, testimonial stacks for days, right? But let's make sure we just
have that kind of stuff... anything we can't 100% stand by."*

The crop was compliant (rating band only, no names) but the NUMBER itself was lifted from a
Senja widget screenshot and never verified against the live review count. There genuinely
are many testimonials; nobody has counted them.

**To bring a review count back:** count them, screenshot the source with a date, and record
where the number came from. A precise number we cannot defend is worse than no number.
