# Second same-day Opus 4.8 run

This folder is a second run of Claude Opus 4.8 from the same day as `../2026-06-07_21-33/`.

## Why two runs exist

The first run (`../2026-06-07_21-33/`) hit the 32,000 output-token cap and was truncated
**mid-sentence in its closing Summary prose**. At the time it looked incomplete, so the
model was re-run here.

On review, the 21-33 run is **findings-complete** — all seven categories (A–G) are present
and the model had finished its findings by its own choice; only the non-scoring narrative
summary was cut off. The re-run was therefore based on a false premise, though it turned out
to be useful anyway (see below).

## How this is used now

Both runs count. RedlineBench moved from a single-run-per-model design to permanent
multi-run aggregation (`redlinebench/build_data.py`) — every scored run is a dated record
that contributes to that model's mean/min/max, and neither run here is treated as
"canonical" or discarded. Per each run's `scores.json`: **21-33 → 19.5 net**, **22-02 (this
folder) → 24.5 net**, giving Opus 4.8 n=2, mean 22.0. The gap between them is genuine
run-to-run variance — exactly what the reliability heatmap on the results page is for.
