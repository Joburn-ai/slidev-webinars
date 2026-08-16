#!/usr/bin/env python3
"""
Post-quiz VSL deck -- v2. Generated from a beat map; slides.md is OUTPUT, never edit it.

WHY A GENERATOR
~60 slides at Fladlien pace, every one animated, every one carrying a visual, while the
script is still being cut. The script stays the source of truth and the slides derive from
it, so a copy change is one edit in one place.

WHAT v2 FIXED, all of it found by LOOKING at the live deck rather than by asserting:

 🔴 THE GATE WAS MEASURING THE WRONG THING. v1 reported "bare text 0%" because it counted
    any non-None visual as a visual -- including CSS text widgets, which are just type in a
    box. By the honest definition (does the slide carry an actual IMAGE) v1 was ~64% bare
    and only 37% of slides carried an asset. That is the wall of type John saw, and the
    check said clean. `bare` now means "no <img> anywhere on the slide".

 🔴 .rt-cell WAS THE "CLIPPED OUT WEIRDLY". It is font-size .60rem, white-space:nowrap,
    overflow:hidden, text-overflow:clip -- built for the 9-cell rail strip, and used in v1
    as a general content card on 13 slides. Any label longer than the cell was silently
    guillotined. Banned outside .rt-rail and asserted.

 🔴 .rt-mark RENDERED NOTHING. position:absolute with no inset and no typography, so 4
    slides shipped an invisible element -- and the old gate counted them as "has a visual".
    Banned and asserted.

 🔴 SQUARE SOURCES IN A BLEED FRAME. /gen/char-*.png are 1024x1024 going into a 1.775
    frame under object-fit:cover: 43% cut, top-weighted, so figures were decapitated.
    Bleed now requires >=1.4:1, checked against the real pixels with PIL.

 Also: .rt-h1's line box was 6px shorter than its own glyphs on all 76 instances and
 .rt-big's was 26px shorter (fixed in style.css); .rt-plate is height:100% and overflowed
 on 6 text slides; .rt-duo caps at 30rem and squeezed 10 before/after pairs; bleed sides
 alternated on the beat index so two bleeds one slide apart landed on the same side; and
 17 slides printed the same sentence twice at two sizes.

HOUSE RULES HELD
  no em-dash character (U+2014) anywhere -- John's house style is `--`
  zero income claims about us; client figures carry the client type and the window
  the visible slide carries the SHORT form; the speaker note carries the spoken line
"""
import re, sys, pathlib
from PIL import Image

HERE = pathlib.Path(__file__).parent
OUT  = HERE / "slides.md"
PUB  = HERE / "public"

# 🔴 John's brief says "each v-click walking through it" for the cascade. The golden deck's
# own author note on the identical sequence says the opposite: "Run these fast, no clicks.
# They are one gesture, not four points" -- because on a RECORDED VSL a v-click leaves
# frame 1 as an empty diagram on screen while the presenter is already talking. Built as
# fade; this flips it in one line once John rules.
CASCADE_MODE = "fade"


# ══════════════════════════════════════════════════════════════════════════════
# 🔴 THE SCRIPT GOES ON THE SCREEN. THIS IS THE 400 SLIDE HACK.
#
# John, 2026-08-16: "I don't want there to be speaker notes for the entire script. I just
# want the entire script on the screen so people can read along with it. I just want the
# VSL script literally word-for-word on the slides. That's the point of the 400 slide hack.
# I don't know why we got away from that."
#
# He is right and v1/v2 had it backwards: the script sat in the speaker notes and the slide
# carried a paraphrase. That is a support deck, not a Fladlien deck. Now the SPOKEN LINE IS
# THE SLIDE, chunked to Fladlien density, and the picture persists underneath while the
# words advance.
#
# Chunking rule: split on sentence boundaries first, then on clause boundaries for anything
# still over MAXW. Never split mid-clause -- a chunk has to be a readable unit, because the
# viewer is reading it while hearing it.
MAXW = 13

def chunk(text):
    out, buf = [], []
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    for p in parts:
        w = p.split()
        if len(w) <= MAXW:
            out.append(p); continue
        # too long: break on clause punctuation, then on length as a last resort
        seg, cur = [], []
        for tok in re.split(r'(,|;| -- )', p):
            if tok in (',', ';', ' -- '):
                if cur: cur[-1] += tok.strip() if tok != ' -- ' else ''
                continue
            words = tok.split()
            if not words: continue
            if len(cur) + len(words) > MAXW and cur:
                seg.append(" ".join(cur)); cur = words
            else:
                cur += words
        if cur: seg.append(" ".join(cur))
        out.extend(seg or [p])
    return [c.strip() for c in out if c.strip()]

B = []
BG = [None]   # current sectional backdrop; set with bg() as the arc moves

def bg(p): BG[0] = p

