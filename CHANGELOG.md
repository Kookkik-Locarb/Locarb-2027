# Changelog

## 2026-10-28 (navbar v3)
- Navbar redesigned as a floating glass pill: inset from the edges, blurred Off-white glass, soft shadow; menu centred with pill hover and a green dot under the current section; compact icon buttons; mega menus open 14 px below with rounder cards
- Shrinks slightly and firms up its background as you scroll (where supported); scroll progress line removed
- Same pill on tablet/mobile with logo, search, Aa, language and menu
- `site/` rebuilt

## 2026-10-28 (blog · solution filter)
- Blog: the Solution filter is now a dropdown beside the category tabs ("Solution: All solutions ⌄") with a check on the active option; highlighted in green when a filter is set; scales to any number of solutions (Design System rule: > 6 options → dropdown)
- `site/` rebuilt

## 2026-10-28 (blog v2)
- Blog redesigned (hub + 3 category pages share one layout): sand hero, sticky filter bar with a segmented category control whose black indicator slides between tabs, solution chips, post count, large featured post, 3-column grid with staggered card entrance on every tab/filter change, Load more
- Category tabs switch in place (no page reload) and update the URL; category pages open on their own tab
- Media coverage (The Nation Thailand, PPTV HD 36) added to News & events, opening in a new tab
- `site/` rebuilt

## 2026-10-28 (intro)
- Logo intro plays only on the first page of a visit (new tab/browser session) or, as a still logo, when a page loads slowly. Clicking the logo no longer replays it
- `site/` rebuilt

## 2026-10-28 (motion v2)
- Tabs: a real sliding indicator — the black pill glides from the previous tab to the new one after every tab change (Blog categories, About sub-nav). Works in every browser, not only those with View Transitions
- Page entrance: hero and first section rise in on every page load
- `site/` rebuilt (runtime keeps the indicator through re-renders)

## 2026-10-28 (motion)
- Page-to-page: soft crossfade; the active tab pill (Blog categories, About sub-nav) slides to its new place (View Transitions; other browsers navigate as before)
- Language switch crossfades; tabs/chips/buttons ease colour and give press feedback; the selected pill pops in
- Blog solution filter: cards re-enter with a short staggered rise on every change
- FAQ answers, contact solution options, route tags, search results and the success message animate in
- All motion respects "reduce motion"
- `site/` rebuilt

## 2026-10-28 (footer · CI)
- Footer follows the CI: Off-white background with the full-colour logo (CI p.14). The self-made "logo on black" variant is no longer used anywhere
- Footer text, links, icons and controls recoloured for the light background (AA contrast)
- `site/` rebuilt

## 2026-10-28 (home · news)
- Home › Insights & client stories: real LO-CARB event photo; featured card links to The Nation Thailand coverage, compact card links to PPTV HD 36 (open in a new tab). Headlines and dates to be replaced with the articles' own
- `site/` rebuilt

## 2026-10-27 (our story hero height)
- Our story hero shortened (about 570 px on a laptop instead of full screen); title, spacing and seal scaled to match
- `site/` rebuilt

## 2026-10-27 (our story hero)
- Our story hero: full-bleed photo background with slow motion, dark left shade, large "Our story" title, intro, glass sub-navigation, Est. 2021 seal, and a curved bottom edge into the green Mission band (same feel as Home)
- `site/` rebuilt

## 2026-10-27 (our story layout)
- Our story: new layout for every section, content unchanged — hero with large title, intro + sub-nav and a wide photo band; centred green Mission; sticky heading with vertical Milestones timeline; black We believe with oversized statement; DNA as editorial columns with large numerals; Key numbers as a bento grid
- `site/` rebuilt

## 2026-10-27 (our story)
- Our story checked line by line against the BD document (Mission, Milestones, We believe, 3 DNAs, Key numbers) in EN and TH
- Key numbers now show the exact BD sentences with the figure inline, e.g. "ลูกค้า [x] รายใน 5 กลุ่มอุตสาหกรรม"
- `site/` rebuilt

## 2026-10-26 (home · clients)
- Home › Our clients: "14 organisations | 5 sectors" shown as one compact fact pill beside the heading, with "See client stories" below it
- `site/` rebuilt

## 2026-10-26 (mobile menu · Home)
- Mobile menu: "Home / หน้าแรก" added as the first item (desktop menu unchanged; the logo and breadcrumbs already lead Home)
- `site/` rebuilt

