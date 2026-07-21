from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return{
        "status": "healthy",
        "application": "NBK AI Assistant",
        "version": "1.0.0"
    }