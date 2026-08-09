---
theme: default
title: Roadmap VSL v7
info: |
  Funnel Futurist Roadmap VSL, v7. FINAL.

  🔴 THE ONE TEST. This asset does not sell. Its only job is to get a stranger to fill in
  ONE FORM. Any change that makes it better at SELLING and no better at GETTING THE FORM
  FILLED is a regression, however good it looks. (John, 2026-08-09.)

  🔴 THE SECOND TEST, from the transcript sweep and missing from every rulings file:
  "the roadmap VSL points to just getting as many people as possible to complete the
  roadmap. That's like four or five minutes long." (strategy_2026_07_28.)
  v7 is a CUT, not an addition: 64 slides against v6's ~120, one idea per frame.

  🔴 JOHN, ONE DECISION NEEDED AND IT IS THE ONLY OPEN ONE. The script as approved is
  852 spoken words, which is 5.2 min at a fast 165 wpm and 6.1 min at a natural 140.
  The spec says four to five. I did not cut your words to hit it, because you also said
  "I want the ENTIRE script verbatim, every single bit." Both cannot be true at once.
  The cheapest 60-90 seconds, in the order I would cut them, all self-contained beats:
    - 29/30 (the process, then the four "their" cards)          ~18 sec
    - 38 (the hard part isn't drawing a path)                    ~6 sec
    - 45 or 46 (they say the same thing twice, keep one)         ~5 sec
    - 58 (yours to keep regardless -- 57 already said it)        ~6 sec
    - 59/60/61 (the follow-ups + the invite + the proposal)     ~17 sec
    - 2 or 3 (keep the wall OR the receipts, not both)          ~8 sec
  Say the word and it is a ten-minute edit. Nothing else in the deck is blocked on this.

  FUNNEL POSITION: cold traffic, front door, first thing they ever see. The SAGE VSL comes
  AFTER, once they are inside (book-a-call thank-you page / YouTube / inside the roadmap).
  So: never introduce the Roadmap Funnel here, never compare alternatives, never do DIY.

  DESIGN: nothing in this deck is invented. The system is lifted from
    internal/roadmap_thesis_2026_08_03  (the .rt-* spine, 145 slides live)
    bradley_pounds/evergreen_60programs_2026_07  (HERO-BLEED, the image system)
    internal/sage_vsl_training_2026_08_01  (contained figure on white, text in notes)
    audit-hub/.../rockstar-organizers  (mark the proof up)
  John 2026-08-09: "there's a deck that's already built and I don't want to fuck with the
  design. We have the ability in the process to do this. Let's just get this done."

  Stylesheet: style_v7.css. Rename it over style.css to build.
class: peak
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  persist: false
transition: none
mdc: true
fonts:
  provider: none
layout: default
---

<!--
================================================================================
 THE VISUAL MAP. Written BEFORE the slides, which is the whole difference between
 this and v6. Brad's deck has one row per slide with a locked treatment legend and
 every image was specified before it was made. v6 had good primitives and no map,
 so images were chosen after the copy and dropped wherever there was room.

 CLOSED TREATMENT LEGEND -- eight names, and every slide is exactly one of them:
   A1 PORTRAIT-DUO   two real headshots, framed as people. Slide 1 only.
   A2 PEAK           dark ground, one line, nothing else. BUDGET 6. Used: 01 05 21 28 36 64
   A3 STATEMENT      white, centred, one idea, <= 12 visible words. The workhorse.
   A3b LEDGER        white, LEFT aligned, headline + qualifier. Breaks a run of centres.
   A4 SPLIT          copy one side, visual the other. ALTERNATES L/R, never 3 the same way.
   A5 HERO-BLEED     photograph fills the frame, scrim under the type. Alternates copy side.
   A6 MARKED PROOF   a real screenshot with numbered rings + a numbered key on v-clicks.
   A7 PROOF WALL     a grid of tiles revealed fast. Density is the argument, nothing read aloud.
   A8 FIGURE         a flow/diagram on a white card, or full-bleed contained with no text.

 COLOUR GRAMMAR, enforced: teal = the path that works. ember = the restart, the failure.
 gold = a gate, an order, a sequence. Ember on anything that is not a failure breaks the deck.
 (v6 put an ember arrow next to John's own name on slide 1. That is the failure colour
 pointing at the founder.)

 ─────────────────────────────────────────────────────────────────────────────
 id   beat  treatment    headline (<= 7 visible words)          asset                          side
 ─────────────────────────────────────────────────────────────────────────────
 01   1     A1 + A2      Yo, what's going on?                   team/john + team/phoenix        R
 02   2     A7           Three years. A small handful.          4 stage/team photos             --
 03   3     A8           Numbers shown, not summarised.         site/ff-proof-index (BAND)      --
 04   4     A3           But you're not really here for that.   --                              --
 05   5     A2           The one thing holding you back.        --                              --
 06   6     A3           Four minutes. Then a few more.         teal rule                       --
 07   7     A5           I talk to owners constantly.           stage/cc_live_600s              L
 08   8     A3           Doing their absolute best.             --                              --
 09   9     A3           Buried under conflicting advice.       --                              --
 10   10    A4           Everyone has an opinion.               gen/concept-06                  R
 11   11    A4 flip      Your business into their model.        gen/concept-04                  L
 12   12    A7 cards     Meanwhile everyone is shouting.        4 ember cards                   --
 13   13    A4           Everyone racing to the bottom.         gen/concept-07                  R
 14   14    A3           Things that worked might be breaking.  --                              --
 15   15    A4 flip      The sequence trap.                     gen/concept-01                  L
 16   16    A8           Disconnected moves.                    flows/01a_pieces_disconnected   --
 17   17    A7 cards     Not because you did it wrong.          3 neutral cards                 --
 18   18    A3           It wasn't the first piece.             --                              --
 19   19    A7 cards     So you find out too late.              2 ember cards                   --
 20   20    A3           The same question as last January.     --                              --
 21   21    A2           "How do I fix this?"                   --                              --
 22   22    A7 cards     One size fits all.                     3 ember cards                   --
 23   23    A3           Does it work for YOUR business?        --                              --
 24   24    A3           Or were you just financially qualified?--                              --
 25   25    A4 flip      Nobody gives you the ORDER.            gen/concept-03                  L
 26   26    A7 cards     Attention. Leads. Capture. Conversion. 5 neutral cards                 --
 27   27    A4           Which one do you fix FIRST?            gen/concept-09                  R
 28   28    A2           A roadmap that was YOURS.              --                              --
 29   29    A3           Everybody gave you a process.          --                              --
 30   30    A7 cards     Handed over like it would transfer.    4 neutral cards                 --
 31   31    A7 cards     Nobody checked your market.            5 ember cards                   --
 32   32    A4           Cheap leads. Nobody showing up.        2 cards (no image)              R
 33   33    A3b          When her buyers could take a call.     1 wide ember card               --
 34   34    A4 flip      We changed one thing.                  1 teal card                     L
 35   35    A3           It fell over. Then she won it back.    proofcard                       --
 36   36    A2           It just wasn't built for them.         --                              --
 37   37    A3           The model sells everyone.              --                              --
 38   38    A3b          Anyone can draw a path.                --                              --
 39   39    A3           Where you actually are right now.      --                              --
 40   40    A4 flip      If you don't know where you are.       gen/concept-02                  L
 41   41    A3b          Not from inside your own business.     --                              --
 42   42    A7 cards     Not another ad. Not another funnel.    3 ember cards                   --
 43   43    A8           From where you are to where you go.    flows/01b_pieces_connected      --
 44   44    A7 cards     And the steps between, in order.       3 cards, third teal             --
 45   45    A3           Simple things, stacked in order.       --                              --
 46   46    A3           Nothing clever. Nothing complicated.   --                              --
 47   47    A7 proof     This is what it looks like.            3 verbatim proofcards           --
 48   48    A4 flip      Same sequence.                         gen/concept-08                  L
 49   49    A3           So here's what I want to do.           teal rule                       --
 50   50    A3           Everything you need to decide.         --                              --
 51   51    A3b          Including the options that aren't us.  1 teal card                     --
 52   52-54 A7 cards     Three steps.                           3 cards on 3 clicks             --
 53   55    A3           You don't have time. That's the reason.--                              --
 54   56    A3b          You've already paid for it.            --                              --
 55   57    A6           The form IS step one.                  site/roadmap-subdomain-step1    L
 56   58    A8           One call. The whole journey.           flows/03a_bowtie_state1           --
 57   59    A3           A thirty, sixty, ninety day plan.      --                              --
 58   60    A3b          Yours to keep regardless.              --                              --
 59   61    A4 flip      A form can only tell us so much.       sticky                          L
 60   62    A3           We might invite you to a next step.    --                              --
 61   63    A3b          Built around your situation.           1 teal card                     --
 62   64    A3           Real clarity, either way.              --                              --
 63   65    A5           The business starts serving you.       team/john-red-carpet            R
 64   66    A2 + A6      Answer the questions below.            site/ff-roadmap-typeform-embed  --
 ─────────────────────────────────────────────────────────────────────────────

 🔴 ASSET QUARANTINE, all verified on disk 2026-08-09. Do not reintroduce any of these.
   public/gen/char-0*.png            PIL mode=RGB. The model painted a checkerboard as
                                     PIXELS. No alpha. John: "This image is brutal."
                                     BANNED until re-cut and verified RGBA-with-transparency.
   public/proof/01_wins_wall.png     renders "92+ sales ... beat its $15K target" plus four
                                     client and team names, legibly. Income claim. DROPPED.
                                     Not blurred -- dropped. Blur proves nothing.
   stage/john-coburn-our-system-for-writing-daily-high-.jpg
                                     the slide behind John reads "$120-180k/m w/ email" and
                                     "about $2.39M in the last ~12 months". Income claim. DROPPED.
   site/ff-home--hero.png            "$1.81M" "$648,022" in the hero tiles. Only legal cropped
   site/ff-proof-index--hero.png     "$648,022" "$630,071" "Over $1.2M tracked" "$1.81M".
   site/ff-case-file-00*--hero.png   "$648,022" / "$1.81M" in the H1 itself.
                                     -> ff-proof-index is used ONCE, inside .rt-band, which
                                        crops to the top 32% and stops above every figure.
                                        Verify on the RENDER at 1600x900, never in markup.
   site/ff-roadmap-form-page--full.png  renders as an empty box. The Typeform is cross-origin
                                     and does not composite into a full-page capture.
                                     Use ff-roadmap-typeform-embed.png instead.
   team/john-mountain-overlook.jpg   EXIF orientation 8, team/john-muaythai-kick.jpg EXIF 6.
                                     Browsers honour EXIF, our tooling does not. Not worth the
                                     risk on a recorded asset. Unused.
   .rt-blur                          DELETED from the stylesheet on purpose.
                                     John: "Everything's blurred out. What is happening?"

 🔴 SPEAKER NOTES ARE THE SCRIPT. John's words are in the notes, verbatim, on every slide,
   because he is recording over these. <= 12 words on the frame. Pasting the spoken sentence
   INTO a headline is what broke v6's layout. When a line must be readable on screen it is
   .rt-say (1.95rem / 34ch), which is the fourth type tier that exists for exactly that.
================================================================================
-->

<!-- slide:v7-01 -->

<div class="rt-split">
<div>

<div class="rt-kicker">FUNNEL FUTURIST</div>
<div class="rt-h1">Yo, what's going on?</div>
<div class="rt-say mt-8">I'm John. My partner's Phoenix Bohannon.</div>

</div>

<div class="rt-visual">
<div class="rt-duo">
  <div>
    <img src="/team/john-headshot.png" alt="John Coburn" class="rt-portrait" />
    <div class="rt-name">John</div>
    <div class="rt-role">Funnel Futurist</div>
  </div>
  <div>
    <img src="/team/phoenix-headshot.png" alt="Phoenix Bohannon" class="rt-portrait" />
    <div class="rt-name">Phoenix</div>
    <div class="rt-role">Partner</div>
  </div>
</div>
</div>
</div>

<!--
HOOK: two names and two faces, said casually, in under three seconds. No production, no claim.
BEATS:
  - Yo, what's going on? I'm John, my partner's Phoenix Bohannon.
TIMING: 4 sec
TRANSITION: do not pause on this. Straight into who we work with.

🔴 JOHN 2026-08-09, VERBATIM, ALL BINDING ON THIS SLIDE:
   "The images on slide one don't make sense. It should be like images of us.
    I'm John left side, Phoenix is on the right side."
   So: John LEFT, Phoenix RIGHT, in that order, always. NO arrow device (v6 drew an ember
   arrow at John's own name, which is the failure colour pointing at the founder and breaks
   the deck's colour grammar). NO stage-talk photos here. NO cutout.
   Both files verified RGBA with real alpha on 2026-08-09, pulled from the live site.
   Do NOT substitute /gen/char-*.png. They have no alpha channel.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-02 -->

<div class="rt-kicker">OVER THE LAST THREE YEARS</div>
<div class="rt-h2">A small handful of clients.</div>

<div class="rt-grid c4 mt-8">
<v-clicks>
<img src="/stage/cc_live_600s.jpg" alt="John presenting a customer journey model on stage" class="rt-shot wall" />
<img src="/stage/day-2-email-marketing-john-coburn.jpg" alt="John speaking at Clients and Community Live" class="rt-shot wall" />
<img src="/stage/12-customer-journey-key-moments-john-coburn-10.jpg" alt="The Clients and Community Live stage" class="rt-shot wall" />
<img src="/team/john-red-carpet.jpg" alt="John and Phoenix at an industry event" class="rt-shot wall" />
</v-clicks>
</div>

<div class="rt-say mt-8" v-click>Five thousand a month, up to six hundred thousand plus.</div>

<div class="rt-foot"><div class="rt-fine">Describes the size of businesses we have worked with. Not a claim about results we produced, and not an offer.</div></div>

<!--
HOOK: four frames in three seconds. Density is the argument and none of it gets read aloud.
BEATS:
  - Three years, a small handful of clients. Five thousand a month up to six hundred thousand plus.
TIMING: 9 sec
TRANSITION: they now expect the case studies. Give them one beat of it, then take it away.

VERBATIM 08-09: "from around 3K a month all the way to 50, 60, 100K a month plus, like 5K all
  the way through to 600K per month plus, that's true."
CLAIM LOCK: the range describes CLIENT SIZE. It is not a claim about what we produced, and the
  standing footer says so on the frame.
🔴 The fourth tile in v6 (john-coburn-our-system...jpg) is DROPPED: the slide behind John in
  that photo reads "$120-180k/m w/ email" and "about $2.39M in the last ~12 months", legibly.
  Zero income claims means zero, including ones sitting in the background of a photograph.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-03 -->

<div class="rt-kicker">IF YOU WANT THE RECEIPTS</div>
<div class="rt-h2">Numbers shown, not summarised.</div>

<div class="rt-band crest mt-8">
  <img src="/site/ff-proof-index--hero.png" alt="The Funnel Futurist proof page" />
</div>

<div class="rt-sticky mt-8 max-w-md" v-click>and exactly how we counted</div>

<!--
HOOK: point at the proof, do not perform it. The whole beat exists so beat 4 can take it away.
BEATS:
  - I could take some time here and show you we've got a couple of really strong case studies,
    a lot more underway, and a ton of other proof.
TIMING: 8 sec
TRANSITION: hard cut. Say "but" before the next slide lands.
LAYOUT NOTE: this was a split until the render was looked at. In a half-width column the band
  is a 140px strip and reads as an accident. Full width it reads as a page. That is the whole
  lesson of "nothing floats" -- an image is either the frame, or half of a split at a size
  where it can be read. There is no third state.

🔴 "CASE FILES" IS CUT. John 08-09: "I don't like case files. I don't know why we went back to
   case files." They are CASE STUDIES. The word does not appear anywhere in this deck.
🔴 WHY .rt-band AND NOT THE FULL SCREENSHOT: ff-proof-index--hero renders "$648,022",
   "$630,071", "Over $1.2M tracked" and "$1.81M" at full size below the fold of this crop.
   .rt-band stops at the top 32%, above every figure. VERIFY THIS ON THE RENDER at 1600x900
   before shipping -- the 2026-08-09 render is exactly how the last set of leaks was found.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-04 -->

<div class="rt-h1">But you're not really here for that.</div>

<!--
HOOK: take the proof away one second after offering it. That is the whole move.
BEATS:
  - But you're not really here for that.
TIMING: 3 sec
TRANSITION: none. Let it sit, then name what they ARE here for.

🔴 ITS OWN SLIDE, per John. One idea per frame, and this idea is a reversal, so it cannot
   share a frame with the thing it reverses.
-->

---
layout: center
class: peak text-center
---

<!-- slide:v7-05 -->

<div class="rt-h1">You're here to find the one thing that's actually holding your business back.</div>

<!--
HOOK: the highest-recall line in the first thirty seconds. Say it, then stop talking.
BEATS:
  - You're here to find the one thing that's actually holding your business back.
TIMING: 6 sec
TRANSITION: hold the dark frame one full beat, then name the exchange.

PEAK 2 of 6. Budget: 01 05 21 28 36 64. Do not add a seventh.
🔴 NEW BEAT 08-09, and the asset never had one: "you're not really here for that. You're here
   to get some value and ultimately eliminate some kind of blocker or constraint in your
   business so you can grow and hit the level that you want."
-->

---
layout: center
class: text-center
---

<!-- slide:v7-06 -->

<div class="rt-kicker">SO HERE'S THE EXCHANGE</div>
<div class="rt-h2">Four minutes here. A few more on the form.</div>

<div class="rt-rule w-80 mx-auto mt-10"></div>

<!--
HOOK: name the price of watching before they work it out themselves. Nobody bails on a
  four-minute video they have been told is four minutes.
BEATS:
  - So here's why it's worth the next four minutes of your life, and a few minutes on the
    form after it.
TIMING: 7 sec
TRANSITION: now earn it. Start with where the observation comes from.

🔴 THE LENGTH SPEC IS A PROMISE ON THE FRAME NOW. From strategy_2026_07_28: "the roadmap VSL
   points to just getting as many people as possible to complete the roadmap. That's like four
   or five minutes long." If this deck ever runs past five minutes, this slide becomes a lie.
   That is deliberate: it is the guard rail that keeps the asset from bloating again.
-->

---
layout: default
class: bleed
---

<!-- slide:v7-07 -->

<div class="absolute inset-0">
  <img src="/stage/cc_live_600s.jpg" alt="" class="rt-bleed" />
  <div class="rt-scrim"></div>
</div>

<div class="absolute inset-0 flex flex-col justify-center pl-16 pr-6 z-10" style="width:62%">
  <div class="rt-kicker" style="color:var(--tealb)">EVERY SINGLE WEEK</div>
  <div class="rt-h2 rt-onimg">I talk to business owners constantly.</div>
  <div class="rt-say rt-onimg mt-6" v-click>At talks, on coaching calls, in co-working spaces.</div>
</div>

<!--
HOOK: authority by CONTEXT, never by claim. The room is the credential.
BEATS:
  - I talk to business owners constantly. At talks, on coaching calls, in co-working spaces.
TIMING: 7 sec
TRANSITION: and here is what I keep seeing. Absolve them first.
SIDE: copy LEFT. The next bleed (63) is copy RIGHT. Never three the same way.

A5 HERO-BLEED is Brad's archetype and it is the one v6 did not have. That is why four stage
photos ended up in a 2x2 thumbnail grid on slide 1 reading as clip-art. A photograph either
fills the frame under a scrim or it is half of a split. There is no third state.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-08 -->

<div class="rt-h1">And most of them are doing their absolute best.</div>

<!--
HOOK: absolution BEFORE diagnosis. If they feel accused they stop listening and the form
  never gets filled.
BEATS:
  - And most of them are doing their absolute best.
TIMING: 4 sec
TRANSITION: so if it isn't effort, what is it.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-09 -->

<div class="rt-h2">They're just buried under conflicting advice about what to do next.</div>

<!--
HOOK: name the condition without naming a villain yet.
BEATS:
  - They're just buried under conflicting advice about what to do next.
TIMING: 5 sec
TRANSITION: where does the conflicting advice come from. Everyone.
-->

---
layout: default
---

<!-- slide:v7-10 -->

<div class="rt-split">
<div>

<div class="rt-kicker">WHERE IT COMES FROM</div>
<div class="rt-h2">Everyone has an opinion about your business.</div>

</div>

<div class="rt-visual">
  <img src="/gen/concept-06-information-abundance.png"
       alt="A single figure under an avalanche of competing instructions"
       class="rt-figure" />
</div>
</div>

<!--
HOOK: it is not that they were told nothing. They were told everything.
BEATS:
  - Everyone has an opinion about what your business needs.
TIMING: 5 sec
TRANSITION: and here is what all of those opinions have in common.
SIDE: visual RIGHT. Next split flips.

KEEP: the concept-0*.png whiteboard images. John liked those specifically. They live in
FRAME 1 (.rt-figure) or as the visual half of a split, never floating.
-->

---
layout: default
---

<!-- slide:v7-11 -->

<div class="rt-split flip">
<div class="rt-visual">
  <img src="/gen/concept-04-fit-model-to-business.png"
       alt="A rigid template forced over an irregular shape"
       class="rt-figure" />
</div>

<div>

<div class="rt-kicker">WHAT ACTUALLY HAPPENS</div>
<div class="rt-h2">Your business, into their model.</div>
<div class="rt-sub mt-6" v-click>Instead of a model fitted to your business.</div>

</div>
</div>

<!--
HOOK: the inversion is the whole diagnosis, and it takes eight words.
BEATS:
  - They're trying to fit your business into their model, instead of fitting a model to
    your business.
TIMING: 7 sec
TRANSITION: and while that is happening, the noise gets louder.
SIDE: visual LEFT.

🔴 JOHN FLAGGED THIS LINE HIMSELF: "I like that line. I actually keep that in there."
   KEEP IT VERBATIM in the notes. The frame only carries the eight-word version.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-12 -->

<div class="rt-kicker">MEANWHILE EVERYONE IS SHOUTING</div>

<div class="rt-grid c2 mt-8">
<v-clicks>
<div class="rt-card bad"><div class="rt-card-t">Go high ticket</div></div>
<div class="rt-card bad"><div class="rt-card-t">Go low ticket</div></div>
<div class="rt-card bad"><div class="rt-card-t">Go webinar</div></div>
<div class="rt-card bad"><div class="rt-card-t">Hire a setter</div></div>
</v-clicks>
</div>

<!--
HOOK: the noise IS the point, so do not dwell on any one card. Four clicks, fast, no commentary.
BEATS:
  - Meanwhile everyone's shouting. Go high ticket. Go low ticket. Go webinar. Hire a setter.
TIMING: 8 sec
TRANSITION: and the ground is moving underneath all of it.

COLOUR: ember on all four, because every one of them is a restart dressed as a strategy.
That is the grammar working: the viewer reads "these are all the same thing" before you say it.
-->

---
layout: default
---

<!-- slide:v7-13 -->

<div class="rt-split">
<div>

<div class="rt-kicker">AND UNDERNEATH ALL OF IT</div>
<div class="rt-h2">Everyone's racing to the bottom.</div>
<div class="rt-sub mt-6" v-click>Ad costs climb. Everyone's on the back foot.</div>

</div>

<div class="rt-visual">
  <img src="/gen/concept-07-trust-recession.png"
       alt="A crowded market with trust draining out of it"
       class="rt-figure" />
</div>
</div>

<!--
HOOK: the pressure is EXTERNAL. This is the earthquake beat, and it is about them without
  accusing them.
BEATS:
  - Meanwhile ad costs climb. Everyone's racing to the bottom, everyone's on the back foot.
TIMING: 7 sec
TRANSITION: which means the thing that used to work for you personally may be failing right now.
SIDE: visual RIGHT.

🔴 "The window to be early on a channel has gone from years to months" stays CUT (08-09).
-->

---
layout: center
class: text-center
---

<!-- slide:v7-14 -->

<div class="rt-h1">Things that worked for you once might be breaking right now.</div>

<!--
HOOK: move the earthquake from the market onto their desk, still without blame.
BEATS:
  - Things that worked for you once might be breaking right now.
TIMING: 5 sec
TRANSITION: so here is what most owners end up doing about it. Name the enemy.
-->

---
layout: default
---

<!-- slide:v7-15 -->

<div class="rt-split flip">
<div class="rt-visual">
  <img src="/gen/concept-01-sequence-trap.png"
       alt="Moves made in the wrong order, each one undoing the last"
       class="rt-figure" />
</div>

<div>

<div class="rt-kicker">SO MOST OWNERS END UP HERE</div>
<div class="rt-h2">The <span v-mark="{ at: 1, color: '#C4552F', type: 'circle' }">sequence trap</span>.</div>

</div>
</div>

<!--
HOOK: the enemy gets a name and a picture in the same breath. A named enemy is arguable;
  an unnamed one is just a mood.
BEATS:
  - So most business owners end up in what I call the sequence trap.
TIMING: 6 sec
TRANSITION: define it in one line, then show it.
SIDE: visual LEFT.

🔴 OPEN QUESTION FOR JOHN, carried forward from 08-09 unanswered: "is the sequence trap the
   best name?" One term, used everywhere, or the asset teaches nothing. If it changes, it
   changes on slides 15 and 16 and nowhere else.
COLOUR: the circle is EMBER because the sequence trap is a failure. That is legal grammar.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-16 -->

<div class="rt-kicker">WHAT IT ACTUALLY LOOKS LIKE</div>
<div class="rt-h2">Disconnected moves.</div>

<div class="rt-figure mt-6">
  <img src="/flows/01a_pieces_disconnected.svg" alt="Pieces of a funnel sitting apart, none of them connected" />
</div>

<!--
HOOK: they recognise their own last two years in a diagram they have never seen.
BEATS:
  - Disconnected moves, instead of the path that makes sense for you.
TIMING: 7 sec
TRANSITION: and then absolve them again, immediately, before they can defend themselves.
DRAW: trace between two disconnected pieces once, live. One stroke. Do not pre-draw it.

🔴 INVISIBLE-RENDER LAW. This is an SVG loaded into a card, not an inline diagram, so it
   cannot silently fail to render nodes -- but it can still letterbox. The deck ground is
   white and .rt-figure is white, so it will not. VERIFY ON THE SCREENSHOT anyway.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-17 -->

<div class="rt-kicker">AND NOT BECAUSE YOU DID IT WRONG</div>

<div class="rt-grid c3 mt-8">
<v-clicks>
<div class="rt-card"><div class="rt-card-t">You read the books</div></div>
<div class="rt-card"><div class="rt-card-t">You hired the agency</div></div>
<div class="rt-card"><div class="rt-card-t">You built the funnel yourself</div></div>
</v-clicks>
</div>

<!--
HOOK: three things they actually did, listed without a single note of criticism.
BEATS:
  - Not because you did it wrong. You read the books. Hired the agency. Built the funnel yourself.
TIMING: 8 sec
TRANSITION: every one of those gave you something. Just not the first thing.

🔴 THESE CARDS ARE NEUTRAL GREY, NOT EMBER, AND THAT IS LOAD-BEARING. None of these were
   mistakes. Ember here would say "you were an idiot three times" and the viewer would close
   the tab. The colour has to agree with the sentence.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-18 -->

<div class="rt-h2">You just got a piece of the puzzle.</div>
<div class="rt-h1 mt-10" v-click>And it wasn't the first piece.</div>

<!--
HOOK: the reveal is one word: FIRST. Everything after this beat is about order.
BEATS:
  - You just got a piece of the puzzle. And it wasn't the first piece.
TIMING: 7 sec
TRANSITION: and the cost of that shows up late, which is why it repeats.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-19 -->

<div class="rt-kicker">SO YOU FIND OUT TOO LATE</div>

<div class="rt-grid c2 mt-8">
<v-clicks>
<div class="rt-card bad"><div class="rt-card-t">Another quarter gone</div></div>
<div class="rt-card bad"><div class="rt-card-t">Another channel abandoned</div></div>
</v-clicks>
</div>

<!--
HOOK: cost of inaction, in their units, not ours. Quarters and channels, never dollars.
BEATS:
  - So you find out too late. Another quarter gone. Another channel abandoned.
TIMING: 6 sec
TRANSITION: and the question survives all of it.
COLOUR: ember, correctly -- both cards ARE the restart.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-20 -->

<div class="rt-h2">And the same question you had last January is still sitting there.</div>

<!--
HOOK: they can DATE it. That is what makes this land rather than resonate.
BEATS:
  - And the same question you had last January is still sitting there.
TIMING: 6 sec
TRANSITION: say the question out loud. Then say nothing.
-->

---
layout: center
class: peak text-center
---

<!-- slide:v7-21 -->

<div class="rt-h1" style="font-size:5rem; max-width:14ch">"How do I fix this?"</div>

<!--
HOOK: their own sentence, in their own head, on a dark frame at full size. Say it and STOP.
BEATS:
  - How do I fix this?
TIMING: 5 sec, and three of those are silence
TRANSITION: hold two full beats. Then answer the question the market usually answers it with.

PEAK 3 of 6.
🔴 JOHN SPECIFIED THE TREATMENT EXACTLY, 08-09: "we can have that in quotes too. How do I
   fix this?" The quotes are his. The 5rem override is the only inline type size in the deck
   and it is deliberate -- max-width is set with it so it still cannot overflow.
🔴 v6 put /gen/char-01-stuck.png on this slide as a cutout. That file is mode=RGB with a
   painted checkerboard. BANNED. The dark frame alone is stronger anyway.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-22 -->

<div class="rt-kicker">AND HERE'S WHAT THEY HAND YOU</div>
<div class="rt-h2">One size, fits all.</div>

<div class="rt-grid c3 mt-8">
<v-clicks>
<div class="rt-card bad"><div class="rt-card-t">Webinar</div></div>
<div class="rt-card bad"><div class="rt-card-t">VSL</div></div>
<div class="rt-card bad"><div class="rt-card-t">High-ticket book-a-call</div></div>
</v-clicks>
</div>

<!--
HOOK: three products, all of which are real and all of which are answers to somebody else's
  question.
BEATS:
  - Most of them hand you a one-size-fits-all model. Webinar. VSL. High-ticket book-a-call.
TIMING: 7 sec
TRANSITION: concede that they work, then ask the only question that matters.

🔴 "HIGH-TICKET BOOK-A-CALL", never "closer model". John said it that way twice on 08-09.
🔴 TRIMMED TO THREE on 08-09: "I don't know if we want to have too many in there."
-->

---
layout: center
class: text-center
---

<!-- slide:v7-23 -->

<div class="rt-h2">It worked for somebody.</div>
<div class="rt-h1 mt-10" v-click>But does it work for <span v-mark="{ at: 2, color: '#209080', type: 'circle' }">your</span> business?</div>

<!--
HOOK: concede before you correct. The concession is what makes the correction land instead
  of reading as an attack on things they may have bought.
BEATS:
  - It worked for somebody. But does it work for your specific business?
TIMING: 7 sec
TRANSITION: and here is the uncomfortable version of the same question.
COLOUR: the circle is TEAL because "your business" is the path that works. Grammar holds.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-24 -->

<div class="rt-h1">Or were you just financially qualified?</div>

<!--
HOOK: the seller's own language turned back on the seller. Play it FLAT. No edge, no smirk.
  Delivered with any heat it becomes an attack on the viewer's past decisions.
BEATS:
  - Or were you just financially qualified?
TIMING: 4 sec
TRANSITION: name what none of them gave you.

"Financially qualified" is John's own phrase from 08-09 and is sharper than "able to afford it".
-->

---
layout: default
---

<!-- slide:v7-25 -->

<div class="rt-split flip">
<div class="rt-visual">
  <img src="/gen/concept-03-critical-path.png"
       alt="One route through a field of possible moves, numbered in order"
       class="rt-figure" />
</div>

<div>

<div class="rt-kicker">AND ALMOST NONE OF THEM</div>
<div class="rt-h2">Give you the <span v-mark="{ at: 1, color: '#D9B96A', type: 'underline' }">order</span> to do things in.</div>

</div>
</div>

<!--
HOOK: this is the mechanism word for the entire asset. Everything from here forward is about
  ORDER, and this is the first time it is said.
BEATS:
  - Almost none of them give you the order to do things in.
TIMING: 6 sec
TRANSITION: because there are five different things it could be, and they are not the same thing.
SIDE: visual LEFT.
COLOUR: GOLD underline. Gold means a gate or a sequence in this deck's grammar, and "order"
  is the gate. Not ember (that would say order is a failure) and not teal (that is the path
  itself, which they do not have yet).
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-26 -->

<div class="rt-kicker">THERE'S A DECENT CHANCE YOU'VE GOT ONE OF THESE</div>

<div class="rt-grid c5 mt-8">
<v-clicks>
<div class="rt-card"><div class="rt-card-t">An attention problem</div></div>
<div class="rt-card"><div class="rt-card-t">A lead problem</div></div>
<div class="rt-card"><div class="rt-card-t">A capture problem</div></div>
<div class="rt-card"><div class="rt-card-t">A conversion problem</div></div>
<div class="rt-card"><div class="rt-card-t">A traffic problem</div></div>
</v-clicks>
</div>

<!--
HOOK: five clicks, fast. The viewer is silently picking theirs while you speak, which is the
  first time in the video they do work.
BEATS:
  - There's a decent chance you've got an attention problem. A lead problem. Capture.
    Conversion. Traffic.
TIMING: 9 sec
TRANSITION: plenty of people have one. That is not the interesting part.

🔴 WIDENED FROM THREE TO FIVE, John 08-09: "an attention problem, a lead problem, a capture
   problem, a conversion problem... I want the full range there."
COLOUR: NEUTRAL, not ember. Having a constraint is not a failure, it is a fact. Ember here
  would break the absolution that slides 8 and 17 spent real time building.
-->

---
layout: default
---

<!-- slide:v7-27 -->

<div class="rt-split">
<div>

<div class="rt-kicker">PLENTY OF PEOPLE DO</div>
<div class="rt-h2">Which one do you fix <span v-mark="{ at: 1, color: '#D9B96A', type: 'underline' }">first</span>?</div>

</div>

<div class="rt-visual">
  <img src="/gen/concept-09-audit-magnifier.png"
       alt="A funnel with one stage circled and the rest left alone"
       class="rt-figure" />
</div>
</div>

<!--
HOOK: the pivot of the entire argument. Not WHICH problem. Which problem FIRST.
BEATS:
  - Plenty of people do. The question is which one you fix first.
TIMING: 6 sec
TRANSITION: and the reason nobody ever answered that for you is coming next. Slow down into it.
SIDE: visual RIGHT.
COLOUR: gold again on "first", deliberately rhyming with slide 25. Same colour, same idea,
  six slides apart. That repetition is what makes a deck read as one system.
-->

---
layout: center
class: peak text-center
---

<!-- slide:v7-28 -->

<div class="rt-h1">Because nobody ever gave you a roadmap that was <span v-mark="{ at: 1, color: '#2BB3A0', type: 'circle' }">yours</span>.</div>

<!--
HOOK: the highest-recall frame in the asset. Say it, then stop.
BEATS:
  - Because nobody ever gave you a roadmap that was yours.
TIMING: 6 sec, two of them silent
TRANSITION: hold the dark frame. Then explain what they got instead.

PEAK 4 of 6.
This line is also the H1 of the live roadmap page (roadmap-subdomain-step1), word for word.
That is not a coincidence and it should stay that way: the video and the page they land on
say the same sentence, which is the cheapest continuity device we have.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-29 -->

<div class="rt-h2">Everybody gave you a process.</div>
<div class="rt-sub mt-8" v-click>Built from <span v-mark="{ at: 2, color: '#C4552F', type: 'underline' }">their</span> situation, not yours.</div>

<!--
HOOK: process versus roadmap. One is generic by construction, the other cannot be.
BEATS:
  - Everybody gave you a process. Built from their situation, not yours.
TIMING: 6 sec
TRANSITION: list what "their situation" actually contained.
COLOUR: ember on "their", because someone else's situation transplanted into yours IS the
  failure. Grammar holds.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-30 -->

<div class="rt-kicker">THEN HANDED OVER</div>
<div class="rt-h2">Like it would transfer.</div>

<div class="rt-grid c4 mt-8">
<v-clicks>
<div class="rt-card"><div class="rt-card-t">Their situation</div></div>
<div class="rt-card"><div class="rt-card-t">Their market</div></div>
<div class="rt-card"><div class="rt-card-t">Their team</div></div>
<div class="rt-card"><div class="rt-card-t">Their timing</div></div>
</v-clicks>
</div>

<!--
HOOK: four clicks and the viewer finishes the sentence before you do.
BEATS:
  - Then handed over like it would transfer.
TIMING: 7 sec
TRANSITION: and here is the one nobody checked at all.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-31 -->

<div class="rt-kicker">AND NOBODY CHECKED</div>
<div class="rt-h2">Whether your market could even support it.</div>

<div class="rt-grid c5 mt-8">
<v-clicks>
<div class="rt-card bad"><div class="rt-card-t">Your time</div></div>
<div class="rt-card bad"><div class="rt-card-t">Your energy</div></div>
<div class="rt-card bad"><div class="rt-card-t">Your attention</div></div>
<div class="rt-card bad"><div class="rt-card-t">Your team</div></div>
<div class="rt-card bad"><div class="rt-card-t">Your budget</div></div>
</v-clicks>
</div>

<!--
HOOK: five clicks, accelerating. The last one lands and the next slide is the proof.
BEATS:
  - And nobody checked whether your market could even support it.
TIMING: 8 sec
TRANSITION: straight into the example. No preamble.

🔴 DO NOT CUT THIS SLIDE. It is the setup for the client example on 32-35. Without it that
   example is an anecdote. With it, the example is the proof of a claim already made.
-->

---
layout: default
---

<!-- slide:v7-32 -->

<div class="rt-split">
<div>

<div class="rt-kicker">HERE'S ONE I WORKED ON RECENTLY</div>
<div class="rt-h2">A book-a-call funnel.</div>

</div>

<div class="rt-visual">
<div class="w-full">
  <div class="rt-card" v-click><div class="rt-card-t">Leads were cheap</div></div>
  <div class="rt-card bad mt-4" v-click><div class="rt-card-t">Almost nobody showed up</div></div>
</div>
</div>
</div>

<!--
HOOK: two facts that should not be able to sit together. That contradiction is the hook.
BEATS:
  - Here's one I worked on recently. Book-a-call funnel. Cheap leads. Almost nobody showing up.
TIMING: 7 sec
TRANSITION: and the reason had nothing to do with the funnel.
SIDE: visual RIGHT.

🔴 NO CLIENT NAME, NO LOGO, NO NUMBERS ON SCREEN for the whole 32-35 run. The client is
   named nowhere; the quote card on 35 uses her first name only, which is cleared.
🔴 THE NUMBERS ARE CUT AND STAY CUT: "22 bookings and none showed", "over 80% showed up",
   "show rate doubled", "$5,500". None of those appear in any of the three transcripts as a
   win. A remembered figure attached to a named client on cold traffic is the one sentence
   in this asset that would get challenged.
COLOUR: card one is NEUTRAL (cheap leads is not a failure, it is the confusing part) and
   card two is EMBER (that one is the failure). The two colours ARE the contradiction.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-33 -->

<div class="rt-kicker">BECAUSE OF WHEN HER BUYERS COULD ACTUALLY TALK</div>

<div class="rt-card bad mt-8 max-w-4xl">
  <div class="rt-card-t">Six in the morning, or after their kid was asleep</div>
  <div class="rt-card-s mt-3">A one-call Zoom close was never going to work for that market</div>
</div>

<!--
HOOK: the constraint is a fact about their LIVES, not about the funnel. That is the whole
  lesson and it takes one card.
BEATS:
  - Because of when her buyers could take a call. Six in the morning, or after their kid
    was asleep.
TIMING: 8 sec
TRANSITION: so we changed one thing. Exactly one.

🔴 VERIFIED AGAINST FIREFLIES 08-09, transcript 01KYTRGEZJ7SY2B8G0RJ821BPP, 2026-08-06, the
   client's own words: "The blocker with it is the hours that Jenny and I can do a Zoom call
   with the family. So we're limited to between 6 and 9am and 6 and 9pm because she's 12
   hours ahead. And we have to do the Zoom calls while the child is asleep."
🔴 CLIENT-SENSITIVE: the child detail is paraphrased on purpose and her vertical is not named
   on the frame. John's explicit say-so is required before the vertical appears on cold traffic.
-->

---
layout: default
---

<!-- slide:v7-34 -->

<div class="rt-split flip">
<div class="rt-visual">
<div class="rt-new w-full">
  <div class="rt-waylabel">THE ONE CHANGE</div>
  <div class="rt-card-t">The first call became a phone call</div>
</div>
</div>

<div>

<div class="rt-kicker">SO WE CHANGED ONE THING</div>
<div class="rt-h2">One variable. Visibly one.</div>

</div>
</div>

<!--
HOOK: one card on the frame, because one thing changed. If there were two cards the argument
  would be weaker and the viewer would know why.
BEATS:
  - So we changed one thing. The first call became a phone call.
TIMING: 6 sec
TRANSITION: and it did not go cleanly, which is the better story.
SIDE: visual LEFT.
COLOUR: TEAL. This is the path that works, and it is the first teal object in the deck.
  Everything before this point has been neutral or ember. That is deliberate: the first time
  teal appears, it means something.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-35 -->

<div class="rt-proofcard max-w-3xl mx-auto text-left">
  <div class="rt-quote">"The one that I just signed up started with a phone call."</div>
  <div class="rt-attrib">Erin &middot; it fell through first, then she won it back</div>
</div>

<!--
HOOK: the recovery arc, not a clean close. A step that survives a fall-through is doing more
  work than a step that never got tested.
BEATS:
  - The first one through fell over. Then she won them back and closed it.
TIMING: 7 sec
TRANSITION: and then the six words that make the whole example a system claim.

🔴 JOHN CORRECTED MY RECORD ON THIS, 08-09: "the deal fell through, but then she got it back.
   So it actually ended up closing, because the one that fell through was from a phone call
   and then she got them back basically."
🔴 THE QUOTE IS VERBATIM AND VERIFIED. The attribution line is attribution, never a claim.
   ✅ NAMING CLEARED 08-09: "they can be named on cold traffic... everybody is, until they
   say hey take my name down."
-->

---
layout: center
class: peak text-center
---

<!-- slide:v7-36 -->

<div class="rt-h1">Same funnel. It just wasn't built for them.</div>

<!--
HOOK: eight words carrying the entire first half of the video. Land here.
BEATS:
  - Same funnel. It just wasn't built for them.
TIMING: 5 sec
TRANSITION: hold the dark frame. Then generalise it to the whole market.

PEAK 5 of 6.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-37 -->

<div class="rt-kicker">THAT'S WHY TRUST IS SO HARD TO COME BY</div>
<div class="rt-h1">The model sells everyone, whether it fits or not.</div>

<!--
HOOK: this explains every bad experience they have had, in one sentence, without naming
  anybody. It is a structural accusation, not a personal one, which is why it is safe.
BEATS:
  - That's why trust is so hard to come by. The model sells everyone, whether it fits or not.
TIMING: 7 sec
TRANSITION: so what is the actually hard part. Not the part they think.

🔴 JOHN FLAGGED THIS AS "a really good line actually" (08-09). Keep verbatim.
🔴 v6 hung /gen/char-05-deciding.png on this slide as a cutout. BANNED, no alpha.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-38 -->

<div class="rt-kicker">AND HERE'S THE PART EVERYONE GETS BACKWARDS</div>
<div class="rt-h2">The hard part isn't drawing a path.</div>
<div class="rt-sub mt-8" v-click>Anyone can draw a path.</div>

<!--
HOOK: concede the thing every competitor sells, out loud, before they can accuse you of
  selling it too.
BEATS:
  - The hard part isn't drawing a path. Anyone can draw a path.
TIMING: 6 sec
TRANSITION: so what is it.

A3b LEDGER, left aligned. This exists to break a run of centred frames without inventing a
new archetype. 37 was centred, 39 is centred, and this sits between them.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-39 -->

<div class="rt-h1">The hard part is working out where you actually are right now.</div>

<!--
HOOK: this is the beat that makes the roadmap impossible to self-serve, and it does it without
  a single word about us.
BEATS:
  - The hard part is working out where you actually are right now.
TIMING: 6 sec
TRANSITION: give them the image for it.
-->

---
layout: default
---

<!-- slide:v7-40 -->

<div class="rt-split flip">
<div class="rt-visual">
  <img src="/gen/concept-02-jungle.png"
       alt="A detailed map held up inside dense jungle with no visible landmark"
       class="rt-figure" />
</div>

<div>

<div class="rt-kicker">IF YOU DON'T KNOW WHERE YOU ARE</div>
<div class="rt-say">It doesn't matter how good the map is.</div>

</div>
</div>

<!--
HOOK: the metaphor does the work that four slides of explanation could not.
BEATS:
  - If you don't know where you are in the jungle, it doesn't matter how good the map is.
TIMING: 7 sec
TRANSITION: and you cannot find your own position from inside.
SIDE: visual LEFT.

🔴 THE JUNGLE MOVED INTO THE VSL on 08-09, overruling the earlier note that it should stay on
   the roadmap page. It earns its place because it is the only image in the deck that makes
   "position" feel like a problem rather than a word.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-41 -->

<div class="rt-kicker">AND NOBODY CAN DO THAT FROM INSIDE</div>
<div class="rt-h2">Not from inside your own business.</div>
<div class="rt-sub mt-8" v-click>Definitely not on a call with someone paid to close you.</div>

<!--
HOOK: the incentive argument, which only works because slide 37 already made it structurally.
  Said here first it would read as bitter; said here it reads as obvious.
BEATS:
  - And nobody can do that from inside their own business. Definitely not on a call with
    someone paid to close you.
TIMING: 8 sec
TRANSITION: so name what they actually need. Start by naming what they do not.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-42 -->

<div class="rt-kicker">SO WHAT YOU NEED ISN'T</div>

<div class="rt-grid c3 mt-8">
<v-clicks>
<div class="rt-card bad"><div class="rt-card-t">Another ad</div></div>
<div class="rt-card bad"><div class="rt-card-t">Another funnel</div></div>
<div class="rt-card bad"><div class="rt-card-t">A better offer</div></div>
</v-clicks>
</div>

<!--
HOOK: three negations, rising. Refusing to sell them the obvious thing is the most persuasive
  move available here.
BEATS:
  - So what you need isn't another ad, another funnel, or a better offer.
TIMING: 7 sec
TRANSITION: now say the thing. Slow.
-->

---
layout: default
---

<!-- slide:v7-43 -->

<div class="rt-kicker">WHAT YOU NEED IS</div>
<div class="rt-say">A roadmap built from where <span v-mark="{ at: 1, color: '#209080', type: 'circle' }">you</span> actually are.</div>

<div class="rt-figure mt-8">
  <img src="/flows/01b_pieces_connected.svg" alt="The same pieces, connected in one order, starting from where you are" />
</div>

<!--
HOOK: the same pieces from slide 16, connected. The viewer sees the answer before they hear it.
BEATS:
  - A roadmap built from where you actually are, to where you want to go.
TIMING: 7 sec
TRANSITION: break it into its three parts, one at a time.
LAYOUT NOTE: full-width figure, not a split, and that was decided at the render. This flow is
  1253x234, so in a half column its labels compute to about 7px and the whole argument becomes
  a grey smudge. It is also the deliberate rhyme with slide 16: same treatment, same size, same
  position, 27 slides apart, one disconnected and one connected. Keep them matched.

🔴 DO NOT NAME THE ROADMAP FUNNEL. John 08-09, unambiguous: "don't introduce roadmap funnel
   on slide 46, that's too much... we're not trying to sell the roadmap mechanism in here."
   The noun on the frame is "a roadmap", plain, and the qualifier is the differentiator.
   The mechanism is what they meet AFTER, in the SAGE VSL. Not here.
COLOUR: teal circle on "you". Same device as slide 28, and both are the payoff colour.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-44 -->

<div class="rt-kicker">THREE PARTS</div>

<div class="rt-grid c3 mt-8">
<v-clicks>
<div class="rt-card"><div class="rt-card-t">Where you are now</div></div>
<div class="rt-card"><div class="rt-card-t">Where you're going</div></div>
<div class="rt-card good"><div class="rt-card-t">The steps between</div><div class="rt-card-s mt-2">In the right order</div></div>
</v-clicks>
</div>

<!--
HOOK: three clicks, each landing exactly on the phrase as it is spoken. Per John, the cards
  arrive with the words, not before them.
BEATS:
  - Where you are now. Where you're going. And the steps between them, in the right order.
TIMING: 9 sec
TRANSITION: and almost none of it is complicated.

🔴 WHY THE THIRD CARD IS THE TEAL ONE: everyone sells "where you can go". Almost nobody sells
   the order. When the last card in a 3-up is the only teal one, the argument is made before
   a word is spoken. That is the colour grammar doing the persuading.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-45 -->

<div class="rt-h1">Most of it is simple things stacked in the right order.</div>

<!--
HOOK: deflate the expectation of complexity, because complexity is the reason they would not
  fill in the form.
BEATS:
  - Most of it is simple things stacked in the right order.
TIMING: 5 sec
TRANSITION: say it twice, plainly.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-46 -->

<div class="rt-h2">Nothing here is clever. Nothing here is complicated.</div>

<!--
HOOK: two negations and then silence. Resist adding a third clause.
BEATS:
  - Nothing here is clever. Nothing here is complicated.
TIMING: 5 sec
TRANSITION: but when the order is right, this is what starts happening.

🔴 JOHN CORRECTED THIS EXACT PAIRING HIMSELF. Do NOT reintroduce "the clever thing is the
   sequence" -- v4 ran "nothing in here is clever" immediately followed by "the clever thing
   is the sequence", which contradicts itself inside eight seconds.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-47 -->

<div class="rt-kicker">BUT WHEN THE ORDER IS RIGHT</div>
<div class="rt-h2">This is what it starts to look like.</div>

<div class="rt-grid c3 mt-8 items-stretch">
<v-clicks>

<div class="rt-proofcard">
  <div class="rt-quote">"Last week we were paying <span style="color:#C4552F">$33 a lead</span>... we're down to $21... like, <span style="color:#209080">$11 a lead</span>."</div>
  <div class="rt-attrib">Bradley &middot; inside one week, message work only</div>
</div>

<div class="rt-proofcard">
  <div class="rt-quote">"We shifted over to an application funnel in less than half a month and we had our <span style="color:#209080">best year ever</span> because of it."</div>
  <div class="rt-attrib">Dr Joe &middot; from a Facebook-group funnel</div>
</div>

<div class="rt-proofcard">
  <div class="rt-quote">"The one that I just signed up <span style="color:#209080">started with a phone call</span>."</div>
  <div class="rt-attrib">Erin &middot; the one thing we changed</div>
</div>

</v-clicks>
</div>

<div class="rt-foot"><div class="rt-fine">Verbatim client quotes from recorded calls. Individual results, described by the clients themselves. Nothing here is a claim about what you would earn.</div></div>

<!--
HOOK: three people, three businesses, one sequence. John's format: "just like this person,
  just like this person, just like this person."
BEATS:
  - But when the order is right, this is what it starts to look like.
TIMING: 12 sec, and you read none of the cards aloud
TRANSITION: the six words that turn three quotes into a system claim.

🔴 EVERY QUOTE IS VERBATIM FROM A FIREFLIES TRANSCRIPT and survived an adversarial
   verification pass on 2026-08-09.
   ✅ NAMING CLEARED, John 08-09: "they can be named on cold traffic."
   🔴 STILL BANNED regardless of who said it: income claims. Bradley's card is a COST metric
     (cost per lead, falling), which is not income. Dr Joe's is a qualitative statement in his
     own words with no figure. Erin's has no figure at all. Nothing here says what anyone made.
BUILD RULE: ONE CLIENT PER CARD. Two cards from the same client reads as one lucky account.
LEGIBILITY GATE: these render at ~264 CSS px in-deck and ~172px embedded. WORD COUNT is the
  gate, not pixel height. One sentence and one number survives. Sixty words does not.
CLAIM LOCK: the cards prove SEQUENCE. They do not say these people bought a roadmap.
-->

---
layout: default
---

<!-- slide:v7-48 -->

<div class="rt-split flip">
<div class="rt-visual">
  <img src="/gen/concept-08-two-roads.png"
       alt="A worn loop returning to its start beside a straight lit road"
       class="rt-figure" />
</div>

<div>

<div class="rt-h2">Different businesses. Different channels.</div>
<div class="rt-h1 mt-10" v-click>Same sequence.</div>

</div>
</div>

<!--
HOOK: the line that turns three anecdotes into a claim about how things work.
BEATS:
  - Different businesses. Different channels. Same sequence.
TIMING: 6 sec
TRANSITION: hard pivot. Change your posture on camera here.
SIDE: visual LEFT.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-49 -->

<div class="rt-h2">So here's what I want to do for you.</div>

<div class="rt-rule w-80 mx-auto mt-10"></div>

<!--
HOOK: the pivot. Everything before this was diagnosis; everything after is the exchange.
BEATS:
  - So here's what I want to do for you.
TIMING: 4 sec
TRANSITION: say the offer plainly, with no adjectives.

NOT A PEAK, deliberately. The peak budget is six and this beat does not need a dark frame --
the teal rule and a posture change on camera carry it. Adding a seventh peak would cheapen
the six that are there.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-50 -->

<div class="rt-say">I'll build you a roadmap with everything you need to decide what's next.</div>

<!--
HOOK: no adjectives, no superlatives, no name for it. Just the thing.
BEATS:
  - I'll build you a roadmap with everything you need to decide what's next.
TIMING: 6 sec
TRANSITION: and then the line that makes it believable.

.rt-say, not .rt-h2. This is a 13-word spoken sentence that has to be readable on screen, and
the fourth type tier exists for exactly this so a sentence never gets forced into a headline
slot. Forcing spoken sentences into .rt-h2 is what broke v6's layout.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-51 -->

<div class="rt-kicker">INCLUDING</div>

<div class="rt-card good mt-8 max-w-3xl">
  <div class="rt-card-t">The options that aren't us</div>
  <div class="rt-card-s mt-3">So you're deciding from abundance, not scarcity</div>
</div>

<!--
HOOK: the ethical spine of the whole asset, and the single most persuasive sentence in it.
  It is also true, which is why it can be said this plainly.
BEATS:
  - Including the options that aren't us.
TIMING: 6 sec
TRANSITION: now make it concrete. Three steps.

🔴 NEW 08-09, near-verbatim from John: "I want to build you a roadmap that gives you everything
   you need to make a decision, including the options that aren't us."
COLOUR: teal, and it should be. This is the path that works.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-52 -->

<div class="rt-kicker">THREE STEPS</div>

<div class="rt-grid c3 mt-8 items-stretch">
<v-clicks>

<div class="rt-card">
  <div class="rt-statl">STEP 01</div>
  <div class="rt-card-t mt-2">Answer the questions in the form below</div>
  <div class="rt-card-s mt-2">Takes a few minutes</div>
</div>

<div class="rt-card">
  <div class="rt-statl">STEP 02</div>
  <div class="rt-card-t mt-2">We build your roadmap from your answers</div>
  <div class="rt-card-s mt-2">Back to you within forty-eight hours</div>
</div>

<div class="rt-card good">
  <div class="rt-statl">STEP 03</div>
  <div class="rt-card-t mt-2">A quick Roadmap Discovery Session</div>
  <div class="rt-card-s mt-2">With specific recommendations</div>
</div>

</v-clicks>
</div>

<!--
HOOK: three clicks, one per spoken step, so the card lands as the words land.
BEATS:
  - Three steps. One, answer the questions in the form below. Takes a few minutes.
  - Two, we build your roadmap from your answers. Back to you within forty-eight hours.
  - Three, a quick roadmap discovery session with specific recommendations.
TIMING: 16 sec
TRANSITION: handle the only objection that actually stops people.

🔴 ONE NAME EVERYWHERE: "Roadmap Discovery Session". John's transcript says it three times.
🔴 "48 hours at the latest" per John, 08-09.
🔴 THREE BEATS, ONE SLIDE, THREE CLICKS. Building this as three separate slides would put the
   same layout three times consecutively, which the build spec bans, and would cost eight
   seconds the four-minute budget does not have.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-53 -->

<div class="rt-h2">And if you think you don't have time for this...</div>
<div class="rt-h1 mt-10" v-click>that's usually the strongest reason to do it.</div>

<!--
HOOK: the strongest objection handler in the asset, and it works because it agrees with them
  first.
BEATS:
  - And if you think you don't have time for this, that's usually the strongest reason to do it.
TIMING: 8 sec
TRANSITION: and then tell them they already paid.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-54 -->

<div class="rt-kicker">YOU'VE ALREADY PAID FOR IT</div>
<div class="rt-h2">In months of ad spend, and time.</div>
<div class="rt-sub mt-8" v-click>And in the things you put off.</div>

<!--
HOOK: sunk cost, reframed as a reason to act rather than a reason to feel bad.
BEATS:
  - You've already paid for it. In months of ad spend, and time, and the things you put off.
TIMING: 7 sec
TRANSITION: and the form is not a gate in front of the roadmap. It IS the roadmap starting.

🔴 SHARPENED 08-09. John: "not doing the work, not figuring out the sequence is what has been
   costing you." Say "the things you put off" -- his stronger phrasing reads as overclaim on
   screen but works spoken.
-->

---
layout: default
---

<!-- slide:v7-55 -->

<div class="rt-kicker">AND THE FORM ISN'T A GATE</div>
<div class="rt-h2">The form is step one of the roadmap.</div>

<div class="rt-split auto mt-4">
<div class="rt-visual">
  <div class="rt-shot">
    <div class="rt-imgwrap">
      <img src="/site/roadmap-subdomain-step1--hero.png" alt="The roadmap page, with three parts marked" />
      <span class="rt-mark" style="top:19%; left:30%; width:39%; height:7%;"><span class="rt-marknum">1</span></span>
      <span class="rt-mark" style="top:35%; left:33%; width:34%; height:30%;"><span class="rt-marknum">2</span></span>
      <span class="rt-mark good" style="top:78.5%; left:27%; width:46%; height:6%;"><span class="rt-marknum">3</span></span>
    </div>
  </div>
</div>

<div>
<ol class="rt-markkey">
<v-clicks>
<li><span class="rt-keynum">1</span>The same sentence you just heard. Nothing has been switched on you.</li>
<li><span class="rt-keynum">2</span>The map is on the page before you answer anything.</li>
<li><span class="rt-keynum good">3</span>Yours to keep whether or not we ever speak.</li>
</v-clicks>
</ol>
</div>
</div>

<!--
HOOK: show them the actual next screen, marked up, so arriving there feels like a continuation
  rather than a handoff. This is the single highest-leverage slide in the asset for the ONE
  TEST, because it is the last thing between them and the form.
BEATS:
  - The form is step one of the roadmap.
TIMING: 12 sec
TRANSITION: and then one call, on the whole journey.
SIDE: shot LEFT, key RIGHT.

🔴 THIS IS THE ARCHETYPE JOHN NAMED: "look at how our audits are where we do screenshots,
   proof, we mark the proof up. Fast-paced and really dialed in." Ring, not box: if an inline
   width miscomputes, an empty box reads as a broken render while a ring degrades to a dot.
   Marker 3 is TEAL because it is the reassurance, not a fault -- and marking one thing in
   three as good is what stops the device reading as sniping.
🔴 REDACTION GATE: this capture carries no client data and no figures, verified 2026-08-09.
   Nothing on it is redacted because nothing on it needs to be. Re-verify on the RENDER at
   1600x900 if the live page changes.
⚠️ COPY DRIFT TO WATCH: the live page footer says "about eight minutes" while slide 52 says
   "a few minutes" and the Typeform header says "a few minutes, mostly taps". Three numbers
   for one thing. Marker 3 deliberately rings the keep-it line and not the time line. JOHN:
   pick one and we will change the other two.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-56 -->

<div class="rt-kicker">THEN ONE CALL</div>
<div class="rt-h2">Your whole customer journey, in one pass.</div>

<div class="rt-figure mt-6">
  <img src="/flows/03a_bowtie_state1.svg" alt="The whole customer journey as a bowtie, acquisition through transformation" />
</div>

<!--
HOOK: the call is described as an examination of THEIR machine, not a conversation about our
  services. That distinction is the entire reason they book it.
BEATS:
  - Then one call, where we look through your whole customer journey to find the single
    constraint.
TIMING: 8 sec
TRANSITION: and the risk reversal, before the value, never after.
DRAW: circle one stage, live, one stroke, as you say "the single constraint".

🔴 THIS IMAGE WAS SWAPPED AFTER LOOKING AT THE RENDER, and the reason is the whole point of
   the Invisible-Render Law. The first choice, /flows/02b_funnel_the_call.svg, renders a node
   reading "We install the Roadmap Funnel" in legible black text. John 08-09: "we're not
   trying to sell the roadmap mechanism in here." A banned phrase can sit inside an SVG and
   pass every source-level check. GREP THE SVG TEXT, then look at the render.
   The bowtie is the correct figure anyway: the spoken line is about their whole customer
   journey, and the bowtie IS the customer journey.
🔴 INVISIBLE-RENDER LAW: screenshot this slide specifically. An SVG that fails to load leaves
   a white card that looks like a design choice.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-57 -->

<div class="rt-h1">Even if you never work with us, you walk away with a plan.</div>

<!--
HOOK: risk reversal BEFORE the value, never after. Said afterwards it sounds like a hedge.
BEATS:
  - So even if you never work with us, you walk away with a thirty, sixty, ninety day plan.
TIMING: 6 sec
TRANSITION: and name what the plan actually tells them.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-58 -->

<div class="rt-kicker">YOU'LL KNOW</div>
<div class="rt-h2">What's been costing you the most.</div>
<div class="rt-sub mt-8" v-click>That's yours to keep regardless.</div>

<!--
HOOK: the deliverable stated as a piece of knowledge they own, not a document we send.
BEATS:
  - You'll know what's been costing you the most. That's yours to keep regardless.
TIMING: 6 sec
TRANSITION: be honest about the limits of a form.
-->

---
layout: default
---

<!-- slide:v7-59 -->

<div class="rt-split flip">
<div class="rt-visual">
  <div class="rt-sticky r max-w-sm">that's where the real picture shows up</div>
</div>

<div>

<div class="rt-kicker">A FORM CAN ONLY TELL US SO MUCH</div>
<div class="rt-h2">So we ask two or three follow-ups.</div>

</div>
</div>

<!--
HOOK: conceding the limits of your own instrument is the cheapest credibility available.
BEATS:
  - A form can only tell us so much. So we ask two or three follow-ups.
TIMING: 6 sec
TRANSITION: and then, only if it makes sense.
SIDE: visual LEFT.

The sticky is the behind-the-scenes register, lifted from the Miro boards. It is the only
place in the deck where we say something as ourselves rather than to them.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-60 -->

<div class="rt-say">If it makes sense at the end, we might invite you to a next step.</div>

<!--
HOOK: "might" is doing real work. Certainty here would undo slide 51 completely.
BEATS:
  - If it makes sense at the end, we might invite you to a next step.
TIMING: 6 sec
TRANSITION: and describe it in one line, without naming it.
-->

---
layout: default
class: flex flex-col justify-center
---

<!-- slide:v7-61 -->

<div class="rt-card good mt-4 max-w-3xl">
  <div class="rt-card-t">A proposal built around your situation</div>
  <div class="rt-card-s mt-3">Not a one-size-fits-all</div>
</div>

<!--
HOOK: closes the loop opened on slide 22. Same phrase, inverted, forty slides apart.
BEATS:
  - A proposal built around your situation. Not a one-size-fits-all.
TIMING: 5 sec
TRANSITION: and either way.

🔴 THE ROADMAP FUNNEL IS NOT NAMED HERE OR ANYWHERE. John 08-09: "that's too much."
   Cold traffic meets the Roadmap VSL first and the mechanism afterwards, inside. Naming the
   product here is the single most common way this asset gets worse.
-->

---
layout: center
class: text-center
---

<!-- slide:v7-62 -->

<div class="rt-h2">Either way you come out of this with real clarity.</div>

<!--
HOOK: the promise restated as an outcome that does not depend on us. That is the whole ask.
BEATS:
  - Either way you come out of this with real clarity.
TIMING: 5 sec
TRANSITION: and then the reason any of it matters.
-->

---
layout: default
class: bleed
---

<!-- slide:v7-63 -->

<div class="absolute inset-0">
  <img src="/team/john-red-carpet.jpg" alt="" class="rt-bleed" />
  <div class="rt-scrim-r"></div>
</div>

<div class="absolute inset-0 flex flex-col justify-center items-end pr-16 pl-6 z-10">
<div style="width:56%">
  <div class="rt-kicker" style="color:var(--tealb)">SO THAT</div>
  <div class="rt-h2 rt-onimg">The business starts serving you.</div>
  <div class="rt-say rt-onimg mt-6" v-click>Instead of you serving it.</div>
</div>
</div>

<!--
HOOK: the destination, shown rather than described, and it is a photograph of a real evening
  rather than a stock image of success.
BEATS:
  - So the business gets to the level where it starts serving you, instead of you serving it.
TIMING: 7 sec
TRANSITION: straight to the ask. Do not add anything between this and the close.
SIDE: copy RIGHT. Slide 7 was copy LEFT. Never three the same way.

🔴 JOHN'S OWN MID-SENTENCE CORRECTION, 08-09: it is the BUSINESS that starts serving you, not
   the roadmap. Do not let this drift back.
🔴 "Stability, profitability and freedom are right around the corner" is CUT and stays cut.
🔴 v6 put /gen/char-06-winning.png here as a cutout. BANNED, no alpha channel.
-->

---
layout: default
class: peak
---

<!-- slide:v7-64 -->

<div class="rt-split">
<div>

<div class="rt-h1">Answer the questions in the form below.</div>
<div class="rt-say mt-8" v-click>Let's get started on the pathway.</div>

<div class="rt-point mt-12 ml-0" style="margin-left:0" v-click></div>

</div>

<div class="rt-visual">
  <div class="rt-shot">
    <div class="rt-imgwrap">
      <img src="/site/ff-roadmap-typeform-embed.png" alt="The first question of the roadmap form" />
      <span class="rt-mark good" style="top:35%; left:29%; width:32%; height:8%;"><span class="rt-marknum">1</span></span>
    </div>
  </div>
</div>
</div>

<!--
HOOK: the last frame is a picture of the thing you want them to do, with the first question
  ringed, so the action is unambiguous the moment the video stops.
BEATS:
  - Answer the questions in the form below, and let's get started on the pathway.
TIMING: 6 sec
TRANSITION: none. End here. Do not add a thank-you slide.

PEAK 6 of 6. Budget closed.
🔴 NO BUTTON. Nobody can click a video. The pointer is a CSS triangle aimed at the real form
   under the player, and it is TEAL because teal is the path that works. An ember arrow here
   would be the failure colour pointing at the call to action, which is what v6 did on slide 1.
🔴 IF THIS ASSET RUNS ANYWHERE THE FORM IS NOT DIRECTLY BELOW THE PLAYER, add the URL in
   .rt-url on this slide. On the roadmap page and the audit page foot, the form IS below the
   player, so the pointer is correct and a URL would be noise.
🔴 NEVER USE site/ff-roadmap-form-page--full.png. It renders as an empty box: the Typeform is
   cross-origin and does not composite into a full-page capture. This embed capture is the
   only screenshot of the form that actually contains the form.

FUNNEL POSITION, for whoever picks this up next: this is the FRONT DOOR. Cold traffic, one
form, nothing else. The SAGE VSL is the asset they meet AFTER, on the book-a-call thank-you
page, on YouTube, and inside the roadmap. Two further assets are named in the transcripts and
remain unscoped: the thank-you "how to show up and actually do the steps" video, and the
roadmap demo. The demo's script beats (timer already started, we reward action takers, a
bonus asset, a $247 skip-the-queue checkout) are verbatim in 67d31de0 and its income framing
CANNOT cross into this asset.
-->
