# Multi-Agent 项目 · 开发看板

## 项目目标
用 5 天时间完成一个可展示的 Multi-Agent 研究助手，作为 AI 应用工程师转型的代表作之一。

---

## 📅 每日任务

### Day 1：环境搭建 ✅
- [ ] 注册硅基流动，获取 API Key
- [ ] 创建项目目录
- [ ] 安装依赖：`pip install -r requirements.txt`
- [ ] 验证 API 连接：`python -c "from openai import OpenAI; ..."`
- [ ] 调通 DuckDuckGo 搜索：`python -c "from duckduckgo_search import DDGS; ..."`
- [ ] 验证通过：能搜到结果

### Day 2：单个 Agent 跑通 ✅
- [ ] 创建 `src/config.py`（API 配置）
- [ ] 创建 `src/tools/search_tool.py`（搜索工具）
- [ ] 创建 `src/agents/planner.py`（规划 Agent）
- [ ] 创建 `src/agents/researcher.py`（搜索 Agent）
- [ ] 创建 `src/agents/writer.py`（写作 Agent）
- [ ] 单 Agent 测试通过

### Day 3：Crew 协作跑通 ✅
- [ ] 创建 `src/crew/research_crew.py`（组装 Crew）
- [ ] 创建 `src/main.py`（入口）
- [ ] 完整流程测试：输入主题 → 输出报告
- [ ] 解决协作问题（结果重复、Agent 跑偏等）
- [ ] 优化提示词

### Day 4：Web 界面 ✅
- [ ] 创建 `src/web_demo.py`（Gradio 界面）
- [ ] 界面美观：标题 + 输入框 + 输出框
- [ ] 本地浏览器打开测试
- [ ] 截图保存

### Day 5：展示准备 ✅
- [ ] 录屏演示（2-3分钟）
- [ ] 更新 README.md
- [ ] 推送到 GitHub
- [ ] 准备面试话术

---

## 🚫 常见问题

| 问题 | 解决 |
|------|------|
| `Import Error: cannot import name 'ChatOpenAI'` | `pip install crewai --upgrade` |
| API Key 无效 | 检查硅基流动后台是否有免费额度 |
| 搜索结果为空 | DuckDuckGo 可能在部分地区限速，换时间重试 |
| 报告输出乱码 | 确保终端编码为 UTF-8 |
| Agent 一直重复 | 降低 temperature 或简化 prompt |

---

## 🎯 验收标准

项目完成当且仅当：
1. ✅ 运行 `python src/main.py` 输入任意主题，能输出研究报告
2. ✅ 能看到三个 Agent 的协作过程日志
3. ✅ Web 界面可以正常打开并使用
4. ✅ 有录屏或截图可以展示

---

## 📌 下一步（完成后）

| 方向 | 内容 |
|------|------|
| 升级方向 | 加「记忆」功能（Chroma 向量数据库） |
| 升级方向 | 加「语音输入/输出」（TTS/ASR） |
| 展示 | 做第二个项目，形成项目组合 |
| 求职 | 整理作品集，准备面试题 |

---

_由同志 ✊ 制定 | 2026-04-27_
