"""All portfolio data as typed Python constants."""
from typing import TypedDict


class SkillDict(TypedDict):
    name: str
    icon: str
    desc: str
    pct: int


class MetricDict(TypedDict):
    value: str
    highlight: bool


class ProjectDict(TypedDict):
    id: str
    type: str
    title: str
    desc: str
    thumb: str
    metrics: list[MetricDict]
    tags: list[str]
    status: str
    year: int
    overview: str
    architecture: list[str]
    achievements: list[str]
    related: list[str]


class RoadMapCardDict(TypedDict):
    step: str
    title: str
    points: list[str]


class BlogDict(TypedDict):
    slug: str
    type: str
    title: str
    date: str
    read_time: str
    desc: str
    content: str


# ─── Personal ────────────────────────────────────────────────────────────────

PERSONAL = {
    "name": "涂炎钊",
    "nickname": "Troy",
    "badge": "数据分析师 · 转型 AI 应用",
    "email": "yanzhao.tu@email.com",
    "wechat": "yan_zhao_tu",
    "github": "",
    "formspree_id": "YOUR_FORM_ID",
    "site_title": "Troy · 数据分析师转型AI应用者",
    "site_description": (
        "5年数据领域经验，深耕大数据处理与业务数据分析。"
        "2025年起系统学习大模型应用：Prompt工程、RAG、AI Agent、向量数据库。"
        "擅长大数据分析、机器学习建模与 AI 应用落地，致力于成为 AI 应用工程师。"
    ),
    "location": "深圳·龙岗",
    "hero_title": "用数据驱动决策",
    "hero_subtitle": "用 AI 创造价值",
    "hero_subtitle2": "数据分析 × AI 应用实践",
    "stats": [
        {"value": "5年+", "label": "数据领域"},
        {"value": "AI+", "label": "转型进行中"},
        {"value": "∞", "label": "持续学习中"},
    ],
    "about": (
        "涂炎钊（Troy），深圳，本科毕业。"
        "5年数据领域经验：曾从事运维工程与大数据开发，现专注数据分析与业务洞察。"
        "擅长大数据处理（Spark/Hive）、SQL建模、机器学习与数据可视化。"
        "2025年起系统学习大模型应用：Prompt工程、RAG检索、AI Agent设计。"
        "记录从数据分析出发，向 AI 应用探索的转型之路。"
    ),
    "highlights": [
        {"icon": "📊", "text": "数据分析"},
        {"icon": "🧮", "text": "大数据处理"},
        {"icon": "🤖", "text": "AI 应用"},
        {"icon": "📝", "text": "技术沉淀"},
    ],
    "hero_tags": ["Python", "SQL", "LLM", "RAG", "AI Agent", "数据可视化"],
    "roadmap_intro": (
        "AI 正在改变数据的玩法。不只是描述过去，而是能预测未来、生成洞见。"
        "记录从传统数据分析出发，向 LLM 应用、AI Agent 探索的过程。"
    ),
    "roadmap": [
        RoadMapCardDict(
            step="基础 ✅",
            title="数据能力",
            points=["Python / SQL", "大数据处理 Spark/Hive", "数据可视化", "业务洞察"],
        ),
        RoadMapCardDict(
            step="进行中 🔥",
            title="AI 技能",
            points=["Prompt 工程", "RAG 检索", "AI Agent", "向量数据库"],
        ),
        RoadMapCardDict(
            step="计划中 🎯",
            title="进阶方向",
            points=["模型微调", "MLOps", "产品落地", "技术输出"],
        ),
    ],
    "contact_note": "数据分析、AI 应用、技术交流都可以找我。也欢迎各种合作机会。",
}

# ─── Skills ──────────────────────────────────────────────────────────────────

