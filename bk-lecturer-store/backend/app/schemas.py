from pydantic import BaseModel

class LecturerBase(BaseModel):
    name: str
    title: str
    role: str
    unit: str
    image: str

class LecturerOut(LecturerBase):
    id: int
    class Config:
        orm_mode = True

class ChatRequest(BaseModel):
    message: str