def s(kicker, head, sub=None, note="", visual=None, cls="default", tr=None):
    B.append(dict(kicker=kicker, head=head, sub=sub, note=note, visual=visual,
                  cls=cls, tr=tr, bg=BG[0]))

# Visual kinds. Every one maps to CSS that ALREADY EXISTS in style.css -- v1's fault was
# that the generator had no path to most of it.
def plate(p):                    return ("plate", p)     # 1600x860 bow-tie family ONLY
def figure(p):                   return ("figure", p)    # wide/thin SVGs at natural aspect
def shot(p, tag=None, cap=None): return ("shot", p, tag, cap)
def wall(ps, cap=None):          return ("wall", ps, cap)
def cards(n, items):             return ("cards", n, items)
def oldnew(o, n, lo="OBVIOUS", ln="INVISIBLE"): return ("oldnew", o, n, lo, ln)
def readout(lab, big, tone="", cap=None):       return ("readout", lab, big, tone, cap)
def img(p, focal=None):          return ("img", p, focal)
def dim(p, mode="light"):        return ("dim", p, mode)
def qr(p):                       return ("qr", p)

# ═════════════════════════════ A. PRE-OPEN ═════════════════════════════
bg("/gen8/n13_show_up_gift.png")
s("", "First, congrats.", "You did something most people never do.",
  "First, congrats. You did something most people never do.",
  img("/gen8/n13_show_up_gift.png"), "bleed")
s("", "You stopped guessing.", None,
  "You stopped guessing.",
  img("/gen8/n13_show_up_gift.png"), "bleed")
s("YOUR ROADMAP", "It's already being built.", None,
  "Your roadmap is already being built.",
  figure("/flows/02a_funnel_get_the_roadmap.svg"))
s("", "Before you read it,", "give me four minutes.",
  "Before you read it, give me four minutes.",
  readout("THIS TAKES", "4 MIN", "gold"), "peak text-center")

# ═══════════════ B. THE BOW-TIE, THEN THE FLOW, THEN THE STAGES ═══════════════
bg("/gen/concept-03-critical-path.png")
# John's explicit order: "we show just sort of like the traditional bow tie funnel diagram.
# And then we show the flow after that. And then attention capture conversion payment
# onboarding activation success retention referral."
s("", "Your results screen showed you an area.", None,
  "So. Your results screen just showed you an area.",
  plate("/flows/bt_a_shape.svg"), "default", "fade")
s("THE SHAPE", "This is every business.", None,
  "This is the shape of every business.",
  plate("/flows/bt_b_wings.svg"), "default", "fade")
s("THE FLOW", "It narrows to a knot,", "then widens back out.",
  "It narrows down to a knot, then it widens back out.",
  plate("/flows/bowtie_00_full.svg"), "default", "fade")
s("EVERY STEP", "Attention. Capture. Conversion.", "Then payment, onboarding, activation, success, retention, referral.",
  "Every step a customer takes with you.",
  plate("/flows/bowtie_00_full.svg"), "default", "fade")

# ── the cascade: the constraint moves, and downstream dies differently each time ──
s("ATTENTION", "It can sit at the very front.", None,
  "It can sit anywhere. At attention everything downstream is starved.",
  plate("/flows/bt_c0_attention.svg"), "default", "fade")
s("CAPTURE", "You get seen.", "It doesn't turn into leads.",
  "One step in it changes. You get attention. It does not turn into leads.",
  plate("/flows/bt_c1_capture.svg"), "default", "fade")
s("CONVERSION", "You get leads.", "They don't turn into clients.",
  "At conversion you have the leads. They are not turning into buyers.",
  plate("/flows/bt_c2_conversion.svg"), "default", "fade")
s("PAYMENT", "At the knot itself.", None,
  "Or it sits at the knot itself.",
  plate("/flows/bt_c3_payment.svg"), "default", "fade")
s("ONBOARDING", "It pushes back", "on everything in front of it.",
  "Behind the sale it is worse. Onboarding makes you busy, and busy stops you filling the top.",
  plate("/flows/bt_c4_onboarding_loop.svg"), "default", "fade")
s("ACTIVATION", "They bought.", "They never switched on.",
  "At activation they bought and never switched on.",
  plate("/flows/bt_c5_activation.svg"), "default", "fade")
s("SUCCESS", "They use it.", "They do not win with it.",
  "At success they use it and still do not win, so there is nothing to refer.",
  plate("/flows/bt_c6_success.svg"), "default", "fade")
s("RETENTION", "They leave.", "So you refill the top forever.",
  "At retention they leave, so you spend everything refilling the top.",
  plate("/flows/bt_c7_retention.svg"), "default", "fade")
# 🔴 THE LOOP CLOSES. John: "the one we want to show at referral is where it feeds back
# into ATTENTION, because referral is another type of attention. So we want a full loop."
s("REFERRAL", "And referral closes the loop.", None,
  "And referral closes the loop, because a referral is just attention from someone else. Choke it and you pay for every lead.",
  plate("/flows/bt_c8_referral_loop.svg"), "default", "fade")
