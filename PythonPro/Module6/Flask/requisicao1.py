from requests import post, get

"""Enviando uma requisição para a nossa API"""

resp = get("http://localhost:5000/novarota")

print(resp.text)

