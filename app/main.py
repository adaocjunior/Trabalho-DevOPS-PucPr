from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import logging


API = FastAPI()
TAREFAS = []
LOGGER = logging.getLogger('devops_tarefas')
LOGGER.setLevel(logging.DEBUG)


fileHandler = logging.FileHandler('devops_tarefas.log', encoding='utf8')
formatter = logging.Formatter(fmt="%(name)s | %(levelname)s | %(asctime)s | %(filename)s:%(lineno)s | %(message)s")
fileHandler.setFormatter(formatter)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

LOGGER.addHandler(fileHandler)
LOGGER.addHandler(streamHandler)

class Tarefa(BaseModel):
        id: int
        titulo: str
        dataCriacao: datetime
        finalizado: bool = False

async def criarTarefa (titulo: str):
        LOGGER.info("Usuario acessou /criar")
        id = len(TAREFAS)
        tarefaNova = Tarefa(id=id, titulo=titulo, dataCriacao=datetime.now(), finalizado=False)

        TAREFAS.append(tarefaNova)

        return {"mensagem": "OK"}

async def paginaInicial():
        LOGGER.info("Usuario acessou /")
        return{"mensagem": "Funcionando!"}

async def mostrarAutor():
        LOGGER.info("Usuario acessou /autor")
        return{"Autor":"Adao Correa da Costa Junior"}

async def listarTarefas():
        LOGGER.info("Usuario acessou /tarefas")
        return TAREFAS



API.add_api_route("/tarefas", listarTarefas, methods=['GET'])
API.add_api_route("/criar", criarTarefa, methods=['POST'])
API.add_api_route("/", paginaInicial, methods=['GET'])
API.add_api_route("/autor", mostrarAutor, methods=['GET'])