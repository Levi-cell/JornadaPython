class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


def criaPessoa():
    nome = input("Digite um nome:")
    sobrenome = input("Digite o sobrenome:")

    # pessoa = Pessoa(nome, sobrenome) forma mais comum

    return Pessoa(nome, sobrenome)  # forma genial

# usando list comprehension

adiciona = [criaPessoa() for n in range(1, 11)]
for x in adiciona:
    print(x.nome)

# Estrutura comum:

# lista_pessoas = []
# for t in range(1, 11):
#
#     novaPessoa = criaPessoa()
#
#     lista_pessoas.append(novaPessoa)
#
# for x in lista_pessoas:
#     print(x.nome)