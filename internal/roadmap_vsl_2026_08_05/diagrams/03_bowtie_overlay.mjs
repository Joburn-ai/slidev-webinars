/**
 * THE OPEN BOWTIE, OVERLAID WITH THE ROADMAP FUNNEL.  v4 slide 44.
 *
 * WHY THIS IS HAND-AUTHORED AND NOT MERMAID
 * CANON_bowtie_overlay_transformation_pulled_forward_2026_08_06.md section 3:
 * mermaid draws graphs, it cannot superimpose two diagrams. This one is a single
 * silhouette with a block of functions that TRANSLATES across it, which no graph
 * layout engine can express. So: geometry by hand, per-state styling by a class
 * on the svg root, one addressable group per idea.
 *
 * THE CANON CONSTRAINTS THAT SHAPE THE DRAWING
 *  - 6.1  no line, no gate, no threshold at commit. A threshold IS the
 *         key-decision framing. COMMIT is a word sitting in the notch under the
 *         waist and nothing else. The two side washes are GRADIENTS that fade to
 *         zero through the middle, precisely so neither one has an edge.
 *  - 5.1  the pinch is OPEN. waist height / outer height = 0.56. A classic
 *         bowtie is about 0.03. It has to read as a pathway, not a wall.
 *  - 5.3  the word hourglass appears nowhere. It is Duct Tape Marketing's, it
 *         carries a TM, and their hourglass is a different idea.
 *
 * COLOUR GRAMMAR
 *   grey  = out of order, not a mistake           state 1, and the vacated slots
 *   ember = the arrangement being argued against  state 2, transformation gated behind commit
 *   gold  = the re-order, the payoff              state 3, the four moved functions
 *   teal  = the path that works                   state 3, the whole pathway lit
 *
 * THREE REVEALS, driven by $clicks. Nothing else changes.
 *   bt-s0  nothing painted
 *   bt-s1  the bowtie alone, dimmed, COMMIT marked
 *   bt-s2  the right side lights ember. The transformation normally lives here
 *   bt-s3  #bt-transformation TRANSLATES -1108 user units, across the commit
 *          label, into the acquisition funnel, and each function picks up the
 *          name of the roadmap-funnel piece that performs it. A movement.
 *
 * TYPE SIZES ARE MEASURED, NOT GUESSED. Every string in here was rendered in
 * chromium and its bbox read back before a width was chosen. The band is 4.8:1,
 * so horizontal room is the binding constraint and short labels are mandatory.
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const DECK = resolve(HERE, "..");

/* ── canvas. 4.8:1, inside the 4:1 to 5:1 band the slide reserves ───────── */
const W = 2400;
const H = 500;

const SANS =
  "Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif";

const C = {
  teal: "#209080",
  tealb: "#2BB3A0",
  ember: "#C4552F",
  emberd: "#8C3419", // ember ink on #FBE3D9
  emberm: "#A34A28",
  gold: "#D9B96A",
  goldd: "#8A6A18", // gold ink on #FBF0D6
  goldm: "#9A7A2C",
  fog: "#7A9199",
  fogd: "#5C7078",
};

/* ── the silhouette ─────────────────────────────────────────────────────── */
const X_L = 76;
const X_R = 2324;
const OUT_T = 86;
const OUT_B = 486;
const WST_T = 174;
const WST_B = 398;
const WST_L = 1065;
const WST_R = 1335;
const MID = (WST_L + WST_R) / 2; // 1200. The commit abscissa. A LABEL, not a line.

const OUTER_H = OUT_B - OUT_T; // 400
const WAIST_H = WST_B - WST_T; // 224
const OPENNESS = +(WAIST_H / OUTER_H).toFixed(3); // 0.56

/* ── the four customer-success functions, and the roadmap-funnel piece that
      performs each one. Canon section 2. The second label only paints at s3,
      which is the overlay: the pieces turn out to BE those functions. ─────── */
