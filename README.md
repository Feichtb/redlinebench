# RedlineBench

An open benchmark measuring how well AI models review architectural construction documents — finding errors, inconsistencies, omissions, and coordination failures that would cause real problems during construction.

**[View the results](https://redlinebench.benfeicht.com)** | **[Methodology](#methodology)**

## What This Is

Architects spend significant time reviewing drawing sets for coordination errors before issuing them for construction. RedlineBench tests whether AI can do this work reliably by giving models a real residential drawing set (with known issues seeded in) and scoring their findings against a 58-issue answer key.

This is a **QAQC benchmark**, not a design benchmark. It measures a model's ability to catch mistakes in completed documents — the same work an architect does during a quality review before issuing for bid or construction.

## What's in This Repo

| Path | Description |
|------|-------------|
| [`test_files/`](test_files/) | Redacted architectural drawing set and specification booklet (the test dataset) |
| [`benchmark-answer-key.md`](benchmark-answer-key.md) | All 58 known issues with scoring guidance, plus neutral and incorrect findings lists |
| [`redlinebench/`](redlinebench/) | Runner, review prompt, scoring prompts, and raw model outputs |
| [`results/`](results/) | Published results page (deployed to [redlinebench.benfeicht.com](https://redlinebench.benfeicht.com)) |

## Results Summary

All models scored against the 58-issue answer key.

| Model | Net Score | % of 58 | Cost |
|-------|----------:|--------:|-----:|
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

The best model found ~39% of known issues. See the [full results page](https://redlinebench.benfeicht.com) for the issue-level heatmap and detailed breakdown.

## Methodology

1. **Test dataset**: A real residential project drawing set and specification booklet, both with known issues intentionally seeded across 7 categories (schedule-to-drawing conflicts, dimensional errors, spec-to-drawing conflicts, building envelope issues, code/life safety, constructability, and completeness/clarity).

2. **Prompt**: A model-agnostic review prompt ([`review.txt`](redlinebench/prompts/review.txt)) that instructs the model to perform a thorough QAQC review.

3. **Execution**: Each model receives the same prompt and both PDFs via its native API. The [runner](redlinebench/runner.py) saves the full response, token counts, latency, and cost.

4. **Triage**: Each model's response is triaged against the answer key using an [AI-assisted triage prompt](redlinebench/scoring_prompts/prompt1_triage.txt). The triage maps each finding to the answer key and flags unmatched findings for human review. When a model identifies something genuinely new, the finding is reviewed and categorized as a new scoreable issue, a neutral finding (debatable/out-of-scope), or an incorrect finding (model misread the documents). The answer key is locked per release, and any changes create a new version that requires full rescoring. 

5. **Scoring**: Each response is scored against the [answer key](benchmark-answer-key.md) at the issue level:
   - **1 point** — found and correctly described
   - **0.5 points** — found but vague or incomplete
   - **0 points** — missed
   - **-1 point** — per incorrect finding (model misread the documents)

   Scoring is human-verified. The triage prompt assists with matching, but all final scores and answer key decisions are made by a licensed architect.

## Limitations

- **Single evaluator**: The answer key reflects the judgment of one architect reviewing one drawing set. Other architects may reasonably disagree on whether specific findings are scoreable, neutral, or incorrect. The answer key and all scoring data are published in full so others can evaluate for themselves.
- **Single drawing set**: Results reflect model performance on one residential project. Performance on other project types (commercial, institutional, multi-family) or other document formats may differ.
- **Answer key may grow**: The 58-issue answer key represents known issues at the time of this release. Models occasionally surface genuine findings not yet in the answer key. These are reviewed and, if valid, will be incorporated into a future answer key version with full rescoring of all models.

## Reproduce It Yourself

```bash
cd redlinebench
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys

# Run all models
python runner.py

# Run specific models
python runner.py --models claude-opus-4-6 gpt-5-mini

# Use a different prompt file
python runner.py --prompt my_custom_prompt.txt
```

See [`redlinebench/README.md`](redlinebench/README.md) for full runner documentation.

## Design Decisions

- **Answer key locked per release** — all scores in a release are against the same answer key. If the answer key changes (new issues added, categories revised), it becomes a new version and all models are rescored from their original outputs.
- **No design advice in scope** — this is QAQC only (post-completion drawing review), not design feedback.
- **No cap on items flagged** — models decide when to stop; this is intentional.
- **Neutral findings have no score impact** — debatable items are tracked but don't affect the score either way.
- **Raw model outputs are included** — every response is in [`redlinebench/outputs/`](redlinebench/outputs/) for full transparency.

## Audience

This benchmark is built for **architects and architecture firm owners** evaluating whether and how to use AI in their practice. Results are designed to be clear and practical, not statistically complex.

## Author

Built by [Ben Feicht](https://benfeicht.com)

## License

[MIT](LICENSE)
