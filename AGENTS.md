# AGENTS.md — everfold-site

Public company site and investor kit for **Everfold Labs** (the owner's umbrella brand over
the product portfolio): homepage + product catalogue, investor pitch page, HTML deck with a
PDF export, and per-product landing pages. Active. **This repo is PUBLIC**: nothing private,
keyed or personal goes in here.

## Stack & layout
Plain static HTML/CSS/JS, no build step, no package manager. Each page is self-contained
(only external dependency: Google Fonts).
- `index.html`: homepage (hero, stats band, flagship bento, numbered product catalogue, founders, About, contact)
- `pitch.html`: investor page with embedded pitch film (`assets/everfold-pitch.mp4`)
- `deck.html`: 13-slide HTML investor deck (arrow keys navigate, P prints); `assets/Everfold-Investor-Deck.pdf` is its PDF export
- `products/<name>/index.html`: product landing pages (ai-os, cartcompare, creator-studio, glowscan, landing-page-fix-pack, passfile, scribeglass)
- `sitemap.xml`, `.nojekyll`, `assets/` (media, og-image)
- `ci/site_check.py`: CI link/asset checker + stager; `scripts/check_html.py`: malformed-tag regression check

## Setup
None. Needs only `python3` (3.12+) and `node` (used by the checker for `node --check` on any JS files).

## Run / build / test / lint
- Local preview: `python3 -m http.server 8178` then open http://localhost:8178/ (unverified)
- Checks (exactly what CI runs), staging output outside the repo so no `_site/` is left behind:
  - `python3 ci/site_check.py --repo everfold-site --output /tmp/everfold-site-_site` (verified 2026-10-11)
  - `python3 scripts/check_html.py` (verified 2026-10-11)
  - `site_check.py` refuses to run if the output dir exists; delete it first on re-runs. Never commit `_site/`.

## Environment variables
None required.

## Codex cloud environment
- Setup script: `python3 --version && node --version` (nothing to install)
- Internet during agent phase: off is fine (all checks are offline)
- Secrets to add: none

## Deployment (do not break)
- GitHub Pages at https://kaustubhtripathi-code.github.io/everfold-site/ .
- `.github/workflows/ci-cd.yml` runs the checks on push/PR, uploads the staged `_site` as a Pages
  artifact, and deploys with `actions/deploy-pages` **only from `main`**. Branch/PR runs never deploy.
  (Older HANDOVER notes describe a legacy "Pages from main, root" build; either way, a push to
  `main` publishes to the live site.)
- Do not push to `main` without the owner's approval. Work on a branch and open a PR.
- Do not edit `.github/workflows/` or `ci/` unless asked. Keep `.nojekyll`.
- Repo was renamed; old Pages paths do not redirect.

## Rules for agents
- **Honesty copy is load-bearing.** Products are betas; revenue is a model, not a fact. Current
  counts: homepage/deck say 15 products built, **10 live betas**; `pitch.html` deliberately
  stays at 14 because the pitch film embedded beside it has that number baked in. Do not bump
  pitch copy without a re-rendered film. Do not add "complete", "validated", present-tense revenue
  or any fabricated raise amount.
- Founders: Kaustubh Tripathi (Founder & CMO) and Shubham (Co-founder, Head of US; surname
  unknown, ask the owner). Snehal Saraf has left: never re-add her. Product is "Therapy OS"
  (never "Sneh"/"Sneh TherapyOS"); the only allowed phrasing is "built and piloted with
  practicing-therapist input" (past tense); its chip is "Live beta", not "Live pilot".
- No white-label offering and no acquisition/exit/asset-sale framing.
- Contact email: the plain address already used in the pages, never a `+alias`.
- Snapline: "included with every FreelancerOS plan", no download link. Deliberately excluded
  from the catalogue: competitor-intel-d2c, trading tools, ReviewLift.
- GlowScan copy makes no accuracy/dermatological claim and its score is labelled "SAMPLE RESULT". Keep it that way.
- Any `deck.html` edit means the PDF must be regenerated (headless Chrome/Edge
  `--headless=new --no-pdf-header-footer --landscape --print-to-pdf=... deck.html`). Verify
  the PDF, not the browser: the print viewport (~734x975) is narrower than desktop. Keep the
  `@media screen and (max-width:760px)` guard (without `screen` the PDF renders mobile layout).
- Adding/removing a catalogue row: renumber the `<span class="n">` row numbers; adding a deck
  slide: renumber footer `NN / 13` and kicker section numbers. Update `sitemap.xml` for new pages.
- `products/{cartcompare,scribeglass,ai-os,creator-studio}` are copies of other kits' landing
  pages with an added `<video>` block after `</header>` (creator-studio also has an added
  head/meta block and attribution bar). A blind re-copy deletes these additions.
- Reveal animations use IntersectionObserver with a rect-based fallback plus a 1200ms failsafe; never remove them (content must not depend on animation).
- Semantic colours (ShelfScore traffic-light, CartCompare green-cheapest, WhatsApp bubbles) are intentionally off-brand.
- Design tokens: Fraunces / Sora / Space Mono; ink `#0B0C10`, cream `#F2EDE4`, amber `#F7A83B`, coral `#F06449`. `index.html` `:root` is the canonical token source.
- Media source (Remotion renderer) lives outside this repo on the owner's machine; only rendered mp4s are committed.

## Open work
- `claude/45-dte-strategy-summary-0xgtie` (adds `docs/45-dte-strategy-summary.md`) and
  `claude/kemet-strategy-guide-53ur2w` (adds `kemet-strategy-guide.html`): unmerged, unrelated
  to the site (personal docs). Do not merge into this public site without the owner.
- `ci/portfolio-20260907`: already merged into `main`.
- pitch.html (14) vs homepage/deck (15) product count drift: needs a pitch-film re-render.
- Creator Studio buy button is a `mailto:` until it is listed on a payment platform.
- `HANDOVER.md` holds the full dated history.
