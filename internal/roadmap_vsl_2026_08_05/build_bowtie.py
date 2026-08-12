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
          beam=None, beam_label=None, show_ghost=True, seen_label=None):
    """beam: index of the stage an EXTERNAL cause is striking.

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

    # Title
    a(f'<text x="{LEFT}" y="72" font-size="17" font-weight="800" letter-spacing="3.4" '
      f'fill="{TEAL}">THE BOWTIE SCAN</text>')
    a(f'<text x="{LEFT}" y="124" font-size="40" font-weight="900" fill="{VOID}" '
      f'letter-spacing="-1">{esc(title)}</text>')

    # Stage ticks + labels
    for i, ((name, _), x, t) in enumerate(zip(STAGES, X, T)):
        hh = half(t)
        a(f'<line x1="{x:.1f}" y1="{MID-MAXHALF-14:.1f}" x2="{x:.1f}" y2="{MID+MAXHALF+14:.1f}" '
          f'stroke="{FOG}" stroke-width="1" opacity="0.30"/>')
        ty = MID + MAXHALF + 46
        col = EMBER if (choke_idx is not None and i == choke_idx) else FOGD
        wgt = 900 if (choke_idx is not None and i == choke_idx) else 700
        a(f'<text x="{x:.1f}" y="{ty}" font-size="15" font-weight="{wgt}" fill="{col}" '
          f'text-anchor="middle" letter-spacing="1.1">{esc(name)}</text>')

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
        a(f'<rect x="{cx-104:.1f}" y="{MID-MAXHALF-78:.1f}" width="208" height="40" rx="7" fill="{EMBER}"/>')
        a(f'<text x="{cx:.1f}" y="{MID-MAXHALF-51:.1f}" font-size="16" font-weight="900" fill="{STAR}" '
          f'text-anchor="middle" letter-spacing="1.6">YOUR CONSTRAINT</text>')

    # Team / operations layer -- the script says plenty of businesses are not stuck on marketing.
    ty0 = MID + MAXHALF + 86
    tfill = EMBER if team_choked else FOG
    top_ = 0.16 if team_choked else 0.10
    a(f'<rect x="{LEFT-24}" y="{ty0}" width="{RIGHT-LEFT+48}" height="62" rx="10" '
      f'fill="{tfill}" opacity="{top_}" stroke="{tfill}" stroke-width="{3 if team_choked else 1}"/>')
    a(f'<text x="{(LEFT+RIGHT)/2:.1f}" y="{ty0+38}" font-size="16" font-weight="800" '
      f'fill="{EMBER if team_choked else FOGD}" text-anchor="middle" letter-spacing="2.2">'
      f'TEAM &amp; DAY-TO-DAY OPERATIONS{" &#8212; THE CONSTRAINT" if team_choked else ""}</text>')

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

if __name__ == "__main__":
    for s in STATES + MOVES + ROOT:
        p = build(**s)
        print(f"wrote {p.name} ({p.stat().st_size} bytes)")
