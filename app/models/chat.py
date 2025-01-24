from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_id: int
    message: str
    document: int
