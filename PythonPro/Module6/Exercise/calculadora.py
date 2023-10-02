"""Modulo para a calculadora"""

def minha_calculadora(data):
    """Função para realizar o calculo da operação escolhida"""
    print(data, data.operacao)

    if data.operacao.name == "SOMA":
        return data.valor1 + data.valor2

    if data.operacao.name == "SUBTRACAO":
        return data.valor1 - data.valor2

    if data.operacao.name == "MULTIPLICACAO":
        return data.valor1 * data.valor2

    if data.operacao.name == "DIVISAO":
        if data.valor2 == 0:
            return "O segundo valor não pode ser 0, tente novamente..."
        return data.valor1 / data.valor2
