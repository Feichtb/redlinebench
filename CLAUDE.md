# RedlineBench — AI Architectural Drawing Review Benchmark

## Project Purpose

RedlineBench benchmarks how well various AI models perform at reviewing architectural construction document sets — finding errors, inconsistencies, omissions, and coordination failures that would cause real problems during construction.

## How It Works

1. **Test files** (`results/dataset/test_files/`): A real residential project drawing set and project specification booklet, both intentionally seeded with known issues across 7 categories.

2. **Prompt** (`results/dataset/prompts/review.txt`): A model-agnostic review prompt. Never edit the prompt file after it has been used for a scored run — create a new file instead (e.g. `review_v2.txt`).

3. **Runner** (`redlinebench/runner.py`): Automated script that sends the prompt + both PDFs to each model API, saves raw responses and metadata, and writes a run manifest with token counts, latency, and cost.

4. **Model responses**: Raw `.txt` files saved in `redlinebench/outputs/YYYY-MM-DD_HH-MM/`.

5. **Benchmark answer key** (`results/dataset/benchmark-answer-key.md`): The scorer's reference listing all 58 known issues, organized by category. Also includes a neutral findings list (no score impact) and an incorrect findings list (score penalty).

6. **Scoring**: Each model response is scored against the answer key at the issue level (AI-assisted triage, spot-checked by a licensed architect before publication — see the "Scoring is human-validated" design decision below). Written to a per-run `scores.json` in that run's output folder — one file per scored run, never edited afterward.

7. **Aggregator** (`redlinebench/build_data.py`): Reads every `redlinebench/outputs/*/scores.json`, groups runs by model, and writes `results/dataset/data.json` plus the flat CSV/JSONL exports in `results/dataset/data/`. This is the only place per-run scores get turned into published numbers; nothing is hand-copied anywhere.

8. **Results page** (`results/index.html`): The published benchmark results page. Fetches `results/dataset/data.json` at load time — no data embedded in the HTML, no build step required. Serves from any local HTTP server or can be opened as a file for static previewing (the `fetch()` call needs an actual HTTP server, not a bare `file://` open).

9. **Hugging Face dataset** (`results/dataset/`): The single canonical folder for every data file in this project — test PDFs, review + scoring prompts, answer key, and the generated `data.json`/CSV/JSONL exports. It's not a separate copy of anything; the runner reads test files and prompts from here directly, and the site fetches `data.json` from here directly. Mirror it to a HF Hub dataset repo manually (`huggingface-cli upload <repo> results/dataset .` or `git subtree push --prefix=results/dataset`) whenever you want to publish an update; nothing is pushed automatically.

## Audience and Purpose

RedlineBench is published on benfeicht.com. The audience is **architects and architecture firm owners** evaluating whether and how to use AI in their practice — not ML researchers. Results should be clear and practical, not statistically complex.

## Benchmark Design Decisions (settled)

