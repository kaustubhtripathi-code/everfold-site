# Everfold Labs — company site + investor kit · HANDOVER

Read this first. Built 2026-07-12 (one session: named the company, built the site, deck, PDF, pitch film).

## What this is
**Everfold Labs** is Kaustubh's company/umbrella brand over all 13 sellable products (was 12; **Personae** added 2026-07-12 — brand-owned AI creators as a service, flagship Naina Rao, links to naina-site). Name = ever + fold ("value that keeps multiplying") — 3rd rename in one day (Tripath Labs → Orrery Labs → Everfold Labs), collision-checked clean (rejected for collisions: Tripath, Handbuilt, Shipwright, Soloforge, Adyant, Tenfold, Manyfold, Northbound, Quiver).

- **LIVE:** https://kaustubhtripathi-code.github.io/everfold-site/ (public repo `kaustubhtripathi-code/everfold-site`, Pages legacy build, main branch, root). Repo was renamed twice — old Pages paths do NOT redirect.
- **Deploy = push to main.** Local preview: launch config `everfold-site` (python http.server :8178) in `~/.claude/.claude/launch.json`.

## 2026-07-19 — honesty-copy pass (`8ca8974`+`d315a31`, PUSHED same day = LIVE on Pages)
Claims brought in line with reality (the products are betas, revenue is a model not a fact):
- deck.html:67 "13 complete products / 10 live deployments" → "13 products built end to end, 10 deployed as live betas"
- pitch.html:83 "12 complete products and 9 live deployments" → "12 products built end to end and 9 deployed as live betas"
- index.html:211 "validated live, scaled worldwide" → "deployed and validating"
- pitch.html:65 "monetized through subscriptions and B2B contracts" (present tense = false revenue claim) → "built to monetize through…". The deck's four-revenue-STREAMS framing was deliberately kept (it's a model, labeled as such).
- ~~KNOWN INCONSISTENCY~~ **RESOLVED same day (owner asked):** pitch.html was the stale one (written pre-Personae) — hero "Twelve"→"Thirteen", velocity tile 12/9→13/10; index.html About §also had a stale "Twelve"→"Thirteen". All three surfaces now agree: **13 built / 10 live betas** (deck, pitch, homepage stats, About). The PDF snapshot was ALSO stale (built 07-12, predating the honesty edits) — regenerated from current deck.html via the msedge command and text-verified ("13 products built end to end, 10 deployed as live betas" present; old "complete products" overclaim absent). Rule stands: any deck.html edit ⇒ regenerate the PDF.
- Pushed to main (owner-approved 2026-07-19) — the copy above is the live site now.

## Files
| File | What |
|---|---|
| `index.html` | Homepage: hero, stats (**13 products / 10 live**), flagship bento (SiteBot, Sneh, FreelancerOS, ChatCommerce, **Personae**), 13-row product catalogue (every row links to a LIVE site), mission tiles, Founders, About, contact. Self-contained; only external dep = Google Fonts. Catalogue rows are auto-renumbered by a python one-liner (regex on `<span class="n">`) — re-run after adding a row. |
| `pitch.html` | Investor page: pitch film embed, why-now tiles, founders, the ask. |
| `deck.html` | **13-slide** HTML investor deck. ←/→ navigate, P = print (print CSS = 1 slide/page). Adding/removing a slide: re-run the renumber (footer page-nums = slide position `NN / 13`; kicker section-nums = sequential `NN · Label`) — a python regex pass, see the 2026-07-12 Personae commit. |
| `assets/Everfold-Investor-Deck.pdf` | PDF export of deck.html. Regenerate after deck edits: `msedge --headless=new --disable-gpu --no-pdf-header-footer --landscape --print-to-pdf=<out> --virtual-time-budget=15000 file:///C:/dev/everfold-site/deck.html` |
| `assets/everfold-pitch.mp4` | 68s 1080p Remotion pitch film (music + fonts baked). |
| `assets/{glowscan,cartcompare,scribeglass,ai-os}-promo.mp4` | Product promo films, embedded on the four product pages below (added 2026-07-26). |
| `products/{glowscan,cartcompare,scribeglass,ai-os}/index.html` | Product landing pages for products with no site of their own. glowscan = built here (original). The other three are COPIES of their kits' landings (CartCompare `site/index.html`, scribeglass-pro `marketing/index.html`, AI Os `marketing/website/index.html`) — when a source kit changes, re-copy + push. **⚠ Each of these four now carries a `<video>` block inserted after `</header>`. A blind re-copy from the source kit DELETES that block — re-add it, or add the embed to the source kit first.** |

