# RedlineBench — AI Architectural Drawing Review Benchmark

## Project Purpose

RedlineBench benchmarks how well various AI models perform at reviewing architectural construction document sets — finding errors, inconsistencies, omissions, and coordination failures that would cause real problems during construction.

## How It Works

1. **Test files** (`test_files/`): A real residential project drawing set and project specification booklet, both intentionally seeded with known issues across 7 categories.

2. **Prompt** (`redlinebench/prompts/review.txt`): A model-agnostic review prompt. Never edit the prompt file after it has been used for a scored run — create a new file instead (e.g. `review_v2.txt`).

3. **Runner** (`redlinebench/runner.py`): Automated script that sends the prompt + both PDFs to each model API, saves raw responses and metadata, and writes a run manifest with token counts, latency, and cost.

4. **Model responses**: Raw `.txt` files saved in `redlinebench/outputs/YYYY-MM-DD_HH-MM/`.

5. **Benchmark answer key** (`benchmark-answer-key.md`): The scorer's reference listing all 58 known issues, organized by category. Also includes a neutral findings list (no score impact) and an incorrect findings list (score penalty).

6. **Scoring**: Each model response is manually scored against the answer key at the issue level.

7. **Results page** (`results/index.html`): The published benchmark results page. All scoring data is embedded directly in the HTML — no build step required. Serves from any local HTTP server or can be opened as a file for static previewing.

## Audience and Purpose

RedlineBench is published on benfeicht.com. The audience is **architects and architecture firm owners** evaluating whether and how to use AI in their practice — not ML researchers. Results should be clear and practical, not statistically complex.

## Benchmark Design Decisions (settled)

- **Single run per model** — deliberate. Multiple runs would complicate the issue-level heatmap, which is the most valuable part of the results page. Single runs are credible for this audience given the transparent methodology and 58-issue answer key.
- **Answer key locked at 58 issues** — never add new issues to an active answer key. If a new genuine issue is discovered, it goes into a new answer key version, which requires full rescoring. Issues that are debatable go on the neutral list instead.
- **No design advice** — benchmark scope is QAQC only (post-completion drawing review), not design feedback.
- **Future rounds use the round-selector UI** — re-running models or adding new models creates a new round, not additional runs within a round.
- **No cap on items flagged** — models decide when to stop; this is intentional.

## Scoring Method

For each of the 58 known issues:
- **1 point** — found and correctly described
- **0.5 points** — found but vague or incomplete
- **0 points** — missed

Penalties:
- **−1.0** per incorrect finding (model flagged something factually wrong — misread the documents)

Neutral findings (debatable, out-of-scope, or judgment calls listed in the answer key) have no score impact either direction.

## Current Results

**Source of truth: `results/index.html`.** All scoring data is the `COMBINED_V3_DATA` object near the bottom of that file; each run's `scores.json` is the per-run record those values are copied from. The table below is a snapshot for quick reference — when it disagrees with the page, the page wins.

Snapshot — 15 models scored against the 58-issue answer key:

| Model | Net Score | % of max (58) | Cost / run |
|-------|----------:|------------:|------------|
| Claude Fable 5 | 26.0 | 44.8% | $3.12 |
| GPT-5.5 | 24.0 | 41.4% | $1.28 |
| GPT-5.5 Pro | 23.0 | 39.7% | $8.27 |
| Claude Opus 4.6 | 22.5 | 38.8% | $1.09 |
| GPT-5.4 Pro | 21.5 | 37.1% | $8.27 |
| Claude Opus 4.7 | 20.0 | 34.5% | $1.12 |
| Claude Opus 4.8 | 19.5 | 33.6% | $1.39 |
| Claude Haiku 4.5 | 14.0 | 24.1% | $0.24 |
| Claude Sonnet 4.6 | 14.0 | 24.1% | $0.74 |
| Gemini 3 Flash | 7.0 | 12.1% | $0.04 |
| Grok 4.20 Beta | 6.0 | 10.3% | $0.25 |
| GPT-5 Mini | 5.5 | 9.5% | $0.03 |
| Gemini 3.1 Pro | 4.5 | 7.8% | $0.27 |
| Claude Sonnet 4.0 | 2.5 | 4.3% | $0.44 |
| GPT-4o | 1.0 | 1.7% | $0.15 |

### Adding a model to the results page

After a model has been run and manually scored, edit `results/index.html`:

