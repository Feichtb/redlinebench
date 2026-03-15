# Triage — claude-sonnet-4-6_run01
**Triaged:** 2026-03-14
**Total findings in model output:** 55
(A: 13 | B: 5 | C: 8 | D: 4 | E: 6 | F: 7 | G: 12)

---

## Findings-to-Answer-Key Mapping

| Model ID | Model Finding (brief) | Answer Key Match | Notes |
|---|---|---|---|
| A-1 | Powder Room (14) assigned F-4 (carpet); conflicts with specs | **A4** | Direct match |
| A-2 | Window schedule: Marvin Ultrex vs. specs Andersen 400 | **C1** | Direct match |
| A-3 | Reading Nook (10) walls: WD-1 in schedule vs. WD-4 in section/spec | **A10** | Direct match |
| A-4 | R-2 called out on West Elevation (A3.01); not defined on A4.01 | *UNMATCHED* | See below |
| A-5 | L7 strip lighting count "2"; irreconcilable with 75 LF described in specs | *UNMATCHED* | See below |
| A-6 | Rooms 07, 11, 18 comments: "FOR SHOWER FINISHES SEE" — no destination reference | *UNMATCHED* | See below |
| A-7 | Cover sheet lists A5.11; set contains A5.20 | **G4** | Direct match |
| A-8 | Spec references sheet A8.10; no such sheet exists | **G12** | Direct match |
| A-9 | Specs prewire for 6 south-facing clerestory windows; window schedule/plans don't account for 6 clerestories | *UNMATCHED* | See below |
| A-10 | Laundry Room (12) assigned F-2 (tile thinset); specs call for SS-2 (honed limestone) | **C9** | Direct match |
| A-11 | E-1 wall tag appears on Level 1 above-grade exterior walls; E-1 is the crawl space CMU assembly | *UNMATCHED* | See below |
| A-12 | Powder Room F-4 vs. SS-2 from spec (duplicate of A-1 + C9) | **A4** + **C9** | Duplicate |
| A-13 | F-2 floor assembly in Master Bath doesn't include hydronic heating mat or tubing layer | **F3** | Direct match |
| B-1 | South stair section shows 8 risers over 10'-0" floor-to-floor → 15" riser height | **KNOWN INCORRECT (I8)** | Stair has 18 total risers (10 east + 8 south); 15" riser is a misread |
| B-2 | East stair: 10 risers at 6-11/16" don't add up to 10'-0" floor-to-floor | **KNOWN INCORRECT (I8)** | 10 × 6-11/16" ≈ 5'-7"; model is reading one run as the full stair |
| B-3 | Crawl space datum: 501'-0" on A3.02 North Elevation vs. 502'-0" on A3.10 and others | **B2** | Direct match |
| B-4 | Three distinct roof pitches; no ridge or valley elevations dimensioned | *UNMATCHED* | See below |
| B-5 | Typical wall section labels ceiling height as "VARIES" with no min/max | *UNMATCHED* | See below |
| C-1 | Marvin Ultrex vs. Andersen (duplicate of A-2) | **C1** | Duplicate |
| C-2 | WD-3 (Thermory Ash) assigned "South and West Facades"; lap siding assigned "North and West" — both on west facade | **C3** | Direct match (cladding facade location conflict) |
| C-3 | Drawings label "VENTED FIBERBOARD SOFFIT"; specs require "Hardiesoffit panels, Smooth, Primed" | **N1** (neutral) | Neutral: soffit terminology interpretation varies |
| C-4 | E-1 CMU shows ½" rigid insulation; code and spec require R10 (2" XPS) | **D2** | Direct match |
| C-5 | E-4 shows conventional plywood + 1½" rigid; spec says "R21 batts + 1" Insulated ZIP Board" | **C2** | Direct match |
| C-6 | Kitchen elevation specifies SS-1 backsplash at 6mm; spec says thickness "TBD" | *UNMATCHED* | See below |
| C-7 | R-1 roof assembly has no roofing underlayment layer | **N25** (neutral) | Neutral: ZIP panels serve as integrated weather barrier |
| C-8 | Clopay garage door has integral windows per spec; door schedule lists "METAL" with no glazing notation | *UNMATCHED* | See below |
| D-1 | E-1 CMU exterior face has only parge coat — no below-grade waterproofing membrane | **N24** (neutral) | Neutral: parge coat adequacy is a site-condition judgment call |
| D-2 | E-1 ½" rigid insulation ≈ R2.5; code requires R10 (duplicate of C-4) | **D2** | Duplicate |
| D-3 | R-1 roof assembly shows weather/air barrier layer below the plywood sheathing | *UNMATCHED* | See below |
| D-4 | Base exterior detail (A4.11/5) lacks capillary break or through-wall flashing at wood sill plate | *UNMATCHED* | See below |
| E-1 | South stair section shows 8 risers at 15" — non-compliant (duplicate of B-1) | **KNOWN INCORRECT (I8)** | Duplicate of B-1 |
| E-2 | Second Bedroom (09) has only fixed windows — no EERO compliant egress opening | **E3** | Direct match |
| E-3 | Guest Bedroom (17) on Level 2 may lack operable windows meeting IRC egress criteria | **E3** | Overlaps E3 |
| E-4 | Code summary lists floor construction as "0 HR" without acknowledging ½" gypsum garage separation requirement | *UNMATCHED* | See below |
| E-5 | No guardrail height dimensioned at Level 2 stair landing or open floor edge | *UNMATCHED* | See below |
| E-6 | South pool edge shown with no railing while other three sides have 48" cable | *UNMATCHED* | See below |
| F-1 | Reading nook bunk structure — no bearing/connection details; A8.10 missing | **G12** | G12 covers missing A8.10 reference; constructability of bunk is secondary |
| F-2 | Porch overhang tube steel — no base plate, anchor bolt, or bearing conditions shown | *UNMATCHED* | See below |
| F-3 | Solar array on roof — no mounting, flashing, attachment, or structural details | **N5** (neutral) | N5: solar panels out of scope; labeled on A3.01 elevation |
| F-4 | Corner window jamb details show no structural post at corner junction | **N22** (neutral) | N22: structural corner post coordination is structural engineering scope |
| F-5 | W-4 wall assembly adds 1¼–1½" to wall thickness not reflected in plan dimensions | *UNMATCHED* | See below |
| F-6 | Garage concrete control joints not dimensioned or coordinated with column locations | *UNMATCHED* | See below |
| F-7 | Deck structure over pool entirely deferred to absent structural drawings | **N14** (neutral) | N14: pool/deck coordination described as schematic |
| G-1 | Sheet A5.11 vs. A5.20 (duplicate of A-7) | **G4** | Duplicate |
| G-2 | Sheet A8.10 missing (duplicate of A-8) | **G12** | Duplicate |
| G-3 | "FOR SHOWER FINISHES SEE" incomplete (duplicate of A-6) | *UNMATCHED* | See below |
| G-4 | R-2 undefined (duplicate of A-4) | *UNMATCHED* | See below |
| G-5 | Hydronic heating deferred to bidder (no criteria) | **F3** | Direct match |
| G-6 | Acoustic insulation specified between rooms in spec; no wall type tags those walls | *UNMATCHED* | See below |
| G-7 | All lighting fixtures TBD | **G6** | Direct match |
| G-8 | Stair sections show 10 vs. 8 risers — conflicting (documentation framing of B-1/B-2) | **KNOWN INCORRECT (I8)** | Same as B-1/B-2; model is flagging the inconsistency of a misread stair |
| G-9 | Keynote callout numbers "2C," "3C," "7C" on enlarged plans — not in any legend | **G3** | G3 covers orphaned keynote tags; scorer should confirm these specific tags |
| G-10 | Geothermal vs. conventional HVAC unresolved | **N4** / **N17** (neutral) | Out of scope |
| G-11 | Hot water heater location not dimensioned | **N11** (neutral) | Out of scope |
| G-12 | W-3 (interior insulated wall) defined on A4.00 but not tagged on any floor plan | *UNMATCHED* | See below |

