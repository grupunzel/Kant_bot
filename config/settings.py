import os
from dotenv import load_dotenv
from config.logger import logger

try:
    load_dotenv()
except Exception as e:
    logger.error(f'.env load failed {e}')

class Settings:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    GIGA_CREDENTIALS = os.getenv("GIGA_CREDENTIALS")


settings = Settings()
