/**
 * PROOF DIAGRAM -- recreated from the reference John shared (Josh Gavin style).
 *
 * Chosen deliberately as the test case because it exercises every primitive at once:
 * two stick-figure poses, eight icons, rough boxes, straight and curved arrows,
 * dashed panel dividers, a strike-through and a checkmark. If this reproduces, the
 * aesthetic is producible from markup and no diagram after it is an art task.
 *
 * Run: node _sketch/build.mjs
 */
import {
  svg, rect, dashed, arrow, text, lines, underline, crossout, figure, desk, icon,
} from "../sketch.mjs";

const W = 1200;
const H = 990;

export const name = "impulse_intention";
export const render = () => {
  let s = "";

  /* ── title ─────────────────────────────────────────────── */
  s += text(600, 74, "'Impulse on the front. Intention on the back.'", {
    size: 38, weight: 900, caps: true,
  });
  s += underline(168, 1032, 90);

  /* ── panel 1: the two ends ─────────────────────────────── */
  s += text(300, 152, "Front end = impulse", { size: 30, caps: true });
  s += text(890, 152, "Back end = intention", { size: 30, caps: true });
  s += dashed(600, 118, 600, 512);

  // left: the impulse buyer
  s += figure(185, 400, 165, "walk-phone");
  s += icon.clock(95, 440, 38);
  s += lines(95, 487, ["No time", "to think"], { size: 17, weight: 700 });
  s += icon.bolt(390, 192, 32);
  s += text(425, 188, "Fast", { size: 23, anchor: "start" });
  s += text(425, 214, "Decision", { size: 23, anchor: "start" });
  s += rect(345, 235, 160, 72);
  s += text(425, 281, "$17-$27", { size: 27 });
  s += arrow(425, 318, 425, 360);
  s += lines(425, 390, ["Easy. Low-Risk.", "No Thinking Required."], {
    size: 19, weight: 700,
  });
  s += text(300, 478, "Converts on cold traffic", { size: 25 });

  // right: the deliberate buyer
  s += desk(662, 398, 168, 58);
  s += figure(748, 461, 148, "sit-think");
  const rows = [
    [246, "Email", icon.envelope],
    [294, "Webinar", icon.video],
    [342, "Content", icon.speech],
    [390, "Upsells", icon.stairs],
  ];
  for (const [y, label, glyph] of rows) {
    s += arrow(838, 318 - (318 - y) * 0.28, 900, y, { curved: y < 318 ? 10 : -10 });
    s += glyph(928, y - 4, 34);
    s += text(962, y + 4, label, { size: 24, anchor: "start" });
  }
  s += text(1078, 438, "$$$", { size: 40, weight: 900 });
  s += icon.cash(1082, 476, 44);
  s += text(818, 486, "Earns the High Ticket Sale", { size: 25 });

  /* ── panel 2: what you get in return ───────────────────── */
  s += dashed(26, 524, 1174, 524);
  s += text(600, 566, "What you get in return", { size: 30, caps: true });
  const cards = [
    [90, "Revenue", icon.money],
    [340, "Pixel Data", icon.target],
    [590, "Trust", icon.handshake],
  ];
  for (const [x, label, glyph] of cards) {
    s += rect(x, 586, 190, 120);
    s += glyph(x + 95, 628, 44);
    s += text(x + 95, 692, label, { size: 22 });
  }
  s += text(312, 656, "+", { size: 36, weight: 900 });
  s += text(562, 656, "+", { size: 36, weight: 900 });
  s += arrow(792, 646, 866, 646, { head: 18 });
  s += rect(876, 590, 240, 112);
  s += lines(996, 632, ["High Ticket", "Sale"], { size: 28, lh: 34 });

  /* ── panel 3: the real goal ────────────────────────────── */
  s += dashed(26, 728, 1174, 728);
  s += text(600, 772, "The real goal", { size: 30, caps: true });
  s += text(330, 826, "Liquidation", { size: 29 });
  s += crossout(330, 816, 196, 46);
  s += text(330, 860, "(not the goal)", { size: 17, weight: 600, italic: true });
  s += icon.check(636, 818, 40);
  s += lines(796, 812, ["Give customers", "an easy first step"], { size: 23, lh: 29 });
  s += text(600, 936, "Liquidation is the side effect. Trust is the goal.", {
    size: 29, weight: 900,
  });

  return svg(W, H, s);
};
