#!/usr/bin/env python3
"""
RedlineBench Runner
-------------------
Sends an architectural review prompt (with an attached drawing set PDF and
optional specifications PDF) to multiple AI model APIs, saves the full
responses and metadata, and writes a run manifest.

Priority: logging, reproducibility, error isolation.
"""

import argparse
import base64
import json
import os
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

# ─── Configuration ────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent

load_dotenv(SCRIPT_DIR / ".env")
PROMPTS_DIR = SCRIPT_DIR / "prompts"
OUTPUTS_DIR = SCRIPT_DIR / "outputs"

# Per-model settings.
# thinking_budget (Claude/Gemini): tokens reserved for internal reasoning.
#   Claude:  must be < max_tokens; remaining is available for text output.
#            Extended thinking requires temperature=1 (handled automatically).
#   Gemini:  -1 = dynamic (model decides how much to think).
# reasoning_effort (OpenAI): "low" | "medium" | "high" — only for o-series
#   and any GPT-5 variant that behaves as a reasoning model.
# no_temperature: True for reasoning models that reject the temperature param.
#
# Cost fields intentionally omitted — add them once pricing stabilises.

MODEL_CONFIG: dict[str, dict[str, Any]] = {
    # ── Anthropic ──────────────────────────────────────────────────────────
    "claude-opus-4-6": {
        "provider": "anthropic",
        "max_tokens": 32000,
        "thinking_budget": 20000,   # ~12 K left for text output
    },
    "claude-sonnet-4-6": {
        "provider": "anthropic",
        "max_tokens": 32000,
        "thinking_budget": 16000,
    },
    "claude-haiku-4-5": {
        "provider": "anthropic",
        "max_tokens": 32000,    # raised; previous 16K was our limit, not the API's
        "thinking_budget": 8000,
    },
    # "Claude Sonnet 4" (first 4.x Sonnet release, prior to 4.5/4.6).
    # Uses older "enabled" thinking type (not "adaptive").
    # Verify this model ID against the Anthropic API if the run fails.
    "claude-sonnet-4-0": {
        "provider": "anthropic",
        "max_tokens": 32000,
        "thinking_budget": 16000,
        "thinking_type": "enabled",     # older models use "enabled" not "adaptive"
    },
    # ── Google Gemini ──────────────────────────────────────────────────────
    # IDs verified against the API's ListModels endpoint (2026-03-12).
    "gemini-3.1-pro-preview": {
        "provider": "gemini",
        "max_tokens": 65536,
        "thinking_budget": -1,      # -1 = dynamic
    },
    "gemini-3-flash-preview": {
        "provider": "gemini",
        "max_tokens": 65536,
        "thinking_budget": -1,
    },
    # ── OpenAI ─────────────────────────────────────────────────────────────
    # Verify exact API model IDs at https://platform.openai.com/docs/models
    # If gpt-5.4-pro or gpt-5-mini turn out to be reasoning (o-series) models,
    # add: "reasoning_effort": "high", "no_temperature": True
    "gpt-5.4-pro": {
        "provider": "openai",
        "max_tokens": 65536,
        "no_temperature": True,     # reasoning model; rejects temperature param
    },
    "gpt-5-mini": {
        "provider": "openai",
        "max_tokens": 16384,
        "no_temperature": True,     # reasoning model; rejects temperature param
    },
    "gpt-4o": {
        "provider": "openai",
        "max_tokens": 32768,        # standard model; temperature=0 applied
    },
    # ── xAI Grok ───────────────────────────────────────────────────────────
    # Uses OpenAI-compatible Chat Completions API at api.x.ai/v1.
    # Reasoning model — rejects temperature param.
    "grok-4.20-beta-0309-reasoning": {
        "provider": "xai",
        "max_tokens": 32000,
        "no_temperature": True,     # reasoning model
    },
}

DEFAULT_MODELS = list(MODEL_CONFIG.keys())
MAX_RUNS = 5


# ─── Data model ───────────────────────────────────────────────────────────────