const CHIP_W = 240;
const CHIP_H = 94;
const CHIP_Y = 256;
const GAP = 16;
const PITCH = CHIP_W + GAP; // 256
const RIGHT_X0 = 1250;
const LEFT_X0 = 142;
const SHIFT = LEFT_X0 - RIGHT_X0; // -1108

const FUNCTIONS = [
  ["onboarding", "ONBOARDING", "your intake form"],
  ["deliverable", "DELIVERABLE", "your roadmap"],
  ["orientation", "ORIENTATION", "the roadmap call"],
  ["activation", "ACTIVATION", "your 30/60/90 plan"],
];

const chipX = (i) => RIGHT_X0 + i * PITCH;
const BLOCK_MID = (RIGHT_X0 + chipX(3) + CHIP_W) / 2; // 1754
const BLOCK_R = chipX(3) + CHIP_W; // 2258

/* ── the acquisition spine. Standard bowtie left ────────────────────────── */
const SPINE_Y = 226;
const SPINE = [
  [210, "ATTENTION"],
  [445, "INTEREST"],
  [790, "A SALES CONVERSATION"],
];
const CHEV = [330, 555];

/* ── primitives ─────────────────────────────────────────────────────────── */
const esc = (s) =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/**
 * 🔴 NEVER PUT font-size ON AN SVG ELEMENT IN A SLIDEV DECK.
 * Slidev's UnoCSS runs presetAttributify, which turns the presentation attribute
 * `font-size="30"` into the generated rule `[font-size~="30"]{font-size:7.5rem}`
 * -- 120px where 30 user units were meant, and a real CSS rule beats a
 * presentation attribute. Every label rendered at 4x and the diagram tore itself
 * apart, while the same file was pixel-correct as a standalone svg, because
 * nothing scans a standalone svg. Caught by screenshotting the REAL deck.
 * So: the type scale lives in the scoped stylesheet, keyed by class, and the
 * only attributes on a <text> are x, y, id and class.
 */
const TYPE = {
  side: { size: 26, weight: 800, track: 3 },
  spine: { size: 24, weight: 800, track: 1.4 },
  commit: { size: 30, weight: 900, track: 5 },
  note: { size: 20, weight: 600, track: 0 },
  cs: { size: 26, weight: 800, track: 1.2 },
  rm: { size: 19, weight: 700, track: 0 },
  label: { size: 26, weight: 900, track: 3 },
};

function t(x, y, str, kind, o = {}) {
  const cls = [`bt-t-${kind}`, o.cls].filter(Boolean).join(" ");
  const a = [`class="${cls}"`, `x="${x}"`, `y="${y}"`];
  if (o.id) a.unshift(`id="${o.id}"`);
  return `<text ${a.join(" ")}>${esc(o.caps ? String(str).toUpperCase() : str)}</text>`;
}

/** The silhouette. ONE continuous path, so there is no seam at the middle. */
function silhouette(id, cls) {
  const r = 44;
  const d = [
    `M ${X_L} ${OUT_T}`,
    `L ${WST_L - r} ${WST_T - 4}`,
    `Q ${WST_L} ${WST_T} ${WST_L + r} ${WST_T}`,
    `L ${WST_R - r} ${WST_T}`,
    `Q ${WST_R} ${WST_T} ${WST_R + r} ${WST_T - 4}`,
    `L ${X_R} ${OUT_T}`,
    `L ${X_R} ${OUT_B}`,
    `L ${WST_R + r} ${WST_B + 4}`,
    `Q ${WST_R} ${WST_B} ${WST_R - r} ${WST_B}`,
    `L ${WST_L + r} ${WST_B}`,
    `Q ${WST_L} ${WST_B} ${WST_L - r} ${WST_B + 4}`,
    `L ${X_L} ${OUT_B}`,
    "Z",
  ].join(" ");
  return `<path id="${id}" class="${cls}" d="${d}" />`;
}

