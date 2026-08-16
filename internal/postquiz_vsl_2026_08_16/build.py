#!/usr/bin/env python3
"""
Build the post-quiz VSL deck (Fladlien 400-slide-hack pace) from a beat map.

WHY A GENERATOR AND NOT HAND-WRITTEN SLIDES
The Fladlien rules make hand-authoring the wrong tool: ~100 slides at 5-15 words
each, every one animated, every one carrying a visual, and the whole thing has to
stay consistent while the script is still being cut. A generator lets the SCRIPT
stay the source of truth and the slides be derived, so a copy change is one edit
in one place rather than a hunt through a hundred blocks.

THE RULES IT ENFORCES (copy-brain/06_Webinars/frameworks/_FLAGSHIP_fladlien_400_slide_hack.md)
  * opening 5-15 words/slide, content 15-30, closing 40-60
  * every slide animates
  * if it will not fit, SPLIT the slide, never shrink the type
  * EVERY SLIDE CARRIES A VISUAL. Bare text cards <=5% of the deck.
    The 2026-08-09 correction: the old "30-50 images per 275 slides" was wrong by
    ~28x. This is the rule whose violation produces the wall of type.

HOUSE RULES HELD
  * no em-dash character anywhere (U+2014). John's house style is `--`.
  * zero income claims about US. Client figures carry the client and the window.
  * the visible slide carries the SHORT form; the speaker note carries the spoken
    line verbatim. Presenter mode is how this gets read.
"""
import re, sys, pathlib

OUT = pathlib.Path(__file__).parent / "slides.md"

# ── the beat map ────────────────────────────────────────────────────────────
# (kicker, visible_headline, visible_sub_or_html, spoken_note, visual)
# visual: ("img", path) | ("svg", path) | ("css", html) | None  -> None must stay <=5%
B = []

def s(kicker, head, sub=None, note="", visual=None, cls="default"):
    B.append(dict(kicker=kicker, head=head, sub=sub, note=note, visual=visual, cls=cls))

# ─────────────────────────── A. PRE-OPEN ────────────────────────────────────
s("", "First, congrats.", "Seriously.",
  "First, congrats. Seriously.",
  ("img", "/gen/char-04-realising.png"), "bleed")
s("", "You stopped guessing.", None,
  "You stopped guessing.",
  ("css", '<div class="rt-big teal">STOPPED<br/>GUESSING</div>'), "peak text-center")
s("YOUR ROADMAP", "It's already being built.", "In your inbox shortly.",
  "Your roadmap is already being built.",
  ("svg", "/flows/02a_funnel_get_the_roadmap.svg"))
s("", "But before you go read it,", "give me four minutes.",
  "But before you go read it, give me four minutes.",
  ("css", '<div class="rt-big gold">4 MIN</div>'), "peak text-center")
s("", "There's a piece of it", "that won't make sense unless I explain this first.",
  "Because one piece of it will not make sense unless I explain this first.",
  ("img", "/gen8/n09_label_inside_the_jar.png"), "bleed")

# ───────────────── B. THE AREA IS NOT THE THING (the mansion) ───────────────
s("WHAT YOU JUST SAW", "Your results screen showed you an area.", None,
  "So. Your results screen just showed you an area.",
  ("svg", "/flows/bowtie_00_full.svg"))
s("THE FOUR AREAS", "Attention. Capture.", "Conversion. Delivery.",
  "Attention, capture, conversion, delivery. One of those lit up.",
  ("svg", "/flows/bowtie_01_conversion.svg"))
s("", "But an area", "is not a thing.",
  "But an area is not a thing.",
  ("css", '<div class="rt-duo"><div class="rt-old">AN AREA</div><div class="rt-new">A THING</div></div>'), "peak text-center")
s("", "It's like knowing", "a pipe is leaking in your house.",
  "It is like knowing a pipe is leaking somewhere in your house.",
  ("img", "/gen8/n10_blind_spot.png"), "bleed")
