nome = "JOAO LIRA"

print("O nome é", nome.title())

x = [150,3,40][-1] # pega o utltimo em [150,3,40]
y = round(24.3, -1)
#round vai arredondar a penultima casa decimal que será o 4, como 4 é menor que 5, será arredondado para 0

z = x / y

print(z)


nome = "Lira"

if nome == "João" or nome == "Paulo" or nome == "Marcus":
    print("Acesso Liberado")
else:
    print("Acesso negado")
# ou

if nome  in ["João", "Paulo", "Marcus"]:
    print("Acesso Liberado")
else:
    print("Acesso negado")