# Triage — grok-4-20-beta-0309-reasoning_run01
**Date:** 2026-03-15
**Answer key:** benchmark-answer-key.md
**Source file:** grok-4-20-beta-0309-reasoning_run01.txt

---

## Overview

Total discrete findings: 28
Matched to scoreable issue: 10
Matched to neutral finding: 3
Matched to known incorrect: 0
Unmatched: 15

---

## Full Finding Map

| Model ID | Description (brief) | Mapped To | Notes |
|---|---|---|---|
| A-1 | Both Thermory Ash (WD-3, south+west) and Hardieplank (north+west) claim west facade in spec — overlap unresolved | **C3** | Partial match. C3 is a spec-vs-drawings conflict (Thermory Ash spec'd south+west, shown south+east on elevations). Grok identifies a within-spec conflict on the west facade. Related but distinct from C3's exact framing; scorer should decide whether this is a 1.0 or 0.5. |
| A-2 | Room numbers, names, and door tags have inconsistent callout density; cross-references to A3.03/A3.21 don't clearly match enlarged plan boundaries | Unmatched | See unmatched table |
| A-3 | East facade rendered brown and west red in 3D views, but material callouts imply different cladding (wood vs. fiber cement) without consistent color coordination | Unmatched | See unmatched table |
| A-4 | Slab-on-grade areas and crawlspace boundaries do not align exactly with Level 1 walls and "deck above" notations | Unmatched | See unmatched table |
| A-5 | G0.11 lists 0 HR ratings for all assemblies; garage-to-living separation details absent from plans and wall types | **E4** | Direct match. E4: garage fire separation not explicitly identified — wall assembly, door rating, ceiling gypsum type ambiguous. |
| B-1 | Pool foundation dimensioned at 62'-0" on crawl space plan but spec describes a 60'×8' lap lane (interior dimensions) | Unmatched | See unmatched table |
| B-2 | Overall building dimensions conflict between floor plans (31'-7½", 30'-2½") and roof plan (31'-10", 29'-10", 29'-3¼") | Unmatched | See unmatched table |
| B-3 | Floor-to-floor height not explicitly dimensioned on any plan, section, or elevation | Unmatched | See unmatched table |
| B-4 | Stair opening and run dimensions on Level 1 do not match tread/riser counts or total run shown on Level 2 plan | Unmatched | See unmatched table |
| C-1 | Wall and horizontal assembly references (WD-3, Thermory Ash, Hardieplank, Accoya, Silestone) not linked by any key or tag system | Unmatched | See unmatched table |
| C-2 | Repeated "TBD", "contact [name]", and "under consideration" entries throughout spec contradict bid-set intent; no allowance values given | **G6** | Direct match. G6: extensive TBDs — lighting, appliances, and material selections left unresolved on a bid set. |
| C-3 | Energy compliance U/SHGC and R-values on G0.11 not referenced to specific assembly layers shown in drawings; compliance unconfirmable | Unmatched | See unmatched table |
| D-1 | Wall assembly (R21 batt + R6 ZIP) and ceiling (R38 batt + 3" XPS) described, but no continuous insulation at framing or air barrier continuity details at transitions, roof, or crawlspace | **D6** | Direct match. D6: air barrier continuity not detailed at transitions (foundation-wall, wall-roof, penetrations). |
| D-2 | Crawlspace vapor barrier and insulation noted in specs but foundation drain and slab transitions lack full detail for a sealed, insulated crawl condition in a humid climate | Unmatched | See unmatched table |
| D-3 | 3:12 roof slopes with standing seam and solar array; no walkability, underlayment, or thermal break details at solar attachments | Unmatched | See unmatched table |
| E-1 | G0.11 lists 0 HR for all elements; no callout for required garage separation (1/2" gypsum on garage side, 20-min door, self-closing hardware) | **E4** | Direct match. Also partially addresses E8 (self-closing hardware requirement). |
| E-2 | No emergency escape and rescue openings dimensioned or tagged for bedrooms 06, 09, 17 | **E3** | Direct match. |
| E-3 | Smoke and carbon monoxide detector locations not shown or scheduled despite specs requiring complete systems | Unmatched | See unmatched table |
| E-4 | No explicit fire-rated assembly or continuity details at garage ceiling where habitable space is above | **E7** | Direct match. E7: guest suite (Rooms 17–20) above garage requires 5/8" Type X gypsum; F-1 floor assembly specifies only standard 1/2" gypsum. |
| F-1 | Solar panels shown on 3:12 standing seam roof without attachment details, penetration coordination, or walkability provisions | Unmatched | See unmatched table |
| F-2 | Hydronic radiant floor limited to master bath; shower subfloor lowering for tile (F-3 assembly) creates coordination conflict at transitions | **F3** | Direct match. F3: hydronic heating system with F-2 thinset in master bath — coordination concern with bidder-designed system. |
| F-3 | Japanese rain chains and collection pots specified but no coordination with foundation drain or site drainage system | Neutral | Matches N7: rain chain drainage routing not shown — site/civil drainage coordination is out of scope. |
| F-4 | Multiple wall and floor penetrations (1¼" PVC, 1½" conduit) required at specific locations but no dedicated detail or coordination with wall assemblies | Neutral | Matches N10: network equipment rough-in details not on architectural drawings — MEP/low-voltage scope. |
| G-1 | Site plan A1.01 relies heavily on "VERIFY IN FIELD" for critical elements (driveway, property lines, septic, well, power) | **G9** | Direct match. G9: "verify in field" on primary building dimensions affecting setback compliance. |
| G-2 | Door and window schedule cross-references and tags on floor plans cannot be fully verified against schedule data | Unmatched | See unmatched table |
| G-3 | Numerous general notes, dimensioning standards, and spec sections carry "TBD", "by others", or outdated references throughout | **G6** | Partial match — same issue as C-2 (G6). Also partially overlaps G7 ("OPENING TBD" at Level 2 stair landing). |
| G-4 | No clear datum, floor-to-floor heights, or benchmark elevations on sections or elevations; all heights referenced to "level one" requiring site verification | Unmatched | See unmatched table |
| G-5 | "Plan Changes" section in spec references a drawing set name that is redacted/removed; no revision history or clouding of changes | Neutral | Matches N2 (specs reference a drawing set name that doesn't match the actual set title) and the broader neutral entries about spec administrative/editorial issues. |

---

## UNMATCHED FINDINGS (FOR SCORER REVIEW)

| # | Model Finding (brief) | Sheet/Spec Ref | Suggested Classification | Reasoning |
|---|---|---|---|---|
| 1 | Room numbers, names, and door tags have inconsistent callout density; cross-references (A3.03, A3.21) don't clearly match enlarged plan detail boundaries | A2.01 vs. A2.01A/B | LIKELY NEUTRAL | A general observation about plan callout density and cross-reference clarity. No specific error is identified. G5 covers one specific confirmed cross-reference error (A3.04/A3.10 mislabel); A1/A2 cover specific schedule errors. This broader documentation quality concern is not a benchmark-level error. |
| 2 | East facade rendered brown and west rendered red in 3D views, but material callouts imply different cladding systems (wood vs. fiber cement) without consistent color coordination | G1.00 3D views vs. A2.01/A3.* | LIKELY NEUTRAL | C3 covers the specific Thermory Ash vs. Hardieplank location conflict (already matched under A-1). This 3D rendering color inconsistency is a lower-impact documentation issue. 3D views are illustrative and rendering colors are not construction-controlling documents. |
| 3 | Slab-on-grade areas and crawlspace boundaries do not align exactly with Level 1 walls and "deck above" notations | A2.00 vs. A2.01 | POTENTIAL NEW ISSUE | A specific claim about plan-to-plan geometric misalignment between the crawl space plan and Level 1 plan. No benchmark item covers this specific cross-plan boundary alignment. If verifiable (crawl space boundary on A2.00 does not match the wall layout on A2.01), this represents a real coordination error affecting foundation contractor scope. Scorer should check these two sheets. |
| 4 | Pool foundation dimensioned at 62'-0" on crawl space plan, but project description specifies a 60'×8' interior lap lane | A2.00 vs. Specs p. 1 | LIKELY NEUTRAL | The 2'-0" difference is consistent with a reasonable wall thickness (1'-0" each side), making 62' the exterior dimension of a 60' interior pool. This is likely not a conflict but a confusion between interior and exterior dimensions. N14 covers pool coordination as intentional deferral. |
| 5 | Overall building dimensions conflict between floor plans (31'-7½", 30'-2½") and roof plan (31'-10", 29'-10", 29'-3¼") | A2.03 vs. A2.01/A2.02 | LIKELY NEUTRAL | Differences between floor plan and roof plan dimensions commonly reflect overhang measurement conventions (floor plan shows footprint; roof plan may include overhangs). B4 covers a specific 1" grid spacing discrepancy. The several-inch differences here may be explained by measurement reference planes rather than a true misalignment. |
| 6 | Floor-to-floor height not explicitly dimensioned on any plan, section, or elevation; all heights reference "level one" requiring site verification | Multiple plans | LIKELY NEUTRAL | B2 covers a specific datum discrepancy (crawl space datum changed from 502'-0" to 501'-0"). G9 covers "verify in field" on setback-critical dimensions. Floor-to-floor heights can typically be inferred from spot elevations and sections. This is a documentation gap, not a specific confirmed dimensional conflict. |
| 7 | Stair opening and run dimensions on Level 1 do not match tread/riser counts or total run shown on Level 2 plan | A2.01 vs. A2.02 | LIKELY NEUTRAL | B5 covers the missing stair headroom dimension. The stair is known to have 18 risers across two runs (per I8). If the model is observing that the Level 1 and Level 2 plan representations look inconsistent without asserting non-compliance, this is a documentation clarity concern rather than a confirmed dimensional error. |
| 8 | Wall and horizontal assembly references in drawings (WD-3, Thermory Ash, Hardieplank, Accoya, Silestone) not linked to spec products by any key or tag system | Specs pp. 2–4 vs. A4.00/A4.01 | LIKELY NEUTRAL | A general editorial observation about the absence of a cross-reference key. C3 covers Thermory Ash location conflict; C7 covers E-2 stud size; C8 covers SS-3 flagstone; C9 covers SS-2 limestone. The broad observation that no linking key exists is a documentation quality concern, not a specific verifiable error. |
| 9 | Energy compliance U/SHGC and R-values listed on G0.11 not referenced to specific assembly layers shown in drawings | G0.11 vs. Specs | LIKELY NEUTRAL | C5 covers the specific R-value discrepancy (R49 in spec vs. R53 in code summary and assembly). This broader observation that the code summary values aren't cross-referenced to assembly layers partially overlaps C5 but is a documentation clarity concern rather than an independent error. |
| 10 | Crawlspace vapor barrier and insulation noted in specs but foundation drain and slab transitions lack full detail for a sealed, insulated crawl condition in a humid climate | A2.00 vs. Specs | LIKELY NEUTRAL | D4 covers the double vapor barrier in E-1. D6 covers air barrier continuity at transitions (already matched under D-1). This broader building-science observation about crawl space detailing partially overlaps D6 but does not identify a specific drawing conflict. |
| 11 | 3:12 diagonal roof slopes with standing seam and solar array; no walkability, underlayment, or thermal break details at solar attachments | A2.03, Specs | LIKELY NEUTRAL | N5 clarifies that detailed solar layout is out of scope for the architectural set. N25 covers the underlayment/weather barrier question as neutral. Thermal breaks at solar attachments are structural/MEP coordination items. This is a collection of neutral concerns, not a specific benchmark error. |
| 12 | Smoke and carbon monoxide detector locations not shown or scheduled despite specs requiring complete systems | A6.01, plans | LIKELY NEUTRAL | Not covered in the answer key or neutral list. Smoke/CO detector locations are typically shown on electrical or life-safety plans, which are outside the architectural scope of this drawing set. The observation is valid but is MEP/electrical scope. |
| 13 | Solar panels shown on 3:12 standing seam roof without attachment details, penetration coordination, or walkability provisions | A2.03, Specs | LIKELY NEUTRAL | Matches N5 (detailed solar layout is out of architectural scope). Attachment, penetration, and walkability details for a solar array are structural/MEP scope items. Not a benchmark-level architectural drawing error. |
| 14 | Door and window schedule cross-references and tags on floor plans cannot be fully verified against schedule data | A8.01 vs. floor plans | LIKELY NEUTRAL | A general statement about schedule cross-reference verifiability. Specific schedule errors are captured as scoreable issues (A1–A11). This broad observation that cross-references are difficult to verify is a documentation quality concern, not a specific error. |
| 15 | No clear datum, floor-to-floor heights, or benchmark elevations on sections or elevations; all heights referenced to "level one" requiring site verification | Entire set | LIKELY NEUTRAL | B2 covers a specific datum discrepancy. G9 covers "verify in field" on setback-critical dimensions. This broader datum documentation concern overlaps both B2 and G9 but does not identify a specific confirmed error beyond what those items already capture. |
