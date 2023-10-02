"""Construção dos metódos da api"""
from enum import Enum
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from pydantic import BaseModel
from calculadora import minha_calculadora




app = FastAPI(title="Calculadora", version="1.0.0")

"""Não é obrigatório utilizar a lib status apenas
 utilizar a numeração do status já serve como 200"""

@app.exception_handler(RequestValidationError)
async def tratamento(*_): # *args or *_args
    """Tratamento para operação inválida"""
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={"resultado": "Operação inválida..."})

@app.get("/")
async def root():
    """API vá no metódo POST para testar a calculadora
           1 - acesse o seguinte caminho para acessar a calculadora: http://127.0.0.1:8000/docs
           2 - abra o metódo POST
           3 - Clique em Try it out
           4 - Coloque os valores que deseja e digite a operação escolhida
           5 - Clique em Execute e verifique o resultado logo abaixo,
           OBSERVAÇÃO: A operação deve estar tudo em miniscúlo e bem acentuado"""

    return {"STATUS": "API de calculadora está ativa",
            "PRIMEIRO PASSO": "acesse o seguinte link para acessar a calculadora:"
                              " http://127.0.0.1:8000/docs",
            "SEGUNDO PASSO": "abra o metódo POST que está em verde",
            "TERCEIRO PASSO": "Clique em Try it out",
            "QUARTO PASSO": "Coloque os valores que deseja e digite a operação escolhida",
            "QUINTO PASSO": "Clique em Execute e verifique o resultado logo abaixo",
            "OBSERVAÇÃO": "A operação deve estar tudo em miniscúlo e bem acentuado"}

class Operacoes(Enum):
    """Classe para definir as operações e validar cada uma com ENUM"""
    SOMA = "soma"
    SUBTRACAO = "subtração"
    MULTIPLICACAO = "multiplicação"
    DIVISAO = "divisão"


class Resp(BaseModel):
    """Classe para validar, tipar e definir as variáveis de calculo"""
    valor1: float
    valor2: float
    operacao: Operacoes


@app.post("/calc")
async def calculo(data: Resp):
    """Função que realiza calculos matemáticos.

    Args:
         "valor1": 20,"valor2": 15, "operacao": "soma | subtração | multiplicação | divisão".

    Return:
         resultado da operação como float.
    """
    print(data.valor1, data.valor2, data.operacao)
    resultado = minha_calculadora(data)

    return {"resultado": resultado}  # padrão de resposta