s("", "Somebody tells you:", '"It\'s in the west wing."',
  "And somebody tells you, it is in the west wing.",
  ("css", '<div class="rt-plate"><div class="rt-h2">"It\'s in the west wing."</div></div>'), "plate")
s("", "Okay.", "But which pipe?",
  "Okay. But which pipe?",
  ("css", '<div class="rt-big ember">WHICH<br/>PIPE?</div>'), "peak text-center")
s("", "The wing isn't the fix.", None,
  "Because the wing is not the fix.",
  ("css", '<div class="rt-big"><span class="rt-strike">THE WING</span></div>'), "peak text-center")
s("", "The fix is the one bolt", "you actually have to turn.",
  "The fix is the one bolt you actually have to turn.",
  ("img", "/gen/concept-09-audit-magnifier.png"), "bleed")
s("THE ZOOM", "The quiz gets you to the wing.", "It cannot get you to the bolt.",
  "The quiz gets you to the wing. It cannot get you to the bolt.",
  ("css", '<div class="rt-grid c3">'
          '<div class="rt-cell on">THE HOUSE</div>'
          '<div class="rt-cell on">THE WING</div>'
          '<div class="rt-cell leak">THE BOLT</div></div>'))
s("", "Say your area is conversion.", None,
  "Say your area came back as conversion.",
  ("svg", "/flows/bowtie_01_conversion.svg"))
s("INSIDE CONVERSION", "Is it the script?", "The pre-call framing? The headline? The order of the offer?",
  "Is it the script? The pre-call framing? The headline? The order you make the offer in?",
  ("css", '<div class="rt-grid c4"><div class="rt-cell">SCRIPT</div><div class="rt-cell">PRE-CALL FRAMING</div>'
          '<div class="rt-cell">HEADLINE</div><div class="rt-cell">OFFER ORDER</div></div>'))
s("THE EPIDEMIC", "There's an epidemic in this market.", None,
  "And this is what nobody is looking at. There is an epidemic in this market right now.",
  ("img", "/gen/concept-06-information-abundance.png"), "bleed")
s("", "I call it", "constraint blindness.",
  "I call it constraint blindness.",
  ("css", '<div class="rt-big gold">CONSTRAINT<br/>BLINDNESS</div>'), "peak text-center")
s("", "People are stuck.", "At 10K. At 50K. At 100K.",
  "People are stuck. At ten K, at fifty K, at a hundred K, wherever.",
  ("css", '<div class="rt-grid c3"><div class="rt-cell">$10K</div><div class="rt-cell">$50K</div><div class="rt-cell">$100K</div></div>'))
s("", "They can feel something's off.", "They can't see what it is.",
  "They can feel something is off. They cannot see what it is.",
  ("img", "/gen/char-01-stuck.png"), "bleed")
s("", "So they work harder", "on whatever's in front of them.",
  "So they work harder on whatever is in front of them.",
  ("img", "/gen8/n17_working_hard_right_things.png"), "bleed")
s("HOW IT ACTUALLY WORKS", "At any moment,", "your business has ONE constraint.",
  "Here is how it actually works. At any moment, your business has one constraint.",
  ("img", "/gen8/n08_one_constraint_gate.png"), "bleed")
s("", "Not five.", "Not twelve. One.",
  "Not five. Not twelve. One.",
  ("css", '<div class="rt-big">ONE</div>'), "peak text-center")
s("", "Fixing anything that isn't the constraint", "does nothing.",
  "Fixing anything that is not the constraint does nothing.",
  ("css", '<div class="rt-keynum">0</div><div class="rt-numlabel">what you get for fixing the wrong thing</div>'), "peak text-center")

