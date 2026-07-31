/**
 * SKETCH ENGINE -- hand-drawn diagrams as declarative markup.
 *
 * WHY THIS EXISTS
 * The training-deck aesthetic needs many cheap diagrams that all look like the same
 * hand drew them. Drawing each one in Excalidraw gives the look but not the
 * consistency, and every edit is a manual redraw. This takes a spec object and emits
 * a seeded SVG, so a diagram is markup we can diff and regenerate, not art we redo.
 *
 * THE ONE AESTHETIC RULE WORTH KNOWING
 * The reference material sketches the DRAWINGS and typesets the TEXT. That hybrid is
 * why it reads as fast-but-legible instead of messy. So: rough.js for every shape,
 * clean bold caps for every word. Never a handwriting font.
 *
 * Seeds are fixed per element so output is byte-stable across runs. Change a seed
 * only to re-roll a shape you dislike; never randomise, or every rebuild churns.
 */
import rough from "roughjs/bundled/rough.cjs.js";

const G = rough.generator();

export const INK = "#111111";
export const PAPER = "#ffffff";

/** House defaults. Roughness 1.4-1.9 reads as marker; above 2.5 reads as broken. */
const STROKE = { roughness: 1.6, bowing: 1.2, stroke: INK, strokeWidth: 2.4, seed: 1 };
const THIN = { ...STROKE, strokeWidth: 1.8 };

let uid = 0;
const nextSeed = () => (uid = (uid + 7) % 9973) + 1;

function paths(drawable, extra = "") {
  return G.toPaths(drawable)
    .map(
      (p) =>
        `<path d="${p.d}" stroke="${p.stroke === "none" ? "none" : p.stroke}" ` +
        `stroke-width="${p.strokeWidth ?? 0}" fill="${p.fill || "none"}" ` +
        `stroke-linecap="round" stroke-linejoin="round" ${extra}/>`,
    )
    .join("");
}

const O = (o = {}) => ({ ...STROKE, seed: o.seed ?? nextSeed(), ...o });

/* ── primitives ──────────────────────────────────────────────────────────── */

export const rect = (x, y, w, h, o) => paths(G.rectangle(x, y, w, h, O(o)));
export const circle = (cx, cy, d, o) => paths(G.circle(cx, cy, d, O(o)));
export const line = (x1, y1, x2, y2, o) => paths(G.line(x1, y1, x2, y2, O(o)));
export const poly = (pts, o) => paths(G.linearPath(pts, O(o)));
export const curve = (pts, o) => paths(G.curve(pts, O(o)));

/** Dashed divider. rough's own dash fill is unreliable on lines, so step it manually. */
export function dashed(x1, y1, x2, y2, o = {}) {
  const dash = o.dash ?? 14;
  const gap = o.gap ?? 10;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.hypot(dx, dy);
  const step = dash + gap;
  let out = "";
  for (let d = 0; d < len; d += step) {
    const t0 = d / len;
    const t1 = Math.min((d + dash) / len, 1);
    out += line(x1 + dx * t0, y1 + dy * t0, x1 + dx * t1, y1 + dy * t1, {
      ...THIN,
      ...o,
      seed: nextSeed(),
    });
  }
  return out;
}

/** Arrow with a proper head. `curved` bows the shaft, which reads friendlier. */
export function arrow(x1, y1, x2, y2, o = {}) {
  const head = o.head ?? 15;
  const a = Math.atan2(y2 - y1, x2 - x1);
  let shaft;
  if (o.curved) {
    const mx = (x1 + x2) / 2;
    const my = (y1 + y2) / 2;
    const nx = -(y2 - y1);
    const ny = x2 - x1;
    const nl = Math.hypot(nx, ny) || 1;
    const b = o.curved;
    shaft = curve([[x1, y1], [mx + (nx / nl) * b, my + (ny / nl) * b], [x2, y2]], o);
  } else {
    shaft = line(x1, y1, x2, y2, o);
  }
  const w = 0.42;
  return (
    shaft +
    line(x2, y2, x2 - head * Math.cos(a - w), y2 - head * Math.sin(a - w), { ...o, seed: nextSeed() }) +
    line(x2, y2, x2 - head * Math.cos(a + w), y2 - head * Math.sin(a + w), { ...o, seed: nextSeed() })
  );
}

/* ── type ────────────────────────────────────────────────────────────────── */

const SANS =
  "'Hanken Grotesk','Helvetica Neue',Helvetica,Arial,'DejaVu Sans',sans-serif";

/**
 * Typeset text. Sketch the shapes, typeset the words -- see the header note.
 * size in px, weight 400-900, `caps` uppercases and adds tracking.
 */
