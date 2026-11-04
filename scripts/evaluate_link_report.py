"""Fail link CI on stable broken links while reporting transient remote errors."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlsplit


TRANSIENT_HTTP_CODES = {401, 403, 408, 429}


def classify(report: dict) -> tuple[list[tuple[str, dict]], list[tuple[str, dict]]]:
    hard: list[tuple[str, dict]] = []
    warnings: list[tuple[str, dict]] = []
    for source, results in report.get("error_map", {}).items():
        for result in results:
            status = result.get("status", {})
            code = status.get("code")
            url = result.get("url", "")
            scheme = urlsplit(url).scheme
            detail = str(status.get("text", ""))
            if scheme == "file" or "invalid" in detail.lower():
                hard.append((source, result))
            elif isinstance(code, int) and 400 <= code < 500 and code not in TRANSIENT_HTTP_CODES:
                hard.append((source, result))
            else:
                warnings.append((source, result))
    for source, results in report.get("timeout_map", {}).items():
        warnings.extend((source, result) for result in results)
    return hard, warnings


def describe(source: str, result: dict) -> str:
    line = result.get("span", {}).get("line", "?")
    status = result.get("status", {})
    detail = status.get("text", "Timed out")
    return f"- `{source}:{line}`: <{result.get('url', '')}> — {detail}"


def evaluate(report: dict) -> tuple[int, str]:
    if not isinstance(report, dict) or not isinstance(report.get("total"), int):
        return 1, "# Link check\n\nInvalid lychee JSON report.\n"
    if report["total"] == 0:
        return 1, "# Link check\n\nLychee found no links.\n"

    hard, warnings = classify(report)
    lines = [
        "# Link check",
        "",
        f"Checked {report['total']} links; {len(hard)} hard failures; "
        f"{len(warnings)} transient or access warnings.",
        "",
    ]
    if hard:
        lines.extend(["## Broken links", ""])
        lines.extend(describe(source, result) for source, result in hard)
        lines.append("")
    if warnings:
        lines.extend(["## Remote warnings", ""])
        lines.extend(describe(source, result) for source, result in warnings)
        lines.append("")
    return (1 if hard else 0), "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: evaluate_link_report.py REPORT.json", file=sys.stderr)
        return 2
    try:
        report = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"Could not read lychee report: {exc}", file=sys.stderr)
        return 2
    code, summary = evaluate(report)
    print(summary, end="")
    if summary_path := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary_path, "a", encoding="utf-8") as stream:
            stream.write(summary)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
