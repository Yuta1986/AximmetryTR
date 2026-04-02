from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
JAPANESE_PATTERN = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")
STYLE_PATHS = {
    "default": WORKSPACE_ROOT / "tools" / "pdf_style.css",
    "mobeon": WORKSPACE_ROOT / "tools" / "pdf_style_mobeon.css",
}
CALLOUT_TYPES = {
    "INFO": "info",
    "WARNING": "warning",
    "CRITICAL": "critical",
}


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
    parser.add_argument(
        "--theme",
        choices=sorted(STYLE_PATHS),
        default="default",
        help="Choose the export theme.",
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


def contains_japanese(text: str) -> bool:
    return bool(JAPANESE_PATTERN.search(text))


def get_style_path(theme: str) -> Path:
    style_path = STYLE_PATHS[theme]
    if not style_path.exists():
        print(f"Theme stylesheet not found: {style_path}", file=sys.stderr)
        sys.exit(1)
    return style_path


def annotate_callouts(body_html: str) -> str:
    for label, callout_type in CALLOUT_TYPES.items():
        body_html = re.sub(
            rf"<blockquote>\s*<p><strong>{label}</strong>",
            (
                f'<blockquote class="callout callout-{callout_type}">'
                f'<p><strong class="callout-label">{label}</strong>'
            ),
            body_html,
        )
    return body_html


def parse_document_header(markdown_text: str, fallback: str) -> tuple[str, str, str, str, str]:
    title = fallback
    subtitle = ""
    display_title = fallback
    kicker = ""
    body_markdown = markdown_text

    lines = markdown_text.splitlines()
    first_content_index = None
    for index, line in enumerate(lines):
        if line.strip():
            first_content_index = index
            break

    if first_content_index is not None and lines[first_content_index].startswith("# "):
        title = lines[first_content_index][2:].strip() or fallback
        next_index = first_content_index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1
        if next_index < len(lines) and lines[next_index].startswith("## "):
            subtitle = lines[next_index][3:].strip()
            body_start = next_index + 1
        else:
            body_start = first_content_index + 1

        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1

        body_markdown = "\n".join(lines[body_start:])

    if subtitle and contains_japanese(subtitle) and not contains_japanese(title):
        display_title = subtitle
        kicker = title
    else:
        display_title = title
        kicker = subtitle if subtitle else ""

    return title, subtitle, display_title, kicker, body_markdown


def build_html(
    markdown_text: str,
    title: str,
    subtitle: str,
    display_title: str,
    kicker: str,
    toc_mode: str,
    theme: str,
) -> str:
    markdown = load_markdown_module()
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists"])
    body_html = md.convert(markdown_text)
    body_html = annotate_callouts(body_html)
    toc_html = md.toc if toc_mode != "none" else ""
    style = get_style_path(theme).read_text(encoding="utf-8")

    header_parts = []
    if kicker:
        header_parts.append(f"<div class=\"doc-kicker\">{html.escape(kicker)}</div>")
    header_parts.append(f"<h1>{html.escape(display_title)}</h1>")
    if subtitle and kicker != subtitle and subtitle != display_title:
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
        button.textContent = collapsed ? "目次を表示" : "目次を隠す";
        button.setAttribute("aria-expanded", String(!collapsed));
      });
    })();
  </script>
"""

    body_class = f"toc-mode-{toc_mode} theme-{theme}"

    if toc_mode == "sidebar":
        content_html = f"""
  <button id="toc-toggle" class="toc-toggle" type="button" aria-controls="toc-sidebar" aria-expanded="true">
    目次を隠す
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
  <title>{html.escape(display_title)}{'' if not title or title == display_title else ' | ' + html.escape(title)}</title>
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


def build_suffix(theme: str, toc_mode: str) -> str:
    suffix = ""
    if theme != "default":
        suffix += f"_{theme}"
    if toc_mode == "inline":
        suffix += "_with_inline_toc"
    elif toc_mode == "sidebar":
        suffix += "_with_sidebar_toc"
    return suffix


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).resolve()
    ensure_markdown_file(input_path)

    output_dir = (WORKSPACE_ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    markdown_text = input_path.read_text(encoding="utf-8")
    title, subtitle, display_title, kicker, body_markdown = parse_document_header(
        markdown_text,
        input_path.stem,
    )

    suffix = build_suffix(args.theme, args.toc_mode)
    html_name = f"{normalize_output_name(input_path.stem)}{suffix}.html"
    html_path = output_dir / html_name

    html_text = build_html(
        body_markdown,
        title,
        subtitle,
        display_title,
        kicker,
        args.toc_mode,
        args.theme,
    )
    html_path.write_text(html_text, encoding="utf-8")

    print(f"HTML: {html_path}")

    if args.target in {"pdf", "both"}:
        pdf_path = export_pdf(html_path, output_dir)
        print(f"PDF:  {pdf_path}")


if __name__ == "__main__":
    main()