/** Left-pointing arrow. The movement cue in state 3. */
function arrowLeft(x1, x2, y, id, cls) {
  const h = 24;
  return (
    `<g id="${id}" class="${cls}">` +
    `<path d="M ${x1} ${y} L ${x2} ${y}" />` +
    `<path d="M ${x2 + h} ${y - h * 0.56} L ${x2} ${y} L ${x2 + h} ${y + h * 0.56}" />` +
    `</g>`
  );
}

/* ── the stylesheet. Every selector scoped to the svg id ────────────────── */
function css(standalone) {
  const S = "#bowtie-overlay";
  // 🔴 the standalone files are sized by their width/height ATTRIBUTES, because an
  // svg with only a viewBox has no intrinsic size and `width:100%;height:auto`
  // resolves to nothing inside an <img>. The three state files rendered as blank
  // broken-image boxes until this split existed. The inline copy is the opposite
  // case: it must NOT carry width/height attributes, because Slidev's attributify
  // would turn `width="2400"` into a utility and blow the box out.
  return `
${S}{display:block;${standalone ? "" : "width:100%;height:auto;"}font-family:${SANS};}
${S} text{fill:${C.fogd};text-anchor:middle;}
${Object.entries(TYPE)
  .map(([k, v]) => `${S} .bt-t-${k}{font-size:${v.size}px;font-weight:${v.weight};letter-spacing:${v.track}px;}`)
  .join("\n")}
${S} .bt-anim{transition:opacity 340ms ease, fill 340ms ease, stroke 340ms ease;}
${S} #bt-transformation{transition:transform 900ms cubic-bezier(.4,0,.2,1), opacity 340ms ease;}
${S}.bt-static *{transition:none !important;}

/* the silhouette */
${S} #bt-outline-base{fill:#FAFBFB;stroke:${C.fog};stroke-width:3.6;}
${S} #bt-outline-lit{fill:none;stroke:${C.teal};stroke-width:4.4;opacity:0;}
${S} #bt-wash-right{fill:url(#bt-grad-right);stroke:none;opacity:0;}
${S} #bt-wash-left{fill:url(#bt-grad-left);stroke:none;opacity:0;}

/* labels */
${S} #bt-label-acq,${S} #bt-label-cs{opacity:.55;}
${S} #bt-acq-spine{opacity:.55;}
${S} #bt-acq-spine .bt-chev{fill:none;stroke:${C.fog};stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round;}
${S} #bt-commit-word{fill:${C.fogd};}
${S} #bt-commit-note{fill:${C.fog};}

/* the four functions, and the slots they leave behind */
${S} .bt-chip rect{fill:#F4F6F6;stroke:${C.fog};stroke-width:2.2;}
${S} .bt-chip .bt-cs{fill:${C.fogd};transform:translateY(14px);transition:transform 340ms ease, fill 340ms ease;}
${S} .bt-chip .bt-rm{fill:${C.goldd};opacity:0;}
${S} #bt-ghosts{opacity:0;}
${S} #bt-ghosts rect{fill:none;stroke:${C.fog};stroke-width:2.2;stroke-dasharray:8 8;}
${S} #bt-move{opacity:0;}
${S} #bt-move path{fill:none;stroke:${C.gold};stroke-width:5;stroke-linecap:round;stroke-linejoin:round;}
${S} #bt-transformation{opacity:.55;}
${S} #bt-transformation-label{fill:${C.fogd};}

/* ── state 0. nothing painted ─────────────────────────────────────────── */
${S}.bt-s0{opacity:0;}

/* ── state 1. the bowtie alone, dimmed, COMMIT marked ─────────────────── */
${S}.bt-s1 #bt-outline-base{opacity:.55;}

/* ── state 2. the right side lights. ember = the arrangement argued against */
${S}.bt-s2 #bt-outline-base{opacity:.6;}
${S}.bt-s2 #bt-wash-right{opacity:1;}
${S}.bt-s2 #bt-label-cs{opacity:1;}
${S}.bt-s2 #bt-label-cs text{fill:${C.ember};}
${S}.bt-s2 #bt-transformation{opacity:1;}
${S}.bt-s2 #bt-transformation-label{fill:${C.ember};}
${S}.bt-s2 .bt-chip rect{fill:#FBE3D9;stroke:${C.ember};stroke-width:2.6;}
${S}.bt-s2 .bt-chip .bt-cs{fill:${C.emberd};}

/* ── state 3. THE MOVEMENT. gold = the re-order, teal = the path that works */
${S}.bt-s3 #bt-outline-base{opacity:.35;}
${S}.bt-s3 #bt-outline-lit{opacity:1;}
${S}.bt-s3 #bt-wash-right{opacity:.18;}
${S}.bt-s3 #bt-wash-left{opacity:1;}
${S}.bt-s3 #bt-label-cs{opacity:.4;}
${S}.bt-s3 #bt-label-acq{opacity:1;}
${S}.bt-s3 #bt-label-acq text{fill:${C.teal};}
${S}.bt-s3 #bt-acq-spine{opacity:1;}
${S}.bt-s3 #bt-acq-spine text{fill:${C.teal};}
${S}.bt-s3 #bt-acq-spine .bt-chev{stroke:${C.tealb};}
${S}.bt-s3 #bt-ghosts{opacity:.5;}
${S}.bt-s3 #bt-move{opacity:1;}
${S}.bt-s3 #bt-transformation{opacity:1;transform:translateX(${SHIFT}px);}
${S}.bt-s3 #bt-transformation-label{fill:${C.goldd};}
${S}.bt-s3 .bt-chip rect{fill:#FBF0D6;stroke:${C.gold};stroke-width:2.8;}
${S}.bt-s3 .bt-chip .bt-cs{fill:${C.goldd};transform:none;}
${S}.bt-s3 .bt-chip .bt-rm{opacity:1;}
`.trim();
}

