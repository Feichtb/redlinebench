# Nicks Bend House — AI Drawing Review Benchmark Answer Key

This document is the scorer's reference. It lists every known issue in the benchmark drawing set, a neutral findings list (no score impact), and a known incorrect findings list (score negatively). The scorer uses this to evaluate each model's output.

---

## How to Score

For each issue on the scoreable list, score the model:
- **1** = Found and correctly described
- **0.5** = Found but vague or incomplete
- **0** = Missed

Additionally track:
- **Incorrect Findings**: Model flagged something that is factually wrong (misread the documents, reached incorrect conclusion). Score **-1** per incorrect finding.
- **Neutral Findings**: Model flagged something on the Neutral list — debatable, out-of-scope, or a judgment call. **No score impact** either direction.
- **Total Items Flagged**: Raw count of everything the model reported.

---

## A. Schedule-to-Drawing Cross-Reference Errors

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| A1 | Door schedule lists door "10-1" but Room 10 (Reading Nook) has no door on floor plans. Original door 11-1 was changed to 10-1. | A8.01 vs. A2.01A | Model should flag that 10-1 doesn't exist on plans, or that Bathroom 11 now has no scheduled door. |
| A2 | Door 09-2 width changed from 5'-0" to 4'-0" in schedule. Enlarged plan A2.01A shows the wider opening. | A8.01 vs. A2.01A | Model should flag width discrepancy between schedule and plan. |
| A3 | Window type 6 count changed from 7 to 8 in schedule. Only 7 type-6 windows appear on plans/elevations. | A8.01 vs. plans/elevations | Model should count type 6 windows and flag the mismatch. |
| A4 | Powder Room (14) floor finish changed from F-2 (tile) to F-4 (carpet). Carpet in a powder room is inappropriate. | A8.01 Room Finish Schedule | Model should flag inappropriate floor finish for a bathroom. |
| A5 | Entry Hall (01) east wall finish changed from WD-1 to P-1. Interior elevations and details (A3.20, A4.10, A7.01) show wood walls, not painted gypsum. Also: base finish B-2 ("wood species to match wall") on the same schedule row becomes internally inconsistent — B-2 specifies a wood base that references the wall material, but the wall is now listed as painted drywall (P-1). | A8.01 vs. A3.20, A7.01 | Model should flag contradiction between finish schedule and drawn elevations. May also flag base/wall material mismatch within the same schedule row. |
| A6 | Door 03-1 material changed from WOOD to METAL in schedule. Frame material still says WOOD. Details on A4.10 show wood door at all entry conditions. Metal door in a wood frame is unusual. | A8.01 vs. A4.10 | Model should flag material conflict and the unusual metal-door / wood-frame combination. |
| A9 | Room 15 (Garage) assigned F-4 (carpet) in finish schedule. Garage has concrete slab per A2.00 and A4.12. Should be F-5. | A8.01 vs. A2.00, A4.01 | Model should flag wrong floor assembly for garage. |
| A10 | Room Finish Schedule assigns WD-1 (maple/birch clear stain) to Room 10 (Reading Nook) walls, but specifications require WD-4 (maple tongue and groove boards) for that space. | A8.01 vs. Specs p.6 | Model should flag wall finish material conflict for the Reading Nook. |
| A11 | Interior elevation 5 on A7.02 is labeled "Guest Bathroom 19 – South" but Room 19 is the Guest Closet; the Guest Bathroom is Room 18. The mislabeling causes shower finish and tile layout references in that elevation to point to the wrong room. | A7.02 vs. A2.01B, A8.01 | Model should flag the label mismatch between the interior elevation title and the room numbering on the floor plan. |

---

## B. Dimensional and Geometric Errors

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| B1 | Office length dimension changed from 11'-6" to 11'-5" on A2.01B. Other plan (A2.01) may show the original dimension. | A2.01B vs. A2.01 | Model should flag 1" discrepancy between plan scales. |
| B2 | Crawl space datum on North Elevation changed from 502'-0" to 501'-0". All other sheets show 502'-0". | A3.02 vs. A2.00, A3.01, A3.03, A3.10 | Model should flag inconsistent datum across sheets. |
| B3 | E-3 wall assembly plan dimension changed from 8-9/16" to 8". Individual layer thicknesses still sum to 8-9/16". | A4.00 | Model should flag that the stated total doesn't match the sum of layers. |
| B4 | Grid spacing between D and E changed from 6'-11 1/2" to 6'-10 1/2" on A2.01. Enlarged plans unchanged. | A2.01 vs. A2.01A/B | Model should flag grid dimension discrepancy between plan scales. |
| B5 | Stair headroom not dimensioned on either stair section. | A3.22 | Model should flag missing headroom dimension. |
| B6 | Crawl space elevation annotations (-6'-0", -7'-0", -9'-0") relationship to datums unclear. | A2.00 | Model should flag ambiguous elevation relationships. |

---

