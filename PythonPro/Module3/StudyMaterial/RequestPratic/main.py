from requests import get, post


resposta = get("https://pt.wikepedia.org/wiki/Hypertext_Transfer_Protocol")

print(resposta)

help(resposta)

print(resposta.text)

print(resposta.ok)