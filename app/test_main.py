from .main import API

from fastapi.testclient import TestClient

CLIENT = TestClient(API)

def testarEndpoint():
    requisicao = CLIENT.get("/tarefas")

    assert requisicao.status_code == 200
    