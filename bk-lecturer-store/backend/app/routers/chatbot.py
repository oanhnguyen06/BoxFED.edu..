from fastapi import APIRouter
from ..schemas import ChatRequest
from ..chatbot.qa_engine import answer_question

router = APIRouter()

@router.post("/")
def chat(req: ChatRequest):
    return {"answer": answer_question(req.message)}