/* ── the body ───────────────────────────────────────────────────────────── */
function body() {
  let s = "";

  /* Both washes fade to zero THROUGH the middle, so neither one has an edge
     anywhere near commit. That is canon 6.1 enforced in paint, not in prose. */
  s +=
    `<defs>` +
    `<linearGradient id="bt-grad-right" gradientUnits="userSpaceOnUse" x1="840" y1="0" x2="1860" y2="0">` +
    `<stop offset="0" stop-color="${C.ember}" stop-opacity="0"/>` +
    `<stop offset="1" stop-color="${C.ember}" stop-opacity="0.16"/>` +
    `</linearGradient>` +
    `<linearGradient id="bt-grad-left" gradientUnits="userSpaceOnUse" x1="1560" y1="0" x2="540" y2="0">` +
    `<stop offset="0" stop-color="${C.teal}" stop-opacity="0"/>` +
    `<stop offset="1" stop-color="${C.teal}" stop-opacity="0.14"/>` +
    `</linearGradient>` +
    `</defs>`;

  s += silhouette("bt-outline-base", "bt-anim");
  s += `<g id="bt-washes">${silhouette("bt-wash-right", "bt-anim")}${silhouette("bt-wash-left", "bt-anim")}</g>`;
  // the same path again, teal, on top. State 3 lights the WHOLE pathway, both
  // sides at once, because by then it is one continuous path and not two halves.
  s += silhouette("bt-outline-lit", "bt-anim");

  /* side labels, outside the shape */
  s += `<g id="bt-label-acq" class="bt-anim">${t(570, 44, "acquisition", "side", { caps: true })}</g>`;
  s += `<g id="bt-label-cs" class="bt-anim">${t(1780, 44, "customer success", "side", { caps: true })}</g>`;

  /* the acquisition spine. Standard bowtie left, and it never moves */
  let sp = "";
  SPINE.forEach(([x, label], i) => {
    sp += t(x, SPINE_Y, label, "spine", { id: `bt-spine-${i + 1}`, caps: true });
  });
  for (const x of CHEV)
    sp += `<path class="bt-chev" d="M ${x} ${SPINE_Y - 13} L ${x + 12} ${SPINE_Y - 6} L ${x} ${SPINE_Y + 1}" />`;
  s += `<g id="bt-acq-spine" class="bt-anim">${sp}</g>`;

  /* COMMIT. A word in the notch under the waist. No line, no gate, no tick. */
  s +=
    `<g id="bt-commit">` +
    t(MID, 444, "commit", "commit", { id: "bt-commit-word", caps: true }) +
    t(MID, 470, "just the next step", "note", { id: "bt-commit-note" }) +
    `</g>`;

  /* the slots the four functions vacate. Grey: not a mistake, just out of order */
  let gh = "";
  for (let i = 0; i < 4; i++)
    gh += `<rect x="${chipX(i)}" y="${CHIP_Y}" width="${CHIP_W}" height="${CHIP_H}" rx="14" />`;
  s += `<g id="bt-ghosts" class="bt-anim">${gh}</g>`;

  /* the movement cue. One long left arrow, tail inside the vacated slots,
     head landing in the open gap just short of the commit label */
  s += arrowLeft(BLOCK_R - 78, LEFT_X0 + 1108 - 78, CHIP_Y + CHIP_H / 2, "bt-move", "bt-anim");

  /* THE MOVER. Four functions plus the word for what they are, one group,
     one translate. The roadmap-funnel names paint only once they have landed. */
  let mv = "";
  for (let i = 0; i < 4; i++) {
    const [id, cs, rm] = FUNCTIONS[i];
    const x = chipX(i);
    const cx = x + CHIP_W / 2;
    mv +=
      `<g id="bt-fn-${id}" class="bt-chip">` +
      `<rect x="${x}" y="${CHIP_Y}" width="${CHIP_W}" height="${CHIP_H}" rx="14" />` +
      t(cx, CHIP_Y + 38, cs, "cs", { id: `bt-cs-${id}`, cls: "bt-cs", caps: true }) +
      t(cx, CHIP_Y + 72, rm, "rm", { id: `bt-rm-${id}`, cls: "bt-rm" }) +
      `</g>`;
  }
  mv += t(BLOCK_MID, 386, "the transformation", "label", { id: "bt-transformation-label", caps: true });
  s += `<g id="bt-transformation">${mv}</g>`;

  return s;
}