- **Multiple runs per model, all permanent** (as of 2026-07) — a model may be scored more than once; every run is a dated, permanent record (model version, prompt version, temperature, tokens, cost, per-issue scores). Never delete or overwrite a historical run, including ones that score lower than a later run of the same model — run-to-run variance is real data, not noise to be hidden. `build_data.py` aggregates all of a model's runs into mean/min/max net score and a per-issue "% of runs caught" reliability heatmap. Most models currently have n=1; the leaderboard and heatmap render the single-run case identically to before, and only show the mean/range/fraction UI once a model has n>1. (This supersedes the old "single run per model" / "round-selector UI" decisions — no round selector was ever built; the natural replacement was per-model aggregation.)
- **Answer key locked at 58 issues** — never add new issues to an active answer key. If a new genuine issue is discovered, it goes into a new answer key version, which requires full rescoring. Issues that are debatable go on the neutral list instead.
- **No design advice** — benchmark scope is QAQC only (post-completion drawing review), not design feedback.
- **No cap on items flagged** — models decide when to stop; this is intentional.
- **Legacy model-ID aliases** — a few early `scores.json` files used shorthand model IDs (`haiku`, `gemini-flash`, `gpt5mini`, `grok-4.20-beta`) instead of the runner's canonical keys. These are never edited in place; `build_data.py`'s `LEGACY_MODEL_ALIASES` map normalizes them at aggregation time. Likewise, `MODEL_DISPLAY_OVERRIDES` in that file is now the canonical source for each model's label/color/provider on the site — several older `scores.json` files recorded generic placeholder colors that collide across models, so the aggregator overrides them rather than trusting whatever a given run happened to record.
- **Opus 4.8 dual-run precedent** — two same-day Opus 4.8 runs exist (`2026-06-07_21-33` net 19.5, `2026-06-07_22-02` net 24.5). The 21-33 folder's README previously framed one as "canonical" and the other as a discardable duplicate (a truncation was suspected, then found not to matter). Under the multi-run model both count as legitimate samples (n=2, mean 22.0) — don't reintroduce a canonical/shadow-copy pattern for future same-model reruns.
- **Scoring is human-validated, not per-cell badged or per-run logged** — every automated scoring pass is spot-checked by a licensed architect before publication; scores are not revised after that review. This is stated once as a methodology claim (site text, dataset card) rather than tracked as a `human_validated`/`validated_by` field on each run — that per-run field existed briefly (2026-07) and was removed because it forced a formal sign-off step that didn't match the actual workflow (spot-checking, not per-run logging). Don't reintroduce it; there's also no per-cell "verified" UI convention on Hugging Face or on the site, so don't invent one there either.
- **Versioning**: this public release is v1 (`benchmark_version: v2` internally, since a v1 answer key existed only during development and was never published). Any future private/internal benchmark version gets calibrated against v1 via bridge runs — models re-run on both versions to confirm relative rankings hold — before being treated as comparable. Never silently replace published v1 numbers.

## Scoring Method

For each of the 58 known issues:
- **1 point** — found and correctly described
- **0.5 points** — found but vague or incomplete
- **0 points** — missed

Penalties:
- **−1.0** per incorrect finding (model flagged something factually wrong — misread the documents)

Neutral findings (debatable, out-of-scope, or judgment calls listed in the answer key) have no score impact either direction.

## Current Results

**Source of truth: `redlinebench/outputs/*/scores.json`.** `results/dataset/data.json` (fetched by the site), `results/dataset/data/*` (the HF export), and the table below are all generated from those files by `python redlinebench/build_data.py` — **never hand-edit the table between the markers**, it's overwritten every time `build_data.py` runs. If it disagrees with `results/dataset/data.json`, regenerate; don't manually reconcile.

15 models scored against the 58-issue answer key (mean net score across all runs; `n` shown only where >1):

<!-- REDLINEBENCH:RESULTS_TABLE:START -->
| Model | Net Score | % of max (58) | Cost / run |
|-------|----------:|------------:|------------|
| GPT-5.6 Sol (n=3, range 26.0–28.0) | 27.0 | 46.6% | $3.25 |
| Claude Fable 5 (n=3, range 26.0–26.5) | 26.33 | 45.4% | $3.31 |
| GPT-5.5 (n=3, range 21.5–29.0) | 24.83 | 42.8% | $1.84 |
| Claude Opus 4.8 (n=3, range 19.5–25.0) | 23.0 | 39.7% | $1.47 |
| GPT-5.5 Pro (n=3, range 19.5–25.5) | 22.67 | 39.1% | $12.21 |
| Claude Opus 4.6 | 22.5 | 38.8% | $1.09 |
| GPT-5.4 Pro | 21.5 | 37.1% | $8.27 |
| Claude Opus 4.7 | 20.0 | 34.5% | $1.12 |
| Claude Haiku 4.5 | 14.0 | 24.1% | $0.24 |
| Claude Sonnet 4.6 | 14.0 | 24.1% | $0.74 |
| Gemini 3 Flash | 7.0 | 12.1% | $0.04 |
| Grok 4.20 Beta | 6.0 | 10.3% | $0.25 |
| GPT-5 Mini | 5.5 | 9.5% | $0.03 |
| Gemini 3.1 Pro | 4.5 | 7.8% | $0.27 |
| Claude Sonnet 4.0 | 2.5 | 4.3% | $0.44 |
| GPT-4o | 1.0 | 1.7% | $0.15 |
<!-- REDLINEBENCH:RESULTS_TABLE:END -->

