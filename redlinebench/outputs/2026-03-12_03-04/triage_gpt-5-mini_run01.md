# Triage: gpt-5-mini_run01
**Run folder:** 2026-03-12_03-04
**Answer key version:** v2 (benchmark-answer-key.md)
**Step:** 1 — Triage only. Do not score yet.

---

## SECTION 1: MATCHED FINDINGS

The model uses pipe-delimited format: [ID] | [Location] | [Description] | [Certainty]. Model uses its own A–G category letters with dashes.

| Model Finding (brief) | Answer Key Match | Notes |
|---|---|---|
| A-2: G0.11 lists "CEILING R = 53" while insulation notes calculate R38 + R15 = R49 — ceiling R-value conflicts within documents | C5 | Found clearly |
| A-3: Window schedule (Ultrex-Marvin) conflicts with spec text (Andersen 400 Series) | C1 | Found clearly. Duplicate of C-1 below — count once. |
| A-7: Interior elevation WD-4 wood finish in Entry Hall not matched by Room Finish Schedule codes/locations | A5 | Partial — A5 is about the Entry Hall east wall finish being changed from WD-1 to P-1 in the schedule while elevations/details still show wood. Model's finding captures the same elevation-vs-schedule conflict; not worded with the specific WD-1→P-1 change. |
| C-1: Spec says Andersen 400 Series; window schedule says Ultrex-Marvin | C1 | Found clearly. Same as A-3 — count once. |
| C-2: G0.11 ceiling R=53 vs assembled detail R49 | C5 | Found clearly. Same as A-2 — count once. |
| C-3: Spec requires complete air barrier but window/door details don't show continuous transitions or terminations | D6 | Found, vague — model describes the spec requirement and the gap, but does not identify the specific transition locations (foundation-wall, wall-roof) flagged in the answer key. Score as partial. |
| E-1: Garage fire separation details (gypsum type, ceiling separation, self-closing door, fire label) not specified | E4, E7, E8 | Found clearly — this single finding captures E4 (fire separation not identified), E7 (Type X ceiling above garage), and E8 (self-closing door hardware). Strong finding. |
| E-2: Egress criteria for sleeping rooms not documented (sill height, clear opening sizes) | E3 | Found clearly |
| E-3: Cable rail system specified but no detail for toprail, deflection, infill termination, or cable tension criteria | E2 | Partial — E2 is specifically about the 26" railing height on the south deck section (below 36" minimum). Model's finding is about missing engineering/detail for the cable system rather than the specific height violation. Score as partial. |
| E-4: Stair headroom not dimensioned on stair sections | B5 | Found clearly |
| G-2: Numerous TBD and owner-option items throughout spec and schedules | G6 | Found clearly |
| G-4: Door hardware sets and required functions not provided; several doors missing hardware specification | E8 | Partial — E8 is specifically about door 16-1 (garage to hallway) requiring self-closing hardware. Model's finding is broader (all door hardware), which encompasses E8 but does not isolate the specific garage door. Score as partial; E8 also captured in E-1 above. |
| G-5: Hydronic radiant in-floor system specified for master bath only, but no plan, manifold, or control detail provided | F3 | Found clearly |
| G-7: Appliance list incomplete; lacks model numbers for several required devices | G6 | Partial — G6 covers extensive TBDs broadly; appliance TBDs are specifically mentioned in G6. Same G6 match as G-2, count once. |

---

