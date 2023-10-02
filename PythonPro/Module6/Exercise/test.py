"""Modulo para realizar os testes unitários"""

from fastapi.testclient import TestClient
from fastapi import status
from api import app

client = TestClient(app)

"""Não é obrigatório utilizar a lib status
 apenas utilizar a numeração do status já serve como 200"""

def test_root():
    """Testando o metódo get para ver se retorna a mensagem esperada"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "STATUS": "API de calculadora está ativa",
        "PRIMEIRO PASSO": "acesse o seguinte link para acessar a calculadora:"
                          " http://127.0.0.1:8000/docs",
        "SEGUNDO PASSO": "abra o metódo POST que está em verde",
        "TERCEIRO PASSO": "Clique em Try it out",
        "QUARTO PASSO": "Coloque os valores que deseja e digite a operação escolhida",
        "QUINTO PASSO": "Clique em Execute e verifique o resultado logo abaixo",
        "OBSERVAÇÃO": "A operação deve estar tudo em miniscúlo e bem acentuado"
    }

def test_calculo_soma():
    """Testando a operação de soma para ver se retorna o resultado esperado"""
    response = client.post("/calc", json={
        "valor1": 20,
        "valor2": 15,
        "operacao": "soma"
    })
    assert response.status_code == 200
    assert response.json() == {"resultado": 35.0}

def test_calculo_divisao_por_zero():
    """Testando a operação de divisão"""
    response = client.post("/calc", json={
        "valor1": 20,
        "valor2": 0,
        "operacao": "divisão"
    })
    assert response.status_code == 200
    assert response.json() == {'resultado': 'O segundo valor não pode ser 0, tente novamente...'}

def test_calculo_operacao_invalida():
    """Testando o tratamento de erro de operação inválida"""
    response = client.post("/calc", json={
        "valor1": 20,
        "valor2": 15,
        "operacao": "potencia"
    })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {"resultado": "Operação inválida..."}
