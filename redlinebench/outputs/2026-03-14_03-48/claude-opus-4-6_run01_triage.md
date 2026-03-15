# Triage — claude-opus-4-6_run01
**Triaged:** 2026-03-14
**Total findings in model output:** 48
(A: 16 | B: 3 | C: 5 | D: 3 | E: 5 | F: 5 | G: 11)

---

## Findings-to-Answer-Key Mapping

| Model ID | Model Finding (brief) | Answer Key Match | Notes |
|---|---|---|---|
| A-1 | Window schedule: Marvin Ultrex vs. specs Andersen 400 | **C1** | Direct match |
| A-2 | Powder Room F-4 (carpet); specs say SS-2 limestone, "carpet in master closet only" | **A4** + **C9** | A4 = carpet in powder room; C9 = generic F-2 vs SS-2 product |
| A-3 | Interior elevation labeled "Guest Bathroom 19" but Room 19 is Guest Closet | *UNMATCHED* | See below |
| A-4 | Door 18-2 frame "None" (frameless) vs. specs say guest shower door is "semi-framed" | *UNMATCHED* | See below |
| A-5 | Code summary R=53 vs. specs state R38+R15=R49 (spec arithmetic wrong) | **C5** | Core R-value conflict; the arithmetic note is extra detail |
| A-6 | E-1 shows ½" rigid insulation; specs/code require 2" XPS = R10 | **D2** | Direct match |
| A-7 | Code summary lists 5 hose bibs; specs say 3 | **C4** | Direct match (C4 covers count discrepancy) |
| A-8 | Code summary says 4 bedrooms but only 3 rooms designated as bedrooms | *UNMATCHED* | See below |
| A-9 | Code summary lists "Tub: 1" but specs identify 2 tubs | *UNMATCHED* | See below |
| A-10 | E-3 assembly omits weather barrier; E-2 and E-4 include one | **D1** | Direct match |
| A-11 | Sheet list says A5.11; sheet is A5.20 | **G4** | Direct match |
| A-12 | L7 strip lighting count "2" irreconcilable with 75 LF across multiple locations | *UNMATCHED* | See below |
| A-13 | Wall assembly shows 1½" rigid insulation; specs say 1" Insulated ZIP Board | **C2** | Direct match (thickness and product conflict) |
| A-14 | Room 11 wall finish "T-1" not defined anywhere | **G11** | Direct match |
| A-15 | Specs spell "Aqua Hydrants"; elevations say "AQUOR HOUSE HYDRANT V2+" | *UNMATCHED* | See below |
| A-16 | Roof assembly tag R-2 referenced on elevation; only R-1 defined on A4.01 | *UNMATCHED* | See below |
| B-1 | 1½" rigid insulation layer doesn't reconcile with wall assembly plan dimensions | **B3** | B3 = stated total doesn't match sum of layers; same dimensional conflict |
| B-2 | Parallel dimension strings on A2.01A at different datums; 30'-10"+31'-0"+10'-3½" vs. 30'-2½"+31'-7½" | *UNMATCHED* | See below |
| B-3 | South stair run tread depth not specified on stair section | *UNMATCHED* | See below |
| C-1 | Specs say single 3"/12" slope; drawings show three slopes | **C6** | Direct match |
| C-2 | Specs say epoxy garage floor; F-5 shows only concrete slab | **N3** (neutral) | Neutral: epoxy in spec, not on drawings is standard |
| C-3 | A4.00 W-4 assembly titled "Wood Veneer"; specs call WD-4 "1×6 T&G boards" | *UNMATCHED* | See below |
| C-4 | WD-2 and WD-5 defined in spec but not depicted as assemblies on A4.00/A4.01 | *UNMATCHED* | See below |
| C-5 | Specs call "R21 5.5" fiberglass batts" (2×6 framing); E-2 shows 2×8 studs | **C7** | Direct match |
| D-1 | 1/4"/12" roof slope below standing seam manufacturer minimums | **G8** | Direct match (note N8 says A4.13 detail addresses it; scorer to determine) |
| D-2 | E-1 CMU wall has vapor barriers on both sides of insulation — moisture trap | **D4** | Direct match |
| D-3 | E-3 exterior wall lacks explicit WRB in assembly description | **D1** | Overlap with A-10 — same D1 finding from a different angle |
| E-1 | F-1 specifies ½" gypsum for garage ceiling beneath Guest Bedroom 17 | **E7** | Direct match |
| E-2 | No fire-rated or self-closing door identified for garage-to-living passage | **E8** + **E4** | E8 = self-closing hardware; E4 = garage fire separation undocumented |
| E-3 | Second Bedroom (09) appears to have only fixed windows | **E3** | Direct match |
| E-4 | Powder Room door 14-1 listed at 1'-10" | **E1** | Direct match |
| E-5 | Reading Nook with bunk bed may be sleeping room but no egress opening identified | **E3** | Overlaps E3 — same sleeping-room egress concern |
| F-1 | Porch overhang: steel-in-wood framing at 1/4"/12" — waterproofing complexity | *UNMATCHED* | See below |
| F-2 | Full-height mirror panel in entry hall window cavity requires undetailed custom blocking | *UNMATCHED* | See below |
| F-3 | Hydronic heating in master bath entirely deferred to bidder with no criteria | **F3** | Direct match |
| F-4 | E-2 wall (11½" thick) transitions to adjacent E-3/E-4 (8–9"); no transition detail | *UNMATCHED* | See below |
| F-5 | Elevated deck spans 10'+ above grade; structural support not shown architecturally | *UNMATCHED* | See below |
| G-1 | Numerous TBD material selections throughout specs | **G6** | Direct match |
| G-2 | All lighting fixtures TBD | **G6** | Overlaps G6; also **G6** |
| G-3 | Door schedule lacks fire rating / self-closing hardware column | *UNMATCHED* | See below |
| G-4 | Door schedule lacks swing direction / hinge side | *UNMATCHED* | See below |
| G-5 | Crawl space plan lacks access hatch, ventilation, dehumidification provisions | *UNMATCHED* | See below |
| G-6 | RCP lacks ceiling heights, materials, soffit/bulkhead indications | *UNMATCHED* | See below |
| G-7 | HVAC system type unresolved (dual-fuel vs. geothermal) | **N4** / **N17** (neutral) | Out of scope for architectural review |
| G-8 | Room Finish Schedule lacks ceiling finish column | *UNMATCHED* | See below |
| G-9 | Network equipment not shown on any drawing | **N10** (neutral) | Out of scope |
| G-10 | L2 skipped in lighting fixture schedule with no explanation | *UNMATCHED* | See below |
| G-11 | Motorized blind prewiring for 6 south-facing clerestories not on drawings | *UNMATCHED* | See below |