# ─────────────────── E. THE CORE FOUR ───────────────────────────────────────
s("SO WHERE DOES IT LIVE?", "Four places.", "Market. Avatar. Offer. Pitch.",
  "So where does it live? Four places. Market, avatar, offer, pitch.",
  ("css", '<div class="rt-grid c4"><div class="rt-cell on">MARKET</div><div class="rt-cell on">AVATAR</div>'
          '<div class="rt-cell on">OFFER</div><div class="rt-cell on">PITCH</div></div>'))
s("MARKET", "Obvious: is it big enough.", "Invisible: what have they already been sold?",
  "Market. Obvious is, is it big enough. Invisible is what they have already been sold, and burned by.",
  ("css", '<div class="rt-duo"><div class="rt-old">IS IT BIG ENOUGH?</div>'
          '<div class="rt-new">WHAT HAVE THEY ALREADY BEEN SOLD?</div></div>'))
s("MARKET", "You're not fighting for attention.", "You're fighting a memory.",
  "If you are the fourth person to say the same thing, you are not fighting for attention. You are fighting a memory.",
  ("img", "/gen8/n15_market_moving_past.png"), "bleed")

s("AVATAR", "Obvious: demographics.", "Invisible: their criteria for saying yes.",
  "Avatar. Obvious is demographics. Invisible is their actual criteria for saying yes.",
  ("css", '<div class="rt-duo"><div class="rt-old">AGE. INCOME.</div>'
          '<div class="rt-new">CRITERIA FOR YES</div></div>'))
s("OFFER", "Obvious: price and deliverables.", "Invisible: the economics underneath.",
  "Offer. Obvious is price and deliverables. Invisible is the economics underneath. What a customer is worth, versus what you can spend to get one.",
  ("css", '<div class="rt-duo"><div class="rt-old">PRICE. DELIVERABLES.</div>'
          '<div class="rt-new">WHAT YOU CAN SPEND TO GET ONE</div></div>'))
s("PITCH", "Obvious: the script.", "Invisible: the ORDER.",
  "Pitch. Obvious is the script. Invisible is the order. Which belief lands before you ask.",
  ("css", '<div class="rt-duo"><div class="rt-old">THE SCRIPT</div><div class="rt-new">THE ORDER</div></div>'))
s("PITCH", "Ask too early?", 'It doesn\'t read as a bad offer.',
  "Ask before that belief is there, and it does not read as a bad offer.",
  ("css", '<div class="rt-plate"><div class="rt-h2">"I don\'t trust this guy."</div></div>'), "plate")
s("PITCH", "It reads as:", '"I don\'t trust this guy."',
  "It reads as, I do not trust this guy.",
  ("css", '<div class="rt-plate tall"><div class="rt-h1">"I don\'t trust<br/>this guy."</div></div>'), "plate")

s("AND A FIFTH", "Your personal profile.", "Sitting underneath all four.",
  "And a fifth underneath all of it. Your personal profile. What people think you are before you speak.",
  ("css", '<div class="rt-grid c4"><div class="rt-cell">MARKET</div><div class="rt-cell">AVATAR</div>'
          '<div class="rt-cell">OFFER</div><div class="rt-cell">PITCH</div></div>'
          '<div class="rt-cell on mt-4" style="width:100%">YOUR PERSONAL PROFILE</div>'))
s("", "You can't fix", "what you can't see.",
  "And you cannot fix what you cannot see. Which is why you do everything right and stay at the same number.",
  ("img", "/gen8/n10_blind_spot.png"), "bleed")

# ─────────────────── F. THE ROADMAP + THE GATE ──────────────────────────────
s("THE GOOD NEWS", "Your quiz answers already told us", "which one you're stuck behind.",
  "So that is the bad news. The good news is your quiz answers already told us which one you are stuck behind.",
  ("svg", "/flows/02a_roadmap_funnel_flow.svg"))
s("", "That's what the roadmap is.", "Not a generic PDF.",
  "That is what the roadmap is. Not a generic PDF.",
  ("css", '<div class="rt-duo"><div class="rt-old">A GENERIC PDF</div><div class="rt-new">YOUR SEQUENCE</div></div>'), "peak text-center")
