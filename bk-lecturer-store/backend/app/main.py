from fastapi import FastAPI
from .database import Base, engine
from .routers import lecturers, chatbot, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BK Lecturer Store API")

app.include_router(lecturers.router, prefix="/lecturers")
app.include_router(chatbot.router, prefix="/chatbot")
app.include_router(admin.router, prefix="/admin")

