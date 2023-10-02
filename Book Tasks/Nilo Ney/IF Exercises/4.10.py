eneriaConsumida = float(input("Digite o tanto de energia consumida esse mês em kWh:"))

instalacao = input("""Agora digite o tipo de instalação usada:
1 - Instalação Residencial
2 - Instalação Comercial
3 - Instação Industrial""" + "\n")

if instalacao == "1":
    if eneriaConsumida <= 500:
        print(f" O preço a pagar é de R$ {eneriaConsumida*0.40}")
    else:
        print(f" O preço a pagar é de R$ {eneriaConsumida * 0.65}")

elif instalacao == "2":
    if eneriaConsumida <= 1000:
        print(f" O preço a pagar é de R$ {eneriaConsumida * 0.55}")
    else:
        print(f" O preço a pagar é de R$ {eneriaConsumida * 0.60}")

elif instalacao == "3":
    if eneriaConsumida <= 5000:
        print(f" O preço a pagar é de R$ {eneriaConsumida * 0.55}")
    else:
        print(print(f" O preço a pagar é de R$ {eneriaConsumida * 0.60}"))

else:
    print("Opção inválida")
