from dotenv import load_dotenv
import os

load_dotenv


class Settings:
    APP_NAME = "NBK AI Assistance"
    
    VERSION = "1.0.0"

    DEBUG = True

    OPEN_API_KEY = os.getenv("OPEN_API_KEY")

    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

settings = Settings() 
    