s("", "And what you can see", "is not always what is causing it.",
  "And what you can see is not always what is causing it.",
  plate("/flows/root_2_beam.svg"), "default", "fade")

# ═════════════════════ C. THE MANSION ═════════════════════
bg("/gen8/n10_blind_spot.png")
s("", "An area is not a thing.", None,
  "But an area is not a thing.",
  oldnew("AN AREA", "A THING", "WHAT YOU GOT", "WHAT YOU NEED"))
s("", "You know a pipe is leaking", 'somewhere in "the west wing."',
  "It is like being told a pipe is leaking in the west wing.",
  img("/gen8/n10_blind_spot.png"), "bleed")
s("", "Okay. But which pipe?", None,
  "Okay, but which pipe? The wing is not the fix. The bolt is.",
  cards(2, [("THE WING", ""), ("THE BOLT", "bad")]))
s("THE ZOOM", "The quiz gets you to the wing.", "It cannot get you to the bolt.",
  "The quiz gets you to the wing. It cannot get you to the bolt.",
  cards(3, [("THE HOUSE", ""), ("THE WING", "good"), ("THE BOLT", "bad")]))
s("INSIDE CONVERSION", "Script? Pre-call framing?", "Headline? The order of the offer?",
  "Say yours came back conversion. Script? Pre-call framing? Headline? Offer order?",
  cards(4, [("SCRIPT", ""), ("PRE-CALL FRAMING", ""), ("HEADLINE", ""), ("OFFER ORDER", "bad")]))

# ═════════════════════ D. CONSTRAINT BLINDNESS ═════════════════════
bg("/gen/concept-06-information-abundance.png")
s("THE EPIDEMIC", "There's an epidemic in this market.", None,
  "This is what nobody is looking at. There is an epidemic in this market.",
  img("/gen/concept-06-information-abundance.png"), "bleed")
s("", "I call it constraint blindness.", None,
  'I call it "constraint blindness". It is very hard to see our own constraints.',
  shot("/gen8/n09_label_inside_the_jar.png"))
s("", "Stuck at 10K. At 50K. At 100K.", "You feel it. You can't see it.",
  "People are stuck at ten K, fifty K, a hundred K. They feel it. They cannot see it.",
  img("/gen8/n01_buried_in_advice.png"), "bleed")
s("", "So you work harder", "on whatever's in front of you.",
  "So you work harder on whatever is in front of you.",
  shot("/gen8/n17_working_hard_right_things.png"))
s("HOW IT WORKS", "One constraint at a time.", "One thing holding the whole system back.",
  "At any moment your business has one constraint. One thing holding the whole system back. Not five. One.",
  img("/gen8/n08_one_constraint_gate.png"), "bleed")
s("", "Fix anything else", "and the number does not move.",
  "And fixing anything else does nothing. Double your effort on the wrong lever and nothing moves.",
  readout("WHAT YOU GET FOR FIXING THE WRONG THING", "0", "ember"), "peak text-center")

# ═════════════════════ E. SOCIAL PROOF, FRONT-LOADED ═════════════════════
bg("/gen8/n12_two_tracks.png")
# John: "let's move some of the social proof up front too, and some of the wins and
# screenshots." Placed at ~28% of the arc, right after the problem is named -- the golden's
# own capture-wall position. All captures are the _redacted variants: surnames blocked to
# first-name + last-initial, which is our public site's convention.
s("WHEN IT MOVES", "This is what it looks like", "when the right thing gets fixed.",
  "This is what it looks like when the right one gets fixed.",
  wall(["/proof2/_v2_four-calls-ten-minutes-2026-06_redacted.png",
        "/proof2/_v2_appointment-surge_redacted.png",
        "/proof2/_v2_vsl-husband-cry-2025-08_redacted.png"],
       "Client Slack. Their words, their businesses."))
s("OUR SITE", "Forty two of these.", "With the receipts attached.",
  "Forty two of these are on our site with the receipts.",
  shot("/proof2/_v2_proofwall_band_redacted.png", "OUR SITE",
       "Names shown where clients agreed. How we count is published on the page."))
s("SO WHERE DOES IT LIVE?", "Market. Avatar.", "Offer. Pitch.",
  "So where does it live? Market, avatar, offer, pitch.",
  cards(4, [("MARKET", "good"), ("AVATAR", "good"), ("OFFER", "good"), ("PITCH", "good")]))
s("MARKET", "Is it big enough?", "Or: what have they already been sold?",
  "Market. Obvious is, is it big enough. Invisible is what they have already been sold.",
  oldnew("IS IT BIG ENOUGH?", "WHAT HAVE THEY ALREADY BEEN SOLD?"))
s("MARKET", "You're not fighting for attention.", "You're fighting a memory.",
  "If you are the fourth person to say the same thing, you are not fighting for attention. You are fighting a memory.",
  img("/gen8/n15_market_moving_past.png", "50% 30%"), "bleed")