## C. Spec-to-Drawing Conflicts

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| C1 | Window manufacturer: specs say "Andersen, 400 Series" but window schedule says "Ultrex-Marvin-Stonewhite." | Specs p.3 vs. A8.01 | Model should flag manufacturer mismatch. |
| C2 | Wall insulation: specs say "1" Insulated ZIP Board" but drawings show "1 1/2" RIGID INSULATION" in E-3/E-4. Different thickness and potentially different product. | Specs p.4 vs. A4.00 | Model should flag thickness and product discrepancy. |
| C3 | Cladding location: specs say Thermory Ash (WD-3) on "South and West Facades." Elevations show wood cladding on South and East. | Specs p.2 vs. A3.01, A3.02 | Model should flag facade location conflict. |
| C4 | Hose bib count: specs say 3, elevations show 5 Aquor House Hydrant V2+ locations. | Specs p.7 vs. A3.01, A3.02 | Model should flag count discrepancy. |
| C5 | Ceiling insulation: specs say R = 49, code summary (G0.11) says R = 53, roof assembly R-1 calculates to ~R53. | Specs p.4 vs. G0.11, A4.01 | Model should flag R-value discrepancy across documents. |
| C6 | Roof slope specification: specs describe a single "3"/12" slope on diagonal" as if there is one pitch. Roof plan A2.03 shows three distinct slopes — 3"/12", 2"/12", and 1/4"/12". The 2"/12" and 1/4"/12" slopes are not mentioned in the specifications. | Specs p.1 vs. A2.03 | Model should flag that the spec implies a single slope while the drawings show multiple slopes, and/or flag the unaddressed slopes. |
| C7 | Wall assembly E-2 stud size: E-2 is drawn and dimensioned with 2x8 studs (7-1/4" cavity, 11-1/2" plan width) but specifications state all conditioned exterior walls to be 2x6. Affects framing, insulation cavity depth, and material procurement. | A4.00 (E-2) vs. Specs p.2 | Model should flag stud size conflict between drawing and specification. |
| C8 | SS-3 flagstone installation method: enlarged plan A2.01A calls out both "DRY-LAID SS-3 PATIO" and "WET-LAID SS-3 RAMP," indicating two different installation methods for the same material. Specifications describe SS-3 (Scott's Stone Heather Grey Flagstone) without distinguishing between dry-laid and wet-laid applications or specifying installation requirements for each. | A2.01A vs. Specs p.3 | Model should flag that two installation methods are shown but only one (or neither) is specified. |
| C9 | Tile flooring material vs. assembly designation: specs call for SS-2 (honed limestone, Corinthian White, Bedrosians) in Entry Hall (01), Laundry Room (12), and Powder Room (14), but the Room Finish Schedule assigns generic F-2 (tile thinset) to these rooms with no cross-reference to the SS-2 product. The schedule does not confirm which tile material applies. | A8.01 vs. Specs p.3 | Model should flag that the spec calls for a specific stone product in these rooms but the schedule uses a generic assembly tag. |

---

## D. Building Envelope and Building Science

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| D1 | Weather barrier label removed from wall assembly E-3 (Fiberboard). E-4 still shows weather barrier. | A4.00 | Model should flag missing weather barrier in E-3 vs. similar E-4. |
| D2 | E-1 CMU wall rigid insulation changed from 2" to 1/2". At ~R-2.5, likely below the R-10 crawl space requirement on G0.11. | A4.00 vs. G0.11 | Model should flag inadequate insulation or discrepancy with code summary. |
| D3 | Sill detail (A4.11/2) flashing membrane reversed — laps under weather barrier instead of over it. Water directed behind WRB. | A4.11 Detail 2 | Model should flag incorrect flashing lap direction. |
| D4 | Second vapor barrier added to exterior face of E-1 CMU wall. Vapor barriers on both sides traps moisture. | A4.00 E-1 | Model should flag double vapor barrier as moisture trap. |
| D5 | Rigid insulation placed inboard of sheathing in E-3/E-4 wall assemblies — unconventional for CZ 4A, creates condensation risk at sheathing. | A4.00 | Model should identify the layer order and assess climate appropriateness. |
| D6 | Air barrier continuity not detailed at transitions (foundation-wall, wall-roof, penetrations). | A4.10, A4.11 | Model should flag missing air barrier transition details. |

---

## E. Code and Life Safety

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| E1 | Door 14-1 (Powder Room) width changed from 3'-0" to 1'-10". Below minimum door width. | A8.01 | Model should flag undersized door. |
| E2 | Cable railing on south deck section changed from 36" to 26". Below 36" minimum guard height. | A5.10 South Section | Model should flag railing below minimum code height. |
| E3 | EERO compliance unverifiable — some bedrooms may have only fixed windows. | A8.01, plans | Model should flag sleeping rooms that may lack operable egress windows. |
| E4 | Garage fire separation not explicitly identified — wall assembly, door rating, ceiling gypsum type ambiguous. | G0.11, A4.00, A8.01 | Model should flag missing garage separation documentation. |
| E5 | Pool barrier cable spacing not detailed (4" max opening required). | A5.01 | Model should flag missing cable spacing specification at pool barrier. |
| E6 | Makeup air for range hood: specified Zephyr range hood is rated at 650 CFM. IRC M1503.6 requires makeup air provisions for exhaust hoods exceeding 400 CFM. No makeup air system is specified or coordinated on architectural drawings or in specifications. | Specs p.6 | Model should flag that code-required makeup air is not specified for the selected range hood. |
| E7 | Garage ceiling fire separation above guest suite: Level 2 guest suite (Rooms 17–20) is located directly above the garage (Room 15) per section A3.10. IRC requires 5/8" Type X gypsum board on the garage ceiling where habitable space is above. Floor assembly F-1 (the Level 2 floor over the garage) specifies standard 1/2" gypsum board, which does not meet this requirement. | A3.10, A4.01 (F-1) | Model should flag that the floor assembly above the garage does not specify the required Type X gypsum. |
| E8 | Garage-to-house door self-closing hardware: door 16-1 (from garage Room 15 to hallway Room 16) is scheduled as a standard solid-core interior wood door with no hardware notation. IRC requires this door to be self-closing. Self-closing hardware is not specified anywhere in the documents. | A8.01 | Model should flag missing self-closing hardware requirement on the garage-to-habitable-space door. |

---

## F. Constructability

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| F1 | Garage door header detail revised: siding extends into Accoya frame, flashing removed. No drainage path. | A4.12 Detail 3 | Model should flag missing flashing and water management failure. |
| F2 | Object/block placed in door swing of door 11-1 in Bathroom 11. Creates clearance conflict. | A2.01A | Model should flag obstruction in door swing or question unidentified element. |
| F3 | Hydronic heating system with F-2 thinset in master bath — coordination concern with bidder-designed system. | A2.01A, A8.01 | Model should flag potential tile/hydronic coordination issue. |
| F4 | Central vacuum system — wall fixtures keynoted but no equipment location, piping, or rough-in details. | Plans | Model should flag missing system details. |

---

## G. Completeness and Clarity

| # | Issue | Location | What to Look For |
|---|-------|----------|-----------------|
| G1 | Roof assembly tag left blank on Entry Hall roof area of East Elevation. The blank tag should read R-2. See also G14, which addresses the related issue that R-2 is referenced on elevation sheets but not defined on A4.01. | A3.01 | Model should flag missing/blank roof tag. May also flag R-2 as undefined; both observations describe the same documentation gap and are valid. |
| G2 | Window tag "5" removed from East Elevation. Window drawn but untagged. | A3.01 | Model should flag untagged window. |
| G3 | Orphaned keynote tag "13" on A2.01A with no legend entry. | A2.01A | Model should flag unidentified keynote. |
| G4 | Sheet list shows deck sections as "A5.11" but actual sheet is A5.20. | Cover sheet vs. A5.20 | Model should flag sheet list / sheet number mismatch. |
| G5 | Plans A2.01, A2.02, and A2.03 cross-reference a building section labeled A3.04, but those callout bubbles show A3.10 and no sheet A3.04 exists in the set. | A2.01, A2.02, A2.03, sheet index | Model should flag that the referenced section sheet does not exist, or that the cross-reference label appears mislabeled. |
| G6 | Extensive TBDs — lighting fixtures L3-L11, appliances all TBD on a bid set. | A6.01, A8.01 | Model should flag incomplete selections preventing bidding. |
| G7 | "OPENING TBD" at Level 2 stair landing — undefined on construction documents. | A2.01B | Model should flag unresolved opening. |
| G8 | Awning roof slope 1/4":12" is below typical standing seam manufacturer minimums (most require 1/2":12" minimum). | A2.03 | Model should flag the low slope as a potential incompatibility with standard standing seam products. |
| G9 | "Verify in field" on primary building dimensions affecting setback compliance. | A1.01, A2.00 | Model should flag deferred setback-critical dimensions. |
| G10 | F-1 floor assembly (typical Level 1) lacks product specification — species, thickness, installation method. | A4.01 | Model should flag missing floor product information. |
| G11 | Room Finish Schedule assigns wall type "T-1" to Bathroom 11, but T-1 is never defined in the specification (unlike P-1 and other finish codes, which are defined). | A8.01 vs. Specs | Model should flag that T-1 is used in the finish schedule but has no corresponding spec definition. |
| G12 | Spec references "Detail 1 on page A8.10" but no sheet A8.10 exists in the drawing set. | Specs vs. sheet index | Model should flag orphaned spec cross-reference to a non-existent sheet. |
| G13 | Bottom stair deleted from A2.01B enlarged north plan. Stair is still visible on interior elevation 8/A7.01. (Moved from A — no stair schedule; this is a plan-to-elevation coordination failure.) | A2.01B vs. A7.01 detail 8 | Model should flag missing stair on plan that appears in the interior elevation. |
| G14 | Roof assembly tag "R-2" is called out on elevation sheets but R-2 is not defined anywhere on A4.01 (which defines only R-1). R-2 is a sloped variant of R-1 with a different overhang condition; the overhang is already captured in detail 7/A4.10. The correct resolution is to remove the R-2 tag and reference R-1. | A3.01 (elevations) vs. A4.01 | Model should flag that R-2 is referenced in the drawings but has no corresponding assembly definition on A4.01. |
| G15 | Lighting fixture L7 (LED strip) is listed in the schedule with a count of "2," but is described in specs and shown in drawings at the kitchen, stair handrail, and Reading Nook — totaling approximately 75 LF of strip lighting. A count of 2 fixtures is irreconcilable with a 75 LF continuous run. | A8.01 (lighting schedule) vs. A6.01, Specs | Model should flag that the L7 schedule count conflicts with the spec and plan descriptions. |
| G16 | Wall assembly W-3 (Interior Insulated Wall) is defined on A4.00 but is not tagged on any floor plan. Specifications require acoustic/thermal insulation in the wall between Master Bedroom (Room 06) and Second Bedroom (Room 09). That wall is not tagged with W-3, leaving the insulated wall scope undefined for the framing contractor. | A4.00 vs. A2.01B, Specs | Model should flag that W-3 is defined but not assigned on plans, particularly at the Master/Second Bedroom party wall. |

---

## Summary

| Category | Issues |
|----------|--------|
| A. Schedule-to-Drawing | 9 |
| B. Dimensional/Geometric | 6 |
| C. Spec-to-Drawing | 9 |
| D. Building Envelope | 6 |
| E. Code/Life Safety | 8 |
| F. Constructability | 4 |
| G. Completeness/Clarity | 16 |
| **Total** | **58** |

*Issue counts are current as of this version. New issues may be added as the drawing set is further tested. Always count from the issue tables above rather than relying on this summary.*

---

## Score Summary Template

| Category | Found | Score | Incorrect |
|----------|-------|-------|-----------|
| A. Schedule-to-Drawing | | | |
| B. Dimensional/Geometric | | | |
| C. Spec-to-Drawing | | | |
| D. Building Envelope | | | |
| E. Code/Life Safety | | | |
| F. Constructability | | | |
| G. Completeness/Clarity | | | |
| **Totals** | | | |
| | | | |
| Neutral Findings (no score impact) | | | |
| Incorrect Findings (−1.0 each) | | | |
| Total Items Flagged | | | |

---

## Neutral Findings Reference

Items a model may flag that are debatable, out-of-scope, or a reasonable judgment call. **No score impact** — do not score for or against. Entries are not numbered; this list grows over time.

| Finding | Notes |
|---------|-------|
| N1: Soffit material terminology: specs call for "Hardiesoffit panels" (fiber cement); drawings label it "FIBERBOARD SOFFIT." | Hardieboard is a type of fiberboard; interpretation varies. Not a clear error. |
| N2: Specs reference "211020 House_Architectural.pdf" — doesn't match the actual drawing set title. | Administrative inconsistency; low construction impact. |
| N3: Garage floor epoxy finish: specs call for epoxy coating; Room Finish Schedule assigns F-5 (concrete slab, no applied finish). | Additional finish info expected in specs rather than schedule. Not a clear drawing error. |
| N4: HVAC system type unresolved (dual-fuel vs. geothermal under consideration). | Out of scope for architectural review. |
| N5: Solar panels referenced in specs but not shown on roof plan. | Solar panels are labeled on elevation 1/A3.01; detailed solar layout is out of scope for the architectural set. |
| N6: Entry door smart lock (Level Lock) specified but not noted in door schedule. | Hardware coordination is typically done at door schedule; omission is minor. |
| N7: Rain chain drainage routing not shown on drawings. | Site/civil drainage coordination is out of scope. |
| N8: Low-slope roof section (1/4"/12") — standing seam manufacturer minimum slope concern. | Detail 5/A4.13 addresses this condition. |
| N9: Window schedule does not identify safety glazing (tempered glass) locations. | Valid observation but out of scope for this architectural review benchmark. |
| N10: Network equipment rough-in details not on architectural drawings. | Out of scope; MEP/low-voltage coordination. |
| N11: Tankless water heater locations not documented on architectural drawings. | Hot water supply noted in crawl space; routing and equipment location are MEP scope. |
| N12: Electrical panel and subpanel locations not annotated on floor plans. | Out of scope; electrical engineering. |
| N13: South porch concealed steel thermal bridging. | Design team reviewed and accepted this approach. |
| N14: Pool/deck/retaining wall coordination described as schematic. | Pool coordination notes are intentional; structural scope is separate. |
| N15: Porch overhang detail shows no gutter in one condition. | Out of scope for this review. |
| N16: Level 2 HVAC system assignment not specified. | Out of scope; mechanical engineering. |
| N17: Geothermal system decision unresolved. | Out of scope for architectural review. |
| N18: Smart electrical panel (Span/Lumin) decision unresolved. | Out of scope for architectural review. |
| N19: Crawl space height described as a range (60"–72") rather than a fixed dimension. | Range is an owner preference; not a drawing error. |
| N20: Specification narrative includes owner-instructional language rather than enforceable requirements. | Spec format is intentionally informal/narrative for this project. |
| N21: Window Tag 15 — schedule says CASEMENT but model number (ESDG4020) uses the fixed window prefix and comments say FIXED. | Window tag 15 may not exist in the current set; cannot be verified. Moved from scoreable (was A8). |
| N22: Corner window conditions eliminate structural corner posts — coordination needed with structural set. | Structural coordination is out of scope for an architectural review. Moved from scoreable (was F4). |
| N23: Aquor House Hydrant V2+ at multiple locations — no rough-in or installation details. | Plumbing rough-in details are typically MEP scope; architectural drawings are not expected to provide them. Moved from scoreable (was F5). |
| N24: CMU foundation wall (E-1) lacks exterior below-grade waterproofing or dampproofing. | Adequacy of parge coat as below-grade protection is a judgment call that depends on site conditions, soil type, and local practice. No score impact. |
| N25: Roof assembly R-1 is missing a waterproof underlayment or weather barrier. | The detail does not explicitly call out ZIP System Roof panels by name, so a model reading a conventional sheathing assembly and flagging missing underlayment is making a reasonable inference. ZIP panels serve as the integrated weather barrier, but this is not apparent from the detail alone. |
| N26: Finish schedule comments for Rooms 07, 11, and 18 read "FOR SHOWER FINISHES SEE" with no destination sheet or spec reference completing the callout. | Specific incomplete cross-reference noted by multiple models. The shower finish information may exist in the specs; the absence of a sheet/detail number in the schedule comment is a documentation gap but the information is not entirely missing from the document set. |
| N27: Sheet G0.01 directs the contractor to door data in "Specifications Div. 8"; the provided specification booklet has no Division 8 section or door data. | Orphaned cross-reference similar in character to G12. Specific and verifiable. No construction action is blocked since door data appears in the schedule and narrative spec, but the reference is broken. |
| N28: Door schedule lists both shower doors generically; specs distinguish master shower door as frameless and guest shower door as semi-framed. Framing type affects hardware procurement and installation. | Specific spec-vs-schedule conflict on shower door framing. The schedule is not expected to replicate all product features from the spec; the spec is the governing document for door type. No separate construction error beyond normal coordination. |
| N29: Pool mechanical equipment: specs describe placement "on the side of the pool opposite the house toward the west end"; drawings locate the pool mechanical area adjacent to the house/deck. | Specific location conflict between spec narrative and drawing layout. Pool coordination is intentional deferral (see N14); the conflict between spec language and drawing may reflect a design evolution. |
| N30: Cat6a vs Cat6e: specs require Cat6a ethernet cabling; reflected ceiling plan notes label the cabling as "Cat6e." Cat6a and Cat6e are different cable standards. | Specific product conflict between spec and drawing callout. Low-voltage cabling coordination is generally MEP scope (see N10), but the label discrepancy is a real documentation inconsistency. |
| Door schedule hardware types (garage door hardware, shower door hardware, etc.) not defined or detailed. | Hardware by allowance or separate spec section is standard practice for residential. |
| Kitchen countertop (SS-1: Silestone Ethereal Glow) and backsplash in spec but not cross-referenced in Room Finish Schedule. | Countertop and backsplash materials are commonly detailed in specs without being listed in finish schedules. Not a drawing error. |
| Multiple roof slopes (3"/12", 2"/12", 1/4"/12", 30°, 45°) across sheets; general multi-slope documentation concern. | Multi-slope roof documentation is not unusual. No specific numerical error. |
| Window elevations lack dimensional callouts for rough opening sizes or center-to-center spacing. | RO dimensions are typically on plans and window schedule, not on exterior elevations. If egress compliance is the concern, see E3. |
| Room ceiling heights not compiled in a schedule or called out on plans. | Ceiling heights are verified via building sections and notes. No confirmed code violation. |
| R-1 roof assembly does not label insulation R-value explicitly in the detail. | Related to C5 conflict, but the insulation is present in the assembly. Distinct documentation gap, not a missing component. |
| Foundation drain routing and slope to daylight not shown on plans. | Site drainage and foundation drain routing are civil/MEP scope. Not expected on architectural plans. |
| Crawl space fresh air intake not shown on A2.00. | Fresh air ventilation for crawl spaces is mechanical scope. Not expected on architectural plans. |
| Hallway widths (Rooms 05, 16) not dimensioned to verify 3'-0" minimum. | No confirmed below-minimum condition. IRC requires 3'-0" but expects contractor to maintain; not a clear architectural error without evidence of a violation. |
| Bathroom accessibility clearances (toilet, vanity, shower) not dimensioned on A7.02. | R-3 occupancy is not subject to ADA. IRC has limited bathroom clearance requirements for single-family residential. |
| Master closet and other built-in dimensions/details absent (rod heights, shelf spacing). | Custom built-in dimensions are shop drawing scope. Not expected in architectural CDs. |
| No penetration schedule or location plan for wall/floor penetrations. | A2.03 note directs contractor to coordinate penetrations with the architect prior to construction. Intentional deferral. |
| Kitchen appliance rough-in dimensions and clearances not shown on plans. | Verified from appliance submittals. Not a clear drawing error absent confirmed conflicts. |
| Bathroom tile products specified in spec; A7.02 details show generic assemblies without product callouts. | Tile layout and product confirmation are shop drawing scope. Standard practice. |
| Appliance schedule (A8.01) uses location codes (A1–A7) not clearly labeled on floor plan A2.01A. | Documentation clarity issue; not a drawing error. |
| Roof plan note "MINIMIZE ROOF PENETRATIONS, COORDINATE W/ ARCHITECT PRIOR TO CONSTRUCTION." | Intentional design-intent deferral on a standing seam roof, not an omission. |
| Plan dimensions don't state reference plane (face of framing, centerline, or finish face). | General drafting documentation concern. No confirmed measurement conflict. |
| Spec lacks product specifications for interior doors, frames, baseboards, trim, and lighting fixtures. | Overlaps with G6 (TBDs) and N20 (informal spec format). Not a distinct error. |
| Code summary "ROOF: 4000 SF" vs. "TOTAL AREA: 3840 SF" — roof area exceeds building footprint. | Roof area represents sloped/impervious surface area, which is expected to exceed the plan footprint on a multi-slope roof. Not an unexplained discrepancy. |
| Floor Assembly F-1 calls for "PLYWOOD SHEATHING" as the subfloor; specifications require "3/4" Advantech." | Spec being more specific than the drawing tag is not a conflict. Advantech is a brand of plywood sheathing; the drawing is not wrong. |
| R-1 roof assembly lacks explicit solid roof deck (plywood/OSB) shown beneath metal panels. | Furring strips are shown secured through rigid insulation. ZIP Roof panels serve as the integrated deck/weather barrier. The connection detail could be clearer, but the assembly is not missing a component. |
| Door plan tags present but no matching elevation or relite disposition detail for each door type. | Door type/relite coordination is a drafting quality observation; benchmark items A1/A2 address confirmed discrepancies. |
| Lighting fixture counts in schedule (e.g., L1=70) unverifiable against RCP at drawing scale. | General legibility observation; no specific count error identified. |
| Deck railing shown at 36" in some sections and 48" at pool barrier — not presented in a single coordinated elevation. | Both heights are code-compliant in context (36" deck rail, 48" pool barrier). Note: models raising this often have not found the actual E2 violation (26"). |
| Wall assembly callout tags on plans don't consistently annotate insulation thickness in associated details. | Documentation quality concern; overlaps with C2 and D6. No new specific discrepancy. |
| Roof slope callouts and top-of-framing heights vary across section cuts without a coordinated diagram. | Multi-slope roof documentation varies by section location. Not a confirmed numerical error beyond benchmark B1/B2/B4. |
| Window head/sill flashing details don't show air barrier membrane wrapping into jamb/head nodes. | General air barrier continuity observation; overlaps with D6. Not a specific benchmark error. |
| Low-slope roof walkability — no walkway pad detail or manufacturer walkway note shown. | Roof walkability is a maintenance coordination item, not an architectural drawing error. |
| Exterior path-of-travel or egress lighting not shown for exterior stairs or driveway. | Exterior lighting is electrical/MEP scope. IRC requirements are limited for single-family residential. |
| Subfloor lowered at tile shower transitions — no dimension or detail to control finished floor elevation relative to adjacent rooms. | Standard construction coordination item; not an architectural drawing error. |
| Reflected ceiling plan references enlarged plans for lighting — mounting heights and blocking not consistently shown. | Fixture blocking and mounting heights are coordinated with MEP/lighting drawings. |
| Vented fiberboard soffit vs. sealed crawl space — no detail explaining isolation between the two systems. | The soffit does not connect to the sealed crawl space; no conflict exists. |
| Accoya frame + furring + rigid insulation + fiberboard cladding build-up — constructability concern about window installation depth. | Detail was worked out; not an error. |
| Project name on A1.00 reads "NICKS BEND HOUSE" while other sheets read "BONFIRE HOUSE." | Minor title block administrative discrepancy; low construction impact. |
| Room 11 labeled "Bathroom" on floor plan and "Bathroom 11" on interior elevations — naming inconsistency. | Including room number in elevation labels is standard drafting practice; not a true inconsistency. |
| Wall assembly type tags on elevation sheets require cross-reference to A4.00; no keyed legend on elevation sheets. | Cross-referencing assembly tags to the schedule is standard practice. Not a drawing error. |
| Roof assembly R-1 rigid insulation placement — structural attachment and compression concern at furring strips. | A legitimate structural engineering observation; the assembly approach is documented. SE review is appropriate but this is not a drawing coordination error. |
| Window frames in details set against rigid insulation without explicit structural buck called out. | Window buck detailing varies by manufacturer. Hard to verify as a clear error without manufacturer data. |
| Garage door header LED strip lighting — no electrical conduit or weatherproofing shown at header. | Electrical coordination scope. The same header detail is flagged in F1 for a separate water management reason. |
| Lowered crawlspace/pool mechanical slab called out at -7'-0" on A2.00 but not shown in building sections or pool sections. | Documentation gap; sections may not cut through that area. No confirmed dimensional conflict. |
| Garage slab shown at -1'-0" spot elevation on Level 1 plan; garage section does not carry a separate floor datum to confirm. | Documentation gap, not a confirmed error. No dimensional conflict established. |
| Roof intersection/valley detail concentrates water into an internal gutter without an explicit secondary waterproofing strategy. | Valley/gutter protection details vary by product. No specific confirmed error without evaluating full detail dimensions and product requirements. |
| Entry hall glazing details over stone/concrete floor do not show a subsill pan or explicit drainage path at window/door base. | Design team may have addressed this in shop drawings. Not a confirmed missing component without knowing full detail intent. |
| Deck-to-foundation details show flashing at wall but no drainage or ventilation strategy for deck edge condition. | General constructability concern overlapping D6. No confirmed error. |
| Code summary (G0.11) mixes IRC and IBC concepts by citing "unlimited area per story" — an IBC concept not applicable under IRC. | Documentation error in the code summary that does not affect construction. IRC governs R-3 residential occupancy. |
| Stair drawings (A3.22) show railings and guards but provide no handrail criteria, profiles, or extension requirements. | Handrail profile and extension details are typically provided in millwork shop drawings. No confirmed non-compliant condition. |
| Removable deck panel for pool-cover access shown only in plan (A5.01); no framing, support, hardware, or removal detail in the set. | Custom condition with no construction documentation. Warrants attention in coordination but is not a drawing conflict or code violation. |
| Rain chains, collection pots, and underground leaders referenced in design intent but no overflow, pot construction, cleanout, or grade connection details shown. | Site drainage and rain chain details are landscape/civil scope. Not expected on architectural drawings. |
| Exposed above-ground pool walls specified to be finished but no drawing identifies the finish material or termination conditions. | Pool interior finish is pool subcontractor scope. Not expected on architectural construction drawings. |
| Title sheet (G1.00) and spec cover leave key project-identification fields (owner, architect, structural engineer) blank. | Administrative placeholder fields. No construction impact. |
| Code summary (G0.11) leaves planning application number blank. | Administrative field. No construction impact. |
| Spec booklet includes placeholder text under "Plan Changes" and an incomplete drawing-set reference. | Administrative/editorial. Overlaps N20. No construction impact. |
| South stair run section shows tread depth for the east run but does not annotate tread depth for the south run. | Missing annotation for one stair run. Tread depth can be inferred from the riser count and floor-to-floor height. Not a confirmed IRC violation. |
| Wall assembly W-4 on A4.00 is titled "Interior Wall, 2×4 Wood Veneer" but WD-4 in the spec is "1×6 T&G boards." Veneer paneling and T&G boards are different materials. | Documentation clarity concern. The WD-1/WD-4 wall finish conflict in the Reading Nook is the scoreable issue (A10); this assembly label discrepancy is secondary. |
| WD-2 (Exterior Window Frame, Accoya) and WD-5 (Exterior horizontal surfaces, Thermory Ash) are defined in the spec but are not depicted as assemblies on A4.00 or A4.01. | Casing and trim materials commonly exist only in the spec without separate drawing assembly tags. Not a drawing error. |
| South porch overhang: tube steel concealed within 2×6 wood framing at 1/4":12" slope — waterproofing and flashing coordination not detailed. | Overlaps N13 (design team accepted porch steel approach). The waterproofing complexity is a judgment call; no specific drawing error confirmed. |
| Entry hall detail shows a full-height mirror panel in the window cavity requiring custom blocking; no blocking or tolerance documentation is shown. | Custom installation concern without a confirmed drawing error. Blocking requirements are resolved in shop drawings. |
| E-2 wall assembly (11½" thick) transitions to adjacent E-3/E-4 walls (8–9") with no wall thickness transition detail shown. | Wall thickness transitions are commonly left to framing contractor coordination. Not a confirmed drawing error. |
| Door schedule does not include a fire rating or self-closing hardware column. | Documentation completeness observation. The specific fire-rating and self-closing concerns are captured under E4 and E8. Absence of a column doesn't preclude the information appearing elsewhere. |
| Door schedule does not include swing direction, hinge side, or hand designation. | Standard residential practice is to read door hand from plan swing arcs. Not a drawing error. |
| Crawl space plan does not indicate access hatch size/location, sealed crawl space ventilation strategy, or dehumidification provisions. | Crawl space ventilation and dehumidification are mechanical scope. Access hatch is a minor gap in isolation. |
| L2 is skipped in the lighting fixture schedule (sequence goes L1, L3, L4…) with no explanation. | Numbering gap without confirmed error. If L2 was deleted, the gap is administrative. No specific fixture confirmed as missing. |
| Specifications call for prewiring for 6 south-facing clerestory motorized blinds, but no conduit paths or power supply locations are shown on architectural drawings. | Low-voltage prewiring is MEP/low-voltage scope. Overlaps N10. Not expected on architectural drawings. |
| Code summary states 4 bedrooms; only 3 rooms (Master 06, Second 09, Guest 17) are designated as bedrooms in the finish schedule and plans. | The egress concern for potential sleeping rooms is captured under E3. Not an independent construction error. |
| Code summary lists "Tub: 1" in fixture count; specs identify two tubs (Toto air bath in Master Bath 07 and Signature Hardware soaking tub in Bathroom 11). | Minor fixture count discrepancy in the code summary. Does not affect construction directly. |
| Specs spell the hose bib manufacturer as "Aqua Hydrants"; elevations annotate it as "AQUOR HOUSE HYDRANT V2+." | Administrative misspelling; the product is clearly identifiable from both references. No construction impact. |
| Clopay garage door (15-1) is specified in specs with integral glazing panels ("Long Panel Windows"); door schedule lists material as plain "METAL" with no glazing notation. | Hardware/glazing detail coordination. The door schedule may not replicate all product features from the spec. Not a confirmed construction error. |
| Kitchen elevation specifies SS-1 backsplash thickness as "6MM"; spec lists SS-1 backsplash thickness as "TBD." Drawing is more specific than spec. | The drawing establishes a dimension the spec explicitly defers. Unusual direction of conflict but does not create a construction problem; if anything the spec should be updated to match the drawing. |
| R-1 roof assembly (A4.01) shows the weather/air barrier layer positioned below the plywood sheathing (between plywood and TJI joists) rather than above it. | Specific layer-order concern distinct from N25 (missing underlayment). The ZIP System panel itself serves as the integrated WRB; the position of the labeled barrier layer may be a drafting convention, not a functional error. Scorer should use judgment. |
| Code summary (G0.11) lists floor construction as "0 HR" without acknowledging the ½" gypsum board requirement that exists independently of a fire rating for garage separation. | Documentation completeness concern about the code summary table. The underlying construction issues are captured under E4 and E7. |
| No guardrail height dimensioned at Level 2 stair landing or open floor edges; compliance with IRC 36" minimum cannot be confirmed from drawings alone. | Observation that compliance is unverifiable, not a confirmed violation. No specific below-minimum condition identified. Different from E2, which is a confirmed 26" reading. |
| Base exterior detail (A4.11/5) shows transition from cladding to CMU foundation; the detail shows a weather barrier with wood offset from CMU block, and an insect screen plus metal flashing provides a drainage gap and air vent. Flagging this as lacking a capillary break is a misread. | The detail does address the transition condition. See also N24 for below-grade CMU waterproofing. |
| Notation system inconsistent across the drawing set: tags such as "W1/E1" appear in plan notes while assemblies are formally designated "W-1/E-1" on A4.00. | Minor drafting convention inconsistency. Context makes assembly identification clear; no confirmed misidentification. |
| Three distinct roof pitches (3"/12", 2"/12", 1/4"/12") meet at ridges and valleys with no ridge or valley elevations dimensioned on the roof plan. | Multi-slope roof documentation observation. No specific numerical error confirmed. General coordination concern, not a benchmark-level architectural error. |
| Typical wall section labels ceiling height as "VARIES" without providing a minimum, maximum, or reference for where ceiling heights are established. | Ceiling heights are expected to be read from building sections. "VARIES" is a recognized documentation approach. |

---

## Known Incorrect Findings Reference

Items models commonly flag that are factually wrong. Score **-1** per incorrect finding if the model presents the conclusion with confidence. Tentative or hedged flags may be scored as neutral. Entries are not numbered; this list grows over time.

**General note:** Dimension strings other than those specifically called out as benchmark issues are likely correct. Do not penalize a model for not flagging a dimension that is not on the answer key.

| Incorrect Finding | Why It Is Wrong |
|------------------|-----------------|
| I1: Room 10 is inconsistently named "Reading" vs "Reading Nook" across plans. | Both plans use "Reading Nook" — the word "Nook" is small and difficult to read at reduced scale, but the name is consistent. |
| I2: "HERO code" reference in specs is an unknown or unclear standard. | HERO is a real North Carolina power company (Duke Energy Progress) residential rebate program. It is a local incentive program, not a building code. |
| I5: Low-slope roof section (1/4"/12") has no detail showing how it is constructed. | Detail 5/A4.13 shows this condition. The claim that it is undetailed is incorrect. |
| I6: Pool deck 36" cable railing is below the 42" IRC pool barrier requirement. | The 36" cable railing appears only in deck sections away from the pool enclosure, not at the pool barrier itself. The pool barrier is separately specified at 48". |
| I7: Sheet index lists sheet A3.02 twice (for both North/South Elevations and Partial Elevations). | The sheet index does not list A3.02 twice. Other sheet list errors are intentional benchmark issues, but this specific claim is a misread. |
| I8: Stair geometry is impossible or non-compliant (e.g., 8 risers or 10 risers for a 10'-0" floor-to-floor height). | The stair has 18 total risers across two runs (10 east + 8 south), yielding approximately 6-11/16" per riser — compliant with IRC maximum of 7-3/4". Models misreading a single run as the full stair count are incorrect. |
| Building length discrepancy between full plan and enlarged plan: 30'-2½" + 31'-7½" = 62'-0" vs. enlarged plan. | 30'-2½" + 31'-7½" = 61'-10" (not 62'-0"). This equals the enlarged plan total of 30'-10" + 31'-0" = 61'-10". No dimensional conflict exists; the model made an arithmetic error. |
| Attic (Room 20) shown on Level 2 plan with no attic access opening or hatch. | A door to the attic is visible on the Level 2 plan. Access exists. Note: the attic is at the same level as Level 2, which may cause models to overlook the access. |
| Entry Hall custom woodwork lacks dimensions and assembly details for construction. | Details are provided on sheet A4.10. The claim that woodwork is undetailed is incorrect. |
| Roof Assembly R-1 does not include the rigid insulation called for in specs for ceilings. | R-1 does include the rigid insulation layer. This is a misread of the assembly. |
| Floor Assembly F-6 (exterior stone) depicts thin-set mortar directly over plywood sheathing, omitting a waterproof membrane. | The thin-set mortar in F-6 is over concrete on the ground, not a wood-framed deck. Not a moisture failure concern. |
| Window Tag 3 count in schedule does not match plan locations (e.g., 6 in schedule vs. 5 on plans). | The correct count of Tag 3 windows is reflected in the schedule. The model is miscounting. |
| Window schedule specifies Marvin/Ultrex fiberglass frames while exterior details show 2x6 Accoya wood frames — material conflict. | The Accoya wood frame is the exterior casing/buck that wraps around the window unit, not the window frame itself. The detail was coordinated; no conflict exists. |
| Door 15-1 garage door listed as 18'-0" × 8'-0") — width conflicts with drawn opening geometry. | 18'-0" × 8'-0" is the correct size of this garage door. The schedule and plans are consistent. |
| Enlarged plan dimension chains don't sum to overall building dimensions — multiple ½" offsets unexplained. | Absent a specific confirmed discrepancy, dimension strings on the enlarged plans should be assumed correct. This is a general observation without a verified numerical error. |
| Foundation-to-wall thermal continuity not detailed — no clear thermal break at sill/foundation-wall interface. | Detail 6/A4.10 clearly shows a 3" thermal break at the foundation-to-wall interface. The claim that it is undetailed is incorrect. |
| Dimension strings on A2.01A at different datums (e.g., 30'-10" + 31'-0" + 10'-3½" vs. 30'-2½" + 31'-7½") are irreconcilable and need reconciliation. | These strings are measuring different structures at different datums, not the same building dimension. The strings are not in conflict; models drawing a comparison between them are misreading the plan. |
| Wall assembly E-3 or E-4 shows 2x8 studs but is dimensioned too narrow to accommodate full 2x8 framing. | E-3 and E-4 both use 2x6 studs. Only E-2 uses 2x8 studs (which is the basis of the scoreable issue C7). Flagging E-3 or E-4 as having a 2x8/dimension conflict is a misread of the assembly. |
| Crawl space plan (A2.00) and Level 1 plan (A2.01) show misaligned slab-on-grade areas or crawlspace boundaries. | The boundaries are correctly aligned. Models flagging a misalignment are misreading the dimension strings on one or both plans. |
| South Elevation (A3.02) shows a window tagged with a hex "1" under the porch, but Window Schedule on A8.01 has no Tag 1. | The apparent Tag 1 is a misread — either of the G2 missing/removed window tag, linework overlapping the tag, or a door tag being read as a window tag. No window Tag 1 should exist in the current set. |
| Door 08-1 (Master Closet) is depicted as a pocket door on enlarged plan A2.01A, but the Door Schedule lacks pocket hardware designation. | Door 08-1 is not labeled or shown as a pocket door. The plan swing arc and schedule entry are consistent. |
| Garage (Room 15) reflected ceiling plan is blank; specs require 4 interior lights in the garage. | Four garage lights are correctly shown on the reflected ceiling plan. The model is misreading the RCP. |
| North side dimension total on plan (A2.01) sums to 72'-1" while the South side sums to 72'-1½" — a ½" discrepancy on the same sheet. | The dimension strings are correct. All plan dimension strings should be assumed accurate unless specifically identified as a benchmark error. |
| Connector/entry roof slope is labeled 1/4" per foot on roof plan (A2.03) but 1/8" per foot on exterior elevations — actual pitch is undefined. | The connector/entry roof slope is correctly labeled as 2" per foot in both plan and section. The confusion likely arises from the main roofs sloping 3":12" diagonally and the porch roof sloping approximately 1/2" over its short span — neither of which matches 1/4" or 1/8". The claim of a labeling conflict is a misread. |
| Corner window jamb details (A4.13/1–4) omit head and sill waterproofing details for high-risk envelope conditions. | Head and sill waterproofing for these conditions is covered by detail 1/A4.11. The claim that the details are absent is incorrect. |
| South pool edge has no railing while three other sides have 48" cable railings; NC pool barrier ordinances require complete enclosure. | The south pool edge is intentionally unenclosed. The pool wall at the south edge extends high enough above grade that no additional guardrail is required. This is correct design. |

---

## Notes for Scorer

- **Found** = count of scoreable issues that the model identified (score > 0).
- **Score** = sum of scores for this category (using 1 / 0.5 / 0 scale).
- **Incorrect** = count of items in the Known Incorrect Findings list that the model flagged confidently. Deduct 1.0 per item.
- **Neutral Findings** = count of items the model flagged that appear on the Neutral list. No score impact.
- **Total Items Flagged** = raw count of everything the model reported, regardless of category.
- Any model finding that doesn't match a scoreable issue, neutral item, or incorrect item should be reviewed and either added to the appropriate list or counted as a general out-of-scope observation.
