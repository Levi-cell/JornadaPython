import pytest
from calculadora import *

class TesteCalculadora:
    def setup(self):
        pass

    def testSoma(self):
        resultado = soma(2, 3)
        resultado2 = soma(5, 8)

        assert resultado == 5
        assert resultado2 > 10

    def testSubtracao(self):
        resultado = subtracao(3, 2)

        assert resultado == 1

    def testMultiplicacao(self):

        resultado = multiplicacao(3, 5)

        assert resultado == 15

    def testDivisao(self):
        resultado = divisao(15, 5)

        assert resultado == 3

        # assert divisao(3, 0) == 0 # aqui irá dar erro

        with pytest.raises(ZeroDivisionError): ## aqui n irá dar erro, é uma estrutura que permite
            divisao(3, 0)