export function text(x, y, str, o = {}) {
  const size = o.size ?? 22;
  const weight = o.weight ?? 800;
  const anchor = o.anchor ?? "middle";
  const caps = o.caps ?? false;
  const body = caps ? String(str).toUpperCase() : String(str);
  return (
    `<text x="${x}" y="${y}" font-family="${SANS}" font-size="${size}" ` +
    `font-weight="${weight}" fill="${o.fill ?? INK}" text-anchor="${anchor}" ` +
    `letter-spacing="${o.tracking ?? (caps ? 0.6 : 0)}" ` +
    `${o.italic ? 'font-style="italic" ' : ""}>${esc(body)}</text>`
  );
}

/** Multi-line text block, centred on x. */
export function lines(x, y, arr, o = {}) {
  const lh = o.lh ?? (o.size ?? 22) * 1.25;
  return arr.map((s, i) => text(x, y + i * lh, s, o)).join("");
}

const esc = (s) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/** Rough underline, for a heading that needs to land. */
export const underline = (x1, x2, y, o) =>
  line(x1, y, x2, y, { ...THIN, strokeWidth: 3, ...o });

/** Struck-through word: the "this is not the goal" move. */
export const crossout = (x, y, w, h, o = {}) =>
  line(x - w / 2, y + h / 2, x + w / 2, y - h / 2, { ...STROKE, ...o, seed: nextSeed() }) +
  line(x - w / 2, y - h / 2, x + w / 2, y + h / 2, { ...STROKE, ...o, seed: nextSeed() });

/* ── stick figures ───────────────────────────────────────────────────────── */

/**
 * Stick figure. `h` is total height; everything scales off it so figures at
 * different sizes stay in proportion.
 *
 * Poses: 'stand' | 'walk-phone' | 'sit-think'
 */
export function figure(x, y, h, pose = "stand", o = {}) {
  const s = h / 100;
  const headD = 26 * s;
  const neck = y - h + headD;
  const hip = y - h * 0.38;
  let out = "";

  if (pose === "walk-phone") {
    // Leaning forward, phone held out AHEAD and BELOW the head -- the impulse buyer.
    // The phone must never cross the head: an arm over the face reads as a broken
    // figure rather than a distracted one, which is the whole point of the pose.
    const lean = 10 * s;
    const shoulder = neck + 8 * s;
    out += circle(x - lean, neck - headD / 2, headD, o);
    out += line(x - lean, neck, x + 2 * s, hip, o); // torso, leaning
    // near arm: shoulder -> elbow -> hand, all forward of the body and below the chin
    out += poly(
      [[x - lean, shoulder], [x - 26 * s, shoulder + 12 * s], [x - 40 * s, shoulder + 4 * s]],
      o,
    );
    out += rect(x - 52 * s, shoulder - 6 * s, 13 * s, 19 * s, { ...o, seed: nextSeed() }); // phone
    out += poly([[x - lean + 3 * s, shoulder + 2 * s], [x + 18 * s, shoulder + 24 * s]], o); // trailing arm
    out += poly([[x + 2 * s, hip], [x - 18 * s, y - 6 * s], [x - 30 * s, y]], o); // back leg
    out += poly([[x + 2 * s, hip], [x + 22 * s, y - 12 * s], [x + 32 * s, y]], o); // striding leg
    // motion ticks behind the heel
    out += line(x + 40 * s, y - 14 * s, x + 56 * s, y - 14 * s, THIN);
    out += line(x + 38 * s, y - 26 * s, x + 54 * s, y - 26 * s, THIN);
    return out;
  }

  if (pose === "sit-think") {
    // Seated at a desk, elbow down, hand to chin -- the deliberate buyer.
    // Legs are deliberately NOT drawn: the desk occludes them in the reference, and
    // drawing them makes the figure read as sitting ON the table.
    out += circle(x, neck - headD / 2, headD, o);
    out += line(x, neck, x - 2 * s, hip, o); // torso
    out += poly(
      [[x - 2 * s, neck + 26 * s], [x - 20 * s, neck + 44 * s], [x - 8 * s, neck + 10 * s]],
      o,
    ); // forearm up to the chin
    out += poly([[x, neck + 12 * s], [x + 22 * s, neck + 34 * s]], o); // resting arm
    return out;
  }

  // stand
  out += circle(x, neck - headD / 2, headD, o);
  out += line(x, neck, x, hip, o);
  out += poly([[x - 24 * s, neck + 26 * s], [x, neck + 8 * s], [x + 24 * s, neck + 26 * s]], o);
  out += poly([[x, hip], [x - 20 * s, y]], o);
  out += poly([[x, hip], [x + 20 * s, y]], o);
  return out;
}

/** Desk: a top edge plus two legs. Pair with pose 'sit-think'. */
export function desk(x, y, w, h, o = {}) {
  return (
    line(x, y, x + w, y, o) +
    line(x + 8, y, x + 8, y + h, o) +
    line(x + w - 8, y, x + w - 8, y + h, o)
  );
}

/* ── icons ───────────────────────────────────────────────────────────────── */

