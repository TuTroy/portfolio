# config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
BASE_URL = "https://api.minimaxi.com"
MODEL = "MiniMax-M2.7"