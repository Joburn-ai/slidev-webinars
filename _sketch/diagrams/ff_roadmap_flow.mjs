/**
 * THE FUNNEL FUTURIST ROADMAP FLOWCHART.
 *
 * Modelled on the structure John pointed at: three problem areas feeding a loop
 * most people never leave, then the break-out into named phases. Same shape as
 * the real-estate board, different nouns, which is the portability argument.
 *
 * DETERMINISTIC. Nothing here is per-prospect. Every lead sees the identical
 * chart; what changes is which node is lit, and that is a class on a node id,
 * never a redraw.
 */
import { svg, rect, line, dashed, arrow, text, lines, icon, circle, poly } from "../sketch.mjs";

const FOCI = ["all", "restart", "order", "gates"];

function band(id, focus, body) {
  const on = focus === "all" || focus === id;
  return `<g id="${id}" opacity="${on ? 1 : 0.13}">${body}</g>`;
}

export const name = "ff_roadmap_flow";
export const render = () => build("all");

// one export per focus state, so build.mjs emits all four
export const focusRestart = { name: "ff_flow_restart", render: () => build("restart") };
export const focusOrder = { name: "ff_flow_order", render: () => build("order") };
export const focusGates = { name: "ff_flow_gates", render: () => build("gates") };

function build(focus) {
  let s = "";

  s += text(620, 56, "Why every push starts over", { size: 34, weight: 900, caps: true });
  s += text(620, 88, "and the order that stops it", { size: 21, weight: 700 });

  /* ── the restart loop ──────────────────────────────────── */
  s += text(290, 146, "The restart", { size: 24, caps: true });
  s += dashed(30, 164, 560, 164);

  // Compressed so the loop stays inside its own band. Boxes 52 tall, 60 apart,
  // and the return curve routes down the far left rather than through the boxes.
  const probs = [
    [200, "No order", "every push starts from zero"],
    [262, "Dashboards disagree", "a good month cannot be read"],
    [324, "Nothing after the sale", "the month restarts at zero"],
  ];
  for (const [y, a, b] of probs) {
    s += rect(64, y - 24, 196, 48);
    s += text(162, y - 4, a, { size: 15 });
    s += text(162, y + 14, b, { size: 11, weight: 600 });
    s += arrow(264, y, 320, y, { head: 11 });
  }

  s += rect(326, 178, 172, 142, { strokeWidth: 3 });
  s += lines(412, 224, ["Every asset", "restarts the", "argument"], { size: 17, lh: 23 });
  s += text(412, 300, "The restart", { size: 12, caps: true, weight: 900 });

  // return path: down from the loop, left along the bottom, back up the outside
  s += poly([[412, 322], [412, 352], [44, 352], [44, 186]], { strokeWidth: 2.2 });
  s += arrow(44, 200, 46, 178, { head: 11 });
  s += text(300, 378, "Most founders stay in this loop for years", { size: 15, weight: 700, italic: true });

  s = band("restart", focus, s);
  let o = "";
  s += dashed(570, 126, 570, 396);

  /* ── the order ─────────────────────────────────────────── */
  o += text(890, 146, "The order", { size: 24, caps: true });
  o += dashed(596, 164, 1210, 164);

  const phases = [
    [620, "1", "Launch", ["One offer", "One channel", "One number you trust"], "offer lock"],
    [816, "2", "Validate", ["The same result twice", "On purpose", "Capacity installed"], "spend lock"],
    [1012, "3", "Scale", ["Multiply what runs", "without you", "You become removable"], "scale lock"],
  ];
  for (const [x, n, title, items, lock] of phases) {
    o += rect(x, 188, 172, 152, { strokeWidth: 2.8 });
    o += circle(x + 26, 214, 30);
    o += text(x + 26, 221, n, { size: 18, weight: 900 });
    o += text(x + 106, 221, title, { size: 22 });
    items.forEach((it, i) => { o += text(x + 86, 258 + i * 22, it, { size: 12, weight: 600 }); });
    const gx = x + 172;
    o += icon.check(gx + 12, 306, 22);
    o += text(gx + 12, 332, lock, { size: 10, caps: true, weight: 900, tracking: 1 });
    if (x < 1012) o += arrow(gx + 2, 258, gx + 22, 258, { head: 12 });
  }
  o += text(900, 378, "Three locks never move. Everything else is a range your market gets a vote on.",
            { size: 15, weight: 700 });

  s += band("order", focus, o);
  let g = "";
  /* ── the gates ─────────────────────────────────────────── */
  g += dashed(30, 416, 1210, 416);
  g += text(620, 458, "What unlocks, and when", { size: 26, caps: true });

  const gates = [
    [120, "1", "Reality check", "Does the diagnosis land?", "Your weakest system, named"],
    [478, "2", "Mechanism check", "Do the four requirements hold?", "Your position on this map"],
    [836, "3", "The unlock", "What will you do first?", "Your book-a-call ad, written"],
  ];
  for (const [x, n, title, ask, gives] of gates) {
    g += rect(x, 496, 296, 174, { strokeWidth: 2.6 });
    g += circle(x + 34, 530, 34);
    g += text(x + 34, 538, n, { size: 19, weight: 900 });
    g += text(x + 178, 538, title, { size: 19 });
    g += text(x + 148, 578, "30 seconds. You answer", { size: 11, weight: 700, caps: true });
    g += text(x + 148, 604, ask, { size: 14, weight: 700 });
    g += line(x + 22, 620, x + 274, 620, { strokeWidth: 1.6 });
    g += text(x + 148, 642, "You get", { size: 10, caps: true, weight: 900, tracking: 1.2 });
    g += text(x + 148, 662, gives, { size: 14 });
    if (x < 836) g += arrow(x + 302, 582, x + 350, 582, { head: 14 });
  }

  s += band("gates", focus, g);
  /* ── the clock and the two exits ───────────────────────── */
  s += dashed(30, 700, 1210, 700);
  s += icon.clock(104, 762, 44);
  s += lines(104, 814, ["72 hours", "from delivery"], { size: 15, weight: 800, lh: 19 });
  s += text(190, 744, "All three inside the window and two things unlock.",
            { size: 18, weight: 700, anchor: "start" });
  s += text(190, 772, "Miss it and you keep the map. You lose the extras.",
            { size: 18, weight: 700, anchor: "start" });

  s += rect(190, 802, 400, 88);
  s += text(390, 836, "Run it yourself", { size: 20 });
  s += text(390, 864, "The plan is yours either way", { size: 13, weight: 600 });

  s += rect(646, 802, 400, 88, { strokeWidth: 3 });
  s += text(846, 836, "Have us hold the gates", { size: 20 });
  s += text(846, 864, "Twenty minutes to find out which", { size: 13, weight: 600 });

  s += text(620, 936, "Same destination. The only difference is who holds the gates.",
            { size: 19, weight: 900 });

  return svg(1240, 960, s);
}
