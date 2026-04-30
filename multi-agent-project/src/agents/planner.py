# agents/planner.py
"""
规划 Agent - 理解任务，拆解子任务
"""
import json
from config import MODEL, BASE_URL, OPENAI_API_KEY
import requests


class PlannerAgent:
    """规划 Agent：理解用户需求，拆解为具体的搜索子任务"""

    def __init__(self, api_key: str):
        self.api_key = api_key or OPENAI_API_KEY

    def run(self, topic: str) -> list[dict]:
        """
        分析研究主题，拆解为子任务

        Returns:
            子任务列表，每个子任务包含 task_id, description, keywords
        """
        prompt = f"""你是一个专业的研究规划师。

用户想要研究的主题是：{topic}

请将这个主题拆解为 3-5 个具体的搜索子任务。每个子任务需要：
1. 一个清晰的描述（说明要搜索什么）
2. 2-3 个搜索关键词（用英文，搜索引擎友好）

请以 JSON 格式输出，结构如下：
[
  {{"task_id": 1, "description": "子任务描述", "keywords": ["关键词1", "关键词2"]}},
  ...
]

只输出 JSON，不要有其他内容。"""

        response = self._call_llm(prompt)
        try:
            return json.loads(response)
        except:
            # 如果 JSON 解析失败，返回默认结构
            return [
                {"task_id": 1, "description": f"搜索 {topic} 相关基础信息", "keywords": [topic, " basics", " overview"]},
                {"task_id": 2, "description": f"搜索 {topic} 最新发展", "keywords": [topic, " latest", " recent"]},
                {"task_id": 3, "description": f"搜索 {topic} 应用案例", "keywords": [topic, " application", " example"]}
            ]

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
            "max_tokens": 1000
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]