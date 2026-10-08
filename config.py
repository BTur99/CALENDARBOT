from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = getenv("TOKEN")
    DB_NAME = "calendar_base.db"