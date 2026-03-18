# RedlineBench Runner

Sends an architectural review prompt plus a drawing set PDF and specification booklet to multiple AI model APIs, saves full responses and metadata, and writes a run manifest for each batch.

## Setup

```bash
cd redlinebench
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env — add API keys and PDF paths (see .env.example)
```

## Running

```bash
# All models, 1 run each (default)
python runner.py

# Specific models only
python runner.py --models claude-opus-4-6 gpt-4o

# Multiple runs per model (max 5)
python runner.py --models claude-sonnet-4-6 --runs 3

# Different prompt file
python runner.py --prompt my_custom_prompt.txt
```

## Output structure

Each batch creates a timestamped folder:

```
outputs/
└── 2025-03-11_14-30/
    ├── claude-opus-4-6_run01.txt        ← extracted text response
    ├── claude-opus-4-6_run01_raw.json   ← full raw API response object
    ├── claude-sonnet-4-6_run01.txt
    ├── claude-sonnet-4-6_run01_raw.json
    ├── gpt-4o_run01.txt
    ├── gpt-4o_run01_raw.json
    └── manifest.json                    ← token counts, costs, errors, metadata
```

The `manifest.json` records: prompt filename, models run, per-model token counts and cost, total run cost, and any errors encountered. Models that fail do not abort the run — their errors are logged in the manifest and the remaining models continue.

## Prompt

The review prompt lives in `prompts/review.txt`. **Never edit the prompt file after it has been used for a scored run.** If you need to change the prompt, create a new file (e.g. `review_v2.txt`) and pass it with `--prompt`. This ensures every output can be traced back to an exact prompt.

## Output retention

**Do not delete the `outputs/` folder between runs.** Each run folder is a permanent record of the experiment. The outputs directory is the research dataset; treat it accordingly.

## Environment variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `GOOGLE_API_KEY` | Google AI API key |
| `GROK_API_KEY` | xAI API key (for Grok models) |
| `DRAWING_SET_DRAWINGS_PATH` | Path to the drawing set PDF |
| `DRAWING_SET_SPECS_PATH` | Path to the specification booklet PDF |

## Supported models

| Model ID | Provider | Notes |
|---|---|---|
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

To add a new model, add an entry to `MODEL_CONFIG` in `runner.py` and, if the provider is new, add a `ModelAdapter` subclass and register it in `PROVIDER_ADAPTER`.

## Pricing note

Token costs in `runner.py` are hardcoded to public list prices as of 2026-03. Update `MODEL_CONFIG` if prices change before relying on cost estimates for budgeting.