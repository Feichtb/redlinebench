# RedlineBench — Triage Report
## claude-opus-4-7 | Run 01 | 2026-04-18

**Total findings in model output:** 85  
**Findings mapped to scoreable issues:** 23 model findings → 20 answer key issues (see scoring)  
**Incorrect findings:** 3 — B-1 (I8), A-7, E-4 (see below)  
**Neutral findings:** 52  
**Unmatched resolved as neutral:** 7  
**New real issue logged (no score impact):** 1  

---

## Incorrect Findings

| Model Finding | Why It Is Wrong | Penalty |
|---|---|---|
| B-1: "East stair: 10 EQ RISERS at 6-11/16" yields only 5'-7" total rise — a single flight cannot reach Level 2 as shown" | Stair has 18 total risers across two runs (10 east + 8 south). Model treated one run as the full stair. I8. | -1.0 |
| A-7: "Window Type 10 (7'-6" × 1'-6", count 1) is scheduled but not locatable/identifiable on any elevation or plan provided" | Window Type 10 is visible on elevation 1/A3.02. The model's claim that it cannot be found is a misread. | -1.0 |
| E-4: "No sill height dimensions or window fall-protection notes for upper-level windows (IRC R312.2)" | Level 2 window sill heights are dimensioned on 2/A3.03 and 1/A3.01. The claim that they are absent is a misread. | -1.0 |

**Total penalty: -3.0**

---

## Unmatched Findings — Scorer Dispositions

| # | Model Finding (brief) | Scorer Disposition | Notes |
|---|---|---|---|
| 1 | Room 21 "Crawlspace" not in Room Finish Schedule | **NEUTRAL** | Crawl space is not a habitable room; omission is standard practice. |
| 2 | Room 10 Reading Nook base finish listed as "-" | **NEUTRAL** | There is a built-out where a baseboard would otherwise be; absence of base is a design condition, not an error. |
| 3 | Window Type 10 not locatable on any elevation or plan | **INCORRECT** | Window Type 10 is visible on elevation 1/A3.02. Penalized above. |
| 4 | Doors 22-1 and 22-2 in schedule but no Room 22 in room schedule | **NEUTRAL** | Pool access gates are not assigned room numbers; standard practice. |
| 5 | Appliance keynotes A6/A7 on plan A2.01A not carried into enlarged laundry elevations on A7.02 | **NEW REAL ISSUE** (see below — no score impact this round) | Genuine documentation gap; logged for future consideration. |
| 6 | Level 2 floor framing boundary / extent not clearly dimensioned on A2.02 | **NEUTRAL** | Dimensions are covered on the preceding sheet; not a duplication error. |
| 7 | No sill height dimensions for upper-level windows (IRC R312.2 fall protection) | **INCORRECT** | Level 2 sill heights are dimensioned on 2/A3.03 and 1/A3.01. Penalized above. |
| 8 | Door 13-3 at 6'-0" wide single-panel — unusual width for JeldWen product line | **NEUTRAL** | This is a double door; the schedule does not differentiate swing type, which is a known documentation convention for this set. |
| 9 | Pool access gates lack code-compliant self-closing/self-latching gate hardware specification | **NEUTRAL** | Covered by E5 (pool barrier cable spacing). Gate hardware details are a secondary coordination concern. |

---

## New Real Issue Log

Issues found by a model that appear genuine but are not in the current answer key. These are logged for future rounds — they do NOT affect current scoring and require all models to be re-scored before they can become active benchmark issues.

| ID | Finding | Source | Details |
|---|---|---|---|
| NRI-1 | Appliance keynotes A6 (washer) and A7 (dryer) appear on the Level 1 plan (A2.01A) for Laundry Room 12, but the enlarged laundry elevations on A7.02 do not tag or reference these appliances — only A3/A4/A5 appear in the kitchen elevation views. A contractor reading only the elevation sheet would have no appliance coordination reference for the laundry rough-in. | claude-opus-4-7, A-9 | Scorer confirmed as a real documentation gap. Flagged by Opus 4.7 only so far. |

---

## Scoring Summary

**Scorer:** Claude Sonnet 4.6  
**Scoring date:** 2026-04-18  

| Category | Max | Score |
|---|---|---|
| A. Schedule-to-Drawing | 9 | 0 |
| B. Dimensional/Geometric | 6 | 3.0 |
| C. Spec-to-Drawing | 9 | 5.5 |
| D. Building Envelope | 6 | 3.0 |
| E. Code and Life Safety | 8 | 7.0 |
| F. Constructability | 4 | 0.5 |
| G. Completeness and Clarity | 16 | 4.0 |
| **Raw total** | **58** | **23.0** |

- Incorrect findings penalized: 3 × (-1.0) = **-3.0**
- **Net score: 20.0**
- **Percent: 34.5%**

### Notable Patterns

**Strong:** Code and Life Safety (7.0/8 = 88%) — found all E-category issues except E1 (Powder Room door at 1'-10", a seeded schedule value).

**Weak:** Schedule-to-Drawing (0/9). The model missed every seeded schedule error (carpet in powder room, wrong door material, mislabeled room numbers, wrong wall finishes). These require data comparison between schedule rows and plans — the model focused on real-world coordination issues instead.

**Incorrect findings (3):** The I8 stair misread recurs again (as in Opus 4.6, Sonnet 4.6, and most other models). Two new incorrect findings — Window Type 10 claim and Level 2 sill height claim — both stem from the model asserting that information "cannot be found" when it exists on specific sheets not checked.
