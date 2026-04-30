# Multi-Agent 研究助手 · 项目方案

> 用三个 AI Agent 协作完成研究任务——规划、搜索、写作，像一个完整的研究团队。

---

## 🎯 项目概述

**项目名称：** Multi-Agent Research Assistant
**Slogan：** 一个会团队协作的 AI 助手

**解决什么问题：** 用户输入一个研究主题，多个 AI Agent 自动分工协作，完成信息搜索、内容整理、报告生成的全流程。

**展示价值：** 证明你理解了 Agent 架构、工具调用、多 Agent 协作原理。

---

## 🏗 系统架构

```
用户输入研究主题
        │
        ▼
┌──────────────────┐
│   规划 Agent      │ ← 理解任务，拆解为子任务
│   (Planner)       │
└────────┬─────────┘
         │ 发送子任务列表
         ▼
┌─────────────────────────────────────────┐
│          并行执行（多个搜索 Agent）       │
│                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ 搜索 Agent │ │ 搜索 Agent │ │ 搜索 Agent │ │
│  │ 任务1     │ │ 任务2     │ │ 任务3     │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       │            │            │        │
│       └────────────┼────────────┘        │
│                    │ 汇总搜索结果         │
│                    ▼                    │
│          ┌──────────────┐               │
│          │  写作 Agent   │ ← 整理信息，写报告│
│          │  (Writer)     │               │
│          └──────┬───────┘               │
└──────────────────┼──────────────────────┘
                   │ 输出最终报告
                   ▼
           ┌──────────────┐
           │  最终输出     │
           │  结构化报告   │
           └──────────────┘
```

---

## 🤖 三个 Agent 职责

### Agent 1：规划师 (Planner)
```
角色：项目经理
职责：
  - 理解用户研究主题
  - 将主题拆解为 3-5 个具体搜索子任务
  - 确定每个子任务的搜索关键词
  - 给搜索结果分配优先级

提示词设计：
  "你是一个专业的研究规划师。用户会给你一个研究主题，
  你需要拆解成具体的搜索子任务，每个任务要有明确的
  搜索关键词组合。输出 JSON 格式的子任务列表。"
```

### Agent 2：搜索专家 (Researcher)
```
角色：信息收集员
职责：
  - 接收规划 Agent 的子任务
  - 使用 DuckDuckGo 搜索相关信息
  - 提取标题、摘要、链接
  - 过滤低质量/重复内容

提示词设计：
  "你是一个专业的信息搜索专家。根据给定的搜索任务，
  使用搜索工具收集信息，返回结构化的搜索结果。"
```

### Agent 3：写作师 (Writer)
```
角色：报告撰写员
职责：
  - 接收所有搜索结果
  - 整理、去重、归纳
  - 按结构化格式输出报告
  - 确保报告逻辑清晰、有结论

提示词设计：
  "你是一个专业的研究报告撰写师。把收集到的信息
  整理成一份结构清晰的研究报告，包含：背景、
  核心发现、分析、结论。"
```

---

## 🛠 技术栈

| 组件 | 选型 | 理由 |
|------|------|------|
| **Agent 框架** | CrewAI | 语法简洁，Multi-Agent 原生支持 |
| **大模型** | 硅基流动 Qwen/Mistral | 免费额度多，国产稳定 |
| **搜索工具** | DuckDuckGo | 免费，无需 API Key |
| **向量存储** | Chroma（可选） | 加记忆功能 |
| **接口** | FastAPI + Gradio | 搭 Web 界面展示 |
| **部署** | 本地跑 + 录屏演示 | 零成本 |

---

## 📁 项目目录结构

```
multi-agent-project/
│
├── SPEC.md                    # 本文件，项目方案
├── README.md                  # 项目介绍（展示用）
│
├── src/
│   ├── __init__.py
│   ├── main.py                # 入口文件，运行主脚本
│   ├── config.py              # API 配置
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── planner.py         # 规划 Agent
│   │   ├── researcher.py      # 搜索 Agent
│   │   └── writer.py          # 写作 Agent
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── search_tool.py     # 搜索工具定义
│   │
│   └── crew/
│       ├── __init__.py
│       └── research_crew.py   # Crew 组装 + 运行
│
├── demo/
│   └── demo_script.py         # 演示脚本（运行示例）
│
├── output/                    # 生成的报告输出目录
│
└── requirements.txt           # 依赖列表
```

