class Pai:
    def __init__(self, msg):
        self.msg = msg

    def exec(self, msg):
        print(msg)


class Filho(Pai):
    def __int__(self, msg):
        super().exec(msg)


print(Filho("teste"))