numero1 = float(input("Digite o primeiro número da operação:"))
numero2 = float(input("Digite o segundo número da operação:"))

operacao = input("""Qual operação deseja fazer?
 1 - Soma
 2 - Subtração
 3 - Multiplicação
 4 - Divisão
 Digite a opção que deseja:""")

if operacao == "1":
    print(f"O resultado da soma é: {numero1+numero2}")

elif operacao == "2":
    print(f"O resultado da subtração é: {numero1-numero2}")

elif operacao == "3":
    print(f"O resultado da multiplicação é: {numero1*numero2}")

elif operacao == "4":
    if numero2 == 0:
        print("O segundo numero da divisão (denominador) não pode ser 0")
    else:
        print(f"O resultado da multiplicação é: {numero1 / numero2}")
else:
    print("Opção inválida...")