---

## 📝 核心代码实现

### 1. config.py（API 配置）

```python
"""
API 配置
"""
import os

# 硅基流动 API Key（免费注册获取）
# https://siliconflow.cn
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")

# 模型选择（性价比优先）
MODEL = "Qwen/Qwen2.5-7B-Instruct"  # 免费额度够用
# 或高性能版：Mistral-7B-Instruct-v0.2

# 搜索配置
SEARCH_MAX_RESULTS = 5  # 每个子任务最多搜索结果数
```

### 2. search_tool.py（搜索工具）

```python
"""
搜索工具 - 使用 DuckDuckGo，无需 API Key
"""
from crewai.tools import tool
from duckduckgo_search import DDGS

@tool("Web Search")
def search_web(query: str) -> str:
    """
    使用 DuckDuckGo 搜索网页信息。

    Args:
        query: 搜索关键词

    Returns:
        搜索结果列表（标题 + 摘要 + 链接）
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "title": r["title"],
                "snippet": r["body"],
                "url": r["href"]
            })

    if not results:
        return "未找到相关结果"

    # 格式化为字符串
    formatted = []
    for i, r in enumerate(results, 1):
        formatted.append(
            f"[{i}] {r['title']}\n"
            f"    {r['snippet']}\n"
            f"    链接：{r['url']}"
        )
    return "\n\n".join(formatted)
```

### 3. planner.py（规划 Agent）

```python
"""
规划 Agent - 理解任务，拆解子任务
"""
from crewai import Agent

def create_planner_agent(llm):
    return Agent(
        role="研究规划师",
        goal="将用户的研究主题拆解为具体的搜索子任务",
        backstory=(
            "你是一个专业的研究规划师，擅长理解复杂的研究需求，"
            "并将其拆解为可执行的搜索任务。你注重任务的多维度和完整性。"
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
```

### 4. researcher.py（搜索 Agent）

```python
"""
搜索 Agent - 搜索信息
"""
from crewai import Agent
from .search_tool import search_web

def create_researcher_agent(llm):
    return Agent(
        role="信息搜索专家",
        goal="根据搜索任务收集高质量的参考资料",
        backstory=(
            "你是一个专业的信息搜索专家，精通各种搜索技巧，"
            "能够快速找到权威、可信的参考资料。"
        ),
        tools=[search_web],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
```

### 5. writer.py（写作 Agent）

```python
"""
写作 Agent - 整理信息，撰写报告
"""
from crewai import Agent

def create_writer_agent(llm):
    return Agent(
        role="研究报告撰写师",
        goal="将收集到的信息整理成结构清晰的研究报告",
        backstory=(
            "你是一个专业的研究报告撰写师，擅长将复杂的信息"
            "整理成逻辑清晰、重点突出的报告。"
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
```

### 6. research_crew.py（Crew 组装与运行）

```python
"""
Multi-Agent Crew - 组装三个 Agent 并协调运行
"""
from crewai import Crew, Process
from .agents.planner import create_planner_agent
from .agents.researcher import create_researcher_agent
from .agents.writer import create_writer_agent

def create_research_crew(llm):
    planner = create_planner_agent(llm)
    researcher = create_researcher_agent(llm)
    writer = create_writer_agent(llm)

    crew = Crew(
        agents=[planner, researcher, writer],
        process=Process.hierarchical,  # 层级协作（规划 → 搜索 → 写作）
        verbose=True,
    )
    return crew

def run_research(topic: str, llm):
    """
    运行研究任务

    Args:
        topic: 研究主题
        llm: 语言模型实例

    Returns:
        最终研究报告
    """
    crew = create_research_crew(llm)
    result = crew.kickoff(inputs={"topic": topic})
    return result
```

### 7. main.py（入口）

