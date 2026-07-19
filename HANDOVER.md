# Everfold Labs — company site + investor kit · HANDOVER

Read this first. Built 2026-07-12 (one session: named the company, built the site, deck, PDF, pitch film).

## What this is
**Everfold Labs** is Kaustubh's company/umbrella brand over all 13 sellable products (was 12; **Personae** added 2026-07-12 — brand-owned AI creators as a service, flagship Naina Rao, links to naina-site). Name = ever + fold ("value that keeps multiplying") — 3rd rename in one day (Tripath Labs → Orrery Labs → Everfold Labs), collision-checked clean (rejected for collisions: Tripath, Handbuilt, Shipwright, Soloforge, Adyant, Tenfold, Manyfold, Northbound, Quiver).

- **LIVE:** https://kaustubhtripathi-code.github.io/everfold-site/ (public repo `kaustubhtripathi-code/everfold-site`, Pages legacy build, main branch, root). Repo was renamed twice — old Pages paths do NOT redirect.
- **Deploy = push to main.** Local preview: launch config `everfold-site` (python http.server :8178) in `~/.claude/.claude/launch.json`.

## 2026-07-19 — honesty-copy pass (committed LOCAL `8ca8974`+`d315a31`, ⚠ NOT PUSHED = not live yet)
Claims brought in line with reality (the products are betas, revenue is a model not a fact):
- deck.html:67 "13 complete products / 10 live deployments" → "13 products built end to end, 10 deployed as live betas"
- pitch.html:83 "12 complete products and 9 live deployments" → "12 products built end to end and 9 deployed as live betas"
- index.html:211 "validated live, scaled worldwide" → "deployed and validating"
- pitch.html:65 "monetized through subscriptions and B2B contracts" (present tense = false revenue claim) → "built to monetize through…". The deck's four-revenue-STREAMS framing was deliberately kept (it's a model, labeled as such).
- **KNOWN INCONSISTENCY, owner's call:** deck says 13 products/10 deployments, pitch says 12/9 — one of them is stale; reconcile before investor use. Also remember the PDF (`assets/Everfold-Investor-Deck.pdf`) is a SNAPSHOT of deck.html — regenerate after any deck edit (command in the Files table).
- Pushing main deploys these copy changes publicly — the owner hasn't asked for that yet.

## Files
| File | What |
|---|---|
| `index.html` | Homepage: hero, stats (**13 products / 10 live**), flagship bento (SiteBot, Sneh, FreelancerOS, ChatCommerce, **Personae**), 13-row product catalogue (every row links to a LIVE site), mission tiles, Founders, About, contact. Self-contained; only external dep = Google Fonts. Catalogue rows are auto-renumbered by a python one-liner (regex on `<span class="n">`) — re-run after adding a row. |
| `pitch.html` | Investor page: pitch film embed, why-now tiles, founders, the ask. |
| `deck.html` | **13-slide** HTML investor deck. ←/→ navigate, P = print (print CSS = 1 slide/page). Adding/removing a slide: re-run the renumber (footer page-nums = slide position `NN / 13`; kicker section-nums = sequential `NN · Label`) — a python regex pass, see the 2026-07-12 Personae commit. |
| `assets/Everfold-Investor-Deck.pdf` | PDF export of deck.html. Regenerate after deck edits: `msedge --headless=new --disable-gpu --no-pdf-header-footer --landscape --print-to-pdf=<out> --virtual-time-budget=15000 file:///C:/dev/everfold-site/deck.html` |
| `assets/everfold-pitch.mp4` | 68s 1080p Remotion pitch film (music + fonts baked). |
| `products/{glowscan,cartcompare,scribeglass,ai-os}/index.html` | Product landing pages for products with no site of their own. glowscan = built here (original). The other three are COPIES of their kits' landings (CartCompare `site/index.html`, scribeglass-pro `marketing/index.html`, AI Os `marketing/website/index.html`) — when a source kit changes, re-copy + push. |

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

## Design system (all surfaces incl. film + product pages)
Fraunces (display) + Sora (body) + Space Mono (labels). Ink `#0B0C10`, cream `#F2EDE4`, amber `#F7A83B`, coral `#F06449`, grad amber→coral→violet. Fold mark = 3 stacked pills. Reveal animations use IntersectionObserver **with a rect-based above-fold fallback** (hidden preview tabs never fire IO — don't remove it).

## Verification conventions
Preview screenshots time out in the embedded browser — verify via read_page / JS eval; resize to a real viewport first (hidden tab reports 0×0 and fakes overflow). After a push, curl the live URL for a content marker, and range-request mp4s (expect 206).
