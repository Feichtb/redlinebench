# Secondary run — NOT the published Claude Opus 4.8 result

This folder is a **second** run of Claude Opus 4.8 from the same day. It is retained as
research data only and is **not** the canonical entry for this model on the results page.

## Why two runs exist

The first run (`../2026-06-07_21-33/`) hit the 32,000 output-token cap and was truncated
**mid-sentence in its closing Summary prose**. At the time it looked incomplete, so the
model was re-run here.

On review, the 21-33 run is **findings-complete** — all seven categories (A–G) are present
and the model had finished its findings by its own choice; only the non-scoring narrative
summary was cut off. The re-run was therefore based on a false premise.

## Which run is published

**`2026-06-07_21-33` is the canonical, published Opus 4.8 run.** Per the benchmark's
single-run-per-model design, every model is represented by its first complete pass. Using
21-33 keeps Opus 4.8 on the same single-shot terms as the other models and avoids selecting
the better of two attempts.

For the record, the two runs scored: **21-33 → 18.5 net**, **22-02 (this folder) → 24.5 net**.
The gap is genuine run-to-run variance, not a truncation artifact.
