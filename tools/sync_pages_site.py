from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync exported guide artifacts into the GitHub Pages site folder."
    )
    parser.add_argument("input", help="Markdown file that was exported.")
    parser.add_argument(
        "--exports-dir",
        default="build/exports",
        help="Directory that contains the generated export pattern folders.",
    )
    parser.add_argument(
        "--site-dir",
        default="site",
        help="Directory used as the GitHub Pages publish root.",
    )
    return parser.parse_args()


def ensure_markdown_file(path: Path) -> None:
    if not path.exists():
        print(f"Input file does not exist: {path}", file=sys.stderr)
        sys.exit(1)
    if path.suffix.lower() != ".md":
        print(f"Input file must be a Markdown file: {path}", file=sys.stderr)
        sys.exit(1)


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"Copied: {source} -> {destination}")


def main() -> None:
    args = parse_args()

    input_path = (WORKSPACE_ROOT / args.input).resolve()
    ensure_markdown_file(input_path)

    exports_dir = (WORKSPACE_ROOT / args.exports_dir).resolve()
    site_dir = (WORKSPACE_ROOT / args.site_dir).resolve()

    base_name = input_path.stem
    source_html = exports_dir / "default" / "sidebar" / f"{base_name}.html"
    source_pdf = exports_dir / "default" / "none" / f"{base_name}.pdf"

    if not source_html.exists():
        print(f"Missing exported HTML for Pages: {source_html}", file=sys.stderr)
        sys.exit(1)
    if not source_pdf.exists():
        print(f"Missing exported PDF for Pages: {source_pdf}", file=sys.stderr)
        sys.exit(1)

    version_dir = site_dir / "versions"

    copy_file(source_html, site_dir / "index.html")
    copy_file(source_pdf, site_dir / f"{base_name}.pdf")
    copy_file(source_html, version_dir / f"{base_name}.html")
    copy_file(source_pdf, version_dir / f"{base_name}.pdf")


if __name__ == "__main__":
    main()