/** Small glyphs, all drawn inside a `s`-sized box centred on (x,y). */
export const icon = {
  envelope: (x, y, s, o) =>
    rect(x - s / 2, y - s * 0.34, s, s * 0.68, o) +
    poly([[x - s / 2, y - s * 0.34], [x, y + s * 0.06], [x + s / 2, y - s * 0.34]], o),
  video: (x, y, s, o) =>
    rect(x - s / 2, y - s * 0.32, s * 0.72, s * 0.64, o) +
    poly([[x + s * 0.24, y - s * 0.1], [x + s / 2, y - s * 0.3], [x + s / 2, y + s * 0.3], [x + s * 0.24, y + s * 0.1]], o),
  speech: (x, y, s, o) =>
    rect(x - s / 2, y - s * 0.36, s, s * 0.6, { ...o, seed: nextSeed() }) +
    poly([[x - s * 0.2, y + s * 0.24], [x - s * 0.28, y + s * 0.46], [x + s * 0.02, y + s * 0.24]], o) +
    line(x - s * 0.28, y - s * 0.12, x + s * 0.28, y - s * 0.12, THIN) +
    line(x - s * 0.28, y + s * 0.04, x + s * 0.14, y + s * 0.04, THIN),
  stairs: (x, y, s, o) =>
    poly(
      [
        [x - s / 2, y + s / 2], [x - s / 2, y + s * 0.16], [x - s * 0.16, y + s * 0.16],
        [x - s * 0.16, y - s * 0.16], [x + s * 0.18, y - s * 0.16],
        [x + s * 0.18, y - s / 2], [x + s / 2, y - s / 2],
      ],
      o,
    ),
  clock: (x, y, s, o) =>
    circle(x, y, s, o) + line(x, y, x, y - s * 0.3, THIN) + line(x, y, x + s * 0.24, y + s * 0.1, THIN),
  bolt: (x, y, s, o) =>
    poly(
      [
        [x + s * 0.18, y - s / 2], [x - s * 0.22, y + s * 0.06], [x + s * 0.02, y + s * 0.06],
        [x - s * 0.16, y + s / 2], [x + s * 0.26, y - s * 0.06], [x + s * 0.02, y - s * 0.06],
        [x + s * 0.18, y - s / 2],
      ],
      o,
    ),
  money: (x, y, s, o) =>
    rect(x - s / 2, y - s * 0.3, s, s * 0.6, o) + circle(x, y, s * 0.34, { ...o, seed: nextSeed() }) +
    text(x, y + s * 0.1, "$", { size: s * 0.34, weight: 800 }),
  target: (x, y, s, o) =>
    circle(x, y, s, o) + circle(x, y, s * 0.52, { ...o, seed: nextSeed() }) +
    circle(x, y, s * 0.14, { ...o, seed: nextSeed() }) +
    line(x + s * 0.3, y - s * 0.3, x + s * 0.62, y - s * 0.62, THIN),
  handshake: (x, y, s, o) =>
    poly([[x - s / 2, y], [x - s * 0.2, y - s * 0.16], [x + s * 0.06, y + s * 0.04]], o) +
    poly([[x + s / 2, y], [x + s * 0.2, y - s * 0.16], [x - s * 0.06, y + s * 0.04]], o) +
    poly([[x - s * 0.24, y + s * 0.1], [x, y + s * 0.26], [x + s * 0.24, y + s * 0.1]], o),
  check: (x, y, s, o) =>
    poly([[x - s * 0.4, y], [x - s * 0.1, y + s * 0.3], [x + s * 0.44, y - s * 0.36]], {
      ...o,
      strokeWidth: 3.4,
    }),
  // Stacked bills. Offsets must exceed the bill height or the three rects merge
  // into a scribble at small sizes.
  cash: (x, y, s, o) =>
    rect(x - s / 2, y - s * 0.34, s, s * 0.22, o) +
    rect(x - s / 2 + s * 0.04, y - s * 0.06, s, s * 0.22, { ...o, seed: nextSeed() }) +
    rect(x - s / 2 + s * 0.08, y + s * 0.22, s, s * 0.22, { ...o, seed: nextSeed() }),
};

/* ── document ────────────────────────────────────────────────────────────── */

/**
 * Wrap body SVG in a document. `frame: true` draws the outer rough border that
 * makes a diagram read as a panel rather than floating marks.
 */
export function svg(w, h, body, o = {}) {
  uid = 0; // deterministic per document
  const border = o.frame === false ? "" : rect(4, 4, w - 8, h - 8, { strokeWidth: 3, seed: 991 });
  return (
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}">` +
    `<rect width="${w}" height="${h}" fill="${o.bg ?? PAPER}"/>` +
    border +
    body +
    `</svg>`
  );
}

/** Reset the seed counter so a diagram built in pieces stays deterministic. */
export const reset = () => {
  uid = 0;
};