## SECTION 2: UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Suggested Classification | Reasoning |
|---|---|---|---|
| 1 | A-1: Window schedule lists Ultrex/Marvin frames (fiberglass) while exterior window details call out 2x6 Accoya wood frames (WD-2) — product/material conflict for window frames | LIKELY NEUTRAL | The answer key C1 is about spec-to-schedule manufacturer conflict (Andersen vs Marvin). This finding is about a schedule-to-detail conflict (fiberglass Marvin frame vs Accoya wood frame shown in details). This could be a real coordination issue, but the Accoya frame in the detail may be the exterior casing/buck, not the window frame itself. Needs scorer verification. Lean neutral. |
| 2 | A-4: Door 15-1 listed as 18'-0" × 8'-0" garage door; model suggests width conflicts with drawn opening geometry | LIKELY NEUTRAL | The answer key does not flag a dimensional issue with door 15-1 specifically. An 18'-0" garage door is a wide but not impossible residential door. Without a confirmed dimensional mismatch shown on the plans, this appears to be a speculation. Likely neutral or unverifiable. |
| 3 | A-5: Several door tags appear on plans but plan elevations don't clearly show door types/relites — missing elevation references for door type/relite disposition | LIKELY NEUTRAL | Door type/relite references between plans and schedule is a drafting coordination issue. The answer key items A1 and A2 address specific door discrepancies (wrong door number on plan, width changed) — this broader observation about missing relite references is not a specific confirmed error. |
| 4 | A-6: Deck railing shows 36" and 48" cable railing at various locations without a single coordinated elevation showing which height applies where | LIKELY NEUTRAL | The answer key E2 is about the specific 26" railing on the south deck section being below code minimum. The model's finding about coordination between 36" and 48" railings at different locations is a different concern — the 36" and 48" heights are code-compliant in their respective contexts (deck rail vs. pool barrier). Model does not appear to have found the 26" violation itself. |
| 5 | A-8: Lighting fixture counts in lighting schedule (e.g., L1=70, L10=12) are not verifiable against the reflected ceiling plan at drawing scale | LIKELY NEUTRAL | Inability to count fixture instances on a reduced-scale plan is a general legibility observation, not a confirmed numerical discrepancy. No specific count error is identified. |
| 6 | A-9: Wall assembly callout tags used on plans but exterior detail references don't consistently annotate the same insulation thicknesses or air barrier continuity | LIKELY NEUTRAL | This is a documentation quality observation that overlaps with C2 (insulation thickness conflict). The model is not identifying a specific new discrepancy beyond what C2 and D6 already cover. |
| 7 | A-10: Roof plan indicates solar array and plumbing vents but PV penetration details are not cross-referenced to a single detail | LIKELY NEUTRAL | N5 addresses solar panel scope: "Solar panels labeled on elevation 1/A3.01; detailed solar layout is out of scope for the architectural set." PV penetration detailing is also largely electrical/MEP scope. |
| 8 | B-1: Stair riser/tread arithmetic inconsistent — plans show 10'-0" floor-to-floor but stair callouts indicate "10 EQ RISERS 11"" which doesn't add up | LIKELY INCORRECT | This matches I8 in the known incorrect list: "Stair has 18 total risers across two runs (10 east + 8 south), yielding approximately 6-11/16" per riser — compliant with IRC maximum of 7-3/4". Models misreading a single run as the full stair count are incorrect." Model appears to be reading a single run (10 risers) as the full stair, which is a misread. Recommend -1 penalty if stated with confidence (which "High" certainty rating suggests). |
| 9 | B-2: Enlarged plan dimension chains don't sum to building overall dimensions — multiple ½" offsets appear without explanation | LIKELY NEUTRAL | This overlaps with B1 (office length 1" discrepancy) and B4 (grid spacing 1" discrepancy), but the model is describing it as a general pattern of dimensional inconsistencies rather than identifying specific benchmark discrepancies. Score as neutral unless the scorer determines specific stated numbers match B1/B4. |
| 10 | B-3: Enlarged pool/deck plan shows removable deck for pool cover access but no scaled dimensions or structural detail for removable panels | LIKELY NEUTRAL | N14: "Pool/deck/retaining wall coordination described as schematic. Pool coordination notes are intentional; structural scope is separate." Pool deck removable panel details are structural/pool contractor scope. |
| 11 | B-4: Roof slope callouts and T.O.F. heights in partial elevations and details are inconsistent across sections | LIKELY NEUTRAL | The answer key B2 covers crawl space datum inconsistency (a specific numerical datum error). Model's finding about roof slope heights being inconsistent across sections is a broader documentation quality observation without a specific numerical error identified. |
| 12 | C-4: Spec requires two Rinnai tankless water heaters but no plumbing riser diagrams or plan-level drawings in the set | LIKELY NEUTRAL | N11: "Tankless water heater locations not documented on architectural drawings. Hot water supply noted in crawl space; routing and equipment location are MEP scope." Out of scope. |
| 13 | C-5: Spec contemplates smart/solar-ready panels and battery backup but electrical drawings don't include PV/backup one-line, battery location plan, or panel schedule | LIKELY NEUTRAL | N5 (solar panels out of scope) and N18 (smart electrical panel decision unresolved). Both are neutral. |
| 14 | D-1: Foundation-to-wall thermal continuity not detailed — no clear thermal break at sill/foundation-wall interface | LIKELY NEUTRAL | D6 covers air barrier continuity at transitions broadly. Foundation-to-wall thermal break detailing is a building science concern but typically MEP/structural coordination. Not a specific benchmark issue. |
| 15 | D-2: Window head and sill details show flashing but don't show exterior air barrier wrapping into jamb/head nodes | LIKELY NEUTRAL | Partially overlaps with D6 (air barrier continuity) and D3 (flashing membrane reversed). The model is not identifying the specific D3 flashing reversal error but is making a general air barrier continuity observation at windows. Consider 0.5 match to D6 if scorer finds it compelling, but lean neutral. |
| 16 | D-3: Drawings call for vented fiberboard soffit and insect screen while spec requires sealed/insulated crawl space — no detail explaining how vented soffit isolates from sealed crawl | LIKELY NEUTRAL | The soffit ventilation vs. sealed crawl space interaction is a building science observation. The answer key does not flag this specific interface as a benchmark issue. The soffit vents and crawl space may not be directly connected depending on construction details. Neutral unless scorer can confirm a direct conflict. |
| 17 | D-4: Low-slope standing seam roof — documents state "ensure roof is walkable" but no walkway detail, loading, or manufacturer-approved walkway note | LIKELY NEUTRAL | G8 in the answer key flags the 1/4":12" slope as being below typical standing seam manufacturer minimums. The walkability concern is adjacent but different — roof walkways are typically a maintenance coordination item rather than an architectural drawing error. |
| 18 | E-5: Emergency egress lighting or path-of-travel lighting for exterior stairs and long driveway not shown | LIKELY NEUTRAL | Exterior egress lighting requirements for single-family residential are limited. Exterior lighting layout is also primarily electrical/MEP scope. Not a benchmark issue. |
| 19 | F-1: Accoya frame + furring + 1½" rigid insulation + fiberboard cladding build-up creates constructability issues and potential conflict with window manufacturer installation depth | LIKELY NEUTRAL | This is a legitimate constructability observation about the window installation depth in a thick wall assembly, but it depends on specific manufacturer requirements that aren't in the drawing set. Hard to verify as a clear error. Neutral pending manufacturer requirements. |
| 20 | F-2: Network equipment penetration details call for 1¼" PVC conduit but no firestop or separation details for penetrations through building envelope or stem wall | LIKELY NEUTRAL | N10: "Network equipment rough-in details not on architectural drawings. Out of scope; MEP/low-voltage coordination." |
| 21 | F-3: Removable deck/panel for pool cover access lacks fastening detail, tolerance, and sequence | LIKELY NEUTRAL | Same as B-3 reasoning. N14 covers pool/deck coordination as intentionally schematic. |
| 22 | F-4: Subfloor noted to be lowered at tile shower transitions (F-3) but no dimension or detail to control finished floor elevation between adjacent rooms and stairs | LIKELY NEUTRAL | Transition floor elevation coordination at tile shower thresholds is a standard construction coordination item. Not a specific benchmark issue. |
| 23 | G-1: Owner and Architect fields at top of specification are blank | LIKELY NEUTRAL | N20: "Specification narrative includes owner-instructional language rather than enforceable requirements. Spec format is intentionally informal/narrative for this project." Blank administrative fields in an informal narrative spec are a minor issue. |
| 24 | G-3: Reflected ceiling plan notes "see enlarged plans for casement and floor lighting" but enlarged plans don't consistently show fixture mounting heights or blocking | LIKELY NEUTRAL | Fixture mounting heights and blocking requirements are typically coordinated between architectural and MEP/lighting drawings. This is a documentation gap but not a specific benchmark error. |
| 25 | G-6: Driveway specified as 10' wide, 420' long with granite block edging but no typical section, subbase, or drainage/culvert detail | LIKELY NEUTRAL | N7: "Rain chain drainage routing not shown on drawings. Site/civil drainage coordination is out of scope." Driveway civil details are out of scope for an architectural review. |
| 26 | G-8: Solar array mounting and PV cabling at roof/garage intersection — no wall penetration/flash detail or structural support detail for conduits and combiner box | LIKELY NEUTRAL | N5: "Solar panels labeled on elevation 1/A3.01; detailed solar layout is out of scope for the architectural set." PV penetration details are electrical/MEP scope. |

