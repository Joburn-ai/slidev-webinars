import { defineConfig } from 'unocss'

/**
 * REPO-WIDE FIX -- 2026-07-28
 *
 * PROBLEM: every deck in this repo shipped with a BLANK toolbar. The drawing
 * pen, undo, erase, colour swatches, nav arrows and slide-overview icons all
 * rendered as empty boxes. Verified across two independently-built decks, so it
 * was never deck-specific.
 *
 * CAUSE: UnoCSS generates icon classes only for the ones it finds while scanning
 * source. Slidev's own toolbar components live inside node_modules/@slidev/client,
 * which is not scanned, so none of their icon classes were ever generated. The
 * buttons were built (.slidev-icon-btn exists, with padding and hover states) --
 * only the glyphs were missing. A button you cannot see is a feature nobody uses,
 * which is why the drawing layer looked broken.
 *
 * FIX: safelist every carbon icon Slidev's internals reference, extracted
 * directly from @slidev/client. 45 icons.
 *
 * IF SLIDEV IS UPGRADED, re-extract with:
 *   grep -rohE "carbon:[a-z0-9-]+" node_modules/@slidev/client/internals/*.vue \
 *     node_modules/@slidev/client/builtin/*.vue | sed 's/carbon:/i-carbon:/' | sort -u
 */

const SLIDEV_TOOLBAR_ICONS = [
  'account', 'align-box-bottom-right', 'apps', 'arrow-left', 'arrow-right',
  'arrow-up-right', 'camera', 'checkbox', 'checkmark', 'chevron-up', 'close',
  'close-outline', 'cursor-1', 'document-pdf', 'download', 'drop-photo',
  'erase', 'error', 'information', 'launch', 'list-boxes', 'logo-twitter',
  'magic-wand', 'magic-wand-filled', 'maximize', 'minimize', 'moon',
  'open-panel-bottom', 'open-panel-right', 'pause', 'pen', 'pin', 'pin-filled',
  'play', 'presentation-file', 'radio-button', 'redo', 'renew',
  'settings-adjust', 'stop-outline', 'sun', 'template',
  'text-annotation-toggle', 'time', 'timer', 'trash-can', 'undo',
  'user-avatar', 'user-speaker', 'video',
].map(n => `i-carbon:${n}`)

export default defineConfig({
  safelist: [...SLIDEV_TOOLBAR_ICONS],
})