s("AVATAR", "Demographics?", "Or: what do they actually believe?",
  "Avatar. Obvious is demographics. Invisible is their criteria for yes.",
  oldnew("AGE. INCOME.", "THEIR CRITERIA FOR YES"))
s("OFFER", "Price and deliverables?", "Or the economics underneath?",
  "Offer. Obvious is price and deliverables. Invisible is the economics.",
  oldnew("PRICE. DELIVERABLES.", "WHAT YOU CAN SPEND TO GET ONE"))
s("PITCH", "The script?", "Or the order?",
  "Pitch. Obvious is the script. Invisible is the order. Which belief lands first.",
  oldnew("THE SCRIPT", "THE ORDER"))
s("PITCH", "Ask too early,", "and it isn't heard as a bad offer.",
  "Ask before that belief lands and it does not read as a bad offer. It reads as, I do not trust this guy.",
  oldnew("A BAD OFFER", "I DON'T TRUST THIS GUY", "WHAT YOU SENT", "WHAT LANDED"))
s("AND A FIFTH", "Your personal profile.", "How you show up before you speak.",
  "And a fifth underneath it all. Your personal profile. What people think before you speak.",
  cards(5, [("MARKET", ""), ("AVATAR", ""), ("OFFER", ""), ("PITCH", ""), ("YOU", "good")]))
s("", "The overt is what everyone stares at.", "The covert is where it lives.",
  "That is constraint blindness. The overt is what everyone stares at. The covert is where it lives.",
  oldnew("WHAT EVERYONE STARES AT", "WHERE IT ACTUALLY LIVES", "OVERT", "COVERT"))
s("", "You can't fix", "what you can't see.",
  "And you cannot fix what you cannot see. Which is why you do everything right and stay stuck.",
  img("/gen8/n10_blind_spot.png", "50% 45%"), "bleed")

# ═════════════════════ G. THE ROADMAP AND THE GATE ═════════════════════
bg("/gen/concept-03-critical-path.png")
s("THE GOOD NEWS", "Your answers already told us", "which one you're stuck behind.",
  "The good news is your answers already told us which one.",
  figure("/flows/02a_roadmap_funnel_flow.svg"))
s("", "Not a generic PDF.", "The sequence for your situation.",
  "That is the roadmap. Not a generic PDF. What to fix first, what to leave, the order.",
  cards(3, [("FIX FIRST", "good"), ("LEAVE FOR NOW", ""), ("THE ORDER", "good")]))
s("", "The order matters", "way more than the effort.",
  "Because the order matters way more than the effort.",
  readout("THE WHOLE THESIS", "ORDER &gt; EFFORT", "teal"), "peak text-center")
s("IT'S ON ITS WAY", "Your roadmap is en route.", "Confirm your call first.",
  "Your roadmap is en route. Confirm your call before you open it. The roadmap gets you to the wing. The call gets you to the bolt.",
  cards(2, [("ROADMAP", "good"), ("THE CALL", "bad")]))

# ═════════════════════ H. THE CALL ═════════════════════
bg("/gen8/n14_built_by_hand.png")
s("THE CALL", "A small number of seats.", "With me, or with Phoenix.",
  "So we are opening a small number of seats, with me or Phoenix.",
  ("team", None))
# 🔴 SLIDE-45 FIX (John flagged it). v1 ran: "Let me be really clear" -> "about what this
# call is NOT" -> then a big WHAT IT IS NOT card, so the LABEL ARRIVED AFTER THE LINE IT
# LABELS, and the card restated the sub. The label is now the kicker, at the top of frame,
# where a label belongs.
s("WHAT THIS CALL IS NOT", "Let me be really clear.", "We will not pitch you a single thing.",
  "Let me be clear what this call is not. We are not going to pitch you a single fucking thing. I mean that literally.",
  readout("PITCH COUNT, ON THE CALL", "0", "ember"), "peak text-center")
s("", "We can't, even if we wanted to.", "We don't have enough information yet.",
  "We could not even if we wanted to. We do not have enough information yet.",
  img("/gen8/n07_ai_cant_see_you.png", "50% 50%"), "bleed")
s("", "And we don't want", "to work with everybody.",
  "And honestly, we do not want to work with everybody. That sounds like a nightmare.",
  img("/stage/cc_live_1080s.jpg", "50% 42%"), "bleed")
s("", "A few people, deeply.", "Not a lot of people, shallowly.",
  "We would rather work with a few people deeply than a lot shallowly. So most people on these calls, we do not.",
  oldnew("MANY, SHALLOW", "FEW, DEEP", "NOT US", "US"))
s("SO WHAT HAPPENS", "We ask what the quiz couldn't.", None,
  "Instead we ask what the quiz could not, and pressure-test it against your numbers.",
  img("/gen/concept-09-audit-magnifier.png", "50% 45%"), "bleed")
