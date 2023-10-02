valorCasa = float(input("Digite o valor da casa:"))
salario = float(input("Digite o seu salário:"))
anos = int(input("Digite em quantos anos deseja pagar:"))

meses = anos*12
prestacaoMensal = valorCasa/meses
if prestacaoMensal > salario*0.3:
    print("A compra foi negada poois o valor da sua prestação mensal é superior a 30% do seu salário")
    print(f"O seu salário é de R$ {salario} e o valor da prestação é de R$ {prestacaoMensal} Mensais")
else:
    print("Compra Aprovada!!")
    print(f"o valor da prestação é de R$ {prestacaoMensal} Mensais")