## Pitch film (Remotion)
Source lives in the shared renderer **`C:\Users\91851\OneDrive\Documents\Anitgravity\scribeglass-pro\marketing\video`**: `src/Everfold.jsx` + `src/everfold-entry.js` (isolated entry; ScribeGlass Root untouched). Music: `make_everfold_music.py` (numpy synth, license-free) → `public/everfold-music.mp3`.
Re-render: `npx remotion render src/everfold-entry.js EverfoldPitch "C:\dev\everfold-site\assets\everfold-pitch.mp4"` then push.
Verify a render before shipping: ffmpeg frame extract (title ~6s, wall ~26s, team ~55s, CTA ~64s) + `volumedetect` on a mid-section (audio stream existing ≠ audio content). Google Fonts load via injected `<link>` + delayRender — works headless.

## Positioning rules (user-ordered, load-bearing)
1. **Founders:** Kaustubh Tripathi — Founder & CMO (product, engineering, growth); **Snehal Saraf — Co-founder · Clinical Lead, Sneh** (practicing psychotherapist = the highlighted moat; "Co-founder", never "Founder"); **Shubham — Co-founder · Head of US** (surname unknown — ask the user before any doc needs it).
2. **NO white-label offering, NO acquisition/exit/asset-sale framing.** Offers = Use / Partner / Back the mission. Revenue slide = subscriptions, B2B contracts, productized deploys, marketplace/affiliate. Ambition line: "a generational, AI-native software house — a portfolio serving 100 million businesses and consumers, built from India for the world."
3. **Contact email = plain `kaustubh.trt@gmail.com` everywhere** — never +aliases.
4. Deck has NO fabricated raise amount ("first outside round") — the user sets numbers.
5. Snapline: listed as "included with every FreelancerOS plan", NO download link (standing rule).
6. Excluded from the catalogue on purpose: competitor-intel-d2c (stealth), trading tools (personal), ReviewLift.

## 2026-07-26 — portfolio-wide video rebrand
Every product film was moved onto one house look instead of thirteen unrelated ones.
- **`src/brand.{jsx,tsx}`** — the shared kit (tokens, Fraunces/Sora/Space Mono loader, FoldMark,
  Mesh, Fade, Kicker, Scene, **EndCard**) — is COPIED into each Remotion project, not published as
  a package: they are separate npm projects with no workspace. Fix a bug in one ⇒ re-copy to all.
  Canonical source of the tokens is still `everfold-site/index.html`'s `:root`.
- Every film now closes on the same `EndCard` (fold mark → product → tagline → URL →
  "AN EVERFOLD LABS PRODUCT"). That end card is what makes the portfolio read as one studio.
- **Semantic colour was deliberately NOT rebranded** in three places, and should stay that way:
  ShelfScore's traffic-light health score, CartCompare's green-means-cheapest, and the
  WhatsApp-authentic bubbles inside ChatCommerce's phone mockup. Pushing those to house amber
  destroys the meaning the scene is built on.
- **GlowScan** got a film built from scratch (`src-glow/` in the shared renderer). It makes no
  accuracy or dermatological claim on purpose — the fairness eval across skin tones has never
  been run — and its sample score is labelled "SAMPLE RESULT". Do not "strengthen" that copy.
- ScribeGlass's "zero bytes uploaded" line was **false** (the same scene offers Gemini/OpenAI/
  Claude enhancement, which uploads the transcript) → now "notes stay on your disk".

