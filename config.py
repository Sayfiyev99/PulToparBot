import os
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()

TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INSTAGRAM_API_URL = os.getenv("INSTAGRAM_API_URL")
TIKTOK_API_URL = os.getenv("TIKTOK_API_URL")
CLICK_TOKEN = os.getenv("CLICK_TOKEN")
PAYME_TOKEN = os.getenv("PAYME_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
