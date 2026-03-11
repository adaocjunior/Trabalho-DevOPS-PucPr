from .main import API

from fastapi.testclient import TestClient

CLIENT = TestClient(API)

def testarEndpointListarTarefas():
    requisicao = CLIENT.get("/tarefas")

    assert requisicao.status_code == 200

def testarEndpointCriarTarefas():
    requisicao = CLIENT.post("/criar", params={'titulo': 'Teste Criar Tarefa'})
    
    assert requisicao.json() == {"mensagem": "OK"}
    
    requisicao = CLIENT.get("/tarefas")

    assert len(requisicao.json()) == 1
    assert requisicao.json()[0]['id'] == 0

def testarPaginaInicial():
    requisicao = CLIENT.get("/")

    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem":"Funcionando!"}

def validarAutor():
    requisicao = CLIENT.get("/autor")

    assert requisicao.status_code == 200
    assert requisicao.json() == {"Autor":"Adao Correa da Costa Junior"}   