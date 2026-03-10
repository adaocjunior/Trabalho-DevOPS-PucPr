from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

API = FastAPI()
TAREFAS = []

class Tarefa(BaseModel):
        id: int
        titulo: str
        data_criacao: datetime
        finalizado: bool = False

async def listarTarefas():
        tarefa_nova = Tarefa(id=0, titulo="Tarefa de teste", data_criacao=datetime.now(), finalizado=False)
        return tarefa_nova

API.add_api_route("/tarefas", listarTarefas, methods=['GET'])