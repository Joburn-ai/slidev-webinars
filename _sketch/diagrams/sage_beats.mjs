/**
 * Diagrams for the SAGE VSL training deck.
 *
 * Three of them, at the only three places in a 17-beat argument where a drawing
 * does something a sentence cannot: the shift (two timelines), the restart (four
 * firsts versus a fourth), and the crossroads (one dot, two paths).
 *
 * Deliberately NOT one per beat. A diagram on every slide is decoration, and the
 * whole property of this aesthetic is that a drawing appears when the argument
 * needs one.
 */
import { svg, rect, line, dashed, arrow, text, lines, figure, icon, curve, poly, circle } from "../sketch.mjs";

/* ── 1. The shift: the ground moved, you did not ─────────────────────────── */

export const shift = {
  name: "sage_shift",
  render: () => {
    let s = "";
    s += text(600, 66, "The ground moved. Your playbook didn't.", { size: 36, weight: 900, caps: true });

    // then
    s += text(300, 150, "Until about 2021", { size: 24, caps: true });
    s += line(80, 300, 520, 300, { strokeWidth: 3 });
    s += figure(140, 296, 120, "stand");
    s += arrow(200, 250, 470, 250, { head: 16 });
    s += text(335, 232, "more traffic", { size: 20, weight: 700 });
    s += text(300, 340, "worked", { size: 26 });
    s += icon.check(300, 372, 34);

    s += dashed(600, 130, 600, 430);

    // now
    s += text(890, 150, "After", { size: 24, caps: true });
    s += line(680, 300, 1120, 300, { strokeWidth: 3 });
    s += figure(740, 296, 120, "stand");
    s += arrow(800, 250, 1070, 250, { head: 16 });
    s += text(935, 232, "more traffic", { size: 20, weight: 700 });
    // the ground itself has shifted under the second timeline
    s += line(680, 330, 900, 352, { strokeWidth: 3, roughness: 2.2 });
    s += line(900, 352, 1120, 330, { strokeWidth: 3, roughness: 2.2 });
    s += text(890, 400, "lands softer", { size: 26 });
    s += text(890, 432, "every year", { size: 26 });

    s += dashed(60, 470, 1140, 470);
    s += lines(600, 520, [
      "Nobody sent a notice. Nobody chose it.",
      "Which is exactly why it is hard to see from inside your own business.",
    ], { size: 22, weight: 700, lh: 32 });
    s += text(600, 606, "Your playbook was not wrong. It expired.", { size: 28, weight: 900 });
    return svg(1200, 650, s);
  },
};

/* ── 2. The restart: four firsts versus a fourth ─────────────────────────── */

export const restart = {
  name: "sage_restart",
  render: () => {
    let s = "";
    s += text(600, 62, "Four firsts, or a fourth", { size: 36, weight: 900, caps: true });

    // top row: four disconnected assets, each starting the argument over
    s += text(600, 128, "What you have now", { size: 22, caps: true });
    const labels = ["Ad", "Page", "Email", "Call"];
    labels.forEach((l, i) => {
      const x = 150 + i * 240;
      s += rect(x, 155, 160, 82);
      s += text(x + 80, 192, l, { size: 24 });
      s += text(x + 80, 218, "starts over", { size: 15, weight: 600 });
      // each one restarts from zero, so a small return arrow to its own start
      s += arrow(x + 80, 258, x + 80, 288, { head: 12 });
      s += text(x + 80, 312, "0", { size: 22, weight: 900 });
    });
    s += text(600, 356, "Four assets seen. Four arguments heard once each.", { size: 20, weight: 700 });

    s += dashed(60, 388, 1140, 388);

    // bottom row: one argument accumulating
    s += text(600, 434, "What you needed", { size: 22, caps: true });
    labels.forEach((l, i) => {
      const x = 150 + i * 240;
      s += rect(x, 462, 160, 82);
      s += text(x + 80, 498, l, { size: 24 });
      s += text(x + 80, 524, `carries ${i + 1}`, { size: 15, weight: 600 });
      if (i < 3) s += arrow(x + 168, 503, x + 232, 503, { head: 14 });
    });
    s += text(600, 596, "One argument, said four times. Same effort. Different result.", {
      size: 24, weight: 900,
    });
    return svg(1200, 640, s);
  },
};

/* ── 3. The crossroads: one dot, two paths ───────────────────────────────── */

export const crossroads = {
  name: "sage_crossroads",
  render: () => {
    let s = "";
    s += text(600, 62, "Ninety days pass either way", { size: 36, weight: 900, caps: true });

    // the dot: a decision point, not a location
    s += circle(220, 300, 26, { strokeWidth: 3.4 });
    s += text(220, 352, "You, today", { size: 20, weight: 700 });

    // upper path: nothing different
    s += curve([[248, 292], [520, 220], [900, 196]], { strokeWidth: 2.6 });
    s += arrow(880, 198, 940, 194, { head: 15 });
    s += figure(1010, 236, 96, "walk-phone");
    s += lines(1010, 290, ["Still the reason", "anything sells"], { size: 18, weight: 700, lh: 24 });

    // lower path: something different
    s += curve([[248, 312], [520, 400], [900, 436]], { strokeWidth: 2.6 });
    s += arrow(880, 432, 940, 440, { head: 15 });
    s += figure(1006, 470, 96, "stand");
    s += lines(1006, 512, ["Can say what next", "month produces"], { size: 18, weight: 700, lh: 24 });

    s += text(560, 174, "Same effort", { size: 20, weight: 700, italic: true });
    s += text(560, 476, "Different order", { size: 20, weight: 700, italic: true });

    s += dashed(60, 560, 1140, 560);
    s += text(600, 606, "The difference is not money and it is not how hard you push.", { size: 22, weight: 700 });
    s += text(600, 640, "It is which order you do things in.", { size: 28, weight: 900 });
    return svg(1200, 670, s);
  },
};
