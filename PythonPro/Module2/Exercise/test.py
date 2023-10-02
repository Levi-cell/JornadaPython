import pytest
class sequenciaFibonacci:
    def __init__(self, qtdTermos):
        self.primeiro = 0
        self.segundo = 1
        self.qtdTermos = qtdTermos

    def __iter__(self):
        return self

    def __next__(self):
        if self.qtdTermos == 0:
            raise StopIteration
        else:
            resultado = self.primeiro + self.segundo
            self.primeiro = self.segundo
            self.segundo = resultado
            self.qtdTermos -= 1
            return self.segundo


def geraFibonnaci(termos):
    sequencia = sequenciaFibonacci(termos)
    return {pos: val for pos, val in enumerate(sequencia, start= 1)}



def teste():
    sequencia = 10
    gerador = geraFibonnaci(sequencia)
    assert sequencia == len(gerador)

