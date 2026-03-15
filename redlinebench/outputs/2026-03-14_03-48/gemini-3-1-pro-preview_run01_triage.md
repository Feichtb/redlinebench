# Triage — gemini-3-1-pro-preview_run01
**Triaged:** 2026-03-14
**Total findings in model output:** 58
(A: 5 | B: 5 | C: 13 | D: 7 | E: 9 | F: 7 | G: 12)

---

## Findings-to-Answer-Key Mapping

| Model ID | Model Finding (brief) | Answer Key Match | Notes |
|---|---|---|---|
| A-1 | Door 11-1 shown on plan at Bathroom 11 but missing from door schedule | **A1** | Direct match (11-1 was changed to 10-1; schedule has 10-1, plan still shows 11-1) |
| A-2 | South Elevation (A3.02) shows a window tagged "1" under the porch; Tag 1 not in window schedule | *UNMATCHED* | See below |
| A-3 | Room Finish Schedule assigns WD-1 to Reading Nook (10); spec/section calls for WD-4 | **A10** | Direct match |
| A-4 | Door 08-1 (Master Closet) drawn as pocket door on plan; door schedule lacks pocket designation | *UNMATCHED* | See below |
| A-5 | Garage 15 is entirely blank on RCP; specs require 4 interior lights in garage | *UNMATCHED* | See below |
| B-1 | North side dimension total 72'-1" vs. South side total 72'-1½" on same plan (A2.01) | *UNMATCHED* | See below |
| B-2 | Stair riser count (10 EQ + 8 EQ at 6-11/16") doesn't cleanly reconcile to 10'-0" floor-to-floor | **KNOWN INCORRECT (I8)** | 18 × 6-11/16" ≈ 10'-0⅜"; model is flagging rounding, not a real error; I8 applies |
| B-3 | E-2 wall assembly text says "2×6 STUDS" but top dimension implies 2×8 (7¼") | **C7** + **B3** | C7 = stud size conflict (spec vs. drawing); B3 = stated total doesn't match layers |
| B-4 | Connector/entry roof slope labeled 1/4" per foot on roof plan (A2.03) but 1/8" per foot on exterior elevations | *UNMATCHED* | See below |
| B-5 | Lowered crawlspace/pool mechanical slab at -7'-0" on crawlspace plan (A2.00) not shown in building or pool sections | *UNMATCHED* | See below |
| C-1 | Window schedule: Marvin Ultrex vs. specs Andersen 400 | **C1** | Direct match |
| C-2 | Door 03-1 listed as "METAL" in schedule; specs call for "Jeld-Wen IWP Wood Exterior Door" | **A6** | Direct match |
| C-3 | E-4 shows 1½" rigid insulation; specs say 1" Insulated ZIP Board | **C2** | Direct match |
| C-4 | E-1 shows ½" rigid insulation; specs/code require 2" XPS = R10 | **D2** | Direct match |
| C-5 | Lap siding specified exclusively on "North and West Facades" in specs; South Elevation shows lap siding on south face of master bedroom | **C3** | Cladding facade location conflict (different material than Thermory Ash but same answer key category) |
| C-6 | Specs require epoxy garage floor; floor assembly and finish schedule show only concrete slab | **N3** (neutral) | Neutral: additional finish info in spec rather than schedule is standard |
| C-7 | Pool enclosure spec says 48" fence on three sides; drawings show 48"/36"/26" cable railing conditions | **E2** + **E5** | E2 = 26" railing below minimum; E5 = pool barrier cable spacing |
| C-8 | Specs require Cat6a ethernet cabling; RCP notes are labeled "Cat6e" | *UNMATCHED* | See below |
| C-9 | Specs describe single 3"/12" slope; roof plan shows multiple slopes (2"/12", 1/4"/12") | **C6** | Direct match |
| C-10 | Specs place pool mechanical equipment "opposite house toward west end"; drawings locate it adjacent to house | *UNMATCHED* | See below |
| C-11 | Sheet G0.01 directs contractor to door data in "Specifications Div. 8"; provided spec booklet has no Division 8 | *UNMATCHED* | See below |
| C-12 | Hose bib quantity: code summary 5, specs call for 3, elevations show yet another count | **C4** | Direct match |
| C-13 | Shower doors: master frameless and guest semi-framed per spec; door schedule lists both generically | *UNMATCHED* | See below |
| D-1 | Low-slope roof areas (1/4"/12") use same standing-seam assembly as main roof; no separate low-slope assembly | **G8** | G8 = below-minimum slope for standing seam; N8 says A4.13 addresses it — scorer to determine |
| D-2 | Roof intersection/valley detail concentrates water in internal gutter with no secondary waterproofing strategy | *UNMATCHED* | See below |
| D-3 | Base details don't establish consistent clearance between cladding/wood components and grade — several terminations vulnerable to splash-back | *UNMATCHED* | See below |
| D-4 | Sealed crawlspace enclosure not shown as continuous air/thermal/vapor barrier at stem-wall-to-floor transition | **D6** | Direct match |
| D-5 | Entry hall glazing details over stone/concrete lack subsill pan or explicit drainage path at window/door base | *UNMATCHED* | See below |
| D-6 | Corner window jamb details (A4.13/1–4) omit head and sill waterproofing details | *UNMATCHED* | See below |
| D-7 | Deck-to-foundation details show flashing at wall but no drainage/ventilation strategy for deck edge | *UNMATCHED* | See below |
| E-1 | Code summary mixes IRC and IBC concepts; states Type V-B/R-3 has "unlimited area per story" | *UNMATCHED* | See below |
| E-2 | Garage wall separation not identified as code-compliant fire separation assembly | **E4** | Direct match |
| E-3 | F-1 floor/ceiling over garage shows ½" gypsum; not identified as fire-rated separation | **E7** | Direct match |
| E-4 | Garage-to-interior door (16-1) scheduled as ordinary solid-core door; no fire rating or self-closing noted | **E8** | Direct match |
| E-5 | Pool barrier documentation incomplete; no self-closing/self-latching gate requirements shown | **E5** | Direct match |
| E-6 | East deck elevation calls out 26" cable railing at stair | **E2** | Direct match |
| E-7 | Safety glazing (tempered) not identified at doors, baths, low glazing, or stair-adjacent glazing | **N9** (neutral) | Neutral: safety glazing identification is out of scope for this benchmark |
| E-8 | Sleeping room windows not identified as emergency escape openings; schedule lacks clear-opening data | **E3** | Direct match |
| E-9 | Stair drawings show railings but no handrail criteria, profiles, or extension information | *UNMATCHED* | See below |
| F-1 | Pool/deck/retaining wall/mechanical interfaces repeatedly deferred to pool contractor | **N14** (neutral) | N14: pool coordination is intentional deferral |
| F-2 | Removable deck panel for pool-cover access shown only in plan; no framing, support, hardware, or removal detail | *UNMATCHED* | See below |
| F-3 | Concealed steel porch/entry overhang — architectural details don't show steel integration with wall assembly | **N13** (neutral) | N13: design team accepted this approach |
| F-4 | Wet-laid and dry-laid SS-3 paths called out; no buildup, edge restraint, or drainage details for exterior paving | **C8** | Direct match (two installation methods shown, spec doesn't distinguish) |
| F-5 | Rain chains, collection pots — no overflow control, pot construction, cleanouts, or pipe connection at grade | *UNMATCHED* | See below |
| F-6 | Exposed above-ground pool walls — finish not identified; no drawing shows how it terminates at grade/deck/pool edge | *UNMATCHED* | See below |
| F-7 | Master bath hydronic floor heat deferred to bidder; no manifold location or coordination criteria | **F3** | Direct match |
| G-1 | Title sheet leaves key project-identification fields (owner, architect, structural engineer) blank | *UNMATCHED* | See below |
| G-2 | Code summary leaves planning application number blank | *UNMATCHED* | See below |
| G-3 | Spec booklet has placeholder text and incomplete drawing-set reference | *UNMATCHED* | See below |
| G-4 | Door schedule leaves hardware blank for most doors; specs don't supply hardware sets | *UNMATCHED* | See below |
| G-5 | Lighting fixture schedule all TBD | **G6** | Direct match |
| G-6 | Major scope selections unresolved: HVAC, HERO certification, stains/colors, carpet, hardware, countertop | **G6** + **N4/N17** (neutral) | G6 for TBDs; HVAC unresolved is neutral (N4/N17) |
| G-7 | Bathroom finish schedule "FOR SHOWER FINISHES SEE" — no destination | *UNMATCHED* | See below |
| G-8 | Finish key "T-1" in room finish schedule; not defined in any drawing legend or spec | **G11** | Direct match |
| G-9 | "Site verify Level One height" and "driveway location verify in field" defer primary design decisions | **G9** | Direct match |
| G-10 | Spec references A8.10 for reading nook bunk detail; no A8.10 in set | **G12** | Direct match |
| G-11 | Pool technical specifications explicitly deferred for later determination | **N14** (neutral) | Neutral |
| G-12 | Notation system inconsistent: W1/E1 in plan notes vs. W-1/E-1 in formal assembly designations | *UNMATCHED* | See below |

---

## UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Suggested Classification | Reasoning |
|---|---|---|---|
| 1 | South Elevation (A3.02) shows a window tagged with a hex "1" under the porch, but Window Schedule on A8.01 starts at Tag 2 and contains no Tag 1 | **POTENTIAL NEW ISSUE** | Specific untagged or mislabeled window on an elevation — different location and different tag than G2 (which is East Elevation, Tag 5 removed). If confirmed, this is a second untagged-window issue. Scorer should verify against A3.02. |
| 2 | Door 08-1 (Master Closet) is depicted as a pocket door on enlarged plan A2.01A, but the Door Schedule lists 08-1 without pocket hardware designation or pocket door notation | **POTENTIAL NEW ISSUE** | Specific plan-vs-schedule type conflict: a pocket door in the plan is listed as a standard door in the schedule, affecting hardware procurement and framing. Verifiable from plan and schedule. |
| 3 | Garage 15 (Room 15) is entirely blank on the First Floor Reflected Ceiling Plan (A6.01), but specs require 4 interior lights in the garage | **LIKELY NEUTRAL** | Lighting in the garage on the architectural RCP is a common coordination gap. RCP is produced by the architect; fixture layout inside the garage is often deferred to electrical scope. Low construction impact. |
| 4 | North side dimension total on plan (A2.01) sums to 72'-1" while the South side of the same plan sums to 72'-1½" — a ½" discrepancy on the same sheet | **POTENTIAL NEW ISSUE** | Specific half-inch discrepancy between north and south dimension strings on the same plan sheet. Different from the known-incorrect item (which involves the enlarged plan vs. overall plan). If confirmed, this would be a new dimensional error — scorer should verify arithmetic on A2.01. |
| 5 | Connector/entry roof slope is labeled 1/4" per foot (1/4":12") on roof plan A2.03 but is labeled 1/8" per foot (1/8":12") on exterior elevations — actual pitch is undefined | **POTENTIAL NEW ISSUE** | Specific slope label conflict between two drawing types for the same roof area. Verifiable from A2.03 and the elevation sheets. A genuine discrepancy here would affect drainage design and product warranty compliance. |
| 6 | Lowered crawlspace/pool mechanical slab is called out at -7'-0" on crawlspace plan A2.00, but building sections and pool sections do not show that depressed slab elevation | **LIKELY NEUTRAL** | Documentation gap: a depressed slab mentioned on one plan but not confirmed in section. Not a confirmed error — sections may simply not cut through that area. Low direct construction impact absent a confirmed conflict. |
| 7 | Specs require Cat6a ethernet cabling; reflected ceiling plan notes are labeled "Cat6e" — different cable category specified | **POTENTIAL NEW ISSUE** | Specific product spec conflict: Cat6a and Cat6e are different cable standards. Verifiable from spec and RCP notes. Also found by GPT. Scorer should confirm RCP note text. |
| 8 | Specs state pool mechanical equipment is "on the side of the pool opposite the house toward the west end," but drawings locate the pool mechanical area adjacent to the house/deck | **POTENTIAL NEW ISSUE** | Specific location conflict between the spec narrative and the drawing layout. If confirmed, this affects utilities routing, acoustics, and access. Verifiable from A5.01 and spec. Also found by GPT. |
| 9 | Sheet G0.01 directs the contractor to door data in "Specifications Div. 8"; the provided specification booklet is a narrative allowance document with no Division 8 section or door data | **POTENTIAL NEW ISSUE** | Specific orphaned cross-reference directing the contractor to a non-existent specification section for door data. Similar in character to G12 (spec references non-existent sheet A8.10). Verifiable from G0.01 and spec. Also found by GPT. |
| 10 | Door schedule lists both shower doors as generic clear glass doors; specs distinguish master shower door as frameless and guest shower door as semi-framed — framing type affects hardware and installation | **POTENTIAL NEW ISSUE** | Specific spec-vs-schedule conflict on shower door framing type. Verifiable from spec and A8.01. Also found by Opus and GPT. Affects hardware procurement and GC/glazing subcontractor coordination. |
| 11 | Roof intersection/valley detail concentrates water into an internal gutter/valley condition without showing a secondary waterproofing strategy beneath the metal roof system | **LIKELY NEUTRAL** | Design judgment call about valley protection. A single waterproofing line under a standing seam valley is standard in many details. No specific confirmed error; adequacy depends on the specific detail not evaluated at triage. |
| 12 | Multiple base details (A4.11/5, A4.10/6, A5.30/3&5) don't establish consistent clearance between cladding or wood components and adjacent grade, paving, or decking | **LIKELY NEUTRAL** | General moisture protection observation across multiple details. No specific confirmed below-minimum clearance. Cladding-to-grade clearance is a judgment call depending on exposure and cladding material. |
| 13 | Entry hall glazing details over stone/concrete floor (A4.10) do not show a subsill pan or explicit drainage path at the base of the custom window and door assemblies | **LIKELY NEUTRAL** | Specific detail concern about window base waterproofing. Design team may have addressed this in shop drawings. Not a confirmed missing component — difficult to verify without knowing exact detail intent. |
| 14 | Custom corner window jamb details (A4.13/1–4) show jamb sections only and omit head and sill waterproofing details for high-risk envelope conditions | **POTENTIAL NEW ISSUE** | Corner windows at exterior corners are high-risk moisture entry points. The absence of head and sill details for these custom conditions is a specific, verifiable documentation gap. Scorer should confirm A4.13 contains only jamb sections. |
| 15 | Deck-to-foundation details (A5.30/3&5) show flashing at the wall but do not show a drainage or ventilation strategy for the deck edge condition adjacent to the insulated foundation/enclosure | **LIKELY NEUTRAL** | General constructability concern about deck edge moisture management. Overlaps D6 (air barrier continuity). No specific confirmed error. |
| 16 | Code summary (G0.11) mixes IRC and IBC concepts by stating that a Type V-B/R-3 building is permitted "unlimited area per story" — which is an IBC concept, not applicable under IRC | **LIKELY NEUTRAL** | Observation about code summary accuracy. The IRC governs this project; the IBC area table reference is a documentation error in the code summary but does not affect construction. Low impact. |
| 17 | Stair drawings (A3.22) show railings and guards but do not provide handrail criteria, profiles, or extension requirements for stair safety code compliance review | **LIKELY NEUTRAL** | Handrail profile and extension details are typically provided in millwork shop drawings or as standard notes. Not a confirmed code violation without evidence of non-compliant profile. |
| 18 | Removable deck panel for pool-cover access is shown only in plan (A5.01) with no framing, support, hardware, or removal detail provided anywhere in the set | **POTENTIAL NEW ISSUE** | Custom condition with zero construction documentation. The panel is shown on plan but has no detail showing how it is built, supported, or removed — a genuine constructability gap. Also found by GPT. |
| 19 | Rain chains, collection pots, and underground leaders are referenced in the design intent (specs) but no details show overflow control, pot construction, cleanouts, or pipe connection at grade | **LIKELY NEUTRAL** | Site drainage/civil scope. Rain chain details are typically a landscape/civil coordination item. Not expected on architectural drawings. |
| 20 | Exposed above-ground pool walls are specified to be finished, but no drawing identifies the finish material or shows how it terminates at grade, deck edge, and pool waterline | **LIKELY NEUTRAL** | Pool finish coordination is typically pool subcontractor scope. Architectural drawings are not expected to detail pool interior finishes. |
| 21 | Title sheet (G1.00) and spec cover leave key project-identification fields (owner, architect, structural engineer) blank | **LIKELY NEUTRAL** | Administrative placeholder fields. Does not affect construction. Common at certain stages of document development. |
| 22 | Code summary (G0.11) leaves the planning application number blank | **LIKELY NEUTRAL** | Administrative field. No construction impact. |
| 23 | Spec booklet includes placeholder text under "Plan Changes" and an incomplete drawing-set reference | **LIKELY NEUTRAL** | Administrative/editorial. Overlaps N20 (informal/narrative spec format). No construction impact. |
| 24 | Door schedule leaves hardware blank for most doors; the narrative spec does not supply hardware sets | **LIKELY NEUTRAL** | Hardware by allowance or separate spec section is standard residential practice. Answer key neutral list includes this general category. |
| 25 | Bathroom finish schedule comments read "FOR SHOWER FINISHES SEE" with no destination sheet or spec reference | **POTENTIAL NEW ISSUE** | Specific incomplete cross-reference in finish schedule. Found by multiple models (Opus, Sonnet, GPT). Leaves shower tile scope unresolvable from the finish schedule. |
| 26 | Notation system is inconsistent across the drawing set: tags such as "W1/E1" appear in plan notes while assemblies are formally designated "W-1/E-1" on A4.00 | **LIKELY NEUTRAL** | Minor drafting convention inconsistency. No confirmed misidentification of an assembly; context makes the intent clear. Low construction impact. |

---

## Notes for Scorer

**Known Incorrect flags in this response:**
- **B-2** (stair riser count doesn't reconcile to 10'-0"): the model presents this at "Moderate" confidence. 18 × 6-11/16" ≈ 10'-0⅜" — within typical construction tolerance. This is a misread consistent with **I8**. Whether to apply the −1 penalty at "Moderate" confidence is scorer's call; the instruction says "tentative or hedged flags may be scored as neutral."

**Priority items for ruling:**
- Items 1 (South Elevation window tag "1"), 2 (pocket door not in schedule), 4 (72'-1" vs 72'-1½"), 5 (roof slope 1/4" vs 1/8"), 7 (Cat6a vs Cat6e), 8 (pool mechanical location), 9 (G0.01 Div. 8 reference), 10 (shower door framing), 14 (corner window waterproofing), 18 (removable deck panel), 25 (shower finishes incomplete) are strongest candidates for new answer key entries.
- Items 7, 8, 9, 10, 25 also appear in GPT triage.
- Items 2 and 10 also appear in Opus triage.
