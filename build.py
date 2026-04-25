#!/usr/bin/env python3
"""portfolio build script — 读取 YAML 数据，生成静态 HTML"""

import yaml, os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE = Path(__file__).parent.resolve()
DATA = BASE / "data"
TPLS = BASE / "templates"
OUT  = BASE / "output"
OUT.mkdir(exist_ok=True)

def load(name):
    with open(DATA / f"{name}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 加载数据
config = load("config")
skills = load("skills")
projects = load("projects")
blogs = load("blogs")

# 准备渲染上下文
ctx = {
    **config,
    "skills":   skills["skills"],
    "projects": projects["projects"],
    "blogs":    blogs["blogs"],
}

# Jinja2 环境
env = Environment(loader=FileSystemLoader(str(TPLS)), autoescape=["html", "xml"])
from datetime import datetime
env.globals["year"] = datetime.now().year

# 生成 index.html
tmpl = env.get_template("index.html")
html = tmpl.render(**ctx)
(OUT / "index.html").write_text(html, encoding="utf-8")
print(f"✅ 生成了 {OUT / 'index.html'}")

# 复制项目详情页
for f in (BASE / "static" / "projects").glob("*.html"):
    dst = OUT / f.name
    dst.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"✅ 复制了 {dst}")

print(f"\n🎉 构建完成，共 {len(ctx['projects'])} 个项目、{len(ctx['blogs'])} 篇文章")