@dataclass
class RunResult:
    model_name: str
    model_version: str      # version string as returned by the API
    prompt_file: str
    run_number: int
    timestamp_start: str    # ISO-8601 UTC
    timestamp_end: str
    latency_seconds: float
    input_tokens: int
    output_tokens: int
    thinking_tokens: int    # 0 if model doesn't report separately
    cost_usd: float         # 0.0 until pricing is configured
    text_response: str
    raw_response: dict
    error: Optional[str] = None


# ─── Base adapter ─────────────────────────────────────────────────────────────

class ModelAdapter(ABC):
    """Abstract base; one concrete subclass per provider."""

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.config = MODEL_CONFIG[model_name]

    @abstractmethod
    def call_api(
        self,
        prompt: str,
        drawings_pdf: Optional[bytes],
        specs_pdf: Optional[bytes],
    ) -> dict:
        """
        Call the provider API and return a dict with keys:
            text            str
            input_tokens    int
            output_tokens   int
            thinking_tokens int   (0 if not separately reported)
            model_version   str
            raw_response    dict  (JSON-serialisable)
        Raise on hard failures; run() wraps in try/except.
        """

    def run(
        self,
        prompt: str,
        drawings_pdf: Optional[bytes],
        specs_pdf: Optional[bytes],
        run_number: int,
        prompt_file: str,
    ) -> RunResult:
        ts_start = datetime.now(timezone.utc).isoformat()
        t0 = time.monotonic()
        try:
            api_result = self.call_api(prompt, drawings_pdf, specs_pdf)
            latency = time.monotonic() - t0
            return RunResult(
                model_name=self.model_name,
                model_version=api_result["model_version"],
                prompt_file=prompt_file,
                run_number=run_number,
                timestamp_start=ts_start,
                timestamp_end=datetime.now(timezone.utc).isoformat(),
                latency_seconds=round(latency, 2),
                input_tokens=api_result["input_tokens"],
                output_tokens=api_result["output_tokens"],
                thinking_tokens=api_result.get("thinking_tokens", 0),
                cost_usd=0.0,
                text_response=api_result["text"],
                raw_response=api_result["raw_response"],
            )
        except Exception as exc:
            latency = time.monotonic() - t0
            return RunResult(
                model_name=self.model_name,
                model_version="unknown",
                prompt_file=prompt_file,
                run_number=run_number,
                timestamp_start=ts_start,
                timestamp_end=datetime.now(timezone.utc).isoformat(),
                latency_seconds=round(latency, 2),
                input_tokens=0,
                output_tokens=0,
                thinking_tokens=0,
                cost_usd=0.0,
                text_response="",
                raw_response={},
                error=str(exc),
            )


# ─── Claude adapter ───────────────────────────────────────────────────────────

class ClaudeAdapter(ModelAdapter):
    """
    Extended thinking is enabled for all Claude models.
    Temperature is forced to 1 when thinking is active (API requirement).
    Both PDFs are attached as document blocks before the prompt text.
    """

    def __init__(self, model_name: str) -> None:
        super().__init__(model_name)
        import anthropic
        self._client = anthropic.Anthropic(
            api_key=os.environ["ANTHROPIC_API_KEY"]
        )

    def _pdf_block(self, pdf_bytes: bytes, label: str) -> dict:
        return {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": base64.standard_b64encode(pdf_bytes).decode(),
            },
            "title": label,
        }

    def call_api(
        self,
        prompt: str,
        drawings_pdf: Optional[bytes],
        specs_pdf: Optional[bytes],
    ) -> dict:
        content: list[dict] = []
        if drawings_pdf:
            content.append(self._pdf_block(drawings_pdf, "Drawing Set"))
        if specs_pdf:
            content.append(self._pdf_block(specs_pdf, "Project Specifications"))
        content.append({"type": "text", "text": prompt})

        thinking_budget = self.config.get("thinking_budget", 0)
        kwargs: dict[str, Any] = {
            "model": self.model_name,
            "max_tokens": self.config["max_tokens"],
            "messages": [{"role": "user", "content": content}],
        }
        if thinking_budget:
            # Extended thinking requires temperature=1 (API enforced).
            # Older models use type "enabled"; newer models use "adaptive".
            thinking_type = self.config.get("thinking_type", "adaptive")
            kwargs["thinking"] = {
                "type": thinking_type,
                "budget_tokens": thinking_budget,
            }
            kwargs["temperature"] = 1
        else:
            kwargs["temperature"] = 0

        # Use streaming — required by the Anthropic SDK for requests that may
        # exceed 10 minutes (large PDFs + extended thinking + high max_tokens).
        with self._client.messages.stream(**kwargs) as stream:
            response = stream.get_final_message()

        # Separate thinking blocks from text blocks
        text_parts = []
        for block in response.content:
            if block.type == "text":
                text_parts.append(block.text)
            # thinking blocks are captured in raw_response; not needed for text output

        usage = response.usage
        thinking_tokens = getattr(usage, "cache_creation_input_tokens", 0) or 0
        # Anthropic doesn't expose a dedicated thinking_tokens field yet;
        # output_tokens already includes thinking tokens.

        return {
            "text": "\n".join(text_parts),
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "thinking_tokens": thinking_tokens,
            "model_version": response.model,
            "raw_response": response.model_dump(),
        }


