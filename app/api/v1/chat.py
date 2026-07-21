from fastapi import APIRouter

from app.models.request import ChatRequest
from app.models.response import ChatResponse

router = APIRouter()

@router.post("/chat", response_model= ChatResponse)
def chat(request : ChatRequest):

    return ChatResponse(
        answer=f"you asked: {request.question}",
        source="Dummy Source"
    )