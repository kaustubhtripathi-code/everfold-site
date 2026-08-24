# Plateline (product 16) — what was left alone, and why

Written 2026-08-25 by the site lane that added `products/plateline/`. Everything listed here
is a **deliberate non-edit**, not an oversight. Read this before bumping any count.

## What WAS changed

| File | Change |
|---|---|
| `products/plateline/index.html` | **New.** Self-contained page on the passfile/glowscan template (house tokens, Fraunces/Sora/Space Mono, ink/cream/amber). |
| `index.html` | Catalogue row 16 → `products/plateline/`. Stats band `15`→`16` "Products built end to end". og+twitter description "Fifteen"→"Sixteen AI-first products". About § "Fifteen products from one engine"→"Sixteen". |
| `sitemap.xml` | `products/plateline/` at priority 0.7, in the same alphabetical slot convention as the others. |

"10 live public deployments" is **unchanged on purpose** — Plateline is a private Android
build with no store listing and no deployment. Its chip is `beta` / "Private build".

## NOT changed: `deck.html` — still says fifteen

`deck.html` carries the count in four places (og + twitter description "15-product",
title-slide sub `15 products`, portfolio slide h2 "Fifteen products, built end to end.",
traction stat `15`). **None of them were touched.** A count bump alone is not a safe edit here:

1. The portfolio slide (`#portfolio .grid.g4`) shows one `.cell` per product. Bumping the
   heading to "Sixteen" without adding a Plateline cell makes the slide contradict itself —
   a heading that says sixteen above a grid of fifteen.
2. Adding the cell is the part that cannot be done blind. HANDOVER (2026-08-02) records that
   **the 14-cell layout already fit to the pixel** at the print viewport, and the 15th cell
   required a scoped density block (`#portfolio .cell` padding 12→10px, grid gap 10→8px) to
   stop the last row clipping under `overflow:hidden`. A 16th cell may well need another
   tightening pass, and the only way to know is to run the headless-Edge print harness —
   **at `--window-size=734,1070`, not `734,975`, or the harness lies in your favour.**
3. Any deck.html edit invalidates `assets/Everfold-Investor-Deck.pdf`, which must be
   re-exported with the msedge recipe in HANDOVER and read back with `pypdf` (13 pages, all
   16 product names present on page 4, no stale "Fifteen products" / "15-product" strings).

No slide renumber is involved — a portfolio cell is not a slide, so `NN / 13` footers stay as
they are. The blocker is the print-overflow re-verification plus the PDF re-export, not the
numbering.

**To finish it:** add the cell
`<div class="cell"><span class="c">Android · Health</span><h4>Plateline</h4><p class="d">Dinner advice from your food log and Health Connect</p><span class="chip beta">Private build</span></div>`
after the Creator Studio cell, bump the four counts, run the print harness, tighten density if
any cell overflows, re-export the PDF, verify with pypdf.

## NOT changed: `pitch.html` — still says fifteen

`pitch.html` says "Fifteen products. One engine." (h1), "15 products built end to end and 10
deployed as live betas" (velocity tile), and "15-product AI-native studio" in three meta
descriptions. Left alone for the **same standing reason** HANDOVER records twice (08-02 and
the Creator Studio entry): `assets/everfold-pitch.mp4` is embedded on that page with the
product count **baked into the render**. Bumping the copy alone puts a page that says sixteen
next to a film that says fifteen.

Either re-render the pitch film from the shared Remotion renderer and bump pitch.html to 16,
or accept pitch (15) vs homepage (16) disagreeing. That is an owner call, not a site edit.

## No promo film

Every other product page carries a `<video>` block right after `</header>`. Plateline has no
film — none was produced — so the block is **omitted rather than pointed at a missing file**.
If a film is made later, drop it beside the page as `./plateline-promo.mp4` with
`poster="../../assets/og-image.png"`, matching the passfile and creator-studio convention.

## Honesty of the status copy

The page does **not** claim the app has been run. TEST-REPORT.md is explicit that on-device
testing never happened (the phone was not attached and the emulator could not boot), so the
page says the app compiles, that 66 unit tests cover the named safety rules, and that
"it has not yet been through a full run on a real handset". Status chip:
**"Private build, not listed"**. No download link, no store badge, no user numbers, no
testimonials. If the copy is ever strengthened, the device lane has to run first.

---

## Pre-existing drift found while working — NOT mine to fix, but real

Both are honesty problems that predate this change and survive the 2026-08-01 founder removal.
Flagging rather than silently editing, because both are owner calls.

1. **`index.html` stats band** still reads `3` / "Founders — product, clinical, US". The
   founder tiles on that same page show **two** founders, and the clinical co-founder left the
   project on 2026-08-01.
2. **`deck.html`** still reads `<strong>a clinical co-founder</strong>` on the title slide
   (line ~90) and carries the traction stat `1` / "Clinical pilot, real clients" (line ~200).
   HANDOVER's positioning rule 1 says no surface may claim a *current* clinical pilot or a
   practicing therapist on the team; the only sanctioned phrasing is the past-tense
   "built and piloted with practicing-therapist input". Fixing these means re-exporting the
   PDF, so it pairs naturally with the deck work above.