## 2026-10-26 (blog covers)
- Insights & client stories: 12 mock news covers (one per post) in the CI style, using the supplied fonts and brand photos; used on the Blog hub and category pages, the featured post, story and article heroes, and related posts on solution pages
- `site/` rebuilt

## 2026-10-26 (mobile menu)
- Mobile/tablet: the menu icon opens a full-height drawer with About Us, Our Solutions and Blog links, language and text-size switches, and a Contact Us button; closes with ✕, the backdrop or Esc
- `site/` rebuilt

## 2026-10-26 (logo)
- Clicking the LO-CARB logo always plays the logo intro: from any page it opens Home with the full animation; on Home it scrolls to the top and replays it
- `site/` rebuilt

## 2026-10-26 (contact)
- Contact: choose more than one solution (checkbox chips, "Select all that apply")
- Contact side panel redesigned: green "Your message goes to" card with topic and selected solutions; one contact card (email, careers, phone, office, social) without repeats
- `site/` rebuilt

## 2026-10-26 (deploy)
- New `site/` folder: static build of all 16 pages for Vercel (fixes the page stuck on the logo animation)
- Root `vercel.json` serves `site/`
- Fix: after switching language during/after the intro, the hero no longer waits another 6 s before appearing

## 2026-10-26
- About Us redesigned (Story, Certificates, Board) with a shared About sub-navigation and a CTA band (Read our blog · Contact Us) on each page
- Story: hero with seedling cut-out and Est. 2021 seal; Mission (black band); Milestones timeline; We believe; 3 DNAs; Key numbers (5, placeholders) — all from the BD document, EN/TH
- Certificates: IFRS Sustainability Alliance & ISSB Training Partner featured first; ISO, ISSB Training Partner, CFO, BSI (CBAM) cards with issuer, year and PDF link (placeholders where unknown)
- Board: one row of four cards (photo, name, title, one-line bio, LinkedIn) with PDPA note; fictional names replaced by placeholders
- Home unchanged
- Solution pages: banner uses the BD text "Thailand’s 1st IFRS Sustainability Alliance & ISSB Training Partner" (IFRS and ISSB pages); Reporting scope = GRI/CDP reports, ESG strategy, Net Zero pathway; CarbonCal benefits = template (Scope 1–3 on one platform, CFO ready for TGO registration, Carbon Camp)
- Removed unverified claims: CarbonCal free-trial length, security and support details now marked "to confirm"; article author replaced with a placeholder

## 2026-10-23
- Copy pass with the blader/humanizer guidelines: plain headings instead of slogans (Home About and Clients titles; CarbonCal benefits; Reporting and portfolio headings), EN and TH

## 2026-10-22
- IFRS Alliance section: all text in one colour (off-white) on green; accents by typeface only
- Hero: real wind-turbine and solar video background (silent, seamless 16 s loop, 2.3 MB) with poster frame, cursor spotlight and parallax; readable copy on a left shade
- Hero H1 restructured for SEO (brand line + "Sustainability consultancy in Thailand for IFRS S1 & S2, carbon accounting and ESG reporting"); page title and meta description added
- Section rhythm: What we do (light) · About (sand) · Clients (light) · IFRS (green)
- Our solutions: one compact row on desktop, stacked list on mobile; fits one screen
- Footer redesigned (contact-first) and scaled down
- Mobile check of all 16 pages at 390 px: no horizontal overflow

## 2026-10-21
- Official LO-CARB logo (from the brand animation) in nav and footer
- Accessible green (#0A7D3F) for small text, buttons and green panels (WCAG AA); CI green kept for graphics
- Our Solutions: expanding panels, short titles, "+" hint on collapsed panels
- Carbon Scout page rewritten to the Content Template (farmland carbon for carbon credits)
- Solution page intros use the Content Template one-liners (EN/TH)
- Hero: calm editorial headline, cursor spotlight, curved bottom edge
- Intro animation plays once per visit; short logo only when a page loads slowly
- Text size and language as standard dropdowns ("Aa", globe)
- Our story: Mission, Milestones, We believe, 3 DNAs, Key numbers (EN/TH)
- Home blog: branded cover mockups, categories in the header, no Topics row
- Clients marquee (14 organisations, 5 sectors) and template certificates; IFRS Alliance section with BD copy
- Fonts limited to the supplied files (Termina, STIX Two Text, Anakotmai)
