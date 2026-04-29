# Troy Portfolio

> Personal portfolio of 涂炎钊 (Troy) — 数据分析师转型 AI 应用者

**Tech stack:** FastAPI + Jinja2 · Mobile-first CSS · Zero external CSS/JS deps

---

## 🎯 Project Structure

```
portfolio/
├── src/
│   ├── main.py              # FastAPI app entry
│   ├── config.py            # Pydantic settings
│   └── data/
│       └── portfolio.py     # All portfolio data (Python constants)
├── templates/portfolio/
│   ├── base.html            # Base template (nav + footer)
│   ├── index.html           # Home page
│   └── project.html         # Project detail template
├── static/
│   ├── css/portfolio.css    # Mobile-first CSS, dark mode
│   └── js/portfolio.js      # Vanilla JS interactions
├── scripts/
│   └── build.py             # Static site generator → output/
├── tests/
│   └── test_portfolio.py    # Data + build sanity checks
├── output/                  # Generated static HTML
├── data/                    # YAML source data (backward compat)
└── multi-agent-project/     # AI project sub-dir (untouched)
```

## 🚀 Quick Start

```bash
# Install dependencies
pip install fastapi jinja2 uvicorn pydantic pydantic-settings pyyaml

# Static build (generates output/)
python scripts/build.py

# Dev server (FastAPI + hot reload)
uvicorn src.main:app --reload --port 5173
```

## 📦 Static Build

```bash
python scripts/build.py
```

Outputs:
- `output/index.html` — main page
- `output/<slug>.html` — project detail pages (all 6 projects)
- `output/static/projects/<slug>.html` — for `/projects/<slug>` routing

Also copies `index.html` and all project pages to the repo root for GitHub Pages.

## ✅ Features

- **Engineering-grade Python structure** — typed data layer, FastAPI routes, Pydantic settings
- **Mobile-first responsive CSS** — 3 breakpoints, hamburger nav, no external deps
- **Dark mode** — `@media (prefers-color-scheme: dark)` with full variable override
- **Scroll-reveal animations** — IntersectionObserver, skill bar animations
- **Vanilla JS contact form** — validation, Formspree integration, success state
- **6 projects preserved** — ticket-classifier, annotation-platform, churn-prediction, sales-dashboard, data-warehouse, multi-agent-research
- **Git history preserved** — no `git init`, no `multi-agent-project/` touched

## 📝 Writing New Content

Edit `src/data/portfolio.py` to add or modify:
- `PERSONAL` — bio, contact, stats, roadmap
- `SKILLS` — name, icon, desc, pct
- `PROJECTS` — id, title, tags, metrics, architecture, achievements
- `BLOGS` — title, date, read_time, desc

Then rebuild:
```bash
python scripts/build.py
```

## 🧪 Tests

```bash
# Manual verification (no pytest needed)
python3 -c "
import sys; sys.path.insert(0, '.')
from src.data.portfolio import PERSONAL, SKILLS, PROJECTS, BLOGS
from src.config import settings
print('✅ All data loaded OK')
print('✅ Projects:', len(PROJECTS))
"
```