# crew/research_crew.py
"""
Multi-Agent 协作系统 - 组装三个 Agent 并协调运行
"""
from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent


class ResearchCrew:
    """研究团队：规划 Agent → 搜索 Agent × N → 写作 Agent"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.planner = PlannerAgent(api_key)
        self.researcher = ResearcherAgent(api_key)
        self.writer = WriterAgent(api_key)

    def kickoff(self, topic: str) -> str:
        """
        执行完整的研究流程

        Args:
            topic: 研究主题

        Returns:
            最终研究报告
        """
        print(f"\n🎯 开始研究：{topic}\n")
        print("=" * 50)

        # Step 1: 规划 - 拆解任务
        print("📋 Step 1/3: 规划 Agent 拆分任务...")
        tasks = self.planner.run(topic)
        print(f"   拆解为 {len(tasks)} 个子任务\n")

        # Step 2: 搜索 - 并行执行多个搜索
        print("🔍 Step 2/3: 搜索 Agent 执行搜索...")
        search_results = []
        for task in tasks:
            print(f"   搜索: {task['description']}")
            result = self.researcher.run(task)
            search_results.append(result)
            print(f"   ✓ 完成 (状态: {result['status']})")
        print()

        # Step 3: 写作 - 整理报告
        print("✍️  Step 3/3: 写作 Agent 撰写报告...")
        report = self.writer.run(topic, search_results)
        print("   ✓ 报告生成完成\n")

        print("=" * 50)
        return report


def run_research(topic: str, api_key: str = None) -> str:
    """
    快捷函数：运行研究任务

    Args:
        topic: 研究主题
        api_key: API Key（可选，默认从 config 读取）

    Returns:
        研究报告
    """
    crew = ResearchCrew(api_key)
    return crew.kickoff(topic)