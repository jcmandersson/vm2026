# CLAUDE.md

Guidance for AI agents working in this repository. Read this before editing.

## What this is

"Loftahammarstipset" – a single-page web app for a 16-person World Cup 2026 betting/tips
game (in Swedish). The served page is one self-contained HTML file with inline CSS/JS.

## ⚠️ The single most important rule

**Every change to HTML/CSS/JS must be made in BOTH files, identically:**

1. `index.html` – the live, served file (what users see now; GitHub Pages serves it at the root).
2. `build_full.py` – contains the entire page as a template string `TPL`; it regenerates
   `index.html` from scratch.

Why: `build_full.py` is the source of truth for a full rebuild. If you only edit the HTML,
a future `python build_full.py` overwrites your change. If you only edit `build_full.py`,
the live file doesn't reflect it until someone rebuilds. So mirror every edit in both.

`build_site.py` is different – it only patches the results block, not design (see below), so
it does **not** need design/structure edits.

Practical approach (used throughout this project): make the same targeted `Edit` (same
exact old/new string) in both files. The HTML and the `TPL` string in `build_full.py` are
byte-identical for all non-templated parts.

## Data flow

- `dataset.json` → participants, their picks (`_g` per fixture nr), fixtures (`{nr,grp,home,away,date}`),
  groups, knockout structure. Injected into `build_full.py`'s `TPL` via `__DATA__`/`__ISO__`.
- `results.json` → facit: `group` (nr → `[home,away]`), `snapshot` (name → rank, for trend
  arrows), `updated`, knockout fields (mostly empty until later). Injected via `__RESULTS__`/`__UPD__`.
- `build_full.py` writes the whole `index.html`.
- `build_site.py` re-injects only `results.json` into the existing HTML using markers:
  - `/*RESULTS_START*/const RESULTS=…;/*RESULTS_END*/`
  - `const totalUpdated="Senast uppdaterad …";`
  **Do not break or rename these markers/placeholders** (`__DATA__`, `__ISO__`,
  `__RESULTS__`, `__UPD__`) or `build_site.py` / `build_full.py` will fail.

## Live results (client-side, runs on every page load)

- `fetchLiveResults()` → fetches `https://n8n.charma.io/webhook/vm2026-resultat.json`
  (timeout ~2.8s), falls back silently on CORS/network failure.
- `mapFeed(j)` → maps feed matches to internal model: `FINISHED` group matches →
  `{group:{nr:[h,a]}}`, `IN_PLAY`/`PAUSED` → `live:{nr:true}`. Returns `{group, updated, live}`.
- `applyResults(res)` → merges into `RESULTS.group`, sets `LIVE`, rebuilds `PLIST`, updates
  `MATCHES[*].score`, `cur`, "Senast uppdaterad", and re-renders.
- Team-name alias map (feed → app), needed because names differ:
  `Bosnia-Herzegovina→Bosnien`, `Cape Verde Islands→Kap Verde`, `Curaçao→Curacao`,
  `Congo DR→DR Kongo`, `Ecuador→Equador`. Keep this in sync if names change.
- `isLive(m)` → live if feed says IN_PLAY/PAUSED, or as a time-based fallback (kickoff
  passed and < ~2.5h ago and no score). Drives the red "PÅGÅR" treatment.

## Key functions / where things live (in the `<script>`)

- `scoreOf(p)` / `buildPlist()` – scoring: group sign = 1p, exact = +3p (exact total 4);
  knockout 2/3/5/7/8 per round, champion 10. `signs` includes exact; "rätt utfall (ej exakt)" = signs − exact.
- `renderMatchList()` – Matcher tab: segment `mSeg` (`upcoming`/`played`), day groups,
  per-row meta/badges (NÄSTA/I DAG/IMORGON/PÅGÅR/exakt-badge) and big "Din gissning" box.
- `renderHero()` – Matcher "Nästa match" hero (only when `mSeg==="upcoming"`).
- `renderFeatured()` + `setupCountdown()` – Hem featured carousel (prev/next). Countdown +
  "Din gissning" pill only for the *next* match; date written via `fmtMatchDate()`.
- `renderPodium()`, `renderRank()`, `renderBracket()`, `renderTables()`, `renderH2H()`,
  `openPerson()` (modal), `openMatch()` (modal), `fillMe()` (name picker + profile icon).
- Countdown markup uses classes `.mxh-cd .cdtop .cdrow .cdu .cdn .cdt .cdsep` (digits in Outfit 900).

## Conventions / gotchas

- The middle dot `·` is stored as the literal escape `·` in several JS template strings.
  When using `Edit`, match what's actually in the file (grep first if unsure).
- Fonts: body = `'Plus Jakarta Sans'`, logo = `'Chicle'`, countdown = `'Outfit'` (loaded via one
  Google Fonts `<link>`). Theme persists in `localStorage` (`loftahammar_theme`), defaults to light;
  intro plays on every page load (respecting `prefers-reduced-motion`), never on tab switch.
- Colors are CSS variables (`--blue`, `--gold`, `--ink`, `--muted`, `--down`, …) with
  `[data-theme=light]`/`[data-theme=dark]` overrides. Reuse them; don't hardcode hex unless matching existing patterns.
- Appended CSS lives just before `</style></head>`; later rules intentionally override earlier ones.
- Mobile: `@media(max-width:560px)` – bottom tab bar is fixed and uses the *opposite* theme for contrast.

## Testing (no real browser available in this environment)

- Validate JS snippets with `node --check` and small logic simulations (`node -e`/temp file).
- Use `Grep` to locate exact strings before editing; HTML lines ≈ `build_full.py` lines minus a fixed offset.
- After edits, sanity-check that markers/placeholders are intact and that both files match.

## Deployment

GitHub Pages serves `index.html` directly (it *is* the self-contained app — no redirect file). Repo:
`git@github.com:jcmandersson/vm2026.git`, URL `https://jcmandersson.github.io/vm2026/`.
Live data needs `Access-Control-Allow-Origin` on the n8n webhook for that origin.