## Design system (all surfaces incl. film + product pages)
Fraunces (display) + Sora (body) + Space Mono (labels). Ink `#0B0C10`, cream `#F2EDE4`, amber `#F7A83B`, coral `#F06449`, grad amber→coral→violet. Fold mark = 3 stacked pills. Reveal animations use IntersectionObserver **with a rect-based above-fold fallback** (hidden preview tabs never fire IO — don't remove it).

## Verification conventions
Preview screenshots time out in the embedded browser — verify via read_page / JS eval; resize to a real viewport first (hidden tab reports 0×0 and fakes overflow). After a push, curl the live URL for a content marker, and range-request mp4s (expect 206).

## 2026-07-25 responsive pass
- Mobile nav no longer deleted at <=900px — the five links + "Get in touch" collapse into a
  `<details>` hamburger (zero JS, 51px tap targets).
- Catalogue rows on mobile: the `grid-template-areas` had no `grid-area` on any child, so
  the arrow auto-placed under the title. Rows now use explicit areas and the **category
  label is restored** instead of being `display:none`d away.
- `.rv` reveal animation got a 1200ms failsafe — 30 elements' visibility depended entirely
  on IntersectionObserver firing. Content must never depend on an animation running.
- Added a **"Everfold Suite" bundle card** at the end of the catalogue linking to
  productivity-suite-site (rebranded from "Studio Stack" the same day). It is deliberately
  a bundle card and **not** a 14th catalogue row, so the "13 products / 10 live" counts in
  the stats band, deck.html and the pitch film stay accurate.

## 2026-08-02 — Passfile added (14th product) — NOT COMMITTED, orchestrator reviews
**Passfile** = versioned per-SKU EU/UK compliance records for small consumer brands (GPSR).
Private technical-file vault per SKU → Declaration of Conformity that cites each document by
SHA-256 fingerprint → permanent public versioned record page with a QR for the packaging →
gap / expired / superseded-standard alerts, plus a free no-signup readiness checker.

**Counts moved 13 → 14 built. "10 live" is UNCHANGED on purpose** — Passfile is built but
still on a private repo and not publicly deployed, so it is not a live deployment. Its chip
everywhere is `beta` / "Design partners", and the page's status line reads
"in design-partner onboarding".

| File | Change |
|---|---|
| `index.html` | New catalogue row 14 → `products/passfile/` (same markup as rows 9–13). Stats band `13`→`14` "Products built end to end". og+twitter description "Thirteen"→"Fourteen AI-first products". About §"Thirteen products from one engine"→"Fourteen". |
| `products/passfile/index.html` | **New.** Self-contained product page on the glowscan template (Fraunces/Sora/Space Mono, ink/cream/amber, `<video>` right after `</header>`). Sections: hero + the delisting problem, vault→DoC→public record/QR→versions, alerts, free readiness checker, honest status line, CTA. |
| `products/passfile/passfile-promo.mp4` | Produced by the concurrent video agent. **Note: this film sits next to its page, not in `assets/` like the other four** — the `<video src>` is `./passfile-promo.mp4` with `poster="../../assets/og-image.png"`. |
| `deck.html` | Passfile cell added to the portfolio grid (no new slide, no renumber — still 13 slides). Slide h2 "Thirteen"→"Fourteen products", title-slide sub `13`→`14 products`, traction stat `13`→`14`, og/twitter "13-product"→"14-product". Plus the print fix below. |
| `assets/Everfold-Investor-Deck.pdf` | Re-exported per the recipe. 13 pages, 602,944 bytes. |
| `sitemap.xml` | `products/passfile/` added at priority 0.7, matching the other four product pages. |

**Not touched — needs a decision:** `pitch.html` still says "Thirteen products" / "13 products
built end to end" (h1, velocity tile, three meta descriptions). It was left at 13 because the
pitch film embedded on that page has "thirteen" baked into the render, and bumping the copy
alone would contradict the film playing beside it. Either re-render `everfold-pitch.mp4` and
bump pitch.html to 14, or accept the surfaces disagreeing.

## 2026-08-02 — Creator Studio added (15th product)
**Creator Studio — for LinkedIn creators.** A writing cockpit sold as ONE self-contained HTML file
that runs locally from disk: composer with a "…see more" fold preview (desktop + mobile),
deterministic post score with tips, idea matrix from your content pillars, hook formulas,
100-template vault, weekly planner that can import best posting days from the sibling product
**LinkedIn Analytics Studio**, and optional AI drafting with the buyer's own Anthropic/OpenAI/Google
key called straight from the browser. No server, no account, no subscription. One-time purchase.

**Counts moved 14 → 15 built. "10 live" is UNCHANGED on purpose** — Creator Studio is a local-file
product, not a deployment. Its chip everywhere is `beta` / "Launching soon", category "Local file".

| File | Change |
|---|---|
| `products/creator-studio/index.html` | **New.** Adapted from the kit's landing at `C:\Users\91851\projects\linkedin-creator-studio\landing\index.html` — same "copy the kit's landing" convention as cartcompare/scribeglass/ai-os, so it keeps its own green design system rather than the house tokens. Added: canonical + og/twitter head block, the `<video>` right after `</header>`, the Everfold contact/attribution bar after `</footer>`. **A blind re-copy from the kit deletes all four — re-add them.** |
| `products/creator-studio/creator-studio-promo.mp4` | Promo film, 6.15MB. Like Passfile's, it sits **next to its page, not in `assets/`** — `<video src="./creator-studio-promo.mp4">` with `poster="../../assets/og-image.png"`. Bench source: **`src-creatorstudio`** in the shared Remotion renderer. |
| `index.html` | New catalogue row 15 → `products/creator-studio/`. Stats band `14`→`15` "Products built end to end". og+twitter description "Fourteen"→"Fifteen AI-first products". About §"Fourteen products from one engine"→"Fifteen". |
| `deck.html` | Creator Studio cell added to the portfolio grid (no new slide, no renumber — still 13 slides). Slide h2 "Fourteen"→"Fifteen products", title-slide sub `14`→`15 products`, traction stat `14`→`15`, og/twitter "14-product"→"15-product". Plus the density tightening below. |
| `assets/Everfold-Investor-Deck.pdf` | Re-exported per the recipe. 13 pages, 606,828 bytes. |
| `sitemap.xml` | `products/creator-studio/` added at priority 0.7, matching the other product pages. |

**Buy button is a `mailto:` until launch.** The kit's landing shipped `href="GUMROAD_URL_HERE"`. The
product is not listed on a payment platform yet, so the button is
`mailto:kaustubh.trt@gmail.com?subject=Creator%20Studio%20early%20access` labelled
"Get early access — launching soon", with an HTML comment above it saying to swap in the Gumroad /
Lemon Squeezy URL and restore the "Buy now — $49 one-time" label at listing time. Two adjacent lines
that assumed a live checkout were softened to match (the sub-button line, and the cross-sell
"same store page" line). Prices ($49 launch / $79 / $59 bundle) are unchanged from the kit.

**`.btn-block` now sets `white-space:normal`.** `.btn` is `white-space:nowrap`; the longer
early-access label made the full-width buy button's min-content width push the price card 35px past
a 360px viewport. One declaration on the only `.btn-block` on the page fixes it at the root.

**pitch.html deliberately left at 14.** `5cf7792` had just bumped it to "Fourteen" *and re-rendered
`assets/everfold-pitch.mp4`* to match. Bumping the copy to 15 alone would contradict the film playing
beside it again. Either re-render the pitch film and bump pitch.html to 15, or accept
pitch (14) vs homepage/deck (15) disagreeing. **The old "Thirteen" drift is gone — this is a new,
smaller one.**

### PDF export: the portfolio slide had ZERO print headroom at 14 cells
Adding the 15th cell pushed the last grid row 10px past the slide's content box at the print
viewport (~734×975), which `overflow:hidden` would have clipped — the exact class of bug fixed on
07-02, resurfacing because the 14-cell layout fit to the pixel. Tightened the scoped density block:
`#portfolio .cell` padding `12px`→`10px` vertical, `#portfolio .grid` gap `10px`→`8px`.
- Measured with a headless-Edge harness that reproduces the print layout: temporarily neutralise
  `@media screen and (max-width:760px)` (print is *under* that breakpoint but the `screen and`
  guard excludes it), force `.slide{display:flex}`, then compare every `.cell`'s bottom against
  `#portfolio`'s content box. **`--window-size=734,975` yields a 880px-tall viewport in headless —
  use `734,1070` to get a true 975px `clientHeight`, or the harness lies in your favour.**
- After the fix: 0 cells overflowing at both 734 and 760 wide; PDF re-exported and read back with
  `pypdf` — 13 pages, all 15 product names present on page 4, "Fifteen products" heading, no stale
  `14 products` / `Fourteen products` / `14-product` anywhere.

### PDF export was silently rendering in the MOBILE layout (pre-existing bug, now fixed)
Chrome's print viewport for this deck is roughly **734 × 975 CSS px**, i.e. *under* the
`max-width:760px` breakpoint. So `@media(max-width:760px)` was applying to every PDF export:
2-column grids and `.slide{overflow-y:auto}`, which drops overflowing content from the PDF
entirely. The committed PDF was therefore missing **ScribeGlass Pro, Snapline and AI OS** from
the portfolio slide — it printed 10 of 13 products under a heading that said "Thirteen".
- Fix: `@media(max-width:760px)` → **`@media screen and (max-width:760px)`**. One word; print
  now uses the desktop layout, screen behaviour is byte-identical.
- Follow-on: at 734×975 the 4-column grid of 14 cells still overflowed the slide, so the
  portfolio slide carries a small scoped density block (`#portfolio` — tighter cell padding,
  `.d` line-height, chip margin, and a wider `h2` max-width so the heading stays on one line).
- **Verifying a deck change means checking the PDF, not the browser** — the print viewport is
  narrower than any desktop screen, and text can be present in the PDF's content stream while
  still being visually clipped. Render the PDF, then also screenshot the slide at 734×975.

### Local verification run (2026-08-02)
Measured in a headless Edge iframe harness at a true layout width (`--allow-file-access-from-files`):
- `index.html` @375 and @1280 — `documentElement.scrollWidth == 375 / 1280`, no element
  crosses the viewport edge, 14 catalogue rows, Passfile row resolves to `products/passfile/`,
  first stat reads `14`, hamburger `<details>` visible at 375 and hidden at 1280 (zero-JS
  mobile nav intact; the new row shows title + description + "SAAS · COMPLIANCE" + chip in the
  `grid-template-areas` layout).
- `products/passfile/index.html` @375 and @1280 — scrollWidth equals viewport, **0 overflowing
  elements**, video resolves to `./passfile-promo.mp4` (0:51, poster shows), 2 mailto links,
  no `+alias` present, disclaimer panel and footer render.
- `deck.html` — PDF re-exported and checked slide by slide: 13 pages, and every slide's visible
  text matches the HTML character-for-character (only difference is `text-transform:uppercase`).
  All 14 products present on the portfolio slide; verified visually at both 734×975 (print) and
  1280×800 (screen) with nothing clipped.
