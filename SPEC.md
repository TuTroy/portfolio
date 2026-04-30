# Troy Portfolio · SPEC.md

## 1. Project Overview

**Name:** Troy Portfolio
**Type:** Personal portfolio / resume site
**Core:** Single-page personal portfolio showcasing Troy's skills, projects, experience, and contact info.
**URL:** https://troy-tu.github.io/

---

## 2. Architecture

### Backend: FastAPI + Jinja2

```
portfolio/
├── SPEC.md
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry + dev server
│   ├── config.py            # Pydantic settings
│   └── data/
│       ├── __init__.py
│       └── portfolio.py     # All portfolio data as typed Python constants
├── templates/
│   └── portfolio/
│       ├── base.html        # Base template with nav + footer
│       ├── index.html       # Home page
│       └── partials/        # Section partials
├── static/
│   ├── css/
│   │   └── portfolio.css    # Mobile-first CSS, CSS variables, dark mode
│   └── js/
│       └── portfolio.js     # Vanilla JS interactions
├── scripts/
│   ├── build.py             # Static site generator → output/
│   └── serve.py             # Local dev server (keep existing)
├── tests/
│   └── test_portfolio.py
└── data/                    # YAML source data (kept as-is for backward compat)
```

### Data Layer

All portfolio content defined in `src/data/portfolio.py` as typed Python dicts/lists.
Categories: personal, skills, projects, experience, education, contact, blogs.
No hardcoded content in templates.

### Frontend Design

**Theme:** Minimal, professional, fast.
**Theme:** Minimal, professional, fast.
**Color palette (CSS vars):**
- `--accent: #0ea5e9`
- `--accent-2: #6366f1` (blue-purple gradient, used for primary actions and highlights)
- `--accent-light: rgba(99, 102, 241, 0.07)`
- `--accent-dark: #0284c7`
- All other vars unchanged

**Fonts:** System fonts (no external CDN dependency).
**No Tailwind.** Plain CSS with custom properties.
**Dark mode** via `@media (prefers-color-scheme: dark)`.

### Interactions

- Smooth scroll between sections
- Scroll-reveal animations (IntersectionObserver, CSS-only transitions)
- Skill bars animate width when scrolled into view
- Project cards: hover lift + link icon reveal + shimmer on thumbnail + title color shift
- **Project filter**: animated show/hide with staggered fade-in (no abrupt display:none)
- **Navigation**: active section highlight via IntersectionObserver as user scrolls
- Navigation: sticky with backdrop blur; hamburger on mobile
- Contact form: vanilla JS with validation + success state (no Element Plus)
- Section reveal on scroll using IntersectionObserver

### Responsive Breakpoints

- Mobile: < 640px (single column, hamburger nav)
- Tablet: 640px - 1024px (2 columns where appropriate)
- Desktop: > 1024px (full layout)

### Templates

Jinja2 block structure:
```
base.html
  ├── nav (sticky, responsive)
  └── footer
index.html extends base.html
  ├── hero
  ├── about
  ├── roadmap
  ├── skills
  ├── projects
  ├── blogs
  ├── contact
  └── footer (from base)
```

---

## 3. Features

- Static HTML generation via `scripts/build.py`
- FastAPI dev server via `src/main.py`
- Fully typed data layer in `src/data/portfolio.py`
- Zero external CSS/JS dependencies (except Google Fonts optional)
- Mobile-first responsive CSS
- Dark mode support
- GitHub Pages compatible output
- Existing git history preserved

---

## 4. Constraints

- **Do NOT touch** `multi-agent-project/` directory
- **Keep** `data/` YAML files as-is
- **Do NOT** re-init git
- Static `index.html` in repo root regenerated from `scripts/build.py`
- All existing project data (ticket-classifier, annotation-platform, churn-prediction, sales-dashboard, data-warehouse, multi-agent-research) preserved as project entries
- Use real Troy data from USER.md

---

## 5. Build & Deploy

```bash
# Install dependencies
pip install -e .

# Dev server
uvicorn src.main:app --reload --port 5173

# Static build
python scripts/build.py

# Output: output/index.html → synced to repo root
```