s("", "What to fix first.", "What to leave alone. And the order.",
  "It is the sequence for your situation. What to fix first, what to leave alone, and the order.",
  ("css", '<div class="rt-grid c3"><div class="rt-cell on">FIX FIRST</div><div class="rt-cell">LEAVE FOR NOW</div><div class="rt-cell">THE ORDER</div></div>'))
s("", "Because the order matters", "way more than the effort.",
  "Because the order matters way more than the effort.",
  ("css", '<div class="rt-big teal">ORDER &gt; EFFORT</div>'), "peak text-center")
s("IT'S ON ITS WAY", "Your roadmap is already en route", "to your inbox.",
  "Your roadmap is already en route to your inbox.",
  ("svg", "/flows/02a_funnel_get_the_roadmap.svg"))
s("", "Do one thing first.", "Confirm your call.",
  "But do one thing before you open it. Confirm your call.",
  ("css", '<div class="rt-big gold">CONFIRM<br/>YOUR CALL</div>'), "peak text-center")
s("WHY IN THAT ORDER", "The roadmap gets you to the wing.", "The call gets you to the bolt.",
  "And the reason is simple. The roadmap gets you to the wing. The call gets you to the bolt.",
  ("css", '<div class="rt-grid c2"><div class="rt-cell on">ROADMAP<br/><span class="rt-fine">the wing</span></div>'
          '<div class="rt-cell leak">THE CALL<br/><span class="rt-fine">the bolt</span></div></div>'))
s("", "Book it now,", "then go read it properly.",
  "Book it now, then go read the whole thing. It will be there when you are done.",
  ("img", "/gen/char-05-deciding.png"), "bleed")

# ─────────────────── G. THE CALL / NEVER PITCH ──────────────────────────────
s("THE CALL", "We're opening a small number of seats.", "With me, or with Phoenix.",
  "We are opening a small number of seats. With me, or with Phoenix.",
  # Real faces, not a stock celebration. The first cut had char-06-winning here,
  # a figure with both fists in the air, directly under a line about being
  # SELECTIVE. The picture was cheering while the script was being restrained.
  # Both headshots were already in public/team/.
  # 🔴 SIZE IS PART OF THE ASSET CHOICE. First attempt used .rt-portrait at
  # width:100% in a 620px grid: 4/5 aspect made each one ~375px tall, the slide
  # overflowed, and the HEADLINE got pushed off the top of the frame. Round
  # portraits at a fixed 132px fit inside the remaining vertical space.
  ("css", '<div class="rt-grid c2" style="max-width: 420px; margin: 0 auto;">'
          '<div><img class="rt-portrait round" src="/team/john-headshot-direct.jpg" alt="John Coburn" '
          'style="width:132px; margin:0 auto;" />'
          '<div class="rt-name">John</div><div class="rt-role">Founder</div></div>'
          '<div><img class="rt-portrait round" src="/team/phoenix-headshot.png" alt="Phoenix" '
          'style="width:132px; margin:0 auto;" />'
          '<div class="rt-name">Phoenix</div><div class="rt-role">Partner</div></div></div>'))
s("", "Let me be really clear", "about what this call is NOT.",
  "And let me be really clear about what this call is not.",
  ("css", '<div class="rt-big ember">WHAT IT IS NOT</div>'), "peak text-center")
s("", "We are not going to pitch you", "a single fucking thing.",
  "We are not going to pitch you a single fucking thing on this call.",
  ("css", '<div class="rt-plate tall"><div class="rt-h1">Not a single<br/>fucking thing.</div></div>'), "plate")
s("", "And I mean that literally.", None,
  "And I mean that literally.",
  ("css", '<div class="rt-mark box">LITERALLY</div>'), "peak text-center")
s("", "We don't have enough information", "to know if it even makes sense.",
  "We do not have enough information to know if working together makes any sense.",
  ("img", "/gen8/n07_ai_cant_see_you.png"), "bleed")
