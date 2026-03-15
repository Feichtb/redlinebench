# Triage — gpt-5-4-pro_run01
**Triaged:** 2026-03-14
**Total findings in model output:** 60
(A: 7 | B: 5 | C: 13 | D: 7 | E: 9 | F: 7 | G: 12)

---

## Findings-to-Answer-Key Mapping

| Model ID | Model Finding (brief) | Answer Key Match | Notes |
|---|---|---|---|
| A-1 | Door tag 11-1 shown on Level 1 plan at Bathroom 11 but no entry in door schedule | **A1** | Direct match (11-1 was renumbered to 10-1; plan still shows old tag) |
| A-2 | Door 10-1 listed in door schedule but no door with tag 10-1 appears on floor plans | **A1** | Direct match — both A-1 and A-2 describe the two sides of A1 |
| A-3 | Powder Room 14 scheduled F-4 (carpet); plan tags it F-2; F-4 is carpet assembly | **A4** | Direct match |
| A-4 | Interior Elevation 5 on A7.02 labeled "Guest Bathroom 19" but Room 19 is Guest Closet; Guest Bathroom is Room 18 | *UNMATCHED* | See below |
| A-5 | Reading Nook (10) walls scheduled WD-1; section/detail shows WD-4 T&G finish | **A10** | Direct match |
| A-6 | L7 strip lighting scheduled with count of "2"; shown at kitchen, stair handrail, and reading nook in multiple drawings | *UNMATCHED* | See below |
| A-7 | Deck drawings show 36"/48"/26" railing heights; plan and elevations are inconsistent | **E2** | 26" condition directly matches E2; inconsistency across conditions is secondary |
| B-1 | North Elevation sets crawl space datum at 501'-0"; plans/sections/other elevations show 502'-0" | **B2** | Direct match |
| B-2 | Stair riser information (10 EQ + 8 EQ at 6-11/16") does not cleanly reconcile to 10'-0" floor-to-floor height | **KNOWN INCORRECT (I8)** | 18 × 6-11/16" ≈ 10'-0⅜" — within tolerance; misread consistent with I8 |
| B-3 | Garage slab shown at -1'-0" spot elevation on Level 1 plan; garage section does not carry a separate garage floor datum to confirm | *UNMATCHED* | See below |
| B-4 | Connector/entry roof slope labeled 1/4" per foot on roof plan (A2.03) but 1/8" per foot on exterior elevations | *UNMATCHED* | See below |
| B-5 | Lowered crawlspace/pool mechanical slab at -7'-0" on crawlspace plan not shown in building or pool sections | *UNMATCHED* | See below |
| C-1 | Specs call for Andersen 400 Series windows; window schedule is based on Marvin Ultrex | **C1** | Direct match |
| C-2 | Specs include exterior door 03-01 in Jeld-Wen wood/glass package; door schedule lists 03-1 as metal door | **A6** | Direct match |
| C-3 | Specs state all conditioned exterior walls are 2×6 framing; wall type E-2 is drawn as 2×8 | **C7** | Direct match |
| C-4 | Specs describe wall insulation as R-21 batts with 1" insulated ZIP board; wall assemblies show 1½" rigid insulation over ½" plywood | **C2** | Direct match |
| C-5 | Ceiling insulation: specs state R-49; code summary states R-53 | **C5** | Direct match |
| C-6 | Specs require epoxy-coated garage floor; garage floor assembly and finish schedule show only concrete slab | **N3** (neutral) | Neutral: epoxy in spec but not drawing schedule is standard |
| C-7 | Pool enclosure: specs describe 48" fence on three sides; drawings show 48"/36"/26" railing conditions | **E2** + **E5** | E2 = 26" below minimum; E5 = pool barrier cable spacing |
| C-8 | Specs require Cat6a ethernet cabling; RCP notes are labeled "Cat6e" | *UNMATCHED* | See below |
| C-9 | Specs describe roofs as 3"/12" slopes; roof plan includes areas labeled 2"/12" and 1/4"/12" | **C6** | Direct match |
| C-10 | Specs place pool mechanical equipment "opposite the house toward the west end"; drawings locate it adjacent to house/deck | *UNMATCHED* | See below |
| C-11 | Sheet G0.01 directs contractor to door data in "Specifications Div. 8"; spec booklet has no Division 8 | *UNMATCHED* | See below |
| C-12 | Hose bib quantity: code summary 5, specs call for 3, elevations show different count | **C4** | Direct match |
| C-13 | Specs distinguish master shower door as frameless and guest shower door as semi-framed; door schedule lists both generically | *UNMATCHED* | See below |
| D-1 | Low-slope roof areas covered by same standing-seam assembly; no separate low-slope assembly provided | **G8** | G8 = below-minimum slope; N8 = A4.13 addresses this — scorer to determine credit |
| D-2 | Roof intersection/valley detail concentrates water in internal gutter with no secondary waterproofing | *UNMATCHED* | See below |
| D-3 | Base details lack consistent clearance between cladding/wood and adjacent grade or paving | *UNMATCHED* | See below |
| D-4 | Sealed crawlspace not shown as continuous air/thermal/vapor barrier at stem-wall-to-floor transition | **D6** | Direct match |
| D-5 | Entry hall glazing over stone/concrete — no subsill pan or drainage path at base of assemblies | *UNMATCHED* | See below |
| D-6 | Corner window jamb details (A4.13) omit head and sill waterproofing details | *UNMATCHED* | See below |
| D-7 | Deck-to-foundation details show flashing at wall but no drainage/ventilation for deck edge condition | *UNMATCHED* | See below |
| E-1 | Code summary mixes IRC and IBC concepts; states unlimited area per story for V-B/R-3 | *UNMATCHED* | See below |
| E-2 | Garage wall not identified as code-compliant fire separation assembly | **E4** | Direct match |
| E-3 | F-1 floor/ceiling over garage shows ½" gypsum; not identified as fire separation assembly | **E7** | Direct match |
| E-4 | Garage-to-interior door (16-1) scheduled as ordinary solid-core door; no fire rating or self-closing | **E8** | Direct match |
| E-5 | Pool barrier documentation incomplete; no self-closing/self-latching gate requirements shown | **E5** | Direct match |
| E-6 | East deck elevation calls out 26" cable railing | **E2** | Direct match |
| E-7 | Safety glazing not identified at doors, baths, low glazing, or stair-adjacent glazing | **N9** (neutral) | Neutral: out of scope for this benchmark |
| E-8 | Sleeping room windows not confirmed as emergency escape openings; schedule lacks clear-opening data | **E3** | Direct match |
| E-9 | Stair drawings show railings/guards but don't provide handrail criteria, profiles, or extension info | *UNMATCHED* | See below |
| F-1 | Pool/deck/retaining wall/mechanical interfaces repeatedly deferred to pool coordination | **N14** (neutral) | Neutral |
| F-2 | Removable deck panel for pool-cover access shown only in plan; no framing, support, hardware, or removal detail | *UNMATCHED* | See below |
| F-3 | Concealed steel porch/entry overhang — architectural details don't show steel integration within wall assembly | **N13** (neutral) | N13: design team accepted this approach |
| F-4 | Wet-laid and dry-laid SS-3 called out; no buildup, edge restraint, or drainage details | **C8** | Direct match |
| F-5 | Rain chains and collection pots — no overflow control, pot construction, or pipe connection details | *UNMATCHED* | See below |
| F-6 | Exposed pool walls finished but no drawing identifies the finish or termination conditions | *UNMATCHED* | See below |
| F-7 | Master bath hydronic floor heat deferred to bidder; no manifold location or criteria | **F3** | Direct match |
| G-1 | Title sheet leaves key project-identification fields blank | *UNMATCHED* | See below |
| G-2 | Code summary leaves planning application number blank | *UNMATCHED* | See below |
| G-3 | Spec booklet has placeholder text and incomplete drawing-set reference | *UNMATCHED* | See below |
| G-4 | Door schedule leaves hardware blank for most doors; specs don't supply hardware sets | *UNMATCHED* | See below |
| G-5 | Lighting fixture schedule all TBD | **G6** | Direct match |
| G-6 | Major scope selections unresolved: HVAC, HERO certification, stains/colors, carpet, hardware, countertop, pool | **G6** + **N4/N17** (neutral) | G6 for TBDs; HVAC unresolved is neutral |
| G-7 | Bathroom finish schedule "FOR SHOWER FINISHES SEE" with no destination | *UNMATCHED* | See below |
| G-8 | Finish key "T-1" in room finish schedule not defined in any legend or spec | **G11** | Direct match |
| G-9 | "Site verify Level One height" and "driveway location verify in field" defer primary design decisions | **G9** | Direct match |
| G-10 | Spec references A8.10 for reading nook bunk detail; no A8.10 exists in set | **G12** | Direct match |
| G-11 | Pool technical specs explicitly deferred for later determination | **N14** (neutral) | Neutral |
| G-12 | Notation inconsistency: W1/E1 in notes vs. W-1/E-1 in formal assembly designations | *UNMATCHED* | See below |

---

## UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Suggested Classification | Reasoning |
|---|---|---|---|
| 1 | Interior Elevation 5 on A7.02 is labeled "Guest Bathroom 19 - South" but Room 19 is the Guest Closet; the Guest Bathroom is Room 18 | **POTENTIAL NEW ISSUE** | Specific, verifiable mislabeled interior elevation that makes shower finishes and tile layout references point to the wrong room. Also found by Opus (A-3) and Gemini (A-4 equivalent). Strong candidate for new answer key entry. |
| 2 | L7 (strip lighting) is scheduled with a count of "2" even though it is shown at the kitchen, stair handrail, and reading nook across multiple drawings — irreconcilable with the spec's 75 LF quantity | **POTENTIAL NEW ISSUE** | Specific verifiable conflict between a stated schedule quantity and the spec/plan. Not a TBD — a stated quantity that conflicts. Also found by Opus (A-12) and Sonnet (A-5). |
| 3 | Garage slab shown at -1'-0" spot elevation on Level 1 plan (A2.01B) but the garage section does not carry a separate garage floor datum to confirm this vertical relationship | **LIKELY NEUTRAL** | Documentation gap, not a confirmed error. The garage slab elevation difference may be correct but unverified in section. No confirmed dimensional conflict. |
| 4 | Connector/entry roof slope is labeled 1/4" per foot on roof plan (A2.03) but 1/8" per foot on exterior elevations — actual pitch is undefined | **POTENTIAL NEW ISSUE** | Specific, verifiable slope label conflict between roof plan and exterior elevation for the same roof area. Affects drainage design and product warranty. Also found by Gemini (B-4). Scorer should compare A2.03 to the elevation sheets. |
| 5 | Lowered crawlspace/pool mechanical slab at -7'-0" on crawlspace plan (A2.00) is not shown in building or pool sections | **LIKELY NEUTRAL** | Documentation gap without confirmed error. Sections may not cut through that area. Low direct construction impact. Also found by Gemini. |
| 6 | Specs require Cat6a ethernet cabling; RCP notes label the cabling as "Cat6e" — different cable standard | **POTENTIAL NEW ISSUE** | Specific, verifiable product conflict between spec requirement and drawing callout. Cat6a and Cat6e are different cabling standards (Cat6a supports 10GbE to 100m; Cat6e is not a TIA-recognized standard). Scorer should confirm RCP note text against spec. Also found by Gemini. |
| 7 | Specs state pool mechanical equipment is "on the side of the pool opposite the house toward the west end," but drawings locate the pool mechanical area adjacent to the house/deck | **POTENTIAL NEW ISSUE** | Specific, verifiable location conflict between spec narrative and drawing layout. Affects utilities routing, noise, and access. Scorer should compare A5.01/A5.10 to spec. Also found by Gemini. |
| 8 | Sheet G0.01 directs the contractor to door data in "Specifications Div. 8"; the provided spec booklet is a narrative allowance document with no Division 8 section or door data anywhere | **POTENTIAL NEW ISSUE** | Specific orphaned cross-reference directing contractor to a non-existent specification section for door scope. Similar in character to G12 (spec references A8.10 that doesn't exist). Verifiable from G0.01 and the spec. Also found by Gemini. |
| 9 | Door schedule lists both shower doors as generic clear glass; specs specify master shower door as frameless and guest shower door as semi-framed — framing type affects hardware and installation | **POTENTIAL NEW ISSUE** | Specific spec-vs-schedule conflict on shower door framing type. Verifiable from spec and A8.01. Also found by Opus (A-4) and Gemini (C-13). |
| 10 | Roof intersection/valley detail concentrates water in an internal gutter/valley without secondary waterproofing beneath the metal roof | **LIKELY NEUTRAL** | Judgment call about valley protection adequacy. Standing seam valley/gutter details vary widely by product. No specific confirmed error — adequacy depends on detail dimensions not evaluated at triage. Also found by Gemini. |
| 11 | Multiple base details don't establish consistent clearance between cladding/wood components and adjacent grade, paving, or decking | **LIKELY NEUTRAL** | General moisture protection observation. No specific confirmed below-minimum clearance identified. Multiple locations bundled together. Also found by Gemini. |
| 12 | Entry hall glazing details over stone/concrete floor do not show a subsill pan or explicit drainage path at the base of custom window and door assemblies | **LIKELY NEUTRAL** | Specific waterproofing detail concern. Design team may have addressed this through shop drawings or product-specific details. Difficult to confirm as an error without knowing the full detail intent. Also found by Gemini. |
| 13 | Corner window jamb details (A4.13/1–4) are jamb sections only; head and sill waterproofing details are omitted for these high-risk exterior corner conditions | **POTENTIAL NEW ISSUE** | Corner window head and sill are high-risk moisture entry points. Absence of these details for custom corner conditions is a specific, verifiable documentation gap. Scorer should confirm A4.13 contains only jamb sections. Also found by Gemini. |
| 14 | Deck-to-foundation details (A5.30) show flashing at the wall but no drainage or ventilation strategy for the deck edge adjacent to the insulated foundation/enclosure | **LIKELY NEUTRAL** | General constructability concern about deck edge moisture management. Overlaps D6 area. No confirmed error. Also found by Gemini. |
| 15 | Code summary (G0.11) mixes IRC and IBC concepts, citing the IBC area table ("unlimited area per story") for a project governed by the IRC | **LIKELY NEUTRAL** | Documentation error in the code summary, not a construction error. The IRC governs R-3 one- and two-family dwellings; the IBC unlimited area concept doesn't apply but its presence in the code summary doesn't affect construction. Also found by Gemini. |
| 16 | Stair drawings (A3.22) show railings and guards but provide no handrail criteria, profiles, or extension information for code compliance review | **LIKELY NEUTRAL** | Handrail profile and extension details are typically provided in millwork shop drawings. No confirmed non-compliant profile. Also found by Gemini. |
| 17 | Removable deck panel for pool-cover access shown only in plan (A5.01); no framing, support, hardware, or removal detail exists in the set | **POTENTIAL NEW ISSUE** | Custom condition with zero construction documentation in the architectural set. The panel is shown in plan but nothing specifies how it is built, supported, or removed. Also found by Gemini. |
| 18 | Rain chains, collection pots, and underground leaders are part of the design intent but no detail shows overflow control, pot construction, cleanouts, or pipe connection at grade | **LIKELY NEUTRAL** | Site drainage/civil scope. Rain chain and collection pot details are landscape architecture or civil engineering scope. Not expected on architectural construction drawings. Also found by Gemini. |
| 19 | Exposed above-ground pool walls are specified to be finished, but no drawing identifies the finish material or termination conditions at grade, deck, and pool edges | **LIKELY NEUTRAL** | Pool finish coordination is typically pool subcontractor scope. Architectural drawings are not expected to detail pool interior surfaces. Also found by Gemini. |
| 20 | Title sheet (G1.00) and spec cover leave key project-identification fields (owner, architect, structural engineer) blank | **LIKELY NEUTRAL** | Administrative placeholder fields. No construction impact. Also found by Gemini. |
| 21 | Code summary (G0.11) leaves the planning application number blank | **LIKELY NEUTRAL** | Administrative field. No construction impact. Also found by Gemini. |
| 22 | Spec booklet includes placeholder text under "Plan Changes" and an incomplete drawing-set reference | **LIKELY NEUTRAL** | Administrative/editorial. Overlaps N20 (informal/narrative spec format). Also found by Gemini. |
| 23 | Door schedule leaves hardware blank for most doors; the narrative spec does not supply hardware sets | **LIKELY NEUTRAL** | Hardware by allowance or separate spec section is standard residential practice. Answer key neutral list includes this category. Also found by Gemini. |
| 24 | Bathroom finish schedule comments end with "FOR SHOWER FINISHES SEE" but identify no destination sheet or spec reference | **POTENTIAL NEW ISSUE** | Specific incomplete cross-reference that leaves shower tile scope unresolvable from the finish schedule. Found by Opus, Sonnet, Gemini, and GPT — the most consistently flagged unmatched finding across all four models. Strong candidate for new answer key entry. |
| 25 | Drawing set notation is inconsistent: plan notes use "W1/E1" style while formal assembly designations on A4.00 use "W-1/E-1" style | **LIKELY NEUTRAL** | Minor drafting convention inconsistency. Context makes assembly identification clear; no confirmed misidentification. Low construction impact. Also found by Gemini. |

---

## Notes for Scorer

**Known Incorrect flags in this response:**
- **B-2** (stair riser math doesn't reconcile): model presents at "Moderate" certainty. 18 × 6-11/16" ≈ 10'-0⅜" — within tolerance. Consistent with **I8**. Whether to apply −1 penalty at "Moderate" confidence is scorer's call.

**Cross-model priority items (appear in 3+ model triages):**
- **Item 24** (Shower finishes "SEE" with no reference) — flagged by all 4 models. Highest priority for new answer key entry.
- **Item 1** (Interior elevation labeled "Guest Bathroom 19") — flagged by Opus, Gemini, and GPT.
- **Item 2** (L7 lighting count = 2 vs 75 LF) — flagged by Opus, Sonnet, and GPT.
- **Item 6** (Cat6a vs Cat6e) — flagged by Gemini and GPT.
- **Item 7** (Pool mechanical location) — flagged by Gemini and GPT.
- **Item 8** (G0.01 references Div. 8) — flagged by Gemini and GPT.
- **Item 9** (Shower door framing) — flagged by Opus, Gemini, and GPT.
- **Item 13** (Corner window head/sill waterproofing) — flagged by Gemini and GPT.
- **Item 17** (Removable deck panel) — flagged by Gemini and GPT.

**Items unique to GPT:**
- Item 4 (roof slope 1/4" vs 1/8" on elevations) — also flagged by Gemini; strong candidate.
