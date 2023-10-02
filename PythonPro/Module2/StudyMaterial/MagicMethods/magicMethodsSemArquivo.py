from json import load

class sistema:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def verficacao(self):
        assert self.login == "admin"
        assert self.senha == "senha"

        return True

    def retorna_login(self):
        return self.login()


sis = sistema("admin", "senha")
sis1 = sistema("admin", "senhaErrada") # irá dar erro

print(sis.verficacao())

# sis.retorna_login()