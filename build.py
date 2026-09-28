#!/usr/bin/env python3
"""
Tiny static-site builder for amantambi.github.io.

    content/    YAML + Markdown (the stuff you edit)
    templates/  Jinja2 templates (layout)
    static/     CSS, JS, media (copied verbatim)
    files/      PDFs etc. (copied to /files/)
    site/       build output (deployed to GitHub Pages)

Usage:
    python build.py            # build once into site/
    python build.py --serve    # build, then serve on http://localhost:8000 and rebuild on change
"""
import argparse
import os
import http.server
import re
import shutil
import sys
import threading
import time
from datetime import date
from functools import partial
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
FILES = ROOT / "files"
OUT = ROOT / "site"  # overridable with --out

MD = markdown.Markdown(
    extensions=["extra", "sane_lists", "smarty", "attr_list", "md_in_html", "toc"],
    output_format="html5",
)

FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


def md(text: str) -> str:
    """Markdown -> HTML (block level)."""
    MD.reset()
    return MD.convert(text or "")


def mdi(text: str) -> str:
    """Markdown -> HTML for a single inline run (no wrapping <p>)."""
    html = md(text).strip()
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        html = html[3:-4]
    return html


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_markdown_doc(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    m = FRONT_MATTER.match(raw)
    meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, raw)
    doc = dict(meta)
    doc.setdefault("slug", path.stem)
    doc["body_html"] = md(body)
    return doc


def load_projects() -> list[dict]:
    projects = [load_markdown_doc(p) for p in sorted((CONTENT / "projects").glob("*.md"))]
    for p in projects:
        p.setdefault("featured", False)
        p.setdefault("page", True)
        p.setdefault("tags", [])
        p.setdefault("links", [])
        p.setdefault("highlights", [])
        p.setdefault("media", {"type": "placeholder"})
        p.setdefault("order", 999)
        p["url"] = f"/work/{p['slug']}/" if p["page"] else (p.get("link") or "")
    projects.sort(key=lambda p: p["order"])
    return projects


def build(verbose: bool = True) -> None:
    # A concurrent `--serve` watcher may be rebuilding at the same moment; retry the reset.
    for attempt in range(5):
        try:
            if OUT.exists():
                shutil.rmtree(OUT)
            shutil.copytree(STATIC, OUT)
            if FILES.exists():
                shutil.copytree(FILES, OUT / "files")
            (OUT / ".nojekyll").touch()
            break
        except (OSError, shutil.Error):
            if attempt == 4:
                raise
            time.sleep(0.5)

    site = load_yaml(CONTENT / "site.yaml")
    projects = load_projects()
    featured = [p for p in projects if p["featured"]]
    more = [p for p in projects if not p["featured"]]
    ctx = dict(
        site=site,
        projects=projects,
        featured=featured,
        more=more,
        experience=load_yaml(CONTENT / "experience.yaml"),
        education=load_yaml(CONTENT / "education.yaml"),
        publications=load_yaml(CONTENT / "publications.yaml"),
        teaching=load_yaml(CONTENT / "teaching.yaml"),
        about_html=md((CONTENT / "about.md").read_text(encoding="utf-8")),
        year=date.today().year,
        build_id=int(time.time()),
    )

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["md"] = md
    env.filters["mdi"] = mdi

    def render(template: str, out: Path, **extra) -> None:
        html = env.get_template(template).render(**ctx, **extra)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")

    render("index.html", OUT / "index.html", page_url="/")
    render("work.html", OUT / "work" / "index.html", page_url="/work/")
    render("404.html", OUT / "404.html", page_url="/404.html")
    paged = [p for p in projects if p["page"]]
    for i, p in enumerate(paged):
        render(
            "project.html",
            OUT / "work" / p["slug"] / "index.html",
            page_url=p["url"],
            project=p,
            prev=paged[i - 1] if i > 0 else None,
            next=paged[i + 1] if i + 1 < len(paged) else None,
        )
    if verbose:
        n = sum(1 for _ in OUT.rglob("*.html"))
        print(f"built {n} pages -> {OUT}/")


def snapshot() -> dict[Path, float]:
    files = {}
    for d in (CONTENT, TEMPLATES, STATIC, FILES):
        if d.exists():
            for f in d.rglob("*"):
                if f.is_file():
                    files[f] = f.stat().st_mtime
    files[ROOT / "build.py"] = (ROOT / "build.py").stat().st_mtime
    return files


def serve(port: int) -> None:
    build()
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    print(f"serving http://localhost:{port}  (Ctrl-C to stop)")
    last = snapshot()
    try:
        while True:
            time.sleep(0.7)
            now = snapshot()
            if now.get(ROOT / "build.py") != last.get(ROOT / "build.py"):
                print("build.py changed, restarting server", flush=True)
                httpd.shutdown(); httpd.server_close()
                sys.stdout.flush()
                os.execv(sys.executable, [sys.executable, *sys.argv])
            if now != last:
                last = now
                try:
                    build()
                except Exception as e:  # keep serving on a bad edit
                    print(f"build failed: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true", help="serve site/ locally and rebuild on change")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--out", help="build into this folder instead of site/")
    args = ap.parse_args()
    if args.out:
        OUT = Path(args.out).resolve()
    serve(args.port) if args.serve else build()
