def adicionaCliente():

    id = 1

    while True:
        nomeCliente = input("Digite o nome do cliente que deseja adicionar:")

        clientes = open('clientes.txt', 'a')
        clientes.write(f"-id: {id}, nome do cliente:  {nomeCliente}" + "\n")
        id += 1
        escolha = input("Deseja adicionar mais algum cliente ? Digite Sim ou Não")
        if escolha == "Não":
            clientes.close()
            break

    return clientes

adicionaCliente()



def modificar_nome_cliente(arquivo, id_cliente, novo_nome):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    for i, linha in enumerate(linhas):
        if f"-id: {id_cliente}," in linha:
            partes = linha.split(", nome do cliente: ")
            if len(partes) == 2:
                linhas[i] = f"-id: {id_cliente}, nome do cliente: {novo_nome}\n"
                break

    with open(arquivo, 'w') as f:
        f.writelines(linhas)

id_cliente = int(input("Digite o id do cliente a ser modificado: "))
novo_nome = input("Digite o novo nome do cliente: ")

modificar_nome_cliente("Clientes.txt", id_cliente, novo_nome)
print("Nome do cliente modificado com sucesso!")