1. **Add a model object** to `COMBINED_V3_DATA.models` — `id`, `label`, `provider`, `color`, `cost_usd`, `raw`, `net`, `max:58`, `pct`, `flagged`, `neutral`, `incorrect:[…]`.
2. **Add the 58-issue score row** to `COMBINED_V3_DATA.scores` keyed by the same `id` (0 / 0.5 / 1 per issue).
3. **Spotlight cards** — only if the model lands in the **top 8 by net score**. The four cards (~line 685) are hand-coded: insert the model's cell in rank order and drop whichever model fell out of the top 8.
4. **JSON-LD count** — bump the model count in the `<script type="application/ld+json">` `description` near the top of the file.
5. **Update the snapshot table above** in this file.

Everything else — leaderboard ranks, "Models evaluated" stat, bar chart (top-8 `slice`), cost/accuracy scatter, and the heatmap — is JS-driven off `models` + `scores` and re-renders automatically. No build step.

## File Index

| File/Folder | Description |
|-------------|-------------|
| `test_files/211020 Bonfire House_Architectural_current.pdf` | Current drawing set (use this for all new runs) |
| `test_files/211020 Bonfire House_Specifications_current.pdf` | Current specification booklet |
| `benchmark-answer-key.md` | Complete 58-issue answer key with scoring guidance |
| `results/index.html` | Published results page — all scoring data embedded in JS |
| `redlinebench/prompts/review.txt` | Current active prompt |
| `redlinebench/outputs/` | All runner output folders — never delete |
| `redlinebench/scoring_prompts/` | Prompts used to assist with scoring (human-verified) |
| `redlinebench/runner.py` | Main runner script |
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

**`MODEL_CONFIG` at the top of `runner.py` is the source of truth** for model IDs, `max_tokens`, thinking budgets, and per-provider flags. The list below mirrors it — keep them in sync when adding a model.

| Model key | Provider | Notes |
|-----------|----------|-------|
| `claude-fable-5` | Anthropic | Most capable model. Thinking always on (`output_config.effort`, no `budget_tokens`); `max_tokens` at the 128K ceiling; requires 30-day data retention |
| `claude-opus-4-8` | Anthropic | Adaptive thinking via `output_config.effort` (no `budget_tokens`) |
| `claude-opus-4-7` | Anthropic | Adaptive thinking via `output_config.effort` (no `budget_tokens`) |
| `claude-opus-4-6` | Anthropic | Extended thinking (`budget_tokens`) |
| `claude-sonnet-4-6` | Anthropic | Extended thinking (`budget_tokens`) |
| `claude-haiku-4-5` | Anthropic | Extended thinking (`budget_tokens`) |
| `claude-sonnet-4-0` | Anthropic | Legacy `enabled` thinking type |
| `gemini-3.1-pro-preview` | Google | Dynamic thinking budget (`-1`) |
| `gemini-3-flash-preview` | Google | Dynamic thinking budget (`-1`) |
| `gpt-5.5` | OpenAI | Reasoning model; `reasoning_effort: xhigh`, no temperature |
| `gpt-5.5-pro` | OpenAI | Reasoning model; `reasoning_effort: xhigh`, no temperature |
| `gpt-5.4-pro` | OpenAI | Reasoning model (no temperature) |
| `gpt-5-mini` | OpenAI | Reasoning model (no temperature) |
| `gpt-4o` | OpenAI | Standard model (temperature=0) |
| `grok-4.20-beta-0309-reasoning` | xAI | Reasoning model (no temperature) |

**Adding a model to the runner:** add an entry to `MODEL_CONFIG` (key = API model ID) with `provider` and `max_tokens`, plus the provider-specific thinking/temperature flags above. New Claude models (4.7+) use the adaptive `output_config.effort` API rather than `budget_tokens` — see the existing Opus 4.7/4.8 entries. Then mirror the row into the table above.

### Output Structure

Each run creates a timestamped folder:

```
redlinebench/outputs/YYYY-MM-DD_HH-MM/
├── <model>_run01.txt         # extracted text response
├── <model>_run01_raw.json    # full raw API response object
└── manifest.json             # token counts, latency, cost_usd, errors, metadata
```

### Known Behaviors

- **Claude uses streaming** — required by the Anthropic SDK for large requests (big PDFs + extended thinking). This is handled automatically.
- **gpt-5-mini and gpt-5.4-pro** are reasoning models and reject the `temperature` parameter. Flag `no_temperature: True` in their config entries.
- **Gemini model IDs** must be verified against the live API — use `gemini-3-flash-preview` and `gemini-3.1-pro-preview`, not the shorter names.
- **Outputs are permanent research data** — never delete the `outputs/` folder between runs.

### .env Variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `GOOGLE_API_KEY` | Google AI API key |
| `DRAWING_SET_DRAWINGS_PATH` | Path to the drawing set PDF |
| `DRAWING_SET_SPECS_PATH` | Path to the specifications PDF |