s("", "And honestly?", "We don't want to work with everybody.",
  "And honestly, we do not want to work with everybody.",
  ("css", '<div class="rt-big">NOT EVERYBODY</div>'), "peak text-center")
s("", "That sounds like", "a nightmare.",
  "That sounds like a nightmare.",
  ("css", '<div class="rt-plate"><div class="rt-h1">That sounds like a nightmare.</div></div>'), "plate")
s("", "A small number of people, deeply.", "Not a lot of people, shallowly.",
  "We would rather work with a few people deeply than a lot of people shallowly. Better upside, less complicated.",
  ("css", '<div class="rt-duo"><div class="rt-old">MANY, SHALLOW</div><div class="rt-new">FEW, DEEP</div></div>'), "peak text-center")
s("", "Which means most people", "who get on these calls, we don't work with.",
  "So most people who get on these calls, we do not work with. That is fine. That is the point.",
  ("css", '<div class="rt-mark">THAT IS THE POINT</div>'), "peak text-center")

s("SO WHAT HAPPENS", "We ask the questions", "the quiz couldn't ask.",
  "So here is what happens instead. We ask the questions the quiz could not.",
  ("img", "/gen/concept-09-audit-magnifier.png"), "bleed")
s("", "We pressure-test the roadmap", "against your real numbers.",
  "We pressure-test the roadmap against your real numbers.",
  ("css", '<div class="rt-grid c2"><div class="rt-cell">THE ROADMAP</div><div class="rt-cell on">YOUR REAL NUMBERS</div></div>'))
s("THE DELTAS", "Where you are now.", "Where you want to be.",
  "We work off two gaps. Revenue now versus where you want it. Hours in the business now versus where you want that.",
  ("css", '<div class="rt-grid c2"><div class="rt-cell">REVENUE NOW<br/><span class="rt-fine">to goal</span></div>'
          '<div class="rt-cell">HOURS NOW<br/><span class="rt-fine">to goal</span></div></div>'))
s("", "Then we build you", "a 30, 60, 90 day plan. On the call.",
  "Then we build you a thirty, sixty, ninety day plan. On the call.",
  ("svg", "/flows/02b_funnel_the_call.svg"))
s("", "We reverse-engineer it backwards", "from your actual goal.",
  "We take your actual goal and reverse-engineer it backwards. Ninety days, sixty, thirty, down to what you do daily.",
  ("css", '<div class="rt-grid c4"><div class="rt-cell">GOAL</div><div class="rt-cell">90</div>'
          '<div class="rt-cell">60</div><div class="rt-cell on">30</div></div>'))
s("", "That's the deliverable.", "You leave with it either way.",
  "That is the deliverable. You leave with it whether we speak again or not.",
  ("css", '<div class="rt-mark good">YOURS EITHER WAY</div>'), "peak text-center")

# ─────────────────── H. THE AUDIT BRANCH + PROOF ────────────────────────────
s("AND WHERE IT FITS", "Where it makes sense,", "we branch into an audit.",
  "And where it makes sense, we branch into an audit.",
  ("css", '<div class="rt-grid c3"><div class="rt-cell on">ADS</div><div class="rt-cell on">EMAIL</div><div class="rt-cell on">CRM</div></div>'))
s("", "Ads. Email. CRM.", "Depending on where the constraint actually is.",
  "Ads, email, or CRM. Depends on where the constraint actually is.",
  ("svg", "/flows/03_bowtie_overlay.svg"))
s("", "Because otherwise", "we're just throwing random shit at you.",
  "Because unless we know that, we are just throwing random shit at you.",
  ("img", "/gen8/n05_stack_of_attempts.png"), "bleed")