```python
"""
Multi-Agent 研究助手 - 主入口
用法: python src/main.py
"""
import os
from crewai import LLM
from crew import run_research
from config import OPENAI_API_KEY, MODEL

def main():
    # 设置 API Key
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # 初始化模型
    llm = LLM(
        model=f"openai/{MODEL}",
        base_url="https://api.siliconflow.cn/v1"  # 硅基流动 API 地址
    )

    # 研究主题
    topic = input("请输入研究主题：") or "AI 应用工程师的薪资情况和技能要求"

    print(f"\n🔍 开始研究：{topic}\n")
    print("=" * 50)

    # 运行研究
    result = run_research(topic, llm)

    print("\n" + "=" * 50)
    print("📄 研究报告：")
    print(result)

if __name__ == "__main__":
    main()
```

---

## 🚀 部署与展示

### 方案一：本地运行 + 录屏演示（推荐，最快）

```bash
# 1. 安装依赖
pip install crewai duckduckgo-search

# 2. 配置 API Key
export OPENAI_API_KEY="your-siliconflow-api-key"

# 3. 运行
python src/main.py
```

录屏要求：
- 录屏时长：2-3分钟
- 展示内容：输入主题 → 看到 Agent 协作过程 → 输出报告
- 重点：展示「三个 Agent 在对话、协作」的过程

### 方案二：Gradio Web 界面（进阶）

```python
import gradio as gr
from crew import run_research

def research_interface(topic):
    result = run_research(topic, llm)
    return str(result)

demo = gr.Interface(
    fn=research_interface,
    inputs="text",
    outputs="text",
    title="Multi-Agent 研究助手",
    description="输入研究主题，多个 AI Agent 协作完成研究"
)
demo.launch()
```

---

## 📋 开发计划（按天）

| 天数 | 任务 | 交付物 |
|------|------|--------|
| **Day 1** | 安装依赖，配置 API，跑通搜索工具 | 搜索功能正常 |
| **Day 2** | 实现三个 Agent，组装 Crew | 单 Agent 跑通 |
| **Day 3** | 调试协作流程，优化提示词 | Multi-Agent 协作正常 |
| **Day 4** | 搭 Gradio 界面 | 有 Web 界面 |
| **Day 5** | 录演示视频，写 README | 可展示的 Demo |

---

## 📊 项目展示要点

### 简历/作品集描述

```
Multi-Agent 研究助手
├── 技术栈：CrewAI + Qwen + DuckDuckGo + FastAPI
├── 原理：实现了一个 Multi-Agent 协作系统，包含规划Agent、
│        搜索Agent、写作Agent，通过层级协作机制完成研究任务
├── 亮点：
│   1. 理解并实现了 Agent 的 ReAct 思维链
│   2. 掌握了多 Agent 协作的任务分解与结果汇总
│   3. 工具调用（Tool Use）实现搜索能力
└── 演示：录屏 + GitHub 代码
```

### 面试可能问的问题（提前准备）

| 问题 | 回答要点 |
|------|----------|
| 什么是 Multi-Agent？ | 多个 Agent 分工协作，各司其职 |
| Agent 之间如何通信？ | 通过共享上下文，Agent 输出作为其他 Agent 输入 |
| 用了什么协作模式？ | 层级协作（Hierarchical）：规划 → 执行 → 汇总 |
| 如何保证输出质量？ | 每个 Agent 有明确角色和提示词约束 |
| 遇到过什么问题？ | 搜索结果重复 → 做了去重逻辑 |

---

## ⚠️ 已知问题与解决

| 问题 | 原因 | 解决 |
|------|------|------|
| 搜索结果重复 | 关键词重叠 | 在 Planner 层做去重 |
| 报告太长 | 搜索结果过多 | 限制每个任务结果数 |
| API 超时 | 模型响应慢 | 增加 timeout 配置 |
| Agent 跑偏 | 提示词不够具体 | 优化 prompt，加入输出格式约束 |

---

## 🔗 参考资源

| 资源 | 链接 |
|------|------|
| CrewAI 文档 | https://docs.crewai.com |
| 硅基流动 | https://siliconflow.cn |
| DuckDuckGo Search | `pip install duckduckgo-search` |

---

*由同志 ✊ 为 Troy 定制 | 2026-04-27*
