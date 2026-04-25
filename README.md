# 涂炎钊 · 个人主页

数据分析师转型AI应用者 · 个人作品集

## 本地运行

```bash
cd portfolio

# 方式一：直接起服务（先构建）
python3 build.py
python3 -m http.server 8080

# 方式二：一键启动
bash start.sh
```

打开浏览器访问 **http://localhost:8080**

## 更新内容

改内容不需要碰 HTML，直接改 YAML 文件，然后重新构建：

| 想改什么 | 编辑文件 |
|---------|---------|
| 个人介绍、联系方式、Hero | `data/config.yaml` |
| 技能（名字、图标、熟练度） | `data/skills.yaml` |
| 项目（标题、描述、标签、指标） | `data/projects.yaml` |
| 文章列表 | `data/blogs.yaml` |

改完后运行 `python3 build.py` 即可。

## 联系表单

表单使用 [Formspree](https://formspree.io/)：

1. 去 [formspree.io](https://formspree.io/) 注册并创建 Form
2. 获取 Form ID，填入 `data/config.yaml` 中的 `formspree_id`
3. 重新 `python3 build.py`

## 技术栈

- **构建**：Python + Jinja2 + YAML
- **前端**：原生 HTML/CSS + Vue 3 + Element Plus（CDN）
- **部署**：纯静态，可发布到 Vercel / Netlify / GitHub Pages

## 项目结构

```
portfolio/
├── data/                   # 📝 内容数据（改这里）
│   ├── config.yaml
│   ├── skills.yaml
│   ├── projects.yaml
│   └── blogs.yaml
│
├── templates/              # 🎨 HTML 模板
│   ├── base.html
│   └── index.html
│
├── static/                # 📄 静态文件（直接复制）
│   └── projects/
│       ├── ticket-classifier.html
│       └── annotation-platform.html
│
├── output/                 # 📦 构建产物（可部署）
│   ├── index.html
│   └── projects/
│
├── build.py               # 🏗️  构建脚本
├── start.sh              # 🚀 启动脚本
└── README.md
```