s("PROOF", "Chris. Coaching business.", "$2.4M in attributed email revenue.",
  "Chris ran a coaching business. The pieces were there, they just were not talking to each other. We rebuilt the email infrastructure and ran the reactivation. Two point four million in attributed email revenue. Same list, same offer.",
  ("css", '<div class="rt-proofcard"><div class="rt-keynum">$2.4M</div>'
          '<div class="rt-numlabel">attributed email revenue &middot; Chris, coaching</div>'
          '<div class="rt-fine mt-3">Same list. Same offer. Client result, not ours.</div></div>'))
s("PROOF", "A tutoring company.", "$1.07M closed-won in 19 months.",
  "And a tutoring company. One point oh seven million closed-won, January twenty twenty five to July twenty twenty six. Around eighty percent traces back to paid social.",
  ("css", '<div class="rt-proofcard"><div class="rt-keynum">$1.07M</div>'
          '<div class="rt-numlabel">closed-won &middot; Jan 2025 to Jul 2026</div>'
          '<div class="rt-fine mt-3">~80% traces to paid social. Client result, not ours.</div></div>'))
s("", "Every deal we can trace,", "we trace to an ad.",
  "Every deal we can trace, we trace to an ad. The ones we cannot, we do not claim.",
  ("css", '<div class="rt-plate"><div class="rt-h2">The ones we can\'t trace, we don\'t claim.</div></div>'), "plate")

s("ONE OPTIONAL THING", "After you book,", "give us view-only access to your ad account.",
  "One optional thing. After you book, we send a link for view-only access to your ad account.",
  ("css", '<div class="rt-grid c2"><div class="rt-cell on">VIEW ONLY</div><div class="rt-cell leak">NO SPEND. NO CHANGES.</div></div>'))
s("", "We show up", "with the diagnosis half-built.",
  "Then we go through your account before the call. So we are not spending twenty minutes asking what your CPA is. We show up with the diagnosis half built.",
  ("img", "/gen/concept-09-audit-magnifier.png"), "bleed")
s("", "No ads running?", "Send your funnel link or your last three emails.",
  "Not running ads? Send your funnel link or your last three emails.",
  ("css", '<div class="rt-card gate"><div class="rt-h2">Funnel link, or your last three emails.</div></div>'))

# ─────────────────── I. FINAL CTA ───────────────────────────────────────────
s("", "You're not spending money here.", "You're spending 30 minutes.",
  "So you are not spending money here. You are spending thirty minutes.",
  ("css", '<div class="rt-big teal">30 MINUTES</div>'), "peak text-center")
s("", "Ninety days pass either way.", None,
  "Ninety days pass either way.",
  ("img", "/gen/concept-08-two-roads.png"), "bleed")
s("", "Ninety days older.", "Or ninety days older holding a plan you executed.",
  "You are either ninety days older, or ninety days older and past the thing holding you.",
  ("css", '<div class="rt-duo"><div class="rt-old">90 DAYS OLDER</div>'
          '<div class="rt-new">90 DAYS OLDER<br/>+ PAST IT</div></div>'), "peak text-center")
s("", "The only difference", "is what you do in the next ten seconds.",
  "The only difference is what you do in the next ten seconds.",
  ("css", '<div class="rt-big gold">10 SECONDS</div>'), "peak text-center")
s("", "Button's below.", "Pick a time.",
  "Button is below. Pick a time.",
  ("css", '<div class="rt-mark box">PICK A TIME</div>'), "peak text-center")
s("", "Then go read your roadmap.", "I'll see you on the call.",
  "Then go and read your roadmap. I will see you on the call.",
  ("img", "/gen/char-06-winning.png"), "bleed")