---

## UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Suggested Classification | Reasoning |
|---|---|---|---|
| 1 | Interior elevation on A7.02 is labeled "Guest Bathroom 19 - South" but Room 19 is the Guest Closet; the Guest Bathroom is Room 18 | **POTENTIAL NEW ISSUE** | Specific, verifiable mislabeled interior elevation; affects which shower detail and finish reference applies. Not covered by any answer key item. |
| 2 | Door 18-2 (guest shower) frame material listed as "None" (frameless) in door schedule, but specs state the guest bathroom shower door is "semi-framed" | **POTENTIAL NEW ISSUE** | Specific schedule-vs-spec conflict on door framing type. Verifiable from schedule and spec page. Not covered by any answer key item. |
| 3 | Code summary states 4 bedrooms; only 3 rooms (Master 06, Second 09, Guest 17) are designated as bedrooms in the finish schedule and plans | **LIKELY NEUTRAL** | Observation about bedroom count classification; the egress concern for potential sleeping rooms is already captured by E3. Not an independent construction error. |
| 4 | Code summary lists "Tub: 1" in fixture count, but specs identify two tubs (Toto air bath in Master Bath 07 and Signature Hardware soaking tub in Bathroom 11) | **LIKELY NEUTRAL** | Minor fixture count discrepancy in the code summary; does not affect construction directly. Low impact. |
| 5 | L7 (strip lighting) is scheduled with a count of "2" but specs describe 75 LF of LED strip across Kitchen, stair handrail, and Reading Nook — a count of 2 fixtures is irreconcilable with a 75 LF quantity | **POTENTIAL NEW ISSUE** | Specific, verifiable discrepancy between lighting schedule quantity and spec description. Different in character from G6 (TBDs) — this is a stated quantity that conflicts, not an omission. |
| 6 | Specs spell the product "Aqua Hydrants"; elevations annotate it as "AQUOR HOUSE HYDRANT V2+" — the manufacturer name is misspelled in the specifications | **LIKELY NEUTRAL** | Administrative misspelling; the product is clearly identifiable from both references. No construction impact. |
| 7 | Roof assembly tag "R-2" is called out on at least one elevation sheet, but R-2 is not defined anywhere on the horizontal assemblies sheet A4.01, which defines only R-1 | **POTENTIAL NEW ISSUE** | Undefined assembly tag leaves a roof area with no specified construction assembly. Verifiable against A4.01 and the elevation(s). Not covered by G1 (which is about a blank tag, not an undefined tag). |
| 8 | A2.01A has parallel dimension strings at different datums — one reads 30'-10" + 31'-0" + 10'-3½" = 72'-1½"; another reads 30'-2½" + 31'-7½" — these strings need reconciliation | **LIKELY NEUTRAL** | Near the known-incorrect zone (see I-entry about 30'-2½" + 31'-7½"). No confirmed numerical error established; dimension string comparison without verification. |
| 9 | South stair run section shows tread depth for the east run but does not confirm tread depth for the south run | **LIKELY NEUTRAL** | Missing annotation for one stair run; overlaps the B5 (missing headroom dimension) area but is not the same. Tread depth can often be inferred; not a confirmed IRC violation. |
| 10 | Wall assembly W-4 on A4.00 is titled "Interior Wall, 2×4 Wood Veneer," but WD-4 is described in the specs as "1×6 T&G boards" — veneer paneling and T&G boards are different materials and methods | **LIKELY NEUTRAL** | Partially covered by A10 (which addresses the WD-1 vs WD-4 finish schedule conflict). The assembly label discrepancy is a documentation clarity issue rather than a confirmed construction error. |
| 11 | WD-2 (Exterior Window Frame, Accoya) and WD-5 (Exterior horizontal surfaces, Thermory Ash) are defined in the spec but are not depicted as assemblies on A4.00 or A4.01 | **LIKELY NEUTRAL** | Material definitions existing only in the spec without drawing assembly tags is common practice for casing and trim materials. Not a drawing error. |
| 12 | South porch overhang: tube steel concealed within 2×6 wood framing at 1/4"/12" slope — waterproofing and flashing coordination not detailed | **LIKELY NEUTRAL** | N13 covers the steel thermal bridging at this same condition as an accepted design approach. The waterproofing complexity is a judgment call; no specific drawing error identified. |
| 13 | Entry hall detail shows a full-height mirror panel in the window cavity requiring custom blocking; no blocking or tolerance documentation is shown | **LIKELY NEUTRAL** | Custom installation concern without a confirmed drawing error. Blocking requirements are commonly resolved in shop drawings. |
| 14 | E-2 wall assembly is 11½" thick (2×8 framing) where it meets adjacent E-3/E-4 walls at approximately 8–9"; no transition detail is shown | **LIKELY NEUTRAL** | Wall thickness transition is a general constructability observation. Transitions are commonly left to framing contractor coordination and shop drawings. |
| 15 | Elevated deck over pool mechanical area spans 10'+ above grade; structural support not shown architecturally; no intermediate support conditions noted | **LIKELY NEUTRAL** | N14 (pool/deck coordination described as schematic) covers this area. Structural support is structural engineering scope. |
| 16 | Door schedule does not include a fire rating or self-closing hardware column | **LIKELY NEUTRAL** | Documentation completeness observation; the absence of a column doesn't mean the information can't exist elsewhere (hardware spec, notes). The specific fire-rating and self-closing concerns are already scored under E4 and E8. |
| 17 | Door schedule does not include swing direction, hinge side, or hand designation | **LIKELY NEUTRAL** | Standard residential practice is to read door hand from plan swing arcs. Not a drawing error. |
| 18 | Crawl space plan does not indicate access hatch size/location, sealed crawl space ventilation strategy, or dehumidification provisions beyond a spec mention | **LIKELY NEUTRAL** | Crawl space ventilation is mechanical scope. Access hatch is a legitimate gap but low construction impact in isolation. Multiple items bundled together. |
| 19 | Reflected ceiling plan does not indicate ceiling heights, ceiling materials, or soffit/bulkhead locations | **LIKELY NEUTRAL** | Standard practice is to read ceiling heights from building sections; ceiling materials from finish schedule. Not a specific drawing error. |
| 20 | Room Finish Schedule does not include a ceiling finish column | **LIKELY NEUTRAL** | Ceiling finishes are typically documented via sections and interior elevations; absence of a column in the schedule is a documentation style choice, not a drawing error. |
| 21 | L2 is skipped in the lighting fixture schedule (sequence goes L1, L3, L4…) with no explanation | **LIKELY NEUTRAL** | Numbering gap without confirmed error. If L2 was deleted, the gap is administrative. No specific fixture confirmed as missing. |
| 22 | Specifications call for prewiring for 6 south-facing clerestory motorized blinds, but no motorized blind locations, conduit paths, or power supply are shown on any drawing | **LIKELY NEUTRAL** | Overlaps N10 (network/low-voltage MEP scope). Low-voltage prewiring is not typically shown on architectural drawings. |

---

## Notes for Scorer

**Priority items to rule on:**
- Items 1, 2, 5, 7 are the strongest candidates for new answer key entries — multiple models flag these and they are specific and verifiable.
- Item 7 (undefined R-2 tag) also appears in the Sonnet triage. If confirmed, it should become a new G-category issue.
- Items 1 and 2 also appear in the GPT triage (Interior Elev. mislabeled; shower door framing).

**Known incorrect flags in this response:** None identified with confidence. The model's B-2 dimension string discussion is close to a known-incorrect zone but is hedged ("need verification") so no penalty is warranted.
