"""
Verify cost calculations in all manifest.json files.
Prices are per million tokens (USD).
Thinking tokens are billed at the output rate.
"""

import json
from pathlib import Path

PRICING = {
    # Anthropic  (input, output) per MTok
    "claude-haiku-4-5":   (1.00,   5.00),
    "claude-sonnet-4-0":  (3.00,  15.00),
    "claude-sonnet-4-6":  (3.00,  15.00),
    "claude-opus-4-6":    (5.00,  25.00),
    # Google
    "gemini-3-flash-preview":   (0.50,   3.00),
    "gemini-3.1-pro-preview":   (2.00,  12.00),
    # OpenAI
    "gpt-4o":      (2.50,  10.00),
    "gpt-5-mini":  (0.25,   2.00),
    "gpt-5.4-pro": (30.00, 180.00),
    # xAI
    "grok-4.20-beta-0309-reasoning": (2.00, 6.00),
}

outputs_dir = Path(__file__).parent / "outputs"
manifests = sorted(outputs_dir.glob("*/manifest.json"))

all_ok = True

for manifest_path in manifests:
    with open(manifest_path) as f:
        data = json.load(f)

    folder = manifest_path.parent.name
    print(f"\n-- {folder} --")

    for result in data["results"]:
        model = result["model_name"]
        recorded = result["cost_usd"]

        if result.get("error") and result["input_tokens"] == 0:
            expected = 0.0
        elif model not in PRICING:
            print(f"  {model}: NO PRICING DATA")
            continue
        else:
            input_price, output_price = PRICING[model]
            input_tokens  = result["input_tokens"]
            output_tokens = result["output_tokens"] + result.get("thinking_tokens", 0)
            expected = (input_tokens * input_price + output_tokens * output_price) / 1_000_000

        match = abs(recorded - expected) < 0.000001
        status = "OK" if match else "MISMATCH"
        if not match:
            all_ok = False
        print(f"  {model}: recorded=${recorded:.6f}  expected=${expected:.6f}  [{status}]")

print()
print("All checks passed." if all_ok else "MISMATCHES FOUND — review above.")
