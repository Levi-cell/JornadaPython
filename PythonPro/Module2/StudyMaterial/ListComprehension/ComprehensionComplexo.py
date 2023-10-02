class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

def criaPessoa():
    nome = input("Digite um nome:")
    sobrenome = input("Digite o sobrenome:")

    # pessoa = Pessoa(nome, sobrenome)
    return Pessoa(nome, sobrenome)

# Usando dict comprehension para criar um dicionário de pessoas
pessoas_dict = {pessoa.nome: pessoa for pessoa in [criaPessoa() for i in range(5)]}

# Imprimindo as informações das pessoas usando o dicionário
for nome, pessoa in pessoas_dict.items():
    print("Nome:", pessoa.nome)
    print("Sobrenome:", pessoa.sobrenome)
    print()

# Outra maneira

# class Pessoa:
#     def __init__(self, sobrenome):
#         self.sobrenome = sobrenome
#
# def criaPessoa():
#     nome = input("Digite um nome:")
#     sobrenome = input("Digite o sobrenome:")
#     return nome, Pessoa(sobrenome)
#
# # Usando dict comprehension para criar um dicionário de pessoas
# pessoas_dict = {nome: pessoa_obj for nome, pessoa_obj in [criaPessoa() for _ in range(5)]}
#
# # Imprimindo os sobrenomes das pessoas usando o dicionário
# for nome, pessoa in pessoas_dict.items():
#     print("Nome:", nome)
#     print("Sobrenome:", pessoa.sobrenome)
#     print()