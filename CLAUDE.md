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

## Current Results — 10 Models

All models scored against the 58-issue answer key. Scored and displayed in `results/index.html`.

| Model | Net Score | % of max (58) | Cost / run |
|-------|----------:|------------:|------------|
| Claude Opus 4.6 | 22.5 | 38.8% | $1.09 |
| GPT-5.4 Pro | 21.5 | 37.1% | $8.27 |
| Claude Haiku 4.5 | 14.0 | 24.1% | $0.24 |
| Claude Sonnet 4.6 | 14.0 | 24.1% | $0.74 |
| Gemini 3 Flash | 7.0 | 12.1% | $0.04 |
| Grok 4.20 Beta | 6.0 | 10.3% | $0.25 |
| GPT-5 Mini | 5.5 | 9.5% | $0.03 |
| Gemini 3.1 Pro | 4.5 | 7.8% | $0.27 |
| Claude Sonnet 4.0 | 2.5 | 4.3% | $0.44 |
| GPT-4o | 1.0 | 1.7% | $0.15 |

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

| Model key | Provider | Notes |
|-----------|----------|-------|
| `claude-opus-4-6` | Anthropic | Extended thinking enabled |
| `claude-sonnet-4-6` | Anthropic | Extended thinking enabled |
| `claude-haiku-4-5` | Anthropic | Extended thinking enabled |
| `claude-sonnet-4-0` | Anthropic | Extended thinking (legacy `enabled` type) |
| `gemini-3.1-pro-preview` | Google | Dynamic thinking budget |
| `gemini-3-flash-preview` | Google | Dynamic thinking budget |
| `gpt-5.4-pro` | OpenAI | Reasoning model (no temperature) |
| `gpt-5-mini` | OpenAI | Reasoning model (no temperature) |
| `gpt-4o` | OpenAI | Standard model |
| `grok-4.20-beta-0309-reasoning` | xAI | Reasoning model (no temperature) |

All model IDs, max_tokens, and thinking budgets are configured in `MODEL_CONFIG` at the top of `runner.py`.

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
