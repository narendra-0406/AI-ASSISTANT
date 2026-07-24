from fastapi import APIRouter, Depends
from app.dependencies.common import get_settings

router = APIRouter()

@router.get("/health")
def health(settings=Depends(get_settings)):

    
    return{
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.VERSION
    }