SKILLS: list[SkillDict] = [
    {"name": "Python", "icon": "🐍", "desc": "数据处理、NLP、脚本自动化", "pct": 92},
    {"name": "SQL", "icon": "🗃️", "desc": "复杂查询、性能优化、数据管道", "pct": 88},
    {"name": "机器学习", "icon": "📈", "desc": "XGBoost、Sklearn、特征工程", "pct": 80},
    {"name": "AI / LLM", "icon": "🤖", "desc": "RAG、Agent、Prompt工程", "pct": 75},
    {"name": "数据可视化", "icon": "📊", "desc": "Tableau、Plotly、数据故事", "pct": 85},
    {"name": "AI Agent", "icon": "🧠", "desc": "工作流设计、工具调用、AutoGPT", "pct": 68},
    {"name": "云平台", "icon": "☁️", "desc": "FastAPI、Docker、AWS/阿里云", "pct": 70},
]

# ─── Projects ────────────────────────────────────────────────────────────────

PROJECTS: list[ProjectDict] = [
    {
        "id": "ticket-classifier",
        "type": "local",
        "title": "客服工单智能分类助手",
        "desc": "基于 LLM + RAG 构建客服工单分类与回复推荐系统，日均处理工单1200+，分类准确率91%。点击查看完整技术方案。",
        "thumb": "🤖",
        "metrics": [
            {"value": "日均 1200+ 工单", "highlight": True},
            {"value": "准确率 91%", "highlight": False},
            {"value": "响应效率提升 40%", "highlight": False},
        ],
        "tags": ["LLM", "RAG", "LangChain", "FastAPI"],
        "status": "进行中",
        "year": 2026,
        "overview": (
            "基于 LLM + RAG 构建客服工单分类与回复推荐系统，日均处理工单1200+，分类准确率91%。"
            "通过检索增强生成技术，结合企业历史工单知识库，实现智能分类和推荐回复。"
        ),
        "architecture": [
            "LLM：调用 GPT / Claude 系列模型",
            "RAG：LangChain + Chroma 向量数据库",
            "知识库：历史工单 + 产品文档",
            "API：FastAPI 提供推理接口",
        ],
        "achievements": [
            "日均处理 1200+ 工单",
            "分类准确率 91%",
            "客服响应效率提升 40%",
        ],
        "related": ["annotation-platform", "churn-prediction"],
    },
    {
        "id": "annotation-platform",
        "type": "local",
        "title": "数据标注平台",
        "desc": "FastAPI + Vue3 搭建的内部标注平台，支持6种任务类型，日均标注量5000+，标注效率提升35%。点击查看架构设计。",
        "thumb": "🛠️",
        "metrics": [
            {"value": "6 种任务类型", "highlight": True},
            {"value": "日均 5000+ 标注量", "highlight": False},
            {"value": "效率提升 35%", "highlight": False},
        ],
        "tags": ["FastAPI", "Vue3", "PostgreSQL", "Docker"],
        "status": "已完成",
        "year": 2026,
        "overview": (
            "为解决模型训练标注数据需求，用 FastAPI + Vue3 搭建内部标注平台。"
            "支持文本分类、实体识别、情感分析等6种任务类型，日均标注量5000+。"
        ),
        "architecture": [
            "后端：FastAPI + SQLAlchemy",
            "前端：Vue3 + Element Plus",
            "数据库：PostgreSQL",
            "部署：Docker 容器化",
        ],
        "achievements": [
            "日均标注量 5000+",
            "支持 6 种任务类型",
            "标注效率提升 35%",
        ],
        "related": ["ticket-classifier", "multi-agent-research"],
    },
    {
        "id": "churn-prediction",
        "type": "local",
        "title": "电商用户流失预测系统",
        "desc": "基于 XGBoost 构建用户流失预警模型，提前14天预测潜在流失用户，准确率83%，落地后留存提升12%。",
        "thumb": "📊",
        "metrics": [
            {"value": "准确率 83%", "highlight": True},
            {"value": "留存提升 12%", "highlight": False},
            {"value": "提前14天预警", "highlight": False},
        ],
        "tags": ["Python", "XGBoost", "SQL", "机器学习"],
        "status": "已完成",
        "year": 2025,
        "overview": (
            "针对电商平台用户流失问题，构建基于XGBoost的流失预警模型。"
            "通过用户行为数据（浏览、收藏、下单频率等）构建特征工程，提前14天预测流失风险。"
        ),
        "architecture": [
            "特征工程：用户行为序列、订单数据、活跃度指标",
            "模型：XGBoost 二分类",
            "数据：Hive 离线特征 + MySQL 业务数据",
            "部署：模型序列化，定期批量预测",
        ],
        "achievements": [
            "准确率 83%",
            "留存率提升 12%",
            "预警提前量 14 天",
        ],
        "related": ["sales-dashboard", "data-warehouse"],
    },
    {
        "id": "sales-dashboard",
        "type": "local",
        "title": "销售数据分析看板",
        "desc": "Tableau 构建集团级销售看板，打通5个业务数据源，日均自动刷新，管理层日活40+用户。",
        "thumb": "📈",
        "metrics": [
            {"value": "5 个数据源打通", "highlight": True},
            {"value": "日活 40+ 用户", "highlight": False},
            {"value": "日自动刷新", "highlight": False},
        ],
        "tags": ["Tableau", "SQL", "ETL", "数据可视化"],
        "status": "已完成",
        "year": 2025,
        "overview": (
            "为解决管理层对销售数据实时掌握的需求，打通5个业务系统数据源，"
            "构建集团级销售数据分析看板，支持多维度下钻（区域/品类/渠道）。"
        ),
        "architecture": [
            "数据：MySQL + 业务系统 API",
            "ETL：Kettle 定时抽取数据",
            "可视化：Tableau Desktop + Server 自动化刷新",
        ],
        "achievements": [
            "5个业务数据源统一整合",
            "日活 40+ 管理层用户",
            "数据时效从 T+1 提升到 T0",
        ],
        "related": ["churn-prediction", "data-warehouse"],
    },
    {
        "id": "data-warehouse",
        "type": "local",
        "title": "电商数据仓库建设",
        "desc": "基于 Hadoop 生态搭建离线数仓，覆盖用户、商品、订单三大主题域，日处理数据量千万级，为上层数据分析与算法模型提供统一数据底座。",
        "thumb": "🏗️",
        "metrics": [
            {"value": "千万级日处理量", "highlight": True},
            {"value": "3 大主题域", "highlight": False},
            {"value": "数据时效 T+1", "highlight": False},
        ],
        "tags": ["Hadoop", "Hive", "Spark", "Sqoop", "Kafka", "Azkaban"],
        "status": "已完成",
        "year": 2024,
        "overview": (
            "基于 Hadoop 生态系统搭建企业级离线数据仓库，覆盖用户、商品、订单三大主题域。"
            "通过统一数据底座，支持上层 BI 报表、数据分析和算法模型的数据需求。"
        ),
        "architecture": [
            "数据源：业务数据库(MySQL/Oracle) + 日志数据(Flume/Kafka)",
            "存储：HDFS分布式存储",
            "计算：Hive离线计算 + Spark实时计算",
            "调度：Azkaban 工作流编排",
            "同步：Sqoop 批量抽取 + DataX 实时同步",
        ],
        "achievements": [
            "覆盖用户、商品、订单三大主题域",
            "日处理数据量千万级",
            "下游支持 10+ 数据分析需求",
        ],
        "related": ["sales-dashboard", "churn-prediction"],
    },
    {
        "id": "multi-agent-research",
        "type": "local",
        "title": "Multi-Agent 研究助手",
        "desc": "手写 Multi-Agent 协作系统，模拟研究团队分工（规划→搜索→写作），展示 AI Agent 设计原理与多 Agent 协作机制。",
        "thumb": "🤖",
        "metrics": [
            {"value": "3 个 Agent 协作", "highlight": True},
            {"value": "零框架依赖", "highlight": False},
            {"value": "纯 Python 实现", "highlight": False},
        ],
        "tags": ["Python", "AI Agent", "Multi-Agent", "DuckDuckGo"],
        "status": "已完成",
        "year": 2026,
        "overview": (
            "用纯 Python 手写 Multi-Agent 协作系统，没有使用 CrewAI 等框架。"
            "三个 Agent（规划师/搜索专家/写作师）分工协作，模拟真实研究团队的工作流程。"
        ),
        "architecture": [
            "规划 Agent（Planner）：调用 LLM 将研究主题拆解为多个搜索子任务",
            "搜索 Agent（Researcher）：调用 DuckDuckGo 并行收集信息",
            "写作 Agent（Writer）：调用 LLM 将搜索结果整理为结构化研究报告",
            "协作调度（Crew）：串联三个 Agent，形成完整的研究流程",
            "大模型：MiniMax-M2.7",
            "搜索：DuckDuckGo（ddgs）",
        ],
        "achievements": [
            "深入理解 Agent = LLM + Tools + Loop 的核心原理",
            "掌握多 Agent 协作架构设计",
            "纯 Python 实现，零外部框架依赖",
            "可作为 AI 应用工程师面试展示项目",
        ],
        "related": ["ticket-classifier", "annotation-platform"],
    },
]

