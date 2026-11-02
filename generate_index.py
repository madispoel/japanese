from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent


def natural_key(value: str) -> list[int | str]:
    return [int(part) if part.isdigit() else part.casefold()
            for part in re.split(r"(\d+)", value)]


def page_title(path: Path) -> str:
    chapter = re.fullmatch(r"chapter[-_ ]?(\d+)(?:_kanji)?", path.stem, re.IGNORECASE)
    if chapter:
        suffix = " Kanji" if path.stem.casefold().endswith("_kanji") else ""
        return f"Chapter {chapter.group(1)}{suffix}"
    return path.stem.replace("-", " ").replace("_", " ").title()


def chapter_pages() -> list[Path]:
    return sorted(
        (path for path in ROOT.glob("*.html") if path.name.casefold() != "index.html"),
        key=lambda path: natural_key(path.name),
    )


def build_index(pages: list[Path]) -> str:
    page_links = "\n".join(
        f'        <a class="chapter" href="{quote(path.name)}">'
        f'<span>{html.escape(page_title(path))}</span>'
        '<span class="arrow" aria-hidden="true">→</span></a>'
        for path in pages
    )
    empty_message = (
        ""
        if pages
        else '<p class="empty">Add HTML flashcard pages to this repository to list them here.</p>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fff1f7">
  <title>Japanese Flashcards · Chapters</title>
  <style>
    :root {{
      color-scheme: light;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #3b3044;
      background: #fff1f7;
      font-synthesis: none;
      text-rendering: optimizeLegibility;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      display: grid;
      min-height: 100vh;
      min-height: 100dvh;
      margin: 0;
      padding: 28px 18px;
      place-items: center;
      background:
        radial-gradient(circle at 12% 18%, #f8d8e8 0 2px, transparent 3px),
        radial-gradient(circle at 88% 76%, #e8defa 0 3px, transparent 4px),
        radial-gradient(ellipse at 50% 42%, #fff 0, #fff8fc 48%, #f9eaf4 100%);
    }}
    main {{
      width: min(100%, 560px);
      padding: clamp(24px, 6vw, 44px);
      border: 2px solid #f0d5e4;
      border-radius: 28px;
      background: #fff;
      box-shadow: 0 18px 55px #743b5a15;
    }}
    h1 {{ margin: 0; font-size: clamp(1.7rem, 6vw, 2.3rem); }}
    .intro {{ margin: 10px 0 24px; color: #817588; line-height: 1.5; }}
    nav {{ display: grid; gap: 10px; }}
    .chapter {{
      display: flex;
      min-height: 58px;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 14px 17px;
      border: 1px solid #f0dce8;
      border-radius: 14px;
      background: #fffafd;
      color: #554258;
      font-weight: 700;
      text-decoration: none;
      transition: border-color 130ms ease, transform 130ms ease, background 130ms ease;
    }}
    .chapter:hover {{ transform: translateY(-2px); border-color: #e595b8; background: #fff0f6; }}
    .chapter:focus-visible {{ outline: 3px solid #eca5c3; outline-offset: 3px; }}
    .arrow {{ color: #b94178; font-size: 1.3rem; }}
    .empty {{ color: #817588; }}
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{ scroll-behavior: auto !important; transition-duration: 0.01ms !important; }}
    }}
  </style>
</head>
<body>
  <main>
    <h1>Japanese Flashcards</h1>
    <p class="intro">Choose a chapter to start studying.</p>
    <nav aria-label="Flashcard chapters">
{page_links}
    </nav>
{empty_message}
  </main>
</body>
</html>
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an index of the repository's HTML pages.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT,
        help="Output directory (HTML pages are copied here alongside the generated index).",
    )
    args = parser.parse_args()
    pages = chapter_pages()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.output_dir.resolve() != ROOT:
        for page in pages:
            shutil.copy2(page, args.output_dir / page.name)
    (args.output_dir / "index.html").write_bytes(build_index(pages).encode("utf-8"))
    print(f"Generated index.html with {len(pages)} chapter page(s) in {args.output_dir}.")
