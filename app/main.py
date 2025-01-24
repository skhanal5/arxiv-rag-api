from fastapi import FastAPI

from app.models.chat import ChatRequest

app = FastAPI()


@app.get("/health")
def read_root():
    return {"status": "healthy"}


@app.post("/chat")
def post_chat(request: ChatRequest):
    return {"answer": "hello"}