# ─── OpenAI adapter ───────────────────────────────────────────────────────────

class OpenAIAdapter(ModelAdapter):
    """
    Uses the OpenAI Responses API, which supports inline PDF file inputs.
    For reasoning models (o-series or GPT-5 variants): set reasoning_effort
    and no_temperature in MODEL_CONFIG. For standard models: temperature=0.
    Both PDFs are attached as input_file content items.
    """

    def __init__(self, model_name: str) -> None:
        super().__init__(model_name)
        import openai
        self._client = openai.OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
            timeout=3600,  # 60 min — reasoning models with large PDFs can be slow
        )

    def _file_block(self, pdf_bytes: bytes, filename: str) -> dict:
        b64 = base64.standard_b64encode(pdf_bytes).decode()
        return {
            "type": "input_file",
            "filename": filename,
            "file_data": f"data:application/pdf;base64,{b64}",
        }

    def call_api(
        self,
        prompt: str,
        drawings_pdf: Optional[bytes],
        specs_pdf: Optional[bytes],
    ) -> dict:
        content: list[dict] = []
        if drawings_pdf:
            content.append(self._file_block(drawings_pdf, "drawing_set.pdf"))
        if specs_pdf:
            content.append(self._file_block(specs_pdf, "specifications.pdf"))
        content.append({"type": "input_text", "text": prompt})

        kwargs: dict[str, Any] = {
            "model": self.model_name,
            "input": [{"role": "user", "content": content}],
            "max_output_tokens": self.config["max_tokens"],
        }

        if self.config.get("reasoning_effort"):
            # Reasoning models (o-series, GPT-5 reasoning variants)
            kwargs["reasoning"] = {"effort": self.config["reasoning_effort"]}

        if not self.config.get("no_temperature"):
            kwargs["temperature"] = 0

        # Use background mode for slow reasoning models — fire and poll instead
        # of holding a long-lived streaming connection that the server may drop.
        response = self._client.responses.create(**kwargs, background=True)
        poll_interval = 30  # seconds
        while response.status not in ("completed", "failed", "cancelled", "incomplete"):
            print(f"\n    (status: {response.status}, polling in {poll_interval}s)", end="", flush=True)
            time.sleep(poll_interval)
            response = self._client.responses.retrieve(response.id)

        if response.status == "failed":
            raise RuntimeError(f"Response ended with status: {response.status}")
        # "incomplete" means the model hit max_output_tokens — save what was generated

        usage = response.usage
        # reasoning_output_tokens is reported for o-series models
        thinking_tokens = getattr(usage, "reasoning_output_tokens", 0) or 0

        return {
            "text": response.output_text,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "thinking_tokens": thinking_tokens,
            "model_version": response.model,
            "raw_response": response.model_dump(),
        }


