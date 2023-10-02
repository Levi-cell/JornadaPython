from requests import get, post
# Enviando requisições para a API do fastAPI

resp = get("http://127.0.0.1:8000")

# Podemos ver a documentação em /docs

print(resp.text)

resp = post("http://127.0.0.1:8000/novarota",
            json={"curso": "pythonpro", "modulo": 6, "tipo": "POST"})

print(resp.text)