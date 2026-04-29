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


class RoadMapCardDict(TypedDict):
    step: str
    title: str
    points: list[str]


class BlogDict(TypedDict):
    title: str
    date: str
    read_time: str
    desc: str


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
    },
]

# ─── Blogs ───────────────────────────────────────────────────────────────────

BLOGS: list[BlogDict] = [
    {
        "title": "用 Python 脚本自动化日常数据报表的全流程",
        "date": "2026-03-15",
        "read_time": "5 min read",
        "desc": "从数据抽取、清洗、到邮件自动发送，手把手搭建一套零人工干预的报表流水线。",
    },
    {
        "title": "RAG 实战：从 0 到 1 搭建客服知识库问答系统",
        "date": "2026-02-28",
        "read_time": "8 min read",
        "desc": "基于 LangChain + ChatGLM3，完整记录 RAG 系统的搭建思路、向量检索优化和 Prompt 调优经验。",
    },
    {
        "title": "用户分群怎么做？K-Means + RFM 实战笔记",
        "date": "2026-01-20",
        "read_time": "6 min read",
        "desc": "用电商真实数据演示 RFM 模型 + K-Means 分群，找到高价值用户、流失风险用户和潜力用户。",
    },
]