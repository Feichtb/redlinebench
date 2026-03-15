# Triage — claude-sonnet-4-0_run01
**Date:** 2026-03-15
**Answer key:** benchmark-answer-key.md
**Source file:** claude-sonnet-4-0_run01.txt

---

## Overview

Total discrete findings: 22
Matched to scoreable issue: 5
Matched to neutral finding: 4
Matched to known incorrect: 1
Unmatched: 12

---

## Full Finding Map

| Model ID | Description (brief) | Mapped To | Notes |
|---|---|---|---|
| A-1 | Door 10-1 in schedule, no matching tag on any floor plan | **A1** | Direct match |
| A-2 | Master Bathroom (07) assigned F-2 but spec names "Layers Trend 12X24 Porcelain" | Unmatched | See unmatched table |
| A-3 | Door 21-1 scheduled at 5'-0"×5'-0" for crawl space access, appears oversized | Unmatched | See unmatched table |
| A-4 | Roof plan notes solar/data cable wall penetration below, but no penetration detail provided | Unmatched | See unmatched table |
| A-5 | Lighting schedule lists 12 step lights (L8) for decks, no installation detail in deck sheets | Unmatched | See unmatched table |
| B-1 | 10 risers × 12" riser height between 508'-0" and 518'-0" exceeds 7-3/4" code max | **I8** (Known Incorrect) | Stair has 18 total risers (10 east + 8 south); model counted only one run. Incorrect finding. |
| B-2 | Deck elevation callouts (-6', -3'6", -11') not clearly related to positive datum (508'-0") | Unmatched | See unmatched table |
| C-1 | Appliance schedule codes (A1–A7) not coordinated with specific model numbers in spec | Neutral | Matches neutral-list entry: "Appliance schedule (A8.01) uses location codes (A1–A7) not clearly labeled on floor plan" |
| C-2 | Generic wall callouts (WD-3) vs. specific product names in spec (Thermory Ash Cladding 1x6 C20) | Unmatched | See unmatched table |
| C-3 | R49 in ceiling spec + rigid above deck creates uncertainty about insulation location and total R-value | **C5** | Describes the same R-value discrepancy between spec (R49) and roof assembly; partial match |
| D-1 | CMU wall E-1 would perform better with exterior continuous insulation (thermal bridging concern) | Unmatched | See unmatched table |
| D-2 | Wall assembly descriptions lack vapor barrier placement details despite sealed crawl space specs | Unmatched | See unmatched table |
| E-1 | Guest bedroom (room 17) egress window sizing not clearly shown | **E3** | Direct match |
| E-2 | Garage fire separation not clearly shown; gypsum type and door 15-1 self-closing hardware absent | **E4** | Primary match; also partially addresses E8 (self-closing hardware on garage-to-house door) |
| F-1 | Porch overhang (A4.13 Detail 5) shows structural steel without connection details to wood framing | Unmatched | See unmatched table |
| F-2 | Pool deck "STONE CAP TO ALIGN WITH WOOD DECK" without construction sequence or connection detail | Unmatched | See unmatched table |
| F-3 | Wall assembly E-4 shows 2x8 studs but appears only 9" total thickness — may not accommodate framing | Unmatched | See unmatched table |
| G-1 | Multiple finish selections marked TBD in spec (siding color, soffit color, countertop thickness) | **G6** | Partial match — G6 covers TBDs broadly across lighting, appliances, and materials |
| G-2 | Hardware schedules and specs not provided for contractor pricing and installation | Neutral | Matches neutral-list entry: "Door schedule hardware types not defined or detailed — hardware by allowance is standard practice" |
| G-3 | Network equipment in spec (wall penetrations, mounting panels) not on architectural drawings | Neutral | Matches N10 (network equipment rough-in is MEP scope, out of scope for architectural review) |
| G-4 | Pool described as "Above Ground Pool (ADI)" in spec but no architectural details in drawing set | Neutral | Matches N14 (pool/deck/retaining wall coordination described as schematic — intentional deferral) |
| G-5 | Image resolution limits verification of keynote cross-references on enlarged plans | Unmatched | See unmatched table |

---

## UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Sheet/Spec Ref | Suggested Classification | Reasoning |
|---|---|---|---|---|
| 1 | Master Bathroom (07) assigned F-2 (generic tile assembly) but spec describes "Layers Trend 12X24 Porcelain" with no cross-reference to the schedule code | A8.01, Specs pp. 4–5 | LIKELY NEUTRAL | C9 covers the same pattern (spec calls specific stone products for Rooms 01, 12, 14 but schedule uses generic F-2). Master Bath (07) is not one of those rooms in the answer key. Could be an additional valid instance of C9's issue type. Scorer should verify whether the spec calls out a specific product for Room 07 that contradicts or is absent from the finish schedule. |
| 2 | Door 21-1 scheduled as 5'-0"×5'-0" for crawl space access; typical access hatches are much smaller and this appears oversized for the foundation opening | A8.01, A2.00 | LIKELY NEUTRAL | No benchmark item covers crawl space access door sizing. If door 21-1 exists in the schedule with this dimension, it may reflect an intentional design choice (e.g., mechanical access panel). Scorer should verify whether door 21-1 actually appears in the schedule. |
| 3 | Roof plan note "SOLAR AND DATA CABLES TO WALL PENETRATION BELOW" appears without a corresponding wall penetration detail in the exterior detail sheets | A2.03, A4.10–A4.13 | LIKELY NEUTRAL | Similar in character to N10 (network equipment rough-in) and N5 (solar details are out of architectural scope). Wall penetration coordination for solar and data cables is typically MEP/low-voltage scope. Not a benchmark-level error. |
| 4 | Lighting schedule lists 12 step lights (L8) for deck areas but no installation detail is provided in the deck detail sheets | A6.01, A5.01–A5.30 | LIKELY NEUTRAL | G6 covers TBD fixture selections for L3–L11 (which includes L8). This finding is about missing installation details rather than a TBD selection, which edges into MEP/electrical scope. Not a specific coordination error captured in the answer key. |
| 5 | Deck elevation callouts (-6'-0", -3'-6", -11'-0") are not clearly related to the positive building datum system (508'-0" for Level 1) | A5.01, A5.10 | LIKELY NEUTRAL | B6 covers ambiguous crawl space elevation annotations using similar negative values (-6', -7', -9'). This is the same datum-ambiguity observation applied to deck/pool sections. Scorer may credit B6 at 0.5 if the model's description is considered close enough, or treat this as an additional unscored instance of the same documentation gap. |
| 6 | Generic wall assembly callouts (WD-3) vs. specific product descriptions in spec (Thermory Ash Cladding 1x6 C20); no key linking drawing tags to spec products | A4.00, Specs pp. 2–3 | LIKELY NEUTRAL | A general editorial observation about assembly tags not being explicitly linked to spec products. C3 covers the specific location conflict for Thermory Ash (south+west in spec, south+east on drawings). This broader labeling observation is not a specific verifiable error but a documentation quality concern. |
| 7 | CMU wall E-1 would perform better with exterior continuous insulation; interior rigid insulation does not prevent thermal bridging through masonry | A4.00 | LIKELY NEUTRAL | Design feedback rather than a drawing error. D2 covers the specific inadequate insulation thickness issue (changed from 2" to 1/2", likely below R-10 code requirement). D4 covers the double vapor barrier. The thermal bridging observation is a design critique beyond the QAQC scope of this benchmark. |
| 8 | Wall assembly descriptions lack vapor barrier placement details despite spec references to sealed crawl space and air sealing requirements | A4.00, Specs p. 4 | LIKELY NEUTRAL | D6 covers air barrier continuity at transitions. D4 covers the double vapor barrier in E-1. This observation about missing vapor barrier detail in the assembly descriptions partially overlaps D6. Scorer may consider crediting D6 at 0.5 if the model's description is close enough. |
| 9 | Porch overhang at A4.13 Detail 5 shows structural steel framing without adequate connection details to the wood framing system | A4.13 | LIKELY NEUTRAL | Matches N13 (south porch concealed steel — design team reviewed and accepted this approach). Connection details for steel-to-wood frame are out of scope for this benchmark review. |
| 10 | Pool deck shows "STONE CAP TO ALIGN WITH WOOD DECK" without construction sequence or connection details between stone and wood elements | A5.20 | LIKELY NEUTRAL | Matches N14 (pool/deck/retaining wall coordination described as schematic — intentional deferral). |
| 11 | Wall assembly E-4 shows 2x8 studs with insulation but the total assembly appears only 9" thick — may not accommodate full 2x8 framing plus sheathing and insulation | A4.00 | POTENTIAL NEW ISSUE | B3 covers E-3 layer total discrepancy (stated total changed to 8", sum of layers remains 8-9/16"). C7 covers E-2 stud size conflict (2x8 drawn vs. 2x6 in spec). If E-4 similarly shows an internally inconsistent dimension (2x8 studs = 7-1/4" alone, yet total stated as 9"), this would be the same type of error as B3 applied to a different assembly. Scorer should verify E-4 layer thicknesses and stated total on A4.00 to confirm or dismiss. |
| 12 | Image resolution limits verification of some keynote cross-references on enlarged plans | A2.01A, A7.10 | LIKELY NEUTRAL | A meta-observation about review limitations, not a specific architectural finding. No score impact expected. |
