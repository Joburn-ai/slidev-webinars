# How To Tell Which Kind Of Care Home Actually Fits Her — walkthrough deck

**The belief asset in the show-up system.** Singh records voice over these slides. About 9 minutes.

| | |
|---|---|
| **Live deck** | https://ecf-walkthrough.vercel.app |
| **Google Slides** | https://docs.google.com/presentation/d/1S8Zlg8060EdNSA2s2NwwjAesqcppXpSZG0yeZNu4Lms/edit |
| **PDF** | `ecf_walkthrough.pdf` (51 pages) |
| **Script, source of truth** | `06_Clients/easycarefinder/02_funnels_and_copy/show_up_system_2026_08_13.md` §5.2 |
| **Per-slide plan** | `_VISUAL_MAP.md` |
| **QC vs goldens** | `_QC_GOLDEN_COMPARISON.md` |

## 🔴 The slides are NOT the script

The deck carries about **two words of visible copy per slide**, on purpose: one idea, seven words
maximum. **The 1,759-word script lives in the speaker notes.** There is nothing to read off the
slide face itself.

Three ways to get the script while recording, whichever suits:

| | |
|---|---|
| **Live deck, presenter mode** | https://ecf-walkthrough.vercel.app/presenter/1 — current slide, next slide, and the notes |
| **Google Slides** | View, then Presenter view. The same notes are in there. |
| **The read-along script** | A document: slide number, what is on screen, the exact line. Built for the realistic setup, which is the deck on one screen and this on a phone. |

Do not improvise, and specifically **do not improvise a number.**

## Rebuild
```bash
cd /root/slidev-webinars/easycarefinder/walkthrough_2026_08_17
npx slidev build slides.md --base / --out dist      # must run from THIS directory
npx slidev export slides.md --output ecf_walkthrough --format pdf --dark false
```

## 🔴 Blocking before he records
1. **A real photograph of Singh** in the doorway of a home he owns, for `cl-02`. It currently ships a
   labelled placeholder. **A generated stand-in for a real person is never acceptable.**
2. **Attorney-cleared ownership and fee disclosure wording** before `cl-04` is recorded. It is on
   camera where it cannot be adjusted per family.
3. **No count of homes** is said anywhere, pending a fresh CCLD pull. Keep it that way until it is
   re-pulled, or the video needs re-recording and it will not be.
