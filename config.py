import os
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()

TOKEN = "7759067760:AAF0KqWe3lvLt-_NiJqJF6EEiGKENPDYFUk"
OPENAI_API_KEY = os.getenv("7759067760:AAF0KqWe3lvLt-_NiJqJF6EEiGKENPDYFUk")
INSTAGRAM_API_URL = os.getenv("INSTAGRAM_API_URL")
TIKTOK_API_URL = os.getenv("TIKTOK_API_URL")
CLICK_TOKEN = os.getenv("CLICK_TOKEN")
PAYME_TOKEN = os.getenv("PAYME_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