# ─── Gemini adapter ───────────────────────────────────────────────────────────

class GeminiAdapter(ModelAdapter):
    """
    Uses the google-genai SDK (not the legacy google-generativeai package).
    Thinking is enabled via ThinkingConfig.thinking_budget.
    Both PDFs are attached as inline Part.from_bytes() items.
    """

    def __init__(self, model_name: str) -> None:
        super().__init__(model_name)
        from google import genai
        self._client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

    def call_api(
        self,
        prompt: str,
        drawings_pdf: Optional[bytes],
        specs_pdf: Optional[bytes],
    ) -> dict:
        from google.genai import types

        contents: list[Any] = []
        if drawings_pdf:
            contents.append(
                types.Part.from_bytes(data=drawings_pdf, mime_type="application/pdf")
            )
        if specs_pdf:
            contents.append(
                types.Part.from_bytes(data=specs_pdf, mime_type="application/pdf")
            )
        contents.append(prompt)

        thinking_budget = self.config.get("thinking_budget")
        cfg_kwargs: dict[str, Any] = {
            "max_output_tokens": self.config["max_tokens"],
        }
        if thinking_budget is not None:
            cfg_kwargs["thinking_config"] = types.ThinkingConfig(
                thinking_budget=thinking_budget  # -1 = dynamic
            )
        else:
            # Only set temperature when thinking is disabled
            # (some Gemini thinking models reject explicit temperature=0)
            cfg_kwargs["temperature"] = 0

        response = self._client.models.generate_content(
            model=self.model_name,
            contents=contents,
            config=types.GenerateContentConfig(**cfg_kwargs),
        )

        usage = response.usage_metadata
        thinking_tokens = getattr(usage, "thoughts_token_count", 0) or 0

        return {
            "text": response.text,
            "input_tokens": usage.prompt_token_count or 0,
            "output_tokens": usage.candidates_token_count or 0,
            "thinking_tokens": thinking_tokens,
            "model_version": self.model_name,  # Gemini doesn't echo version
            "raw_response": response.model_dump(),
        }


# ─── xAI Grok adapter ─────────────────────────────────────────────────────────

class GrokAdapter(ModelAdapter):
    """
    Uses xAI's Responses API at api.x.ai/v1/responses (OpenAI-compatible).
    PDFs must be uploaded to the Files API first; the returned file_id is
    then referenced via input_file content blocks.
    Uploaded files are deleted after each call to avoid accumulation.
    Reasoning tokens are pulled from usage.reasoning_output_tokens.
    """

    def __init__(self, model_name: str) -> None:
        super().__init__(model_name)
        import openai
        self._client = openai.OpenAI(
            api_key=os.environ["GROK_API_KEY"],
            base_url="https://api.x.ai/v1",
            timeout=3600,
        )

    def _upload_pdf(self, pdf_bytes: bytes, filename: str) -> str:
        """Upload a PDF to the Files API and return the file_id."""
        import io
        response = self._client.files.create(
            file=(filename, io.BytesIO(pdf_bytes), "application/pdf"),
            purpose="assistants",
        )
        return response.id

    def call_api(
        self,
        prompt: str,
        drawings_pdf: Optional[bytes],
        specs_pdf: Optional[bytes],
    ) -> dict:
        content: list[dict] = []
        file_ids: list[str] = []

        if drawings_pdf:
            print(" (uploading drawings PDF...)", end="", flush=True)
            fid = self._upload_pdf(drawings_pdf, "drawing_set.pdf")
            file_ids.append(fid)
            content.append({"type": "input_file", "file_id": fid})
        if specs_pdf:
            print(" (uploading specs PDF...)", end="", flush=True)
            fid = self._upload_pdf(specs_pdf, "specifications.pdf")
            file_ids.append(fid)
            content.append({"type": "input_file", "file_id": fid})
        content.append({"type": "input_text", "text": prompt})

        kwargs: dict[str, Any] = {
            "model": self.model_name,
            "input": [{"role": "user", "content": content}],
            "max_output_tokens": self.config["max_tokens"],
        }
        if not self.config.get("no_temperature"):
            kwargs["temperature"] = 0

        try:
            response = self._client.responses.create(**kwargs)
        finally:
            # Clean up uploaded files regardless of success/failure
            for fid in file_ids:
                try:
                    self._client.files.delete(fid)
                except Exception:
                    pass

        usage = response.usage
        thinking_tokens = getattr(usage, "reasoning_output_tokens", 0) or 0

        return {
            "text": response.output_text,
            "input_tokens": usage.input_tokens if usage else 0,
            "output_tokens": usage.output_tokens if usage else 0,
            "thinking_tokens": thinking_tokens,
            "model_version": response.model,
            "raw_response": response.model_dump(),
        }