/* ── emit ───────────────────────────────────────────────────────────────── */
function doc(stateClass, { standalone = true } = {}) {
  const cls = `bt ${stateClass}${standalone ? " bt-static" : ""}`;
  const open =
    `<svg id="bowtie-overlay" class="${cls}" xmlns="http://www.w3.org/2000/svg" ` +
    (standalone ? `width="${W}" height="${H}" ` : "") +
    `viewBox="0 0 ${W} ${H}" role="img" ` +
    `aria-label="An open bowtie with a thick middle. Acquisition on the left, customer ` +
    `success on the right, COMMIT labelled in the notch under the wide middle. Four ` +
    `customer-success functions move left across the commit label into the acquisition ` +
    `funnel, where each one is named as a piece of the roadmap funnel.">`;
  return `${open}<style>${css(standalone)}</style>${body()}</svg>`;
}

/** The slide markup. $clicks drives the state class, and nothing else. */
function slide() {
  // 🔴 ONE LINE, NO BLANK LINES. A blank line inside an html block ends the block
  // in markdown-it and the rest of the svg gets parsed as markdown. The stylesheet
  // is readable in the standalone file and collapsed in the inlined copy.
  const inline = doc("bt-s0", { standalone: false })
    .replace(`class="bt bt-s0"`, `:class="'bt bt-s' + Math.min($clicks, 3)"`)
    .replace(/\s*\n\s*/g, " ");
  return `---
layout: default
clicks: 3
class: flex flex-col justify-center
---

<!-- slide:rv-44 -- the bowtie overlay. v4 script beat 11, slide 44. -->

<div class="rt-kicker">AND HERE IS WHY THAT WORKS</div>
<div class="rt-h2">So even if you decide not to work with us at all, you walk away with a thirty, sixty, ninety day plan.</div>

<div class="rt-figure mt-5">
${inline}
</div>

<div class="rt-h2 mt-5" v-click="3">You are basically already being treated like a client, inside our process.</div>

<!--
VERBATIM. The headline is script [44]. The second line is JOHN'S OWN PHRASE from the canon note and
  it lands on click 3, on the movement itself, which is the sentence that beat exists to earn.
  If the parent build maps [44]'s tail ("that's yours to keep either way") to its own slide, swap
  the headline and leave everything below it alone -- the diagram only needs \`clicks: 3\` and the
  \`:class\` binding.
JOHN, 2026-08-06, DO NOT PARAPHRASE EITHER PHRASE: "pulling the transformation out of customer
  success and into the acquisition funnel" / "you're basically already treating them like a client
  inside your process."
THE THREE REVEALS. \`clicks: 3\`, and \`$clicks\` drives the diagram. The diagram uses NO v-click
  elements, because the third beat is a TRANSFORM and v-click only toggles visibility.
  click 1  bt-s1  the bowtie alone, dimmed, COMMIT marked
  click 2  bt-s2  the right side lights ember. The transformation normally lives here
  click 3  bt-s3  #bt-transformation translates ${SHIFT} user units across the commit label in
                  900ms, lands inside the acquisition funnel, turns gold, and each function
                  picks up the name of the roadmap-funnel piece that performs it.
                  A MOVEMENT, not a before-and-after pair. Canon section 3.
CANON 6.1: no line, no gate, no threshold at commit. The two side washes are gradients that fade
  to zero through the middle so neither one has an edge. COMMIT is a word in the notch, and the
  note under it says what it is: just the next step.
CANON 5.1: the pinch is OPEN. waist / outer height = ${OPENNESS}. A classic bowtie is about 0.03.
CANON 5.3: never call it an hourglass. That is Duct Tape Marketing's, and it is marked.
DIAGRAM: hand-authored, ${W}x${H} = ${(W / H).toFixed(2)}:1, generated by
  diagrams/03_bowtie_overlay.mjs. All three states screenshot-verified and looked at.
-->
`;
}

