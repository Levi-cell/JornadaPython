from json import dump, dumps, load, loads

# arquivo
# Criando um arquivo de exemplo
jsonExemplo = {
    "chave1": "valor1",
    "chave2": "valor2"

}
print("Como dicionario:")
print(jsonExemplo)
print("-"*30)
# para fazer a conversão do formato dicionário para string usamos a funçaõ dumps

stringJson = dumps(jsonExemplo)
print("Como string:")
print(stringJson[2])
print("-"*30)

# para fazer a conversão de string para dicionário usamos a função loads

jsonStr2dict = loads(stringJson)
print("Como dicionario:")
print(stringJson)
print("-"*30)

# Para salvar em um arquivo no formato JSON usamos a função dump

# with open("jsonExemplo.json", "w") as file:
#     dump(jsonStr2dict, file)

# Para ler de um arquivo JSON usamos a função load

with open("jsonExemplo.json") as file:
    leituraDoJson = load(file)
print("imprimindo arquivo:")
print(leituraDoJson)