# ─── Adapter factory ──────────────────────────────────────────────────────────

PROVIDER_ADAPTER: dict[str, type[ModelAdapter]] = {
    "anthropic": ClaudeAdapter,
    "openai": OpenAIAdapter,
    "gemini": GeminiAdapter,
    "xai": GrokAdapter,
}


def build_adapter(model_name: str) -> ModelAdapter:
    cfg = MODEL_CONFIG.get(model_name)
    if cfg is None:
        raise ValueError(
            f"Unknown model '{model_name}'. "
            f"Valid choices: {list(MODEL_CONFIG)}"
        )
    return PROVIDER_ADAPTER[cfg["provider"]](model_name)


# ─── I/O helpers ──────────────────────────────────────────────────────────────

def load_prompt(filename: str) -> str:
    path = PROMPTS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def _load_pdf(env_var: str) -> Optional[bytes]:
    """Load a PDF from an env var path. Returns None if unset."""
    path_str = os.environ.get(env_var, "").strip()
    if not path_str:
        return None
    p = Path(path_str)
    if not p.exists():
        raise FileNotFoundError(f"{env_var} points to missing file: {p}")
    print(f"  {env_var}: {p.name} ({p.stat().st_size / 1024:.0f} KB)")
    return p.read_bytes()


def load_pdfs() -> tuple[Optional[bytes], Optional[bytes]]:
    """
    Load drawings and specs PDFs from env vars.
    At least one must be set.
    """
    drawings = _load_pdf("DRAWING_SET_DRAWINGS_PATH")
    specs = _load_pdf("DRAWING_SET_SPECS_PATH")
    if drawings is None and specs is None:
        raise EnvironmentError(
            "At least one of DRAWING_SET_DRAWINGS_PATH or "
            "DRAWING_SET_SPECS_PATH must be set in .env"
        )
    return drawings, specs


def slugify_model(model_name: str) -> str:
    return model_name.replace("/", "-").replace(":", "-").replace(" ", "_").replace(".", "-")


