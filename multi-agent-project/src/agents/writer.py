# agents/writer.py
"""
写作 Agent - 整理信息，撰写报告
"""
import json
from config import MODEL, BASE_URL, OPENAI_API_KEY
import requests


class WriterAgent:
    """写作 Agent：整理搜索结果，撰写结构化研究报告"""

    def __init__(self, api_key: str):
        self.api_key = api_key or OPENAI_API_KEY

    def run(self, topic: str, search_results: list[dict]) -> str:
        """
        根据搜索结果撰写报告

        Args:
            topic: 研究主题
            search_results: 搜索结果列表

        Returns:
            结构化研究报告
        """
        # 汇总所有搜索内容
        content_parts = []
        for result in search_results:
            content_parts.append(f"## 子任务 {result['task_id']}: {result['description']}\n{result['results']}")
        combined_content = "\n\n".join(content_parts)

        prompt = f"""你是一个专业的研究报告撰写师。

请根据以下搜索结果，撰写一份关于「{topic}」的结构化研究报告。

---
{combined_content}
---

报告要求：
1. 包含：背景介绍、核心发现、详细分析、结论与建议
2. 使用 Markdown 格式
3. 逻辑清晰，重点突出
4. 综合多个搜索来源，不要只依赖一个

请直接输出报告内容，不要有其他说明。"""

        return self._call_llm(prompt)

    def _call_llm(self, prompt: str) -> str:
        """调用 MiniMax API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 3000
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]