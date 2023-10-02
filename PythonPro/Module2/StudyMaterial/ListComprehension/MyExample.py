def criaPessoa():
    nome = input("Digite um nome:")
    sobrenome = input("Digite o sobrenome:")

    return nome, sobrenome


# Usando um dict comprehension para chamar a função 10 vezes
pessoas_dict = {nome: sobrenome for nome, sobrenome in [criaPessoa() for i in range(10)]}
for nome, sobrenome in pessoas_dict.items():
    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print()


# dic_pessoa[nome] = sobrenome outra forma de fazer key  value

# Estrutura comun

# lista_pessoas = []
# for t in range(1, 11):
#
#     nome, sobrenome = criaPessoa()
#
#     dic_pessoa = {
#         "Nome": nome,
#         "Sobrenome": sobrenome
#     }
#
#     lista_pessoas.append(dic_pessoa)
#
# for x in lista_pessoas:
#     print(x)


