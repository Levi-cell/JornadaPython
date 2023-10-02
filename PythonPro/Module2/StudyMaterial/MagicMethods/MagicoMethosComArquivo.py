from json import load
# antes de criarmos nossa classe precisamos carregar um arquivo
class sistema:

    def __init__(self):
        with open("acesso.json") as f:
            acesso = load(f) #cria um dicionario em python com o arquivo json

        self.login = acesso["login"]
        self.senha = acesso["senha"]

    def verficacao(self):
        assert self.login == "admin"
        assert self.senha == "senha"

        return True

    def retorna_login(self):
        return self.login()


sis = sistema()

print(sis.verficacao())

sis.retorna_login()