def save_run_outputs(result: RunResult, run_dir: Path) -> tuple[Path, Path]:
    """Write .txt (text response) and _raw.json (API metadata). Returns both paths."""
    slug = slugify_model(result.model_name)
    run_tag = f"run{result.run_number:02d}"
    base_name = f"{slug}_{run_tag}"

    txt_path = run_dir / f"{base_name}.txt"
    json_path = run_dir / f"{base_name}_raw.json"

    txt_path.write_text(result.text_response, encoding="utf-8")
    json_path.write_text(
        json.dumps(result.raw_response, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    return txt_path, json_path


def write_manifest(
    results: list[RunResult],
    run_dir: Path,
    prompt_file: str,
    drawings_pdf_name: Optional[str],
    specs_pdf_name: Optional[str],
    errors: list[str],
) -> Path:
    manifest = {
        "prompt_file": prompt_file,
        "drawings_pdf": drawings_pdf_name,
        "specs_pdf": specs_pdf_name,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "run_directory": str(run_dir),
        "models_run": sorted({r.model_name for r in results}),
        "results": [
            {
                "model_name": r.model_name,
                "model_version": r.model_version,
                "run_number": r.run_number,
                "timestamp_start": r.timestamp_start,
                "timestamp_end": r.timestamp_end,
                "latency_seconds": r.latency_seconds,
                "input_tokens": r.input_tokens,
                "output_tokens": r.output_tokens,
                "thinking_tokens": r.thinking_tokens,
                "cost_usd": r.cost_usd,
                "error": r.error,
            }
            for r in results
        ],
        "errors": errors,
    }
    path = run_dir / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


# ─── CLI ──────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="RedlineBench — run architectural review prompt across AI models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"Available models: {', '.join(DEFAULT_MODELS)}",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        metavar="MODEL",
        help="Which models to run (default: all).",
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        metavar="N",
        help=f"Runs per model, 1–{MAX_RUNS} (default: 1).",
    )
    parser.add_argument(
        "--prompt",
        default="review_v3.txt",
        metavar="FILE",
        help="Prompt filename inside prompts/ (default: review_v3.txt).",
    )
    return parser.parse_args()


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    if not (1 <= args.runs <= MAX_RUNS):
        sys.exit(f"--runs must be between 1 and {MAX_RUNS}.")

    unknown = [m for m in args.models if m not in MODEL_CONFIG]
    if unknown:
        sys.exit(
            f"Unknown model(s): {unknown}\n"
            f"Valid choices: {list(MODEL_CONFIG)}"
        )

    print(f"\n{'-' * 60}")
    print("RedlineBench Runner")
    print(f"{'-' * 60}")
    print(f"  Prompt : {args.prompt}")
    print(f"  Models : {args.models}")
    print(f"  Runs   : {args.runs} per model")

    try:
        prompt_text = load_prompt(args.prompt)
    except FileNotFoundError as e:
        sys.exit(str(e))

    try:
        drawings_pdf, specs_pdf = load_pdfs()
    except (EnvironmentError, FileNotFoundError) as e:
        sys.exit(str(e))

    drawings_name = (
        Path(os.environ.get("DRAWING_SET_DRAWINGS_PATH", "")).name or None
    )
    specs_name = (
        Path(os.environ.get("DRAWING_SET_SPECS_PATH", "")).name or None
    )

    run_ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M")
    run_dir = OUTPUTS_DIR / run_ts
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"  Output : {run_dir}\n")

    all_results: list[RunResult] = []
    top_level_errors: list[str] = []

    for model_name in args.models:
        print(f"[{model_name}]")
        try:
            adapter = build_adapter(model_name)
        except Exception as e:
            print(f"  ERROR building adapter: {e}")
            top_level_errors.append(f"{model_name}: {e}")
            continue

        for run_num in range(1, args.runs + 1):
            print(f"  run {run_num}/{args.runs} — calling API...", end="", flush=True)
            result = adapter.run(
                prompt=prompt_text,
                drawings_pdf=drawings_pdf,
                specs_pdf=specs_pdf,
                run_number=run_num,
                prompt_file=args.prompt,
            )
            all_results.append(result)

            if result.error:
                print(f" FAILED ({result.latency_seconds}s)")
                print(f"    Error: {result.error}")
                top_level_errors.append(f"{model_name} run {run_num}: {result.error}")
                save_run_outputs(result, run_dir)
            else:
                think_str = (
                    f" | {result.thinking_tokens} think tok"
                    if result.thinking_tokens
                    else ""
                )
                print(
                    f" OK ({result.latency_seconds}s | "
                    f"in:{result.input_tokens} out:{result.output_tokens}"
                    f"{think_str})"
                )
                txt_p, json_p = save_run_outputs(result, run_dir)
                print(f"    -> {txt_p.name}, {json_p.name}")

    manifest_path = write_manifest(
        all_results,
        run_dir,
        args.prompt,
        drawings_name,
        specs_name,
        top_level_errors,
    )

    successful = sum(1 for r in all_results if not r.error)
    print(f"\n{'-' * 60}")
    print(f"Done. {successful}/{len(all_results)} runs succeeded.")
    print(f"Manifest : {manifest_path}")
    if top_level_errors:
        print(f"Errors   : {len(top_level_errors)} (see manifest.json)")
    print(f"{'-' * 60}\n")


if __name__ == "__main__":
    main()
