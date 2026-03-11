from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

API = FastAPI()
TAREFAS = []

class Tarefa(BaseModel):
        id: int
        titulo: str
        dataCriacao: datetime
        finalizado: bool = False

async def criarTarefa (titulo: str):
        id = len(TAREFAS)
        tarefaNova = Tarefa(id=id, titulo=titulo, dataCriacao=datetime.now(), finalizado=False)

        TAREFAS.append(tarefaNova)

        return {"mensagem": "OK"}

async def paginaInicial():
        return{"mensagem": "Funcionando!"}

async def listarTarefas():
        return TAREFAS

API.add_api_route("/tarefas", listarTarefas, methods=['GET'])
API.add_api_route("/criar", criarTarefa, methods=['POST'])
API.add_api_route("/", paginaInicial, methods=['GET'])