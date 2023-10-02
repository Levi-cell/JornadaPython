class calcular:
    def fizzbuzz(valor):
        resposta = ""
        if valor % 5 == 0:
            resposta += "fizz"
        if valor % 7 == 0:
            resposta += "buzz"
        if len(resposta) == 0:
            resposta += "miss"

        return resposta