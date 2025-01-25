from fastapi.testclient import TestClient

from app.main import app
from app.models.chat import ChatRequest

client = TestClient(app)


def test_read_root():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_chat():
    request = ChatRequest(user_id=1, message="hello", document=1)
    response = client.post("/chat", json=request.model_dump())
    assert response.status_code == 200
    assert response.json() == {"answer": "hello"}
