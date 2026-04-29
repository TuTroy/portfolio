from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    site_url: str = "https://troy-tu.github.io"
    site_title: str = "Troy · 数据分析师转型AI应用者"
    site_description: str = (
        "5年数据领域经验，深耕大数据处理与业务数据分析。"
        "2025年起系统学习大模型应用：Prompt工程、RAG、AI Agent、向量数据库。"
        "擅长大数据分析、机器学习建模与 AI 应用落地，致力于成为 AI 应用工程师。"
    )
    author_name: str = "涂炎钊"
    author_email: str = "yanzhao.tu@email.com"
    wechat: str = "yan_zhao_tu"
    github: str = ""
    formspree_id: str = "YOUR_FORM_ID"
    theme_color: str = "#0ea5e9"

    @property
    def static_dir(self) -> Path:
        return Path(__file__).parent.parent / "static"

    @property
    def templates_dir(self) -> Path:
        return Path(__file__).parent.parent / "templates"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()