# ── emit ────────────────────────────────────────────────────────────────────
HEAD = '''---
theme: default
title: Post-Quiz VSL -- Constraint Blindness (Fladlien cut)
info: |
  POST-QUIZ VSL -- "CONSTRAINT BLINDNESS". Fladlien 400-slide-hack cut.

  PLACEMENT: quiz results page, immediately after submission. GOAL: book a call.

  SOURCE SCRIPT (verbatim, John): ai-os/03_Funnels_and_VSLs/roadmap_sage/
    SCRIPT_post_quiz_vsl_constraint_blindness_2026_08_16.md
  BUILD NOTES + the cut list: NOTES_post_quiz_vsl_build_2026_08_16.md

  HOW TO USE IT: every spoken word is in the speaker notes of the slide it belongs
  to, in order. Open presenter mode and READ THE NOTES. The visible slide carries
  the short form. Generated by build.py -- edit the beat map there, not here.

  CLAIM RULES HELD: zero income claims about us. Both client figures carry the
  client and the window. "Every deal we can trace" replaces "literally every deal",
  which measurement did not support (210 of 257, ~80%).
class: peak text-center
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  persist: false
transition: none
mdc: true
fonts:
  provider: none
layout: center
---

<!-- slide:00 -- HOLDING SLIDE, never on camera -->

<div class="rt-kicker">POST-QUIZ VSL &middot; PRESENTER NOTES CARRY THE SCRIPT</div>
<div class="rt-h1 mt-2">Constraint Blindness</div>
<div class="rt-sub mt-8">Press <strong>P</strong> for presenter mode. Read the notes.</div>

<!--
HOLDING SLIDE. Do not start the recording on this. Advance once, then hit record.
Nothing is spoken here.
-->
'''

def esc(t):
    return t if t else ""


# ── 🔴 ASSET EXISTENCE GATE ─────────────────────────────────────────────────
# Slidev resolves /foo.svg against public/ at BUILD time, so a wrong directory is
# not a broken image on screen -- it is a hard build failure 60 seconds later, or
# worse, a silent blank on a slide nobody re-checked. Two of these shipped in the
# first pass of this very file (/funnels/ for a file that lives in /flows/, and a
# stray /team/../gen/ path). Fail here instead, where the fix is obvious.
PUB = pathlib.Path(__file__).parent / "public"
missing = []
for i, b in enumerate(B, 1):
    v = b["visual"]
    if not v:
        continue
    if v[0] in ("img", "svg"):
        if not (PUB / v[1].lstrip("/")).exists():
            missing.append((i, v[1]))
    elif v[0] == "css":
        # 🔴 css blocks can carry <img src=...> too, and the first version of this
        # gate did not look inside them -- so the very next edit (real headshots in
        # a css grid) slipped straight past the check built to catch exactly that.
        # A guard that only covers the case you thought of is not a guard.
        for m in re.findall(r'src="([^"]+)"', v[1]):
            if m.startswith("/") and not (PUB / m.lstrip("/")).exists():
                missing.append((i, m))
if missing:
    print("\n🔴 MISSING ASSETS -- refusing to write slides.md:")
    for i, p in missing:
        print(f"   slide {i:02d}  {p}")
    sys.exit(1)

