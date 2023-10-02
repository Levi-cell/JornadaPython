from Cardapio import *
def abre_conta():

    while True:
        try:
            numero_mesa = int(input("Digite o número da mesa: " + "\n"))
            break
        except ValueError:
            print("Entrada inválida. Digite o número da mesa novamente novamente:" + "\n")



    garcom = input("Digite o nome do garçom:" + "\n")
    while len(garcom) <= 2 or not garcom.isalpha():
        garcom = input("Nome de garçom invalido, digite novamente" + "\n")

    conta = {

        'Número da mesa': numero_mesa,
        'Nome do garçom': garcom,
        'Itens': [],

    }
    contasAbertas = open("Contas abertas.txt", 'a')
    contasAbertas.write(f"{conta}" + "\n")
    contasAbertas.close()

    return conta


def adiciona_item(lista_contas):
    dados = open('dadosRestaurante.txt', 'a')# control alt enter : formata automaticamente
    while True:
        try:
            numero_mesa = int(input("Digite o número da mesa : " + "\n"))
            break
        except ValueError:
            print("Entrada inválida." + "\n")
    if not lista_contas:
        print("Você ainda não abriu nenhuma conta..." + "\n")
        return lista_contas

    achou_mesa = False
    posicao = 0
    while not achou_mesa and posicao < len(lista_contas):
        if lista_contas[posicao]['Número da mesa'] == numero_mesa:

            item = input("Digite o nome do item que deseja adicionar:" + "\n")
            if item not in cardapio_dia:
                while item not in cardapio_dia:
                    print("Essa prato não está no cardapio, confira o cardapio:" + "\n")
                    for prato in cardapio_dia:
                        print(f"{prato} : R$ {cardapio_dia[prato]}")
                    print(" ")
                    item = input("Digite o prato novamente (cuidado com letras maisculas e minisculas):" + "\n")
            while True:
                try:
                    quantidade = int(input("Digite a quantidade que deseja adicionar:" + "\n"))
                    break
                except ValueError:
                    print("Entrada inválida." + "\n")

            valor_unitario = cardapio_dia[item]

            item = {
                'Nome do item': item,
                'quantidade': quantidade,
                'valor unitário do Item': valor_unitario

            }

            valor_total = quantidade * valor_unitario
            print("----------------------")
            print(f"Foi adicionado {quantidade} poções de {item['Nome do item']} por {valor_total}"
                  f" na mesa {lista_contas[posicao]['Número da mesa']}" + "\n")
            print("----------------------")
            lista_contas[posicao]['Itens'].append(item)
            achou_mesa = True
            dados.writelines(f"{item}" + "\n")
        posicao += 1
    dados.close()
    if not achou_mesa:
        print("Mesa não encontrada")
    return lista_contas


def fechar_conta(lista_contas):
    while True:
        try:
            numero_mesa = int(input("Digite o número da mesa: " + "\n"))
            break
        except ValueError:
            print("Entrada inválida." + "\n")
    valor_total_conta = 0
    if not lista_contas:
        print("Você ainda não abriu nenhuma conta...." + "\n")
        return valor_total_conta

    achou_mesa = False
    posicao = 0
    while not achou_mesa and posicao < len(lista_contas):
        if lista_contas[posicao]['Número da mesa'] == numero_mesa:
            print("Itens:")
            for item in lista_contas[posicao]['Itens']:
                total_pedido = item['quantidade'] * item['valor unitário do Item']
                valor_total_conta += total_pedido
                print(f"{item['Nome do item']}: {item['quantidade']} x {item['valor unitário do Item']} "
                      f"= R$ {total_pedido}")
            lista_contas.remove(lista_contas[posicao])
            achou_mesa = True
        posicao += 1

    if not achou_mesa:
        print("Não há nenhuma conta aberta nesta mesa...." + "\n")
        return valor_total_conta

    dez_por_cento = gorjeta(valor_total_conta)
    valor_total_conta += dez_por_cento
    print(f"Valor que o garçom receberá será R$ {dez_por_cento}")
    print("----------------------")
    print(f"A conta foi encerrrada no valor de R$ {valor_total_conta}")
    print("----------------------")

    return valor_total_conta


def gorjeta(valor_total):  # nem precisa usar essa função
    return valor_total * 0.1


def faturamento_dia(contas_fechadas):
    return sum(contas_fechadas)

def historicoVendas():
    dados = open('dadosRestaurante.txt', 'r')

    linhas = dados.readlines()
    for linha in linhas:
        dados1 = linha.split(';')
        print(f"{dados1}")
    dados.close()


cardapio_dia = cardapio()
lista_conta = []  # Armazena contas
contas_fechadas = []  # Armazena o valor de contas fechadas

# MENU

while True:

    menu = (input("""
       Confira as opções:
       1 - Abrir uma conta.
       2 - Adicionar um item a uma conta.
       3 - Fechar uma conta e Calcular valor do garçom.
       4 - Consultar o Cardápio
       5 - Consultar o faturamento até agora.
       6 - Consultar contas abertas.
       7 - Atualizar Cardapio
       8 - Histórico de venda
       9 - Encerrar o expediente (Recomendável Fechar todas as contas antes).
       O que deseja fazer:""" + "\n"))
    print("-----------------")

    if menu == "1":
        recebe_conta = abre_conta()
        lista_conta.append(recebe_conta)
        print("-----------------------")
        print(f"Conta adicionada, Confira:")
        print(f"Número da mesa : {recebe_conta['Número da mesa']}, Garçom: {recebe_conta['Nome do garçom']}" "\n")
        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")

    elif menu == "2":
        lista_conta = adiciona_item(lista_conta)
        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")

    elif menu == "3":
        valor_conta = fechar_conta(lista_conta)
        contas_fechadas.append(valor_conta)
        totaisContas = open("Valores totais de cada conta.txt", 'a')
        totaisContas.write(f"R$ {valor_conta}" + "\n")

        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")

    elif menu == "4":
        print("Cardápio atualizado:", "\n")
        for x in cardapio_dia:
            print(f"{x} : R$ {cardapio_dia[x]}")
        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")

    elif menu == "5":
        faturamento = faturamento_dia(contas_fechadas)
        print(f"o faturamento até agora é {faturamento}")
        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")

    elif menu == "6":
        for x in lista_conta:
            print(f"Número da mesa: {x['Número da mesa']}, Nome do garçom: {x['Nome do garçom']}, Itens {x['Itens']}")
            print("------------------------------------------------ ")
        if len(lista_conta) == 0:
            print("Nenhuma conta aberta")
        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")

    elif menu == "7":
        cardapio_dia = cardapio()

    elif menu == "8":
        historicoVendas()

    elif menu == "9":
        faturamento = faturamento_dia(contas_fechadas)
        print(f"O faturamento fechou em: {faturamento}")
        break
    else:
        print("opção invalida")
        interativo = input("Digite qualquer coisa para voltar pro menu:" + "\n")