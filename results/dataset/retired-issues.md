# Retired issues — defects in the v1 answer key

These three entries in `benchmark-answer-key.md` describe something the test files
do not actually contain, so a model could not have found them.

They are **not** deleted from the answer key. The key stays as published; this
file is the overlay that says which of its 58 entries are void, and it is the
single list both the deck and any rescoring pass read.

Found 2026-08-10, while framing a drawing view for every issue for the Oregon
Design Conference deck — the first time each entry was checked against the
drawings one at a time rather than in aggregate.

<!-- retired:begin -->
| # | Answer key says | What the test files actually contain |
|---|---|---|
| A9 | Room 15 (Garage) assigned F-4 (carpet); should be F-5 | The room finish schedule on A8.01 already reads **F-5** for the Garage. The seeded error is not in the file. |
| G5 | Plans cross-reference a building section labelled A3.04, which does not exist | The string `A3.04` appears nowhere in the drawing set. The callout bubbles read A3.10, which is a sheet that does exist. |
| G7 | "OPENING TBD" at the Level 2 stair landing on A2.01B | `TBD` appears nowhere on A2.01B. In the whole drawing set it appears only on A6.01, which is issue G6. |
<!-- retired:end -->

## What this costs

Three of the four were caught by **no model, in any run**: A9, G5, G7 scored 0.00
across all sixteen models. Dropping them can only raise percentages, and it
raises every model's by the same denominator change.

## Corrections — entries reworded rather than retired

### G16 — reworded 2026-08-10

G16 is not like the other three, and it is the one row here that probably should
not be a row at all.

**The underlying issue is real; the answer key states it wrongly.** Wall tags on
the plan sheets are: A2.01A has W-2 twice and W-4 twice and no W-3; A2.01B has
W-3 twice; A2.01 and A2.02 have none. So W-3 *is* assigned — but not on A2.01A,
which is the sheet carrying the Master Bedroom 06 / Second Bedroom 09 party wall
the specification wants acoustically insulated. The real defect is "the bedroom
party wall on A2.01A is not tagged W-3", not "W-3 is never assigned".

**The wrong wording changed the scoring.** Two of the three models that scored on
G16 did not say the same thing:

- **Claude Sonnet 4.6** (scored 1.0): "W-3 ... is defined on A4.00 but is not
  visibly tagged on any interior wall on the Level 1 or Level 2 floor plans."
  That is false — it is tagged twice on A2.01B. Under the rubric a factually
  wrong claim about the documents is an incorrect finding at −1.0, so this run
  was credited +1.0 for something that should have cost it a point, a 2.0 swing.
- **Claude Opus 4.8** (scored 0.67): "Spec requires acoustic-insulated walls
  between Master/Second bedrooms ... but those partitions are not clearly tagged
  as the insulated type (W-3)." That is correct, and is arguably a full catch of
  the real issue rather than a partial one.
- **GPT-5.5** (scored 0.33, one run in three) has not been read yet.

**Resolution.** G16 stays in the benchmark; its answer-key row was rewritten to
the issue the documents actually contain — the spec-named walls are not tagged
W-3 — and the row now says explicitly that claiming W-3 is untagged everywhere is
an incorrect finding rather than a catch. The rescoring pass therefore has to
re-judge the four responses above against the new wording, not just drop a
column. All four were re-read; the verdicts are in the table below.

## What the rescore did — 2026-08-10

1. Dropped the three retired entries from the denominator: **58 → 55**, and the
   per-category maxima with them (A 9→8, G 16→14). None of the three had ever
   scored above zero for any model in any run, so no raw score moved because of
   them.
2. Re-judged the four runs that had scored G16, and recomputed every model's
   totals from the per-issue scores. No model was re-run.
3. Kept the answer key as **v1**. The audit removes entries that were never
   answerable and corrects one that was misworded rather than adding an issue,
   so it was applied to the published numbers instead of forked into a v2.

