salario = float(input( "Digite o salário do funcionário: " + "\n"))

if salario > 1250.00:
    aumento = salario * 0.10
    salario = salario + aumento
    print("você teve aumento de: %.2f" % aumento, "\n",
          " e o seu salário agora é de: %.2f" % salario)

else:
    aumento = salario * 0.15
    salario = salario + aumento

    print("você teve aumento de: %.2f" % aumento, "\n",
          " e o seu salário agora é de: %.2f" % salario)
