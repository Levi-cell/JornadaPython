from collections import defaultdict

novo_dict = defaultdict(lambda: "Esta chave não existe")

print(novo_dict[1])

teste = {}
teste["a"] = 0

print(teste.get("a"))
print(teste.get("b"))