Two numbers moved for reasons worth knowing:

- **Claude Sonnet 4.6: 14.0 → 12.0.** Its G16 finding is now an incorrect
  finding, which costs it the point and adds the penalty.
- **Claude Opus 4.8: 23.0 → 22.67**, and this one is not the audit's doing. Run
  `2026-07-05_16-27` recorded `raw = 26.0` while its own per-issue scores sum to
  25.0, so the leaderboard and the heatmap had disagreed about that run ever
  since it was published. Recomputing from the per-issue scores — which any
  rescore has to do — settles it at 25.0. That run's own notes also say it was
  never approved by a human scorer; that is still outstanding.

The deck stops showing slides for these three as soon as they are listed here,
and since the rescore its charts plot the same 55-issue numbers the site does.

## Re-judged runs

Four runs scored G16 before it was reworded. Each was re-read against the new
wording on 2026-08-10. Three named the specific partitions the specification
calls out and stand as catches; one asserted the thing that is not true.

<!-- rescored:begin -->

| Run | Model | Issue | Was | Now | Counts as | Why |
|---|---|---|---|---|---|---|
| 2026-03-14_03-48 | claude-sonnet-4-6 | G16 | 1.0 | 0 | incorrect finding | Claimed W-3 is "not visibly tagged on any interior wall on the Level 1 or Level 2 floor plans". It is tagged twice on A2.01B, so this misreads the drawings. |
| 2026-06-07_22-02 | claude-opus-4-8 | G16 | 1.0 | 1.0 | catch | Named the Master/Second bedroom partitions specifically, not the whole set. |
| 2026-07-05_16-27 | claude-opus-4-8 | G16 | 1.0 | 1.0 | catch | Named the bedroom partitions and the 2nd-bath walls at hallway and kitchen. |
| 2026-07-05_17-17 | gpt-5.5 | G16 | 1.0 | 1.0 | catch | Same, citing spec p.4 and A2.01A. |
| 2026-03-14_03-48 | claude-opus-4-6 | B3 | 0.5 | 1.0 | catch | Its B-1 states the plan dimensions only work if the rigid insulation is about 1" rather than 1-1/2". That is exactly the defect, now that B3 is understood as a callout mismatch rather than a layer-sum mismatch. |
| 2026-09-07_23-55 | claude-fable-5-1 | B3 | 0.5 | 1.0 | catch | Attributed the E-3/E-4 discrepancy to the "1-1/2 RIGID INSULATION" callout. The 2026-09-08 check confirms the callout is the culprit, so this is a full catch, not a wrong-culprit partial. |
| 2026-09-07_23-42 | claude-fable-5-1 | B5 | 0.5 | 0 | not a catch | Scored on Powder Room ceiling height beneath the stair soffit, which is N31 — a separate observation from the missing stair headroom dimension on 2/A3.22. |
| 2026-09-08_00-10 | claude-fable-5-1 | B5 | 0.5 | 0 | not a catch | Same: headroom at the Powder Room fixture, not stair headroom. |
| 2026-09-07_23-55 | claude-fable-5-1 | G1 | 0.5 | 0 | not a catch | Observed only that R-2 is undefined, which is G14 and already scored 1.0 there. Under the corrected G1 row that is not a blank-tag finding. |
| 2026-09-08_00-05 | gpt-6-astra | G1 | 0.5 | 0 | not a catch | Same — R-2-undefined only, no blank tag observed. |
| 2026-09-08_00-10 | claude-fable-5-1 | G1 | 0.5 | 0 | not a catch | Same — R-2-undefined only, no blank tag observed. |
| 2026-09-08_00-24 | gpt-6-astra | G1 | 0.5 | 0 | not a catch | Same — R-2-undefined only, no blank tag observed. |
| 2026-09-08_00-25 | gpt-6-astra | G1 | 0.5 | 0 | not a catch | Same — R-2-undefined only, no blank tag observed. |

