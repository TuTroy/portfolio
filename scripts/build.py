#!/usr/bin/env python3
"""
Portfolio 构建脚本
从 YAML 数据 + HTML 模板生成静态页面
"""
import os
import yaml
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

# 路径配置
BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
STATIC_DIR = OUTPUT_DIR / "static" / "projects"


def load_yaml(filename):
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_and_build():
    profile = load_yaml("profile.yaml")
    projects = load_yaml("projects.yaml")
    skills = load_yaml("skills.yaml")

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR, encoding="utf-8"),
        autoescape=select_autoescape(["html", "xml"])
    )

    # 清理并重建输出目录
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "static").mkdir(parents=True, exist_ok=True)
    STATIC_DIR.mkdir(parents=True, exist_ok=True)

    # 渲染 index.html
    tmpl_index = env.get_template("index.html")
    html_index = tmpl_index.render(
        profile=profile,
        projects=projects["projects"],
        skills=skills,
    )
    with open(OUTPUT_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(html_index)
    print("✅ 生成了 index.html")

    # 渲染项目详情页
    tmpl_proj = env.get_template("project.html")
    for proj_id in ["ticket-classifier", "annotation-platform"]:
        proj = next(p for p in projects["projects"] if p["id"] == proj_id)

        # 渲染到 static/projects/（返回路径 ../../index.html）
        html = tmpl_proj.render(project=proj, back_path="../../index.html")
        with open(STATIC_DIR / f"{proj_id}.html", "w", encoding="utf-8") as f:
            f.write(html)

        # 复制到根目录（返回路径 index.html）
        html_root = tmpl_proj.render(project=proj, back_path="index.html")
        with open(OUTPUT_DIR / f"{proj_id}.html", "w", encoding="utf-8") as f:
            f.write(html_root)

        print(f"✅ 生成了 {proj_id}.html（两处）")

    # 同步到仓库根目录（GitHub Pages 从根目录读取）
    shutil.copy2(OUTPUT_DIR / "index.html", BASE_DIR / "index.html")
    for proj_id in ["ticket-classifier", "annotation-platform"]:
        shutil.copy2(OUTPUT_DIR / f"{proj_id}.html", BASE_DIR / f"{proj_id}.html")
    print(f"✅ 同步到仓库根目录")

    print(f"\n📦 构建完成: {OUTPUT_DIR}")
    print(f"🚀 启动服务: cd {BASE_DIR} && python3 serve.py")


if __name__ == "__main__":
    render_and_build()