---

## UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Suggested Classification | Reasoning |
|---|---|---|---|
| 1 | R-2 roof assembly called out on West Elevation (A3.01) but not defined anywhere in A4.01 or elsewhere in the set | **POTENTIAL NEW ISSUE** | Undefined assembly tag leaves a roof area with no specified construction. Specific and verifiable. Not covered by G1 (blank tag) or any other item. Also found by Opus. |
| 2 | L7 (strip lighting) scheduled with a count of "2," irreconcilable with 75 LF of strip noted in specs across kitchen, stair handrail, and Reading Nook | **POTENTIAL NEW ISSUE** | Specific verifiable conflict between schedule quantity and spec description. Not a TBD — a stated quantity that conflicts. Also found by Opus and GPT. |
| 3 | Room Finish Schedule comments for Rooms 07, 11, 18 read "FOR SHOWER FINISHES SEE" with no sheet/detail number completing the callout | **POTENTIAL NEW ISSUE** | Specific incomplete cross-reference that leaves shower tile scope unresolvable from the finish schedule. Specific and verifiable. Found by multiple models. |
| 4 | Specs require prewiring for 6 south-facing clerestory windows (motorized blinds), but the window schedule and plans do not appear to account for 6 clerestory windows of any type | **LIKELY NEUTRAL** | Overlaps N10 (low-voltage/network MEP scope). Motorized blind prewiring is not expected on architectural drawings. The window count dimension is not independently verified here. |
| 5 | E-1 wall assembly tag appears on Level 1 above-grade exterior walls; E-1 is the crawl space CMU assembly; ambiguous whether CMU continues above grade at Level 1 | **LIKELY NEUTRAL** | Documentation clarity concern without a confirmed error. The transition between crawl space CMU and Level 1 framing may be intentional. No specific dimension conflict identified. |
| 6 | Three distinct roof pitches (3"/12", 2"/12", 1/4"/12") meeting at ridges and valleys with no ridge or valley elevations dimensioned on the roof plan | **LIKELY NEUTRAL** | Multi-slope roof documentation observation. No specific numerical error confirmed. General coordination concern but not a benchmark-level architectural error. |
| 7 | Typical wall section (A3.20/4) labels ceiling height as "VARIES" without providing a minimum, maximum, or reference for where ceiling heights are established | **LIKELY NEUTRAL** | Ceiling heights are expected to be read from building sections. "VARIES" is a recognized documentation approach. No confirmed code violation or construction conflict. |
| 8 | Kitchen elevation (A7.01/1) specifies SS-1 backsplash thickness as "6MM," but the spec lists SS-1 backsplash thickness as "TBD" — the drawing establishes a dimension the spec explicitly defers | **POTENTIAL NEW ISSUE** | Unusual direction of conflict: the drawing is more specific than the spec. The spec's TBD contradicts the drawing's explicit dimension. Specific and verifiable. |
| 9 | Clopay garage door (15-1) is specified in specs with integral glazing panels ("Long Panel Windows"), but door schedule lists material as plain "METAL" with no glazing notation | **LIKELY NEUTRAL** | Hardware/glazing coordination detail; the door schedule may not be expected to replicate all spec product features. Not a confirmed construction error. |
| 10 | R-1 roof assembly (A4.01) shows the weather/air barrier layer positioned below the plywood sheathing (between plywood and TJI joists) rather than above, creating a potential moisture trap at the sheathing | **POTENTIAL NEW ISSUE** | Specific layer-order concern in the roof assembly distinct from N25 (which covers a missing underlayment). If the WRB is below the structural sheathing, moisture infiltrating from above has no drainage path. Scorer should verify layer sequence against A4.01. |
| 11 | Base exterior detail (A4.11/5) shows transition from cladding to CMU foundation with no capillary break or through-wall flashing at the wood sill plate to prevent moisture wicking from CMU to wood framing | **LIKELY NEUTRAL** | Overlaps D6 (air barrier continuity at transitions) and N24 (CMU below-grade protection). No specific confirmed error; moisture at sill plate depends on site conditions and local practice. |
| 12 | Code summary (G0.11) lists floor construction as "0 HR" without acknowledging the ½" gypsum board requirement that exists independently of fire-rating for garage separation | **LIKELY NEUTRAL** | Documentation completeness concern about the code summary table. The underlying construction issue is already captured by E4 (garage separation not identified) and E7 (wrong gypsum type). Not a separate actionable finding. |
| 13 | No guardrail height is dimensioned at the Level 2 stair landing or open floor edges; compliance with IRC 36" minimum cannot be confirmed | **LIKELY NEUTRAL** | Observation that compliance is unverifiable, not a confirmed violation. No specific below-minimum condition identified. Different from E2 (which is a confirmed 26" reading at a deck section). |
| 14 | South pool edge is shown as open (no railing) while three other sides have 48" cable railings; NC pool barrier ordinances typically require complete enclosure | **LIKELY NEUTRAL** | Pool barrier completeness concern; E5 covers cable spacing at pool barrier. Whether the south edge is intentionally unenclosed (e.g., backed by a wall or grade condition) cannot be determined from the triage. Related to E5 but distinct — scorer should confirm if south pool edge is genuinely unenclosed. |
| 15 | Porch overhang tube steel detail (A4.13/5) lacks base plate connections, anchor bolts, or bearing conditions — structural connection absent from architectural details | **LIKELY NEUTRAL** | Structural connection details are engineering scope. N13 covers the same porch steel condition as an accepted design approach. Absence of base plate detail in the architectural set is expected. |
| 16 | W-4 wall assembly adds 1¼–1½" to wall thickness beyond what is reflected in the plan dimension notation "PLAN DIM"; this will create conflicts at door frames and trim in W-4 walls | **LIKELY NEUTRAL** | Construction coordination concern about wall dimension build-up. Not a confirmed dimensional error on the drawing; shop drawing coordination typically resolves this. |
| 17 | Garage (Room 15) concrete control joint locations shown as dashed lines on plan but are not dimensioned or coordinated with column/wall locations | **LIKELY NEUTRAL** | Concrete joint layout is typically contractor-coordinated. Not an architectural drawing error. |
| 18 | Specifications require acoustic insulation in the interior wall between Master Bedroom and Second Bedroom and in bathroom walls shared with hallway/kitchen, but no wall type in the assembly schedule designates acoustic treatment, and plans don't tag those specific walls with an acoustic wall type | **POTENTIAL NEW ISSUE** | Specific coordination gap: acoustic insulation requirement in spec is not reflected in any wall assembly type or plan tag, leaving scope undefined for the framing contractor. Verifiable from spec and A4.00. |
| 19 | W-3 (Interior Insulated Wall) is defined on A4.00 but is not visibly tagged on any interior wall on Level 1 or Level 2 floor plans; which specific walls receive this assembly is unclear | **LIKELY NEUTRAL** | Overlaps Item 18 above. Documentation gap about wall assignment; connected to the acoustic insulation issue. If Item 18 is added to the answer key, W-3 tagging absence is part of the same finding. |

---

## Notes for Scorer

**Known Incorrect flags in this response:**
- **B-1, B-2, E-1, G-8** all relate to stair geometry. The model confidently states impossible riser heights (15") for the south run, and claims the east run math doesn't reconcile to 10'-0". Both are misreads consistent with **I8**. Scorer should apply **−1 penalty** for I8 (the stair geometry claim). Note that G-8 is a documentation framing of the same misread — scorer may count as one I8 penalty or two, depending on interpretation.

**Priority items for ruling:**
- Items 1 (R-2 undefined), 2 (L7 count), 3 (FOR SHOWER FINISHES SEE), 8 (backsplash 6mm vs TBD), 10 (WRB layer order in R-1), 18 (acoustic insulation not tagged) are the strongest candidates for new answer key entries.
- Item 1 (R-2) also appears in the Opus triage.
- Items 2 and 3 appear in Opus and GPT triages as well.