# ─── Blogs ───────────────────────────────────────────────────────────────────

BLOGS: list[BlogDict] = [
    {
        "slug": "python-automation-report",
        "type": "article",
        "title": "用 Python 脚本自动化日常数据报表的全流程",
        "date": "2026-03-15",
        "read_time": "5 min read",
        "desc": "从数据抽取、清洗、到邮件自动发送，手把手搭建一套零人工干预的报表流水线。",
        "content": (
            "在日常数据分析工作中，报表制作是最耗时又最没技术含量的工作之一。"
            "每周固定时间要从数据库里导出数据、清洗、对齐Excel格式、发邮件——全流程手工操作，"
            "不仅效率低，还容易出错。本篇文章记录我用 Python 实现全自动化报表流水线的完整过程。\n\n"
            "## 一、整体架构\n\n"
            "这套自动化报表系统分为四个模块：数据抽取（Extract）、数据清洗（Transform）、"
            "数据加载（Load）、邮件发送（Send）。整个流程由 crontab 定时触发，零人工干预。\n\n"
            "数据源方面，公司业务系统是 MySQL + PostgreSQL，我会用 SQLAlchemy 做 ORM 映射，"
            "配合 Pandas 做批量读取。数据量大的情况下先在数据库里做预聚合，减少 Python 侧的内存压力。\n\n"
            "## 二、数据抽取（E）\n\n"
            "```python\n"
            "from sqlalchemy import create_engine\n"
            "import pandas as pd\n\n"
            "def extract(query, params=None):\n"
            "    engine = create_engine('mysql+pymysql://user:pass@host/db')\n"
            "    with engine.connect() as conn:\n"
            "        df = pd.read_sql(query, conn, params=params)\n"
            "    return df\n"
            "```\n\n"
            "这里踩过一个坑：直接用 pd.read_sql 跑大查询时容易 OOM。后来改成在 SQL 里先做聚合，"
            "只拉取结果集而不是原始明细数据，单次查询时间从 40s 降到 3s，内存占用减少 90%。\n\n"
            "## 三、数据清洗（T）\n\n"
            "清洗逻辑根据业务规则来，一般包括：去除重复行、处理缺失值、统一日期格式、"
            "关联维表补全字段名等。用 Pandas 的链式操作可以写得非常干净：\n\n"
            "```python\n"
            "df = (df.drop_duplicates()\n"
            "        .assign(date=lambda x: pd.to_datetime(x['date']))\n"
            "        .merge(dim_product, on='product_id', how='left')\n"
            "        .fillna(0)\n"
            ")\n"
            "```\n\n"
            "## 四、数据加载（L）+ 邮件发送\n\n"
            "数据导出用 xlsxwriter 写 Excel，保留原始格式和条件颜色。"
            "邮件发送用 smtplib + email，报表作为附件定时推送：\n\n"
            "```python\n"
            "import smtplib\n"
            "from email.mime.multipart import MIMEMultipart\n"
            "from email.mime.base import MIMEBase\n"
            "\n"
            "def send_email(report_path, recipients):\n"
            "    msg = MIMEMultipart()\n"
            "    msg['Subject'] = f'日报 {date.today()}'\n"
            "    msg['To'] = ', '.join(recipients)\n"
            "    with open(report_path, 'rb') as f:\n"
            "        part = MIMEBase('application', 'octet-stream')\n"
            "        part.set_payload(f.read())\n"
            "    # ... attach and send\n"
            "```\n\n"
            "## 五、定时任务配置\n\n"
            "最后在服务器上配置 crontab，每天早上 9 点自动跑：\n\n"
            "```\n"
            "0 9 * * * /usr/bin/python3 /opt/scripts/daily_report.py >> /var/log/report.log 2>&1\n"
            "```\n\n"
            "上线三个月以来，报表送达准时率 100%，人工干预次数降为 0，"
            "彻底解放了每周至少 2 小时的重复工作时间。\n\n"
            "如果你也在做类似的事情，建议先画流程图，把每个环节的输入输出理清楚，"
            "再动手写代码。磨刀不误砍柴工。"
        ),
    },
    {
        "slug": "rag-practice",
        "type": "article",
        "title": "RAG 实战：从 0 到 1 搭建客服知识库问答系统",
        "date": "2026-02-28",
        "read_time": "8 min read",
        "desc": "基于 LangChain + ChatGLM3，完整记录 RAG 系统的搭建思路、向量检索优化和 Prompt 调优经验。",
        "content": (
            "RAG（Retrieval-Augmented Generation，检索增强生成）是这两年大模型应用最火的技术方向之一。"
            "它的核心思想很简单：不让 LLM 只靠自身参数回答问题，而是先从外部知识库检索相关内容，"
            "再把检索结果作为上下文交给 LLM 生成答案。这样做的好处是：答案更准确、可溯源、"
            "且可以实时更新知识库而不需要重新训练模型。\n\n"
            "## 一、业务场景\n\n"
            "我做的这套客服知识库问答系统，服务于一家约 200 人客服团队。"
            "历史累积的工单、FAQ、产品文档加起来超过 10 万条。"
            "客服人员每次接电话要先翻知识库找答案，平均一次查询耗时 3-5 分钟，既慢又容易出错。\n\n"
            "目标是：输入一个用户问题，系统自动从知识库里检索相关内容，"
            "生成准确答案并推荐给客服。客服只需要确认或微调，可以把单次处理时间压到 1 分钟以内。\n\n"
            "## 二、技术选型\n\n"
            "- LLM：ChatGLM3-6B（本地部署，避免数据外流）\n"
            "- 向量数据库：Chroma（轻量、易用，支持本地持久化）\n"
            "- 框架：LangChain（方便串起 retrieval + generation 流程）\n"
            "- Embedding：sentence-transformers（all-MiniLM-L6-v2，轻量且效果不错）\n\n"
            "## 三、知识库构建\n\n"
            "知识库构建分为三步：文档解析、文本分块（Chunking）、向量化。\n\n"
            "文档解析用 pdfplumber 提取 PDF 内容，工单数据从 MySQL 导出后清洗成结构化文本。"
            "分块策略是门学问——太大则上下文稀释，太小则语义不完整。"
            "我最后用的是 512 token、 overlap 50 的滑动窗口分块，在测试集上召回率最高。\n\n"
            "```python\n"
            "from langchain.text_splitter import RecursiveCharacterTextSplitter\n\n"
            "splitter = RecursiveCharacterTextSplitter(\n"
            "    chunk_size=512,\n"
            "    chunk_overlap=50,\n"
            "    separators=[\"\\n\\n\", \"\\n\", \".\", \"，\", \" \"]\n"
            ")\n"
            "docs = splitter.create_documents(raw_texts)\n"
            "```\n\n"
            "向量化直接用 sentence-transformers，把每块文本编码成 384 维向量存进 Chroma。"
            "实测 10 万条 chunk，embedding 耗时约 20 分钟（CPU），可以接受。\n\n"
            "## 四、检索策略优化\n\n"
            "RAG 效果好不好，检索是关键。我尝试过几种检索策略：\n\n"
            "1. 纯语义检索（dense）：效果最好，但慢\n"
            "2. 关键词检索（BM25）：快但语义理解差\n"
            "3. 混合检索（hybrid）：先 BM25 粗排，再用 dense 精排\n\n"
            "最终用混合检索，取 top-5 相关文档传给 LLM。"
            "加入重排序（rerank）后，准确率从 78% 提升到 91%。\n\n"
            "## 五、Prompt 调优\n\n"
            "Prompt 设计遵循「清晰上下文 + 明确任务 + 约束输出格式」三原则：\n\n"
            "```\n"
            "你是一名资深客服。请根据以下参考内容，准确回答用户问题。\n"
            "如果参考内容不足以回答，请如实说明，不要编造。\n\n"
            "【参考内容】\n"
            "{context}\n\n"
            "【用户问题】\n"
            "{question}\n\n"
            "【回答要求】\n"
            "- 语言简洁、专业\n"
            "- 如有步骤，给出 1/2/3 编号\n"
            "- 涉及金额或期限的内容要注明"
            "```\n\n"
            "## 六、效果评估\n\n"
            "上线后每周统计客服采纳率和用户满意度："
            "采纳率从第一周的 62% 提升到第四周的 89%，平均每次处理时间从 4.2 分钟降到 0.9 分钟。"
            "目前系统日均处理 1200+ 次查询，准确率 91%，客服团队反馈非常正面。\n\n"
            "RAG 这条路还有很多可以优化的空间：多跳推理、幻觉检测、实时知识更新……"
            "后续计划引入 vector index 的增量更新，不让知识库成为静态快照。"
        ),
    },
    {
        "slug": "user-segmentation-kmeans-rfm",
        "type": "article",
        "title": "用户分群怎么做？K-Means + RFM 实战笔记",
        "date": "2026-01-20",
        "read_time": "6 min read",
        "desc": "用电商真实数据演示 RFM 模型 + K-Means 分群，找到高价值用户、流失风险用户和潜力用户。",
        "content": (
            "精细化运营的前提是对用户有足够的了解。"
            "大多数公司一开始只看 GMV、UV 这些汇总指标，"
            "但真正驱动增长的是搞清楚『谁在使用产品、为什么买、为什么流失』。"
            "本文用一个电商真实数据集，演示 RFM + K-Means 的完整分群方法论。\n\n"
            "## 一、RFM 模型简介\n\n"
            "RFM 是用户价值评估的经典框架：\n\n"
            "- R（Recency）：用户最近一次消费距今多少天，越近越有价值\n"
            "- F（Frequency）：单位时间内的消费频次，越高频越有价值\n"
            "- M（Monetary）：单位时间内的消费金额，越高越有价值\n\n"
            "三个维度组合起来，可以把用户划分成不同群体："
            "高价值用户、潜力用户、流失风险用户、沉默用户等。"
            "每个群体的运营策略完全不同，不能一刀切。\n\n"
            "## 二、数据准备\n\n"
            "数据来自某中型电商平台 2024 年全年订单，共 48 万条记录，"
            "去重后约 12 万有效用户。先在 Hive 里把用户维度和交易事实关联好，"
            "导出 R/F/M 三个指标：\n\n"
            "```sql\n"
            "SELECT\n"
            "    user_id,\n"
            "    DATEDIFF('2025-01-01', MAX(order_date)) AS recency,  -- R\n"
            "    COUNT(order_id)                           AS frequency, -- F\n"
            "    SUM(order_amount)                          AS monetary   -- M\n"
            "FROM dwd_order\n"
            "WHERE order_date >= '2024-01-01'\n"
            "  AND order_status = '已完成'\n"
            "GROUP BY user_id\n"
            "```\n\n"
            "## 三、数据分布与预处理\n\n"
            "RFM 三个指标的分布通常都是严重右偏的——少数用户贡献了大量消费。"
            "直接用原始值跑 K-Means 会导致少数异常值主导距离计算。"
            "标准做法是先做对数变换，再做 Z-Score 标准化：\n\n"
            "```python\n"
            "import numpy as np\n"
            "from sklearn.preprocessing import StandardScaler\n\n"
            "df['R'] = np.log1p(df['recency'])\n"
            "df['F'] = np.log1p(df['frequency'])\n"
            "df['M'] = np.log1p(df['monetary'])\n\n"
            "scaler = StandardScaler()\n"
            "rfm_scaled = scaler.fit_transform(df[['R', 'F', 'M']])\n"
            "```\n\n"
            "## 四、K-Means 分群\n\n"
            "K-Means 的 K 怎么定？用肘部法则（Elbow Method）+ 轮廓系数（Silhouette Score）联合判断：\n\n"
            "```python\n"
            "from sklearn.cluster import KMeans\n"
            "from sklearn.metrics import silhouette_score\n\n"
            "scores = []\n"
            "for k in range(2, 10):\n"
            "    km = KMeans(n_clusters=k, random_state=42, n_init=10)\n"
            "    labels = km.fit_predict(rfm_scaled)\n"
            "    scores.append(silhouette_score(rfm_scaled, labels))\n\n"
            "best_k = scores.index(max(scores)) + 2\n"
            "```\n\n"
            "测试结果：K=5 时轮廓系数最高（0.63），确定为 5 个用户群体。\n\n"
            "## 五、分群结果解读\n\n"
            "跑出来的 5 个群体特征如下：\n\n"
            "| 群体 | R(天) | F(次) | M(元) | 命名 | 占比 |\n"
            "|------|-------|-------|-------|------|------|\n"
            "| 1 | 280 | 1.2 | 89 | 流失风险 | 22% |\n"
            "| 2 | 45 | 3.1 | 156 | 潜力用户 | 28% |\n"
            "| 3 | 15 | 8.4 | 632 | 高价值用户 | 18% |\n"
            "| 4 | 180 | 1.8 | 210 | 沉寂用户 | 24% |\n"
            "| 5 | 8 | 1.1 | 45 | 新用户 | 8% |\n\n"
            "## 六、运营策略\n\n"
            "分群的价值在于指导运营动作：\n\n"
            "- **群体 3（高价值）**：VIP 专项服务，专属客服、优先发货、专属折扣\n"
            "- **群体 2（潜力）**：用复购激励（满减券），推动向高价值转化\n"
            "- **群体 1（流失风险）**：流失预警触发，Push + 专属挽回优惠\n"
            "- **群体 4（沉寂）**：沉睡唤醒计划，大额券刺激首复购\n"
            "- **群体 5（新用户）**：新手引导链路完善，重点提升首单转化\n\n"
            "## 七、效果验证\n\n"
            "策略上线后追踪 3 个月："
            "群体 2→3 的转化率达到 31%，群体 1 的流失挽回率 18%，"
            "整体 GMV 提升约 12%。分群维度的运营比一刀切策略效果好了不止一倍。\n\n"
            "RFM + K-Means 是入门用户分群的好起点，"
            "但实际业务中建议逐步引入更多标签（用户画像特征、行为序列），"
            "让分群结果更精细、更动态。"
        ),
    },
]