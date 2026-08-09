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


def build(choke_idx, title, consequence, team_choked=False, out_name="bowtie.svg"):
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

    # The consequence line, in John's own words from the script.
    a(f'<text x="{LEFT}" y="{H-40}" font-size="21" font-weight="700" fill="{VOID}">'
      f'{esc(consequence)}</text>')

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

if __name__ == "__main__":
    for s in STATES:
        p = build(**s)
        print(f"wrote {p.name} ({p.stat().st_size} bytes)")
