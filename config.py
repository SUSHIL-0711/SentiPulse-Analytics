from dotenv import load_dotenv
import os

load_dotenv()  # load from .env

BEARER_TOKEN = os.getenv("BEARER_TOKEN")