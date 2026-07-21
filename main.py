from fastapi import FastAPI
from app.config.settings import settings
from app.core.logger import logger
from app.api.routes import api_router


app = FastAPI(

    title= settings.APP_NAME,

    version= settings.VERSION
)

app.include_router(api_router)

@app.get("/")
def home():
     

    print("HOME API EXECUTED")

    logger.info("HOME API Called")

    return{
        "message": "NBK AI Assistant Running Successfully"
    }