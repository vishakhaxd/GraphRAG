
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env if present at project root

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MODEL: str = os.getenv("LLM_MODEL", "gpt-3.5-turbo")

settings = Settings()