<!-- rescored:end -->

## Second audit — 2026-09-08

Fifteen open scoring questions raised by the Fable 5.1 and GPT-6 Astra scoring
round were checked against the drawings one at a time. The answer key was
corrected in place; no scoreable issue was added or removed, so the key stays
**v1** and the denominator stays **55**.

What changed in the key:

| Row | Change |
|---|---|
| B3 | The drawn layers on E-3/E-4 *do* sum to 8". What does not reconcile is the "1-1/2 RIGID INSULATION" callout against the 1" drawn layer. Either framing now scores as a full catch. |
| B4 | The seeded grid dimension is between **C and D**, not D–E as published. The resulting 1" north/south chain difference on A2.01 is a real symptom and a valid partial route to B4. |
| B5 | Scoped to the missing **stair** headroom dimension on 2/A3.22. Powder Room ceiling height is a separate observation (N31). |
| E2 | The 26" section label and the conflicting 36" plan reading are both present, so either framing is a full catch. |
| E8 | Door **13-2** (garage to office) is also a garage-to-house door with no closer; naming either 16-1 or 13-2 is a catch. 13-1 is office-to-hallway and is not a garage door. |
| G1 | **G1 and G14 are separate defects.** The blank tag appears in 1/A3.01, 1/A3.02 and 1/A3.03; the R-2 callout appears on 2/A3.01. The old row said either observation was valid for both, which paid one finding into two scoreable issues. |
| G14 | Notes where the R-2 callout actually appears, and that it scores separately from G1. |
| G16 | Many interior walls are untagged by design (N32), so the defect is the unassigned assembly at the walls the specification names — not untagged walls as such. |
| I8 | Narrowed to *misreading one run as the whole stair*. The 18 × 6-11/16" = 120-3/8" arithmetic observation is neutral (N33). |
| A2.01 chain entry | **Voided.** See below. |
| N31–N37 | Seven observations confirmed against the drawings as real-but-unseeded, intentional, or unresolvable from the drawing alone. None carries score. |

Two of the new neutral rows are real errors that are simply not in this key —
the E-2 rigid insulation callout (N35) and the duplicated A3 appliance tag on the
range hood (N37). Both are candidates for a future key version; neither can be
added to v1 without forcing a full rescore of every model.

## Voided penalties

One Known Incorrect Findings entry turned out to describe a real defect. The
A2.01 north and south dimension chains genuinely differ, because the seeded B4
grid change propagates into one chain and not the other — so every model
penalized for flagging it was penalized for being right.

The same 2026-09-08 pass confirmed that the stair riser arithmetic is not the I8
misread: 18 risers at 6-11/16" really does leave 3/8" against a 120" floor-to-
floor, and that gets resolved in the field. Two runs had been penalized under I8
for making only that observation, having read the stair correctly.

Removing a penalty is the mirror of the `rescored` table's ability to add one,
and `build_data.py` reads this table the same way.

<!-- voided-penalties:begin -->

| Run | Model | Ref | Why |
|---|---|---|---|
| 2026-03-14_03-48 | gemini-3.1-pro-preview | I (72' dimensions) | Flagged the A2.01 north/south chain difference. The chains do differ; the voided key entry claimed they do not. |
| 2026-03-14_13-54 | gpt-5.4-pro | I8 | Read the stair correctly as 10 + 8 risers at 6-11/16" and only observed that it does not cleanly reconcile to 10'-0". That is N33, not the I8 misread — and it was hedged at Moderate confidence besides. |
| 2026-03-15_15-32 | gpt-4o | I8 | Claimed only that riser heights do not sum to the floor-to-floor height, which is true. No single-run misread was made. |

<!-- voided-penalties:end -->

Applied by `redlinebench/build_data.py` at aggregation time. The per-run
`scores.json` files are permanent records and are not rewritten — same rule the
legacy model-ID aliases follow.
