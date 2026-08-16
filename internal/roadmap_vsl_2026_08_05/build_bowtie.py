#!/usr/bin/env python3
"""
THE BOWTIE SCAN — constraint visual generator.

John, 2026-08-09: "I want to show a visual with the bowtie funnel showing where the
constraint can move and block at different levels."

WHY THIS IS PARAMETRIC AND NOT HAND-DRAWN SVG:
The previous bowtie states (03a/03b/03c_bowtie_state*.svg) were hand-authored, all came
out 8,568 bytes, and a review returned FIX_FIRST -- "all three states draw the thick
middle, so the pinch is never shown." Three states that look identical teach nothing.
Here the band geometry is COMPUTED from a throughput model, so a choke at stage N
mathematically starves every stage after it. The states cannot silently converge.

THE MODEL
  Each stage has a baseline throughput (the bowtie: wide -> pinch at the sale -> wide again).
  A constraint at stage k multiplies throughput from k onward by a severity factor.
  Band half-height at each stage is proportional to sqrt(throughput) so the pinch reads
  strongly without the tail vanishing to a hairline.

Usage:  python3 build_bowtie.py            # writes public/flows/bowtie_*.svg
"""

import math
import pathlib

# ── FF palette ────────────────────────────────────────────────────────────────
VOID, SPACE = "#0A2230", "#103040"
TEAL, TEALB = "#209080", "#2BB3A0"
PARCH, STAR = "#F0E4BC", "#FAF6EA"
EMBER, GOLD = "#C4552F", "#D9B96A"
FOG, FOGD = "#7A9199", "#5C7078"

W, H = 1600, 860
# 🔴 DO NOT CHANGE H. It is a CALIBRATED CONSTANT, not a canvas preference.
# style.css .rt-cropbox crops the top 80px of these SVGs (to hide "THE BOWTIE SCAN" on the
# slides that run BEFORE the name is revealed) and encodes that as `aspect-ratio: 1600/780`
# plus `top: -10.3%`, where 10.3% = 80/780. On 2026-08-11 I raised H to 940 to make room for
# the beam labels and it silently broke the crop for EVERY bowtie slide, not just the new
# ones -- the label came off the top and nothing errored. If a label needs room, put it in
# the safe band (y 92..200: below the crop line, above the band), not by resizing the canvas.
MID = 430                      # vertical centre of the band
LEFT, RIGHT = 120, 1500

# The nine stages, in the script's own order and words.
STAGES = [
    ("ATTENTION",   1.00),
    ("CAPTURE",     0.62),
    ("CONVERSION",  0.26),
    ("PAYMENT",     0.07),      # the knot of the bowtie
    ("ONBOARDING",  0.26),
    ("ACTIVATION",  0.46),
    ("SUCCESS",     0.62),
    ("RETENTION",   0.80),
    ("REFERRAL",    1.00),
]
MAXHALF = 210                  # half-height of the band at throughput 1.0


def half(t: float) -> float:
    """Band half-height from throughput.

    Exponent 0.62, not sqrt(0.5). sqrt lifts small values so hard that the knot at PAYMENT
    read as a gentle wave rather than a bowtie -- the shape the whole mechanism is named
    after was not actually on screen. 0.62 deepens the knot while still keeping a starved
    tail thick enough to see.
    """
    return max(4.0, MAXHALF * (max(t, 0.0) ** 0.62))


def xs():
    step = (RIGHT - LEFT) / (len(STAGES) - 1)
    return [LEFT + i * step for i in range(len(STAGES))]


def throughputs(choke_idx=None, severity=0.16):
    """Baseline bowtie, then a HARD CAP from the choke onward.

    🔴 The cap is the whole point and the first version got it wrong. A constraint does not
    SCALE what follows it, it CEILINGS it: nothing downstream can carry more than the
    bottleneck passes. Scaling by a factor let the band widen again toward Referral, which
    drew the opposite of the lesson -- it implied you can recover downstream of your
    constraint. You cannot. That is why fixing the wrong thing costs you months.
    """
    out = []
    cap = None
    for i, (_, base) in enumerate(STAGES):
        if choke_idx is not None and i == choke_idx:
            cap = base * severity
        out.append(base if cap is None else min(base, cap))
    return out