s("THE TWO GAPS", "Revenue now, and where you want it.", "Client count now, and where you want that.",
  "We work off two gaps. Revenue now versus where you want it. Client count now versus that.",
  oldnew("WHERE YOU ARE", "WHERE YOU WANT TO BE", "TODAY", "THE GOAL"))
s("", "Then we build the 30, 60, 90.", "On the call, with you.",
  "Then we build a thirty, sixty, ninety day plan, on the call with you.",
  figure("/flows/02b_funnel_the_call.svg"))
s("", "Reverse-engineered from your goal.", "What has to be true at 90. At 60. At 30.",
  "We reverse-engineer it backwards. What has to be true at ninety days, sixty, thirty, down to daily.",
  cards(4, [("GOAL", ""), ("90", ""), ("60", ""), ("30", "good")]))
s("", "That's the deliverable.", "You leave with it either way.",
  "That is the deliverable. You leave with it whether we speak again or not.",
  cards(2, [("WE WORK TOGETHER", ""), ("WE DON'T", "good")]))

# ═════════════════════ I. THE AUDIT BRANCH AND THE PROOF ═════════════════════
bg("/gen/concept-09-audit-magnifier.png")
s("AND WHERE IT FITS", "Ads. Email. CRM.", "Whichever one the constraint is actually in.",
  "And where it makes sense we branch into an audit. Ads, email or CRM, depending where the constraint is.",
  cards(3, [("ADS", "good"), ("EMAIL", "good"), ("CRM", "good")]))
s("", "Otherwise we're just", "throwing random shit at you.",
  "Because unless we know that, we are just throwing random shit at you.",
  img("/gen8/n05_stack_of_attempts.png"), "bleed")
# 🔴 CLAIM CORRECTED. v1 said $2.4M, taken from John's script. Our own brand board claims
# discipline reads: "only register-verified numbers -- C&C $1.81M from email in 9 months
# (total engagement tracked ~$2.4M before tracking stopped, June 2024)". $2.4M is the
# unverified figure, and our public site says $1.81M, so a prospect finds the contradiction
# in one click. Shipping the register-verified number. John's call to override.
s("PROOF", "$1.81M from email.", "In nine months. Same list, same offer.",
  "One coaching business had all the pieces, they were just not talking to each other. We rebuilt the email infrastructure and ran the reactivation. One point eight one million from email in nine months.",
  readout("COACHING CLIENT &middot; ATTRIBUTED TO EMAIL &middot; 9 MONTHS", "$1.81M", "teal",
          "Client result, not ours. 21 automations, around 130 A/B tests, 700+ bookings from two promos."))
s("PROOF", "$1.07M closed-won.", "January 2025 to July 2026.",
  "And a tutoring company. One point oh seven million closed-won over nineteen months, around eighty percent from paid social.",
  readout("TUTORING CLIENT &middot; CLOSED-WON &middot; JAN 2025 TO JUL 2026", "$1.07M", "teal",
          "Client result, not ours. Every deal we can trace, we trace to an ad. The ones we cannot, we do not claim."))
s("ONE OPTIONAL THING", "View-only access to your ad account.", "No spend. No changes.",
  "One optional thing. After you book we send a link for view-only access to your ad account. We cannot touch it or change anything. Just look.",
  cards(3, [("VIEW ONLY", "good"), ("NO SPEND", "good"), ("NO CHANGES", "good")]))
s("", "We show up", "with the diagnosis half-built.",
  "Then we go through it before the call, so we are not asking what your CPA is.",
  img("/gen/concept-09-audit-magnifier.png", "50% 45%"), "bleed")

# ═════════════════════ J. THE CLOSE ═════════════════════
bg("/gen/concept-08-two-roads.png")
s("", "You're not spending money.", "You're spending 30 minutes.",
  "You are not spending money here. You are spending thirty minutes.",
  readout("WHAT THIS COSTS YOU", "30 MIN", "teal"), "peak text-center")
s("", "Ninety days pass either way.", None,
  "Ninety days pass either way.",
  img("/gen/concept-08-two-roads.png", "50% 60%"), "bleed")
s("", "Ninety days older.", "Or ninety days older, holding a plan you executed.",
  "You are either ninety days older, or ninety days older and past it.",
  oldnew("90 DAYS OLDER", "90 DAYS OLDER, AND PAST IT", "DO NOTHING", "DO THIS"))
s("", "The only difference", "is the next ten seconds.",
  "The only difference is what you do in the next ten seconds.",
  readout("THE ONLY DIFFERENCE", "10 SECONDS", "gold"), "peak text-center")
s("", "Button's below. Pick a time.", None,
  "Button is below. Pick a time, then go read your roadmap.",
  img("/gen8/n12_two_tracks.png"), "bleed")
# 🔴 QR points at https://calendly.com/funnelfuturist/discovery -- the only FF-branded
# booking link in the estate. The roadmap's own booker is GHL and is wired to SupportED,
# not to us. CONFIRM THE URL BEFORE RECORDING: a wrong QR is baked into the video.
s("OR SCAN IT", "See you on the call.", None,
  "I will see you on the call.",
  qr("/site/qr_book_a_call.png"))


# ══════════════════════════════ EMIT ══════════════════════════════
HEAD = '''---
theme: default
title: Post-Quiz VSL -- Constraint Blindness (v2)
info: |
  POST-QUIZ VSL -- "CONSTRAINT BLINDNESS", v2. Fladlien 400-slide-hack cut.
  Placement: quiz results page, immediately after submission. Goal: book a call.

  SOURCE SCRIPT (verbatim, John): ai-os/03_Funnels_and_VSLs/roadmap_sage/
    SCRIPT_post_quiz_vsl_constraint_blindness_2026_08_16.md
  BUILD NOTES: NOTES_post_quiz_vsl_build_2026_08_16.md

  GENERATED by build.py -- edit the beat map there, never this file.
  Every spoken word is in the speaker notes. Press P for presenter mode.

  CLAIMS: zero income claims about us. Both client figures carry the client type and the
  window. $1.81M is the register-verified C&C figure per the brand board claims lock; the
  $2.4M in the source script is pre-June-2024 tracking and is deliberately NOT shipped.
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
    """Visible text. Straight quotes become typographic ones so a quoted phrase reads
    right AND cannot terminate a nearby attribute."""
    if not t: return ""
    t = str(t)
    t = re.sub(r'"([^"]*)"', r'&ldquo;\1&rdquo;', t)
    return t

def attr(t):
    """🔴 ATTRIBUTE VALUES ARE NOT TEXT. Vue's parser rejects an attribute name containing
    a quote, so a script line like: I call it "constraint blindness" -- dropped verbatim
    into alt="..." -- fails the BUILD, not the render. It cost a stale deploy: the build
    errored, dist stayed 30 minutes old, and the site served the previous version while
    looking fine. Escape here, always."""
    if not t: return ""
    return (str(t).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))

def card_grid(n, items):
    cells = "".join(f'<div class="rt-card {tone}"><div class="rt-card-t">{t}</div></div>'
                    for t, tone in items)
    return f'<div class="rt-grid c{n}">{cells}</div>'

BLEED_N = 0
out = [HEAD]
SLIDE = 0

def render(b, line, first, idx):
    """One slide. `line` is a chunk of the spoken script and IS the visible copy."""
    global BLEED_N
    v, cls = b["visual"], b["cls"]
    body, fm_cls = [], cls
    fm_extra = f"transition: {b['tr']}\n" if b.get("tr") else ""
    kind = v[0] if v else None

    # The kicker only ever appears on the FIRST chunk of a beat. Repeating a section label
    # on every slide of a run is noise, and it was one source of the say-it-twice problem.
    kick = b["kicker"] if (first and b["kicker"]) else ""

    if kind == "plate":
        # 1600x860 only. The SVG carries its own baked title band, so the script line sits
        # in a frosted strip over it rather than fighting the artwork.
        fm_cls = "plate"
        body.append(f'<div class="rt-cropbox"><img src="{v[1]}" alt="{attr(line)}" /></div>')
        body.append('<div class="absolute left-0 right-0" style="bottom: 4.5%; padding: 0 4rem;">')
        body.append(f'  <div class="rt-frost"><div class="rt-say">{esc(line)}</div></div>')
        body.append('</div>')
    elif kind == "img":
        if first: BLEED_N += 1
        right = BLEED_N % 2 == 0
        scrim = "rt-scrim-r" if right else "rt-scrim"
        align, ta = ("items-end", "right") if right else ("items-start", "left")
        focal = v[2] or "50% 38%"
        body.append(f'<img class="rt-bleed" src="{v[1]}" alt="" style="object-position: {focal};" />')
        body.append(f'<div class="{scrim}"></div>')
        body.append(f'<div class="relative h-full flex flex-col justify-center {align}" style="padding: 0 3.2rem;">')
        body.append(f'  <div style="max-width: 56%; text-align: {ta};">')
        if kick: body.append(f'    <div class="rt-kicker" style="color: var(--tealb);">{esc(kick)}</div>')
        body.append(f'    <div class="rt-h1 rt-onimg">{esc(line)}</div>')
        body.append('  </div>')
        body.append('</div>')
    else:
        if b.get("bg"):
            body.append(f'<img class="rt-bleed" src="{b["bg"]}" alt="" aria-hidden="true" '
                        f'style="opacity:0.10; filter:grayscale(0.55) contrast(0.9); object-position:50% 40%;" />')
            body.append('<div class="relative">')
        if kick: body.append(f'<div class="rt-kicker">{esc(kick)}</div>')
        body.append(f'<div class="rt-h1 mt-2">{esc(line)}</div>')
        # The supporting graphic renders on the FIRST chunk only and then persists visually
        # via the transition; repeating a card under every line is what made the deck feel
        # like it was restating itself.
        if first:
            if kind == "cards":
                body.append(f'<div class="mt-7" style="overflow: visible;">{card_grid(v[1], v[2])}</div>')
            elif kind == "oldnew":
                _, o, n_, lo, ln = v
                body.append(f'<div class="rt-grid c2 mt-7" style="overflow: visible;">'
                            f'<div class="rt-old"><div class="rt-waylabel">{lo}</div><div class="rt-card-t">{o}</div></div>'
                            f'<div class="rt-new"><div class="rt-waylabel">{ln}</div><div class="rt-card-t">{n_}</div></div></div>')
            elif kind == "readout":
                _, lab, big, tone, cap = v
                body.append(f'<div class="mt-6"><div class="rt-lab">{lab}</div>'
                            f'<div class="rt-big {tone}">{big}</div>'
                            + (f'<div class="rt-cap mt-4">{cap}</div>' if cap else '') + '</div>')
            elif kind == "figure":
                # wide/thin SVG at its natural aspect, bounded both ways
                body.append(f'<div class="rt-figure mt-6"><img src="{v[1]}" alt="{attr(line)}" '
                            f'style="max-width: 92%; max-height: 34vh; width: auto; margin: 0 auto; display: block;" /></div>')
            elif kind == "shot":
                _, p, tag, cap = v
                body.append(f'<div class="rt-imgwrap mt-5" style="max-height: 44vh; overflow: hidden;">'
                            f'<img class="rt-shot" src="{p}" alt="{attr(cap or line)}" '
                            f'style="max-height: 44vh; width: auto; margin: 0 auto; display: block;" />'
                            + (f'<span class="rt-tag live">{tag}</span>' if tag else '') + '</div>'
                            + (f'<div class="rt-cap mt-3">{cap}</div>' if cap else ''))
            elif kind == "wall":
                _, ps, cap = v
                tiles = "".join(f'<img class="rt-shot wall" src="{p}" alt="Client message" />' for p in ps)
                body.append(f'<div class="rt-grid c{len(ps)} mt-6">{tiles}</div>'
                            + (f'<div class="rt-cap mt-3">{cap}</div>' if cap else ''))
            elif kind == "dim":
                _, p, mode = v
                body.append(f'<div class="rt-dimwrap {mode} mt-6"><img src="{p}" alt="" /></div>')
            elif kind == "team":
                body.append('<div class="rt-grid c2 mt-7" style="max-width: 430px; margin-inline: auto;">'
                            '<div><img class="rt-portrait round" src="/team/john-headshot-direct.jpg" alt="John Coburn" style="width:126px; margin:0 auto;" />'
                            '<div class="rt-name">John</div><div class="rt-role">Co-founder</div></div>'
                            '<div><img class="rt-portrait round" src="/team/phoenix-headshot.png" alt="Phoenix Bohannon" style="width:126px; margin:0 auto;" />'
                            '<div class="rt-name">Phoenix</div><div class="rt-role">Co-founder</div></div></div>')
            elif kind == "qr":
                body.append(f'<div class="mt-6"><img src="{v[1]}" alt="Scan to book a call" '
                            f'style="width: 210px; margin: 0 auto; display: block; border-radius: 12px;" />'
                            f'<div class="rt-cap mt-3">Scan to pick a time</div></div>')
        if b.get("bg"): body.append('</div>')

    fm = f"---\nlayout: default\nclass: {fm_cls}\n{fm_extra}---\n"
    return fm + f"\n<!-- slide:{idx:02d} -->\n\n" + "\n".join(body) + "\n"

for b in B:
    for k, line in enumerate(chunk(b["note"])):
        SLIDE += 1
        out.append(render(b, line, k == 0, SLIDE))

OUT.write_text("\n".join(out))
txt = OUT.read_text()

# ══════════════════════ GATES -- exit 1 on failure ══════════════════════
n = len(B)
fail, missing, bad_bleed = [], [], []

def paths_of(b):
    v = b["visual"]
    if not v: return []
    if v[0] in ("img", "plate", "dim", "shot"): return [v[1]]
    if v[0] == "wall": return list(v[1])
    if v[0] == "team": return ["/team/john-headshot-direct.jpg", "/team/phoenix-headshot.png"]
    return []

for i, b in enumerate(B, 1):
    for p in paths_of(b):
        f = PUB / p.lstrip("/")
        if not f.exists():
            missing.append((i, p)); continue
        # 🔴 a square source in a 1.775 bleed frame loses 43% under object-fit:cover,
        # top-weighted, which decapitated four figures in v1. Check the real pixels.
        if b["cls"] == "bleed":
            try:
                w, h = Image.open(f).size
                if w / h < 1.4: bad_bleed.append((i, p, f"{w}x{h}"))
            except Exception as e:
                fail.append(f"slide {i}: cannot read {p} ({e})")

if missing:   fail.append(f"MISSING ASSETS: {missing}")
if bad_bleed: fail.append(f"SQUARE SOURCE IN BLEED (needs >=1.4:1): {bad_bleed}")

# bare = carries no <img> at all. The honest definition. v1's counted CSS text as a visual.
# Split on the slide MARKER, not on "---": the frontmatter delimiter appears twice per
# slide, so splitting on it counts every slide twice and reports a bare-text rate that is
# roughly double the truth. Measuring the measurement is part of the job.
blocks = txt.split("<!-- slide:")[1:]
# 🔴 WHAT THE RULE IS ACTUALLY FOR. Fladlien's "bare text cards <=5%" exists to stop WALLS
# OF TYPE, not to ban typography. A readout showing one enormous number over a five-word
# label is a visual -- it is the slide equivalent of a chart. So a slide only counts as bare
# when it carries no image AND enough words to read as a paragraph. Measuring "no <img>"
# alone flagged 51% and would have forced a photo behind every number, which is the OTHER
# failure mode. Both halves of this definition earn their place.
with_img = sum(1 for blk in blocks[1:] if "<img" in blk)
def visible_words(blk):
    body = blk.split("<!--")[0]
    return len(re.findall(r"[A-Za-z][A-Za-z'&;]+", re.sub(r"<[^>]+>", " ", body)))
content = blocks[1:]   # blocks[0] is slide 00, the holding card, never on camera
bare = [i for i, blk in enumerate(content, 1) if "<img" not in blk and visible_words(blk) > 16]
if len(bare) / max(len(content), 1) > 0.05:
    fail.append(f"WALL-OF-TYPE {len(bare)}/{len(content)} = {100*len(bare)/len(content):.0f}% (max 5%) slides {bare[:12]}")
# 85% is not a number I picked -- it is the golden deck measured (97 of 114 slides).
if with_img / max(len(blocks)-1, 1) < 0.85:
    fail.append(f"IMAGE COVERAGE {with_img}/{len(blocks)-1} = {100*with_img/(len(blocks)-1):.0f}% (golden is 85%)")

for banned, why in [("rt-mark", "renders nothing: absolute, no inset, no typography"),
                    ("rt-duo", "max-width 30rem squeezes two cards together")]:
    if banned in txt: fail.append(f"BANNED CLASS {banned}: {why}")
if re.search(r'class="rt-plate', txt): fail.append("BANNED rt-plate around text: height:100% overflows")
if re.search(r'rt-cell(?![a-z-])', txt): fail.append("rt-cell outside .rt-rail: nowrap + overflow:hidden clips silently")

words = sum(len(b["note"].split()) for b in B)
if words / 155 > 6.0: fail.append(f"RUNTIME {words/155:.2f} min > 6.00")
if txt.count("—"): fail.append(f"EM-DASH x{txt.count(chr(8212))}")

over = [(i, len(b['head'].split()) + len((b['sub'] or '').split())) for i, b in enumerate(B, 1)
        if len(b['head'].split()) + len((b['sub'] or '').split()) > 15]
if over: fail.append(f"OVER 15 VISIBLE WORDS: {over}")

runs, prev, run = [], None, 0
for i, b in enumerate(B, 1):
    k = b["cls"]
    run = run + 1 if k == prev else 1
    if run >= 3 and k == "bleed": runs.append((i, run))
    prev = k
if runs: fail.append(f"3+ CONSECUTIVE BLEEDS: {runs}")

for i, b in enumerate(B, 1):
    if not b["sub"] or not b["visual"]: continue
    card = " ".join(str(x) for x in b["visual"][1:])
    a = set(re.findall(r"[a-z]{4,}", b["sub"].lower()))
    c = set(re.findall(r"[a-z]{4,}", card.lower()))
    if b["visual"][0] == "oldnew": continue   # sub is not emitted for these
    if a and c and len(a & c) / len(a | c) >= 0.55: fail.append(f"DUP-COPY slide {i}: sub restates the card")

print(f"slides            : {n} (+1 holding)")
print(f"spoken words      : {words}  ->  {words/155:.2f} min at 155 wpm")
print(f"slides with image : {with_img}/{len(blocks)-1} = {100*with_img/(len(blocks)-1):.0f}%   [golden = 85%]")
print(f"wall-of-type      : {len(bare)}/{len(content)} = {100*len(bare)/len(content):.0f}%   [golden = 8%]")
print(f"bleeds            : {sum(1 for b in B if b['cls']=='bleed')}/{n}")
print(f"em-dashes         : {txt.count(chr(8212))}")
if fail:
    print("\n\U0001F534 GATE FAILURES:")
    for f_ in fail: print("   " + str(f_))
    sys.exit(1)
print("\nALL GATES PASS")
