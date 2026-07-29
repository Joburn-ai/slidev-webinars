#!/usr/bin/env node
/**
 * fill.mjs -- fill a roadmap deck's placeholders and REFUSE to ship an unfilled one.
 *
 * WHY THIS EXISTS. The template originally used {{Var}}. Vue compiles that as an
 * interpolation, so every placeholder rendered as an EMPTY STRING with no error --
 * the Snapshot slide showed three sets of empty quote marks and nobody could see
 * which variables were unfilled. Worse, {{Var}} inside a v-motion binding survived
 * as a literal invalid CSS string, so all three constraint bars animated 0 to 0.
 *
 * Placeholders are now @@VAR@@ (not %%VAR%%, because %% is Mermaid's comment and
 * init-directive syntax and would collide inside flowchart slides).
 *
 * Usage:  node fill.mjs vars.json slides.md out.md
 *         node fill.mjs --check slides.md          (gate: list unfilled tokens)
 */
import fs from 'node:fs'

const RE = /@@([A-Za-z_][A-Za-z0-9_]*)@@/g

if (process.argv[2] === '--check') {
  // strip HTML comments first -- tokens inside speaker notes and doc blocks never
  // render, so flagging them would make the gate cry wolf and get ignored.
  const src = fs.readFileSync(process.argv[3], 'utf8').replace(/<!--[\s\S]*?-->/g, '')
  const left = [...new Set([...src.matchAll(RE)].map(m => m[1]))]
  if (left.length) {
    console.error(`GATE FAILED -- ${left.length} unfilled placeholder(s):`)
    left.forEach(v => console.error('  @@' + v + '@@'))
    process.exit(1)
  }
  console.log('GATE PASSED -- no unfilled placeholders')
  process.exit(0)
}

const [varsPath, inPath, outPath] = process.argv.slice(2)
const vars = JSON.parse(fs.readFileSync(varsPath, 'utf8'))
let src = fs.readFileSync(inPath, 'utf8')

const missing = new Set()
src = src.replace(RE, (_, name) => {
  if (vars[name] === undefined || vars[name] === '') { missing.add(name); return `@@${name}@@` }
  return String(vars[name])
})

// constraint bar widths ride CSS vars, not text substitution
const pct = k => (vars[k] === undefined ? null : String(vars[k]).replace('%', '') + '%')
const t = pct('Constraint_Time_Pct'), e = pct('Constraint_Energy_Pct'), a = pct('Constraint_Attention_Pct')
if (t && e && a) {
  src += `\n<style>\n:root{--ct-time:${t};--ct-energy:${e};--ct-attention:${a};}\n</style>\n`
} else {
  missing.add('Constraint_*_Pct (all three required)')
}

if (missing.size) {
  console.error(`REFUSING TO WRITE -- ${missing.size} missing:`)
  ;[...missing].forEach(v => console.error('  ' + v))
  process.exit(1)
}
fs.writeFileSync(outPath, src)
console.log(`filled -> ${outPath}`)
