#!/usr/bin/env python3
"""
Portfolio static site generator.
Renders Jinja2 templates with Python data → static HTML in output/.
"""
from pathlib import Path
import shutil
import sys

# Ensure src is on path
sys.path.insert(0, str(Path(__file__).parent.parent))

from jinja2 import Environment, FileSystemLoader, select_autoescape
from src.data.portfolio import PERSONAL, SKILLS, PROJECTS, BLOGS
from src.config import settings

BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = settings.templates_dir
OUTPUT_DIR = BASE_DIR / "output"
STATIC_PROJ_DIR = OUTPUT_DIR / "static" / "projects"
BLOGS_OUTPUT_DIR = OUTPUT_DIR / "blogs"


def build():
    # Clean output dir
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "static").mkdir(parents=True, exist_ok=True)
    STATIC_PROJ_DIR.mkdir(parents=True, exist_ok=True)
    BLOGS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR / "portfolio"), encoding="utf-8"),
        autoescape=select_autoescape(["html", "xml"]),
    )

    personal = {**PERSONAL, "formspree_id": settings.formspree_id}

    # ── Render index.html ───────────────────────────────────────
    tmpl = env.get_template("index.html")
    html = tmpl.render(personal=personal, skills=SKILLS, projects=PROJECTS, blogs=BLOGS)
    out_index = OUTPUT_DIR / "index.html"
    out_index.write_text(html, encoding="utf-8")
    print(f"✅  Generated {out_index.relative_to(BASE_DIR)}")

    # ── Render project detail pages ─────────────────────────────
    tmpl_proj = env.get_template("project.html")
    for proj in PROJECTS:
        slug = proj["id"]
        html = tmpl_proj.render(project=proj, personal=personal, projects=PROJECTS)

        # output/static/projects/slug.html  (for /projects/slug routes)
        (STATIC_PROJ_DIR / f"{slug}.html").write_text(html, encoding="utf-8")

        # output/slug.html  (copied to root for backward compat)
        (OUTPUT_DIR / f"{slug}.html").write_text(html, encoding="utf-8")

        print(f"✅  Generated {slug}.html (output/ and output/static/projects/)")

    # ── Render blog detail pages ───────────────────────────────
    tmpl_blog = env.get_template("blog.html")
    for blog in BLOGS:
        slug = blog["slug"]
        html = tmpl_blog.render(blog=blog, personal=personal)

        # output/blogs/slug.html
        (BLOGS_OUTPUT_DIR / f"{slug}.html").write_text(html, encoding="utf-8")

        print(f"✅  Generated blogs/{slug}.html")

    # ── Sync to repo root ───────────────────────────────────────
    shutil.copy2(OUTPUT_DIR / "index.html", BASE_DIR / "index.html")
    for proj in PROJECTS:
        shutil.copy2(OUTPUT_DIR / f"{proj['id']}.html", BASE_DIR / f"{proj['id']}.html")
    for blog in BLOGS:
        shutil.copy2(BLOGS_OUTPUT_DIR / f"{blog['slug']}.html", BASE_DIR / f"{blog['slug']}.html")
    print(f"✅  Synced to repo root")

    print(f"\n📦 Build complete: {OUTPUT_DIR}")
    print(f"🚀  Dev server:  uvicorn src.main:app --reload --port 5173")


if __name__ == "__main__":
    build()