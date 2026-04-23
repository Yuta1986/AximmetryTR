from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
EXPORT_SCRIPT = WORKSPACE_ROOT / "tools" / "export_pdf.py"

PATTERNS = [
    {"theme": "default", "toc_mode": "none", "target": "pdf"},
    {"theme": "default", "toc_mode": "inline", "target": "pdf"},
    {"theme": "default", "toc_mode": "sidebar", "target": "html"},
    {"theme": "mobeon", "toc_mode": "none", "target": "pdf"},
    {"theme": "mobeon", "toc_mode": "inline", "target": "pdf"},
    {"theme": "mobeon", "toc_mode": "sidebar", "target": "html"},
    {"theme": "mobeon-dark", "toc_mode": "none", "target": "pdf"},
    {"theme": "mobeon-dark", "toc_mode": "inline", "target": "pdf"},
    {"theme": "mobeon-dark", "toc_mode": "sidebar", "target": "html"},
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export the active Markdown into every supported pattern folder."
    )
    parser.add_argument("input", help="Markdown file to export.")
    parser.add_argument(
        "--output-dir",
        default="build/exports",
        help="Directory for output files.",
    )
    return parser.parse_args()


def run_export(input_path: str, output_dir: str, theme: str, toc_mode: str, target: str) -> None:
    command = [
        sys.executable,
        str(EXPORT_SCRIPT),
        input_path,
        "--output-dir",
        output_dir,
        "--target",
        target,
        "--theme",
        theme,
        "--toc-mode",
        toc_mode,
    ]
    print(
        "Sync pattern:",
        f"theme={theme}",
        f"toc={toc_mode}",
        f"target={target}",
    )
    subprocess.run(command, check=True, cwd=WORKSPACE_ROOT)


def main() -> None:
    args = parse_args()
    for pattern in PATTERNS:
        run_export(
            args.input,
            args.output_dir,
            pattern["theme"],
            pattern["toc_mode"],
            pattern["target"],
        )


if __name__ == "__main__":
    main()
