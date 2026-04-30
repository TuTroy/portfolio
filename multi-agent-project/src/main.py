# main.py - Multi-Agent 研究助手入口
"""
用法: python src/main.py
"""
from crew.research_crew import run_research
from config import OPENAI_API_KEY
import getpass

def main():
    # 获取 API Key
    api_key = OPENAI_API_KEY
    if not api_key:
        api_key = getpass.getpass("请输入 MiniMax API Key: ").strip()
        if not api_key:
            print("错误：未提供 API Key")
            return

    # 研究主题（交互式输入）
    print("\n🎯 Multi-Agent 研究助手")
    print("=" * 40)
    topic = input("请输入研究主题：").strip()
    if not topic:
        print("错误：研究主题不能为空")
        return

    # 运行研究
    report = run_research(topic, api_key)

    # 输出报告
    print("\n" + "=" * 40)
    print("📄 研究报告：\n")
    print(report)


if __name__ == "__main__":
    main()