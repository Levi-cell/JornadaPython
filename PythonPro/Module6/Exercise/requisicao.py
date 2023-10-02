"""Aqui você poderá fazer requisiçoes de teste diretamente na IDE"""
from requests import post

# Enviando requisições para a API do fastAPI

resp = post("http://127.0.0.1:8000/calc",
            json={
                "valor1": 20,
                "valor2": 15,
                "operacao": "soma"}, timeout=2)
print(resp.json())

resp = post("http://127.0.0.1:8000/calc",
            json={
                "valor1": 20,
                "valor2": 0,
                "operacao": "divisão"
            }, timeout=2)
print(resp.json())

resp = post("http://127.0.0.1:8000/calc",
            json={
                "valor1": 20,
                "valor2": 15,
                "operacao": "potencia"
            }, timeout=2)

print(resp.json())

resp = post("http://127.0.0.1:8000/calc",
            json={
                "valor1": 20,
                "valor2": 10,
                "operacao": "multiplicação"
            }, timeout=2)
print(resp.json())

resp = post("http://127.0.0.1:8000/calc",
            json={
                "valor1": 20,
                "valor2": 10,
                "operacao": "divisão"
            }, timeout=2)
print(resp.json())
