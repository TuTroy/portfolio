# tools/search_tool.py
"""
搜索工具 - 使用 DuckDuckGo（ddgs）
"""
from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> str:
    """
    使用 DuckDuckGo 搜索网页信息。

    Args:
        query: 搜索关键词
        max_results: 最大结果数

    Returns:
        搜索结果列表（标题 + 摘要 + 链接）
    """
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append({
                    "title": r.get("title", ""),
                    "snippet": r.get("body", ""),
                    "url": r.get("href", "")
                })

        if not results:
            return "未找到相关结果"

        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append(
                f"[{i}] {r['title']}\n"
                f"    {r['snippet']}\n"
                f"    链接：{r['url']}"
            )
        return "\n\n".join(formatted)
    except Exception as e:
        return f"搜索失败：{str(e)}"