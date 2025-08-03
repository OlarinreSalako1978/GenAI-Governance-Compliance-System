import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env file

def get_openai_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not found in environment or .env file")
    return key
