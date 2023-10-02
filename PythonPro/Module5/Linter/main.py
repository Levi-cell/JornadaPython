from fizzbuzz import calcular
def run():
    """
    Função principal para execução da biblioteca
    :return:
     """
    while True:
        valor = input("Digite um número natural: ")
        if int(valor) < 0 or isinstance(valor, int):
            print("O valor digitado não pertence ao grupo dos números naturais")
        else:
            break
    resultado = calcular.fizzbuzz(int(valor))
    print(f"Para o número digitado a resposta é {resultado}")


run()