const OUT = resolve(DECK, "public/flows");
mkdirSync(OUT, { recursive: true });
writeFileSync(`${OUT}/03_bowtie_overlay.svg`, doc("bt-s1"));
writeFileSync(`${OUT}/03a_bowtie_state1.svg`, doc("bt-s1"));
writeFileSync(`${OUT}/03b_bowtie_state2.svg`, doc("bt-s2"));
writeFileSync(`${OUT}/03c_bowtie_state3.svg`, doc("bt-s3"));
writeFileSync(`${HERE}/03_bowtie_overlay.slide.md`, slide());

console.log(
  JSON.stringify(
    {
      viewBox: `0 0 ${W} ${H}`,
      aspect: +(W / H).toFixed(3),
      openness: OPENNESS,
      waist: [WST_L, WST_R, WAIST_H],
      outer_h: OUTER_H,
      commit_x: MID,
      shift: SHIFT,
      chips_right: FUNCTIONS.map((f, i) => [f[0], chipX(i), chipX(i) + CHIP_W]),
      chips_left: FUNCTIONS.map((f, i) => [f[0], chipX(i) + SHIFT, chipX(i) + CHIP_W + SHIFT]),
      gap_between_blocks: [LEFT_X0 + 3 * PITCH + CHIP_W, RIGHT_X0],
    },
    null,
    2,
  ),
);
