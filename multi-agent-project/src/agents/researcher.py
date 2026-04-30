# agents/researcher.py
"""
搜索 Agent - 搜索信息
"""
from config import MODEL, BASE_URL, OPENAI_API_KEY
import requests
from tools.search_tool import search_web


class ResearcherAgent:
    """搜索 Agent：根据子任务调用搜索工具，收集信息"""

    def __init__(self, api_key: str):
        self.api_key = api_key or OPENAI_API_KEY

    def run(self, task: dict) -> dict:
        """
        执行搜索任务

        Args:
            task: 子任务，包含 task_id, description, keywords

        Returns:
            搜索结果，包含 task_id, description, results, status
        """
        keywords = task.get("keywords", [])
        search_queries = [task.get("description", "")] + keywords[:2]

        all_results = []
        for query in search_queries:
            result = search_web(query.strip())
            if result and "搜索失败" not in result and "未找到" not in result:
                all_results.append(f"【搜索词: {query}】\n{result}")

        return {
            "task_id": task.get("task_id"),
            "description": task.get("description"),
            "results": "\n\n".join(all_results) if all_results else "未找到有效结果",
            "status": "success" if all_results else "no_results"
        }