def band_path(X, T):
    """One closed path: along the top edge left-to-right, back along the bottom."""
    top = [(x, MID - half(t)) for x, t in zip(X, T)]
    bot = [(x, MID + half(t)) for x, t in zip(X, T)]
    d = [f"M {top[0][0]:.1f} {top[0][1]:.1f}"]
    for i in range(1, len(top)):
        x0, y0 = top[i - 1]
        x1, y1 = top[i]
        cx = (x0 + x1) / 2
        d.append(f"C {cx:.1f} {y0:.1f} {cx:.1f} {y1:.1f} {x1:.1f} {y1:.1f}")
    d.append(f"L {bot[-1][0]:.1f} {bot[-1][1]:.1f}")
    for i in range(len(bot) - 1, 0, -1):
        x0, y0 = bot[i]
        x1, y1 = bot[i - 1]
        cx = (x0 + x1) / 2
        d.append(f"C {cx:.1f} {y0:.1f} {cx:.1f} {y1:.1f} {x1:.1f} {y1:.1f}")
    d.append("Z")
    return " ".join(d)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(choke_idx, title, consequence=None, team_choked=False, out_name="bowtie.svg",
          beam=None, beam_label=None, show_ghost=True, seen_label=None,
          show_stages=True, wings=False, ceiling=False, fade_downstream=False,
          hatch=False, feedback=None):
    """beam: index of the stage an EXTERNAL cause is striking.

    ── THE CONSTRAINT-CASCADE KWARGS (added 2026-08-16) ──────────────────────────
    show_stages=False     drop the stage tick+label loop and the team-bar text, so the
                          frame is the SHAPE alone (used to introduce the bowtie before
                          any stage is named).
    wings=True            NARROWS / THE KNOT / WIDENS brackets, ported from
                          quiz-hub/scripts/build_roadmap_diagrams.py. They NAME the three
                          regions of the shape; they do not argue. Drawn ONLY in the safe
                          band y 92..200 (below the 80px crop, above the band at y 220).
    ceiling=True          the literal lid: a dashed ember horizontal at the choke's own
                          half-height, running from the choke to the right edge. Nothing
                          downstream can be taller than the bottleneck passes.
    fade_downstream=True  ticks + stage names after the choke drop to FOG/0.35 so the eye
                          reads "past here nothing happens" before it reads a word.
    hatch=True            45-degree ember hatch filling the gap between the healthy ghost
                          band and the live band, DOWNSTREAM OF THE CHOKE ONLY -- the
                          hatched area is the throughput the constraint is eating.
    feedback=(f, t)       a routed dashed ember arrow from stage f back into stage t,
                          i.e. back pressure. Routed BELOW everything (y 820, verified
                          clear: the team bar ends at 788 and its text sits at 764) and
                          jogged around the stage labels, never through one.

    John, 2026-08-11: "sometimes the constraint is sort of invisible... a foundational thing
    you're not even aware of, because you're looking at the mechanics of it but you're not
    looking at the deeper underlying root cause. Projecting something like it's an external
    source that's causing the constraint, almost like a laser beam."

    So the beam is drawn from OUTSIDE the frame onto one stage. The pinch is the MECHANICS --
    what you can see from inside. The beam is the ROOT CAUSE -- only visible from outside.
    That distinction is the whole point, so the beam always originates off-canvas.
    """
    X = xs()
    T_base = throughputs(None)
    T = throughputs(choke_idx if not team_choked else None)
    if team_choked:
        # A team/ops constraint starves DELIVERY: everything from Onboarding on.
        T = throughputs(4, severity=0.30)

    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'font-family="Inter, ui-sans-serif, system-ui, sans-serif">')
    a(f'<rect width="{W}" height="{H}" fill="{STAR}"/>')

    # Ghost of the healthy bowtie, so the loss is visible as an absence.
    if show_ghost:
        a(f'<path d="{band_path(X, T_base)}" fill="{FOG}" opacity="0.16"/>')

    # The live band.
    a('<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">'
      f'<stop offset="0%" stop-color="{TEALB}"/><stop offset="100%" stop-color="{TEAL}"/>'
      '</linearGradient></defs>')
    a(f'<path d="{band_path(X, T)}" fill="url(#g)"/>')

    # ── THE HATCH: the throughput the constraint is eating, downstream only ───────
    # One evenodd path (ghost outline + live outline) gives the RING between them; a
    # clip from the choke to the right edge keeps it downstream, where the loss is.
    if hatch and choke_idx is not None:
        cxh = X[choke_idx]
        a('<defs>'
          '<pattern id="hx" width="12" height="12" patternUnits="userSpaceOnUse" '
          'patternTransform="rotate(45)">'
          f'<line x1="0" y1="0" x2="0" y2="12" stroke="{EMBER}" stroke-width="3"/>'
          '</pattern>'
          f'<clipPath id="hxc"><rect x="{cxh:.1f}" y="0" width="{W-cxh:.1f}" height="{H}"/>'
          '</clipPath></defs>')
        a(f'<path d="{band_path(X, T_base)} {band_path(X, T)}" fill-rule="evenodd" '
          f'fill="url(#hx)" opacity="0.10" clip-path="url(#hxc)"/>')

    # ── THE WINGS: the three regions of the shape, named ──────────────────────────
    if wings:
        # Spans re-registered against THIS geometry. quiz-hub uses (0,1)/(2,3)/(4,8),
        # which on a 1600-wide canvas puts the "THE KNOT" bracket ENDING at the pinch and
        # its label centred out on the narrowing slope -- the word names the wrong piece
        # of the shape. (0,2)/(2,4)/(4,8) tiles the whole span with no gaps and centres
        # THE KNOT exactly on PAYMENT, which is where the knot actually is.
        for i0, i1, label in ((0, 2, "NARROWS"), (2, 4, "THE KNOT"), (4, 8, "WIDENS")):
            xa, xb = X[i0], X[i1]
            a(f'<path d="M {xa:.1f} 192 L {xa:.1f} 180 L {xb:.1f} 180 L {xb:.1f} 192" '
              f'fill="none" stroke="{FOG}" stroke-width="1.6"/>')
            a(f'<text x="{(xa+xb)/2:.1f}" y="166" font-size="16" font-weight="800" '
              f'fill="{FOGD}" text-anchor="middle" letter-spacing="1.8">{esc(label)}</text>')

    # Title
    a(f'<text x="{LEFT}" y="72" font-size="17" font-weight="800" letter-spacing="3.4" '
      f'fill="{TEAL}">THE BOWTIE SCAN</text>')
    # 🔴 ON BEAM STATES THE TITLE MOVES OUT FROM UNDER THE CONE.
    # The cone descends from off-canvas straight down onto its stage, and on root_2 that
    # column is x~463 -- directly through the left-aligned title, so the translucent beam and
    # its dotted leader crossed the words "What is actually causing it". Caught by the
    # 2026-08-11 review. Nudging the title clear is correct rather than moving the beam,
    # because WHERE the beam lands is the information.
    tx = LEFT
    if beam is not None:
        bx = X[beam]
        if bx < W * 0.55:                  # cone on the left -> push the title right of it
            tx = min(bx + 120, W - 700)
    a(f'<text x="{tx}" y="124" font-size="40" font-weight="900" fill="{VOID}" '
      f'letter-spacing="-1">{esc(title)}</text>')

    # Stage ticks + labels
    if show_stages:
        for i, ((name, _), x, t) in enumerate(zip(STAGES, X, T)):
            hh = half(t)
            dim = fade_downstream and choke_idx is not None and i > choke_idx
            # 🔴 The tick's own baseline opacity is 0.30. Downstream it goes to 0.12
            # (0.30 x 0.35) -- writing the literal 0.35 onto the tick would make the dead
            # half of the diagram BRIGHTER than the live half, which is the opposite of
            # the instruction's intent. The 0.35 lands on the label text, as specified.
            top_i = "0.12" if dim else "0.30"
            a(f'<line x1="{x:.1f}" y1="{MID-MAXHALF-14:.1f}" x2="{x:.1f}" y2="{MID+MAXHALF+14:.1f}" '
              f'stroke="{FOG}" stroke-width="1" opacity="{top_i}"/>')
            ty = MID + MAXHALF + 46
            col = EMBER if (choke_idx is not None and i == choke_idx) else FOGD
            wgt = 900 if (choke_idx is not None and i == choke_idx) else 700
            op = ' opacity="0.35"' if dim else ''
            if dim:
                col = FOG
            a(f'<text x="{x:.1f}" y="{ty}" font-size="15" font-weight="{wgt}" fill="{col}"{op} '
              f'text-anchor="middle" letter-spacing="1.1">{esc(name)}</text>')

    # ── THE CEILING: the lid the constraint puts on everything after it ───────────
    if ceiling and choke_idx is not None:
        cxc, hhc = X[choke_idx], half(T[choke_idx])
        a(f'<path d="M {cxc:.1f} {MID-hhc:.1f} L {RIGHT} {MID-hhc:.1f} '
          f'M {cxc:.1f} {MID+hhc:.1f} L {RIGHT} {MID+hhc:.1f}" fill="none" '
          f'stroke="{EMBER}" stroke-width="2" stroke-dasharray="6 5"/>')

    # The choke marker
    if choke_idx is not None:
        cx = X[choke_idx]
        hh = half(T[choke_idx])
        a(f'<line x1="{cx:.1f}" y1="{MID-MAXHALF-10:.1f}" x2="{cx:.1f}" y2="{MID+MAXHALF+10:.1f}" '
          f'stroke="{EMBER}" stroke-width="5"/>')
        # pincers
        for sgn in (-1, 1):
            y = MID + sgn * (hh + 26)
            a(f'<path d="M {cx-30:.1f} {y - sgn*26:.1f} L {cx:.1f} {y:.1f} L {cx+30:.1f} {y - sgn*26:.1f}" '
              f'fill="none" stroke="{EMBER}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
        # 🔴 The chip is centred on the choke, which hangs it off the canvas the moment the
        # choke is stage 0 or stage 8 -- neither of which any earlier state used, so nothing
        # caught it until ATTENTION got its own frame. Clamp to the left/right margins.
        # This is a no-op for every pre-existing file: their chokes are 1,2,3,5,7, all of
        # which already sit inside the clamp.
        chip_x = min(max(cx - 104, LEFT - 24), RIGHT + 24 - 208)
        a(f'<rect x="{chip_x:.1f}" y="{MID-MAXHALF-78:.1f}" width="208" height="40" rx="7" fill="{EMBER}"/>')
        a(f'<text x="{chip_x+104:.1f}" y="{MID-MAXHALF-51:.1f}" font-size="16" font-weight="900" fill="{STAR}" '
          f'text-anchor="middle" letter-spacing="1.6">YOUR CONSTRAINT</text>')

    # Team / operations layer -- the script says plenty of businesses are not stuck on marketing.
    ty0 = MID + MAXHALF + 86
    tfill = EMBER if team_choked else FOG
    top_ = 0.16 if team_choked else 0.10
    # On a back-pressure frame the loop lands ON operations, so the bar is ember-stroked
    # (outline only -- the fill stays neutral, because the TEAM is not the constraint here,
    # it is what absorbs the constraint).
    if feedback is not None:
        # 🔴 `opacity` on the rect fades the STROKE as well as the fill, so an ember outline
        # written that way renders grey and the emphasis is silently lost -- exactly what the
        # first render of this frame did. Use fill-opacity so only the fill is knocked back.
        # Kept as a separate branch so the two pre-existing bar variants stay byte-identical.
        a(f'<rect x="{LEFT-24}" y="{ty0}" width="{RIGHT-LEFT+48}" height="62" rx="10" '
          f'fill="{tfill}" fill-opacity="{top_}" stroke="{EMBER}" stroke-width="3"/>')
    else:
        a(f'<rect x="{LEFT-24}" y="{ty0}" width="{RIGHT-LEFT+48}" height="62" rx="10" '
          f'fill="{tfill}" opacity="{top_}" stroke="{tfill}" stroke-width="{3 if team_choked else 1}"/>')
    if show_stages:
        a(f'<text x="{(LEFT+RIGHT)/2:.1f}" y="{ty0+38}" font-size="16" font-weight="800" '
          f'fill="{EMBER if team_choked else FOGD}" text-anchor="middle" letter-spacing="2.2">'
          f'TEAM &amp; DAY-TO-DAY OPERATIONS{" &#8212; THE CONSTRAINT" if team_choked else ""}</text>')

    # ── BACK PRESSURE: a routed feedback arrow from one stage into an earlier one ──
    # 🔴 EVERY VERTEX HERE IS A CLEARANCE DECISION, not a shape preference:
    #   y 820  -- the only free lane. Stage labels sit at 686, the team bar spans
    #             726..788 and its text baseline is 764. 820 is under all of it and
    #             still 40 above the calibrated H=860.
    #   x +46 off the choke -- the choke draws a 5px ember rule and 60-wide pincers at
    #             X[from]; starting on top of them reads as a thicker choke, not an arrow.
    #   the right-hand descent at X[from]+252 -- threaded between the ACTIVATION label
    #             (ends ~1030) and SUCCESS (starts ~1122), and clear of the team bar's
    #             centred text (ends ~980).
    #   the left-hand ascent at X[to]-52 -- clear of the CAPTURE label's left edge (~261),
    #             then a short jog so the ARROWHEAD ITSELF is vertical, pointing up into
    #             the band rather than glancing off it.
    if feedback is not None:
        fi, ti = feedback
        fx, tx2 = X[fi], X[ti]
        y_start = MID + half(T[fi])
        drop_x = fx + 46
        right_x = fx + 252
        rise_x = tx2 - 52
        tip_y = MID + half(T[ti]) - 4
        a(f'<path d="M {drop_x:.1f} {y_start:.1f} L {drop_x:.1f} 648 L {right_x:.1f} 648 '
          f'L {right_x:.1f} 820 L {rise_x:.1f} 820 L {rise_x:.1f} 620 L {tx2:.1f} 620 '
          f'L {tx2:.1f} {tip_y+14:.1f}" fill="none" stroke="{EMBER}" stroke-width="4" '
          f'stroke-dasharray="9 6" stroke-linecap="round" stroke-linejoin="round"/>')
        a(f'<path d="M {tx2:.1f} {tip_y:.1f} L {tx2-14:.1f} {tip_y+28:.1f} '
          f'L {tx2+14:.1f} {tip_y+28:.1f} Z" fill="{EMBER}"/>')
        # ONE two-word chip, sitting on the wire in the y 800..852 safe band.
        cw, cx2 = 190, 660
        a(f'<rect x="{cx2-cw/2:.1f}" y="800" width="{cw}" height="40" rx="7" fill="{EMBER}"/>')
        a(f'<text x="{cx2:.1f}" y="827" font-size="15" font-weight="900" fill="{STAR}" '
          f'text-anchor="middle" letter-spacing="1.6">BACK PRESSURE</text>')

    # ── THE BEAM: an external cause, drawn from off-canvas onto one stage ──────
    if beam is not None:
        bx = X[beam]
        by = MID - half(T[beam]) - 30
        a('<defs>'
          f'<linearGradient id="bm" x1="0" y1="0" x2="0" y2="1">'
          f'<stop offset="0%" stop-color="{EMBER}" stop-opacity="0.10"/>'
          f'<stop offset="70%" stop-color="{EMBER}" stop-opacity="0.55"/>'
          f'<stop offset="100%" stop-color="{EMBER}" stop-opacity="0.95"/>'
          '</linearGradient></defs>')
        a(f'<path d="M {bx-64:.1f} -40 L {bx+64:.1f} -40 L {bx+15:.1f} {by:.1f} L {bx-15:.1f} {by:.1f} Z" '
          f'fill="url(#bm)"/>')
        a(f'<circle cx="{bx:.1f}" cy="{by+6:.1f}" r="9" fill="{EMBER}"/>')
        if beam_label:
            # 🔴 GEOMETRY, LEARNED THE HARD WAY 2026-08-11. Three separate defects in the first
            # version, all of which rendered and none of which any assertion would have caught:
            #   1. the box was sized at 11px/char and the label CLIPPED ("...GIVE YO")
            #   2. the box was centred over the beam, which sits directly on top of the title
            #   3. the subtitle landed on the band's top edge
            # So: measure generously, pin the box TOP-RIGHT away from the left-aligned title,
            # and draw a leader to the beam instead of sitting on it.
            fs = 16
            lw = int(len(beam_label) * (fs * 0.70)) + 52     # 0.70em/char for bold caps + padding
            lx = W - lw - 44
            ly = 92          # 🔴 below the 80px crop line, or the label is cropped away
            a(f'<rect x="{lx}" y="{ly}" width="{lw}" height="44" rx="8" fill="{VOID}"/>')
            a(f'<text x="{lx + lw/2:.1f}" y="{ly+28}" font-size="{fs}" font-weight="800" fill="{STAR}" '
              f'text-anchor="middle" letter-spacing="0.4">{esc(beam_label)}</text>')
            a(f'<text x="{lx + lw/2:.1f}" y="{ly+64}" font-size="12" font-weight="800" fill="{EMBER}" '
              f'text-anchor="middle" letter-spacing="2.2">THE ROOT CAUSE &#183; OUTSIDE THE BUSINESS</text>')
            # leader from the label down-left to the beam cone
            a(f'<path d="M {lx:.1f} {ly+22} L {bx+90:.1f} {ly+22} L {bx+16:.1f} {max(by-60, ly+70):.1f}" '
              f'fill="none" stroke="{EMBER}" stroke-width="2" stroke-dasharray="5 4" opacity="0.75"/>')

    # `seen_label` is intentionally NOT drawn. The 860 canvas has no free band below the team
    # bar, and it is commentary rather than diagram -- so it lives in slide copy, where it can
    # also be revealed on a click. Kept in the signature so the STATES table stays readable.

    # 🔴 THE CONSEQUENCE LINE IS NO LONGER DRAWN, and this is a correctness fix not a
    # style one. Baking the spoken sentence into the SVG meant the IMAGE ran AHEAD OF THE
    # SCRIPT: bowtie_01 printed "More traffic makes it worse..." so the slide BEFORE that
    # line is spoken already displayed it, and bowtie_02 printed the activation sentence
    # that the notes explicitly say must hang and complete on the next slide. Three
    # deliberate reveals were dead on arrival. Caught by the 2026-08-11 visual review.
    #
    # The diagram shows STATE. The script says the SENTENCE. Whoever controls the reveal
    # must control the timing, and that is the deck, not the asset. `consequence` is kept
    # in the signature so the STATES tables stay self-documenting -- it is the caption to
    # put in slide copy, not something to render here.

    a('</svg>')
    out = pathlib.Path(__file__).parent / "public" / "flows" / out_name
    out.write_text("\n".join(p))
    return out


STATES = [
    dict(choke_idx=2, title="When the constraint is CONVERSION",
         consequence="More traffic makes it worse. You just pay more money to lose more people.",
         out_name="bowtie_01_conversion.svg"),
    dict(choke_idx=5, title="When the constraint is ACTIVATION",
         consequence="They never start, so they never win. Never renew, never refer, never send a testimonial.",
         out_name="bowtie_02_activation.svg"),
    dict(choke_idx=None, team_choked=True, title="When the constraint is your TEAM",
         consequence="A better funnel just hands you more work nobody can do.",
         out_name="bowtie_03_team.svg"),
    dict(choke_idx=None, title="Every step a customer takes with you",
         consequence="At any moment, one of these is holding everything else back. That one is your constraint.",
         out_name="bowtie_00_full.svg"),
]

# ── THE CONSTRAINT MOVES. John 2026-08-11: "I want to show more of how the constraint
#    moves up and down the business." Same diagram, the pinch travelling stage by stage, so
#    the movement is the message rather than any single position.
MOVES = [
    dict(choke_idx=1, title="It can sit at CAPTURE",
         consequence="Traffic arrives and nothing is held. Everything downstream is starved of people.",
         out_name="move_1_capture.svg"),
    dict(choke_idx=3, title="It can sit at PAYMENT",
         consequence="They decided yes and the checkout lost them. The hardest work is already done.",
         out_name="move_2_payment.svg"),
    dict(choke_idx=5, title="It can sit at ACTIVATION",
         consequence="They paid and never started. Nothing after this can happen.",
         out_name="move_3_activation.svg"),
    dict(choke_idx=7, title="It can sit at RETENTION",
         consequence="You win them and lose them. You are refilling a bucket with a hole in it.",
         out_name="move_4_retention.svg"),
]

# ── THE INVISIBLE CONSTRAINT: mechanics vs root cause, the Erin case.
ROOT = [
    dict(choke_idx=2, title="What you can see", show_ghost=True,
         seen_label="FROM INSIDE THE BUSINESS: \u201cour show rate is bad\u201d",
         consequence="So you fix the mechanics. More reminders. Better copy. Sharper hook. Better ads.",
         out_name="root_1_mechanics.svg"),
    dict(choke_idx=2, title="What is actually causing it", show_ghost=True, beam=2,
         beam_label="YOUR MARKET HAS NO TIME TO GIVE YOU",
         seen_label="THE MECHANICS WERE NEVER THE PROBLEM",
         consequence="The funnel was fine. A 45 minute call was never something that market could give.",
         out_name="root_2_beam.svg"),
    dict(choke_idx=5, title="It works the same anywhere", show_ghost=True, beam=5,
         beam_label="NOBODY OWNS THE FIRST WEEK",
         seen_label="FROM INSIDE: \u201cpeople just are not engaging\u201d",
         consequence="Same shape, different stage. The cause is always outside the thing you are staring at.",
         out_name="root_3_beam_activation.svg"),
]

# ── THE CONSTRAINT CASCADE (2026-08-16) ──────────────────────────────────────────
# Two setup frames that teach the SHAPE with nothing named on it, then the pinch walked
# stage by stage with the three new devices switched on together: the CEILING (the lid),
# the HATCH (the throughput being eaten) and the FADE (past here, nothing happens).
# 🔴 bt_ prefix on every one. Nothing above is touched -- these are additional files, and
# the STAGES list is deliberately unchanged so all 11 existing outputs keep their geometry.
CASCADE = [
    dict(choke_idx=None, title="", show_stages=False, show_ghost=False,
         out_name="bt_a_shape.svg"),
    dict(choke_idx=None, title="", show_stages=False, wings=True, show_ghost=False,
         out_name="bt_b_wings.svg"),
    dict(choke_idx=0, title="It can sit at ATTENTION", ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c0_attention.svg"),
    dict(choke_idx=1, title="It can sit at CAPTURE", ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c1_capture.svg"),
    dict(choke_idx=2, title="It can sit at CONVERSION", ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c2_conversion.svg"),
    dict(choke_idx=3, title="It can sit at PAYMENT", ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c3_payment.svg"),
    dict(choke_idx=4, title="It can sit at ONBOARDING", feedback=(4, 1), ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c4_onboarding_loop.svg"),

    # John, 2026-08-16: "we can show it can sit at activation, it can sit at success, it
    # can sit at retention, it can sit at referral, and all of them introduce more
    # constraints. And the one we want to show at referral is where it feeds back into
    # ATTENTION, because referral is another type of attention. So we want a full loop."
    dict(choke_idx=5, title="It can sit at ACTIVATION", feedback=(5, 2), ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c5_activation.svg"),
    dict(choke_idx=6, title="It can sit at SUCCESS", feedback=(6, 3), ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c6_success.svg"),
    dict(choke_idx=7, title="It can sit at RETENTION", feedback=(7, 1), ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c7_retention.svg"),
    # 🔴 THE FULL LOOP. Referral feeds all the way back to ATTENTION, because referral IS
    # attention. This is the frame that closes the bow-tie into a cycle rather than a line,
    # and it is the only one where the arrow spans the whole canvas.
    dict(choke_idx=8, title="It can sit at REFERRAL", feedback=(8, 0), ceiling=True,
         fade_downstream=True, hatch=True, out_name="bt_c8_referral_loop.svg"),]

if __name__ == "__main__":
    for s in STATES + MOVES + ROOT + CASCADE:
        p = build(**s)
        print(f"wrote {p.name} ({p.stat().st_size} bytes)")