out = [HEAD]
for i, b in enumerate(B, start=1):
    cls = b["cls"]
    if cls == "bleed":
        fm = "---\nlayout: default\nclass: bleed\n---\n"
    elif cls == "plate":
        fm = "---\nlayout: default\nclass: plate text-center\n---\n"
    elif cls.startswith("peak"):
        fm = f"---\nlayout: default\nclass: {cls}\n---\n"
    else:
        fm = "---\nlayout: default\n---\n"

    body = [f"\n<!-- slide:{i:02d} -->\n"]
    vis = b["visual"]

    if vis and vis[0] == "img":
        # 🔴 THE GOLDEN'S BLEED PATTERN, and the first pass got it wrong.
        # .rt-scrim is a 90deg gradient: 94% opaque at the LEFT edge, 10% at the
        # right. So it creates a dark PANEL on one side, not an even wash. The
        # text has to be CONFINED to that panel. v1 of this generator dropped a
        # full-width h1 across the whole frame, so on any image carrying its own
        # labels (the flow diagrams, the stage charts) the headline landed on top
        # of the diagram's own type. That is the "images inserted in a strange
        # way" defect, reproduced exactly.
        # Golden reference: roadmap_vsl_2026_08_05/slides_v8.md slides 15 and 48.
        # Sides alternate so 30 bleeds in a row do not read as one long slide.
        right = (i % 2 == 0)
        scrim = "rt-scrim-r" if right else "rt-scrim"
        align = "items-end" if right else "items-start"
        ta = "right" if right else "left"
        body.append(f'<img class="rt-bleed" src="{vis[1]}" alt="{esc(b["head"])}" />')
        body.append(f'<div class="{scrim}"></div>')
        body.append(f'<div class="relative h-full flex flex-col justify-center {align}" style="padding: 0 3.2rem;">')
        body.append(f'  <div style="max-width: 54%; text-align: {ta};">')
        if b["kicker"]:
            body.append(f'    <div class="rt-kicker" style="color: var(--tealb);">{esc(b["kicker"])}</div>')
        body.append(f'    <div class="rt-h1 rt-onimg">{esc(b["head"])}</div>')
        if b["sub"]:
            body.append(f'    <div class="rt-sub rt-onimg mt-6" v-click style="color: var(--parch);">{esc(b["sub"])}</div>')
        body.append('  </div>')
        body.append('</div>')
    else:
        if b["kicker"]:
            body.append(f'<div class="rt-kicker">{esc(b["kicker"])}</div>')
        body.append(f'<div class="rt-h1 mt-2">{esc(b["head"])}</div>')
        # 🔴 ANIMATE THE PAYOFF, NOT THE PICTURE. v1 put v-click on the figure, so
        # every non-bleed slide ARRIVED as a headline floating in an empty frame and
        # only became composed after a click. On a recorded VSL that is most of the
        # frames most of the time. The visual is the slide; the sub is the reveal.
        # Where there is no sub, the visual takes the click so the Fladlien
        # "every slide animates" rule still holds.
        click_sub = ' v-click' if b["sub"] else ''
        click_vis = '' if b["sub"] else ' v-click'
        if b["sub"]:
            body.append(f'<div class="rt-sub mt-6"{click_sub}>{esc(b["sub"])}</div>')
        if vis and vis[0] == "svg":
            # 🔴 CONSTRAIN THE HEIGHT, NOT JUST THE WIDTH. max-width alone let the
            # bow-tie SVGs render tall enough to push the headline out of the frame
            # on slides 7, 8 and 16. A slide is a fixed box; an image inside it needs
            # both dimensions bounded or the text is what gives way.
            body.append(f'<div class="rt-figure mt-6"{click_vis}>'
                        f'<img src="{vis[1]}" alt="{esc(b["head"])}" '
                        f'style="max-width: 720px; max-height: 44vh; width: auto; margin: 0 auto; object-fit: contain;" />'
                        f'</div>')
        elif vis and vis[0] == "css":
            body.append(f'<div class="mt-8"{click_vis}>{vis[1]}</div>')

    body.append(f"\n<!--\n{b['note']}\n-->\n")
    out.append(fm + "\n".join(body))

OUT.write_text("\n".join(out))

# ── self-check against the house rules ──────────────────────────────────────
txt = OUT.read_text()
n = len(B)
bare = sum(1 for b in B if b["visual"] is None)
words = sum(len(b["note"].split()) for b in B)
emdash = txt.count("—")
print(f"slides           : {n} (+1 holding)")
print(f"spoken words     : {words}  ->  {words/155:.1f} min at 155 wpm")
print(f"bare text slides : {bare}  ({100*bare/n:.1f}%)   [rule: <=5%]")
print(f"em-dash chars    : {emdash}   [rule: 0]")
over = [(i, len(b['head'].split()) + len((b['sub'] or '').split()))
        for i, b in enumerate(B, 1) if len(b['head'].split()) + len((b['sub'] or '').split()) > 15]
print(f"slides >15 visible words: {len(over)}  {over[:8]}")
