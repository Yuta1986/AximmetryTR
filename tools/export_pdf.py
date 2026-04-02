from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
STYLE_PATH = WORKSPACE_ROOT / "tools" / "pdf_style.css"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Markdown to HTML and PDF with PDF bookmarks via LibreOffice."
    )
    parser.add_argument("input", help="Markdown file to export.")
    parser.add_argument("--output-dir", default="exports", help="Directory for output files.")
    parser.add_argument(
        "--target",
        choices=["html", "pdf", "both"],
        default="pdf",
        help="Export HTML only, PDF only, or both.",
    )
    parser.add_argument(
        "--toc-mode",
        choices=["none", "inline", "sidebar"],
        default="none",
        help="Choose no TOC, inline TOC, or a sidebar TOC in the generated HTML.",
    )
    return parser.parse_args()


def load_markdown_module():
    try:
        import markdown  # type: ignore
    except ImportError:
        print(
            "Missing Python package 'markdown'. Run the VS Code task "
            "'PDF: Install Markdown Dependency' once first.",
            file=sys.stderr,
        )
        sys.exit(1)
    return markdown


def find_soffice() -> Path:
    candidates = [
        Path(r"C:\Program Files\LibreOffice\program\soffice.exe"),
        Path(r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate

    found = shutil.which("soffice")
    if found:
        return Path(found)

    print(
        "LibreOffice (soffice.exe) was not found. Install LibreOffice or update the script paths.",
        file=sys.stderr,
    )
    sys.exit(1)


def extract_title(markdown_text: str, fallback: str) -> tuple[str, str]:
    title = fallback
    subtitle = ""

    lines = markdown_text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            if index + 1 < len(lines) and lines[index + 1].startswith("## "):
                subtitle = lines[index + 1][3:].strip()
            break

    return title, subtitle


def build_html(markdown_text: str, title: str, subtitle: str, toc_mode: str) -> str:
    markdown = load_markdown_module()
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists"])
    body_html = md.convert(markdown_text)
    toc_html = md.toc if toc_mode != "none" else ""
    style = STYLE_PATH.read_text(encoding="utf-8")

    header_parts = [
        f"<h1>{html.escape(title)}</h1>",
    ]
    if subtitle:
        header_parts.append(f"<div class=\"doc-subtitle\">{html.escape(subtitle)}</div>")
    header_html = "\n".join(header_parts)

    inline_toc_block = ""
    sidebar_toc_block = ""
    script_block = ""

    if toc_html and toc_mode == "inline":
        inline_toc_block = (
            "<section class=\"toc-block\">"
            "<h2>Table of Contents / 目次</h2>"
            f"{toc_html}"
            "</section>"
        )

    if toc_html and toc_mode == "sidebar":
        sidebar_toc_block = (
            "<aside id=\"toc-sidebar\" class=\"toc-sidebar\">"
            "<h2>Table of Contents / 目次</h2>"
            f"{toc_html}"
            "</aside>"
        )
        script_block = """
  <script>
    (function () {
      const body = document.body;
      const button = document.getElementById("toc-toggle");
      if (!button) return;
      button.addEventListener("click", function () {
        const collapsed = body.classList.toggle("toc-collapsed");
        button.textContent = collapsed ? "Show TOC" : "Hide TOC";
        button.setAttribute("aria-expanded", String(!collapsed));
      });
    })();
  </script>
"""

    body_class = f"toc-mode-{toc_mode}"

    if toc_mode == "sidebar":
        content_html = f"""
  <button id="toc-toggle" class="toc-toggle" type="button" aria-controls="toc-sidebar" aria-expanded="true">
    Hide TOC
  </button>
  <div class="page-layout">
    {sidebar_toc_block}
    <div class="content-shell">
      <header class="doc-header">
        {header_html}
      </header>
      <main class="doc-main">
        {body_html}
      </main>
    </div>
  </div>
{script_block}"""
    else:
        content_html = f"""
  <header class="doc-header">
    {header_html}
  </header>
  {inline_toc_block}
  <main class="doc-main">
    {body_html}
  </main>"""

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
{style}
  </style>
</head>
<body class="{body_class}">
{content_html}
</body>
</html>
"""


def export_pdf(html_path: Path, output_dir: Path) -> Path:
    soffice = find_soffice()
    subprocess.run(
        [
            str(soffice),
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(output_dir),
            str(html_path),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return output_dir / f"{html_path.stem}.pdf"


def ensure_markdown_file(path: Path) -> None:
    if not path.exists():
        print(f"Input file not found: {path}", file=sys.stderr)
        sys.exit(1)
    if path.suffix.lower() != ".md":
        print(f"Input file must be a Markdown file: {path}", file=sys.stderr)
        sys.exit(1)


def normalize_output_name(stem: str) -> str:
    return re.sub(r"[^\w.-]+", "_", stem).strip("_") or "document"


def build_suffix(toc_mode: str) -> str:
    if toc_mode == "inline":
        return "_with_inline_toc"
    if toc_mode == "sidebar":
        return "_with_sidebar_toc"
    return ""


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).resolve()
    ensure_markdown_file(input_path)

    output_dir = (WORKSPACE_ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    markdown_text = input_path.read_text(encoding="utf-8")
    title, subtitle = extract_title(markdown_text, input_path.stem)

    suffix = build_suffix(args.toc_mode)
    html_name = f"{normalize_output_name(input_path.stem)}{suffix}.html"
    html_path = output_dir / html_name

    html_text = build_html(markdown_text, title, subtitle, args.toc_mode)
    html_path.write_text(html_text, encoding="utf-8")

    print(f"HTML: {html_path}")

    if args.target in {"pdf", "both"}:
        pdf_path = export_pdf(html_path, output_dir)
        print(f"PDF:  {pdf_path}")


if __name__ == "__main__":
    main()