---

## SECTION 3: COUNTS

| Metric | Count |
|---|---|
| Total model findings | 40 |
| Matched to scoreable issues | 9 distinct answer key items: A5 (partial), B5, C1, C5, D6 (partial), E2 (partial), E3, E4/E7/E8 (via E-1), F3, G6 |
| Matched to neutral list | 7 findings → N5 (×2), N10, N11, N14, N18, N20 |
| Matched to incorrect list | 1 (B-1 → I8: stair geometry misread) |
| Unmatched (for scorer review) | 26 items in Section 2 |

**Notable duplicates within model output:** A-2 and C-2 are the same C5 finding. A-3 and C-1 are the same C1 finding. G-2 and G-7 are both G6. These do not add separate scoreable matches.

**Notable misses (answer key items not found at all):** A1, A2, A3, A4, A6, A9, A10, B1, B2, B3, B4, B6, C2, C3, C4, C6, C7, C8, C9, D1, D2, D3, D4, D5, E1, E5, E6, A7/G, G1, G2, G3, G4, G5, G7, G8, G9, G10, F1, F2, F6.

---

## Notes for Scorer

1. **B-1 (stair riser arithmetic)** — Strong match to I8 (known incorrect). The model states "High" certainty and presents stair geometry as inconsistent. Per the answer key, the stair has 18 total risers across two runs; misreading one run as the full stair is a known incorrect finding. Recommend -1 penalty.
2. **E-1 (garage fire separation)** — This single finding plausibly covers three answer key items: E4 (fire separation not identified), E7 (Type X gypsum ceiling above garage), and E8 (self-closing door hardware). The scorer should decide whether to award points for each item separately based on how specifically each is described, or treat as one finding covering all three.
3. **A-1 (window frame material conflict)** — If the scorer can confirm that window details show Accoya wood as the structural frame (not just casing) while the schedule specifies Marvin fiberglass units, this may warrant a new A-category issue. Alternatively, if Accoya is the exterior casing and Marvin is the window unit, there is no conflict. Scorer should verify.
4. **D-2 (window air barrier)** — If scorer finds this observation compelling enough to partially match D6, a 0.5 score for D6 is defensible. The finding is vague but directionally correct about air barrier continuity at window openings.
5. **G-4 (door hardware broadly)** — E8 is already captured by E-1. G-4 is a broader finding about all door hardware. The scorer may choose to score E8 from E-1 and treat G-4 as neutral/redundant.
