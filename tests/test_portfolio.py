"""Tests for Troy Portfolio."""
import sys
from pathlib import Path

# Ensure src is importable
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.portfolio import PERSONAL, SKILLS, PROJECTS, BLOGS
from src.config import settings


def test_personal_has_required_fields():
    required = ("name", "email", "wechat", "hero_title", "hero_subtitle", "about")
    for field in required:
        assert field in PERSONAL, f"PERSONAL missing field: {field}"


def test_personal_non_empty():
    assert PERSONAL["name"]
    assert PERSONAL["email"]
    assert "@" in PERSONAL["email"]


def test_skills_is_list():
    assert isinstance(SKILLS, list)
    assert len(SKILLS) > 0


def test_skills_have_required_fields():
    for skill in SKILLS:
        assert "name" in skill
        assert "pct" in skill
        assert 0 <= skill["pct"] <= 100


def test_projects_is_list():
    assert isinstance(PROJECTS, list)
    assert len(PROJECTS) > 0


def test_projects_have_required_fields():
    for proj in PROJECTS:
        assert "id" in proj
        assert "title" in proj
        assert "type" in proj


def test_projects_unique_ids():
    ids = [p["id"] for p in PROJECTS]
    assert len(ids) == len(set(ids)), "Duplicate project IDs found"


def test_blogs_is_list():
    assert isinstance(BLOGS, list)


def test_config_static_dir_exists():
    assert settings.static_dir.exists(), f"static_dir not found: {settings.static_dir}"


def test_config_templates_dir_exists():
    assert settings.templates_dir.exists(), f"templates_dir not found: {settings.templates_dir}"


def test_output_index_generated():
    output_index = Path(__file__).parent.parent / "output" / "index.html"
    assert output_index.exists(), f"output/index.html not found. Run: python scripts/build.py"
    content = output_index.read_text(encoding="utf-8")
    assert "Troy" in content or "炎钊" in content
    assert "<html" in content.lower()


def test_all_project_slugs_have_detail_page():
    output_dir = Path(__file__).parent.parent / "output"
    for proj in PROJECTS:
        slug = proj["id"]
        detail = output_dir / f"{slug}.html"
        assert detail.exists(), f"Missing output/{slug}.html"