from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
from functools import lru_cache
from jinja2 import Environment, FileSystemLoader, Template

from ..config import settings
from ..data.portfolio import PERSONAL, SKILLS, PROJECTS, BLOGS

router = APIRouter()


class Jinja2Templates:
    """Minimal Starlette-free Jinja2 renderer, avoids starlette 1.0.0 cache bug."""

    def __init__(self, directory: str | Path):
        self.directory = Path(directory)
        self.env = Environment(
            loader=FileSystemLoader(str(self.directory)),
            auto_reload=False,
            cache_size=0,  # Disable template-level cache entirely
        )

    def get_template(self, name: str) -> Template:
        # Bypass the env-level cache by loading fresh each time
        return self.env.loader.load(self.env, name, self.env.make_globals(None))

    def TemplateResponse(self, name: str, context: dict) -> HTMLResponse:
        template = self.get_template(name)
        content = template.render(**context)
        return HTMLResponse(content=content)


@lru_cache
def get_templates() -> Jinja2Templates:
    return Jinja2Templates(directory=str(settings.templates_dir / "portfolio"))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Render the main portfolio page."""
    tmpl = get_templates()
    return tmpl.TemplateResponse(
        "index.html",
        {
            "request": request,
            "personal": {**PERSONAL, "formspree_id": settings.formspree_id},
            "skills": SKILLS,
            "projects": PROJECTS,
            "blogs": BLOGS,
        },
    )


@router.get("/projects/{proj_id}", response_class=HTMLResponse)
async def project_detail(proj_id: str, request: Request) -> HTMLResponse:
    """Render a project detail page."""
    tmpl = get_templates()
    project = next((p for p in PROJECTS if p["id"] == proj_id), None)
    if not project:
        return HTMLResponse(content="<h1>Project not found</h1>", status_code=404)
    # Related projects
    related = [p for p in PROJECTS if p["id"] in project.get("related", [])]
    return tmpl.TemplateResponse(
        "project.html",
        {
            "request": request,
            "project": project,
            "personal": PERSONAL,
            "projects": PROJECTS,
            "related_projects": related,
        },
    )


@router.get("/blogs/{slug}", response_class=HTMLResponse)
async def blog_detail(slug: str, request: Request) -> HTMLResponse:
    """Render a blog article detail page."""
    tmpl = get_templates()
    blog = next((b for b in BLOGS if b["slug"] == slug), None)
    if not blog:
        return HTMLResponse(content="<h1>Article not found</h1>", status_code=404)
    return tmpl.TemplateResponse(
        "blog.html",
        {
            "request": request,
            "blog": blog,
            "personal": PERSONAL,
            "projects": PROJECTS,
        },
    )