### Adding a model (or a new run of an existing model)

1. **Run it**: `python runner.py --models <key>` from `redlinebench/` (add `--runs N` for multiple runs in one batch).
2. **Score it**: produce `scores.json` in that run's output folder per `results/dataset/prompts/scoring/`. If it's a genuinely new model, also add a `MODEL_DISPLAY_OVERRIDES` entry (`label`/`provider`/`color`) in `build_data.py` so it gets a stable color instead of falling back to whatever's in its `scores.json`.
3. **Regenerate**: `python build_data.py` from `redlinebench/`. This writes `results/dataset/data.json`, `results/dataset/data/*` (the HF export), **and re-syncs the results table above and the supported-models table below** — no manual table edits needed anywhere. Check the printed sanity-check warnings are clean.
4. **Spotlight cards** (`results/index.html`, ~line 685) — hand-coded, only touch if the model lands in the **top 8 by mean net score**: insert its cell in rank order and drop whichever model fell out of the top 8. (The only remaining hand-maintained model list in the whole project — everything else is generated.)
5. **JSON-LD count** — bump the model count in the `<script type="application/ld+json">` `description` near the top of `results/index.html`.
6. Commit `results/dataset/data.json`, `results/dataset/data/*`, the synced doc changes, and the new `redlinebench/outputs/` folder together.

Everything else — leaderboard ranks/mean-range display, "Models evaluated" stat, bar chart (top-8 `slice`), cost/accuracy scatter, and the reliability heatmap — is JS-driven off `results/dataset/data.json` and re-renders automatically. No build step for the site itself; `build_data.py` is the only thing you run by hand.

## File Index

| File/Folder | Description |
|-------------|-------------|
| `results/dataset/test_files/211020 Bonfire House_Architectural_current.pdf` | Current drawing set (use this for all new runs) |
| `results/dataset/test_files/211020 Bonfire House_Specifications_current.pdf` | Current specification booklet |
| `results/dataset/benchmark-answer-key.md` | Complete 58-issue answer key with scoring guidance |
| `results/dataset/prompts/review.txt` | Current active review prompt |
| `results/dataset/prompts/scoring/` | Prompts used to assist with scoring (human-verified) |
| `results/dataset/data.json` | Generated by `build_data.py`; single source the site reads. Never hand-edit. |
| `results/dataset/data/` | Generated flat CSV/JSONL exports for the Hugging Face dataset viewer. Never hand-edit. |
| `results/dataset/README.md` | Dataset card — also the Hugging Face card when this folder is published there |
| `results/dataset/` (as a whole) | The single canonical copy of every data file in the project. This exact folder is what gets published to Hugging Face — nothing here is a copy of something that lives elsewhere. |
| `results/index.html` | Published results page — fetches `results/dataset/data.json`, no embedded data |
| `redlinebench/outputs/` | All runner output folders — never delete. Each scored run has a `scores.json`. Raw research archive; not part of the published dataset. |
| `redlinebench/runner.py` | Main runner script |
| `redlinebench/build_data.py` | Aggregates all `scores.json` into `results/dataset/data.json` and `results/dataset/data/` |
| `redlinebench/.env` | API keys and PDF paths (git-ignored) |

---

## Runner

`redlinebench/runner.py` sends the prompt and both PDFs to each model's API and saves outputs.

### Setup

```bash
cd redlinebench
pip install -r requirements.txt
# .env already configured with API keys and PDF paths
```

### Running

```bash
# All models, 1 run each
python runner.py

# Specific models
python runner.py --models claude-haiku-4-5 gemini-3-flash-preview gpt-5-mini

# Multiple runs per model (max 5)
python runner.py --models claude-sonnet-4-6 --runs 3

# Different prompt file
python runner.py --prompt my_custom_prompt.txt
```

### Supported Models

**`MODEL_CONFIG` at the top of `runner.py` is the source of truth** for model IDs, `max_tokens`, thinking budgets, and per-provider flags. The table below is generated straight from it by `build_data.py` (via `render_model_config_table()`) — **never hand-edit between the markers**; it's mechanically derived and will look terser than hand-written prose (nuance like retention requirements or output caps belongs in a comment next to the `MODEL_CONFIG` entry itself, not duplicated here).

<!-- REDLINEBENCH:MODEL_TABLE:START -->
| Model key | Provider | Notes |
|-----------|----------|-------|
| `claude-fable-5` | Anthropic | Adaptive thinking via `output_config.effort` ("high", type "adaptive") |
| `claude-opus-4-8` | Anthropic | Adaptive thinking via `output_config.effort` ("high", type "adaptive") |
| `claude-opus-4-7` | Anthropic | Adaptive thinking via `output_config.effort` ("high", type "adaptive") |
| `claude-opus-4-6` | Anthropic | Extended thinking (`budget_tokens=20000`) |
| `claude-sonnet-4-6` | Anthropic | Extended thinking (`budget_tokens=16000`) |
| `claude-haiku-4-5` | Anthropic | Extended thinking (`budget_tokens=8000`) |
| `claude-sonnet-4-0` | Anthropic | Extended thinking (`budget_tokens`, legacy `enabled` type) |
| `gemini-3.1-pro-preview` | Google | Dynamic thinking budget (`-1`) |
| `gemini-3-flash-preview` | Google | Dynamic thinking budget (`-1`) |
| `gpt-5.6-sol` | OpenAI | Reasoning model (no temperature) |
| `gpt-5.5` | OpenAI | Reasoning model; `reasoning_effort: xhigh`, no temperature |
| `gpt-5.5-pro` | OpenAI | Reasoning model; `reasoning_effort: xhigh`, no temperature |
| `gpt-5.4-pro` | OpenAI | Reasoning model (no temperature) |
| `gpt-5-mini` | OpenAI | Reasoning model (no temperature) |
| `gpt-4o` | OpenAI | Standard model (temperature=0) |
| `grok-4.20-beta-0309-reasoning` | xAI | Reasoning model (no temperature) |
<!-- REDLINEBENCH:MODEL_TABLE:END -->

**Adding a model to the runner:** add an entry to `MODEL_CONFIG` (key = API model ID) with `provider` and `max_tokens`, plus the provider-specific thinking/temperature flags. New Claude models (4.7+) use the adaptive `output_config.effort` API rather than `budget_tokens` — see the existing Opus 4.7/4.8 entries. Then run `build_data.py` to pick up the new row here automatically — no manual mirroring.

### Output Structure

Each run creates a timestamped folder:

```
redlinebench/outputs/YYYY-MM-DD_HH-MM/
├── <model>_run01.txt         # extracted text response
├── <model>_run01_raw.json    # full raw API response object
├── manifest.json             # token counts, latency, cost_usd, temperature, prompt_version, errors, metadata
└── scores.json               # added once scored — the permanent per-run scoring record
```

### Known Behaviors

- **Claude uses streaming** — required by the Anthropic SDK for large requests (big PDFs + extended thinking). This is handled automatically.
- **gpt-5-mini and gpt-5.4-pro** are reasoning models and reject the `temperature` parameter. Flag `no_temperature: True` in their config entries.
- **Gemini model IDs** must be verified against the live API — use `gemini-3-flash-preview` and `gemini-3.1-pro-preview`, not the shorter names.
- **Outputs are permanent research data** — never delete the `outputs/` folder between runs.
- **`manifest.json`'s `temperature`** is `null` for models/providers that reject the parameter (reasoning models) — this is expected, not a bug.
- **`manifest.json`'s `prompt_version`** is auto-derived from the prompt filename and is only a convenience default. `scores.json`'s `prompt_version` (set by the scorer) is the authoritative value — `review.txt` has in practice been revised in place without a rename more than once, so the filename-derived version can lag reality.

### .env Variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `GOOGLE_API_KEY` | Google AI API key |
| `DRAWING_SET_DRAWINGS_PATH` | Path to the drawing set PDF |
| `DRAWING_SET_SPECS_PATH` | Path to the specifications PDF |
