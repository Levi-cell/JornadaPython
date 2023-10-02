def cadastro_aluno():

        nome_aluno = input("Digite o nome do aluno:" + "\n")
        tamanho_camisa = input("Digite o tamanho da camisa:" + "\n")

        while tamanho_camisa != "P" and tamanho_camisa != "p"\
              and tamanho_camisa != "M" and tamanho_camisa != "m"\
              and tamanho_camisa != "G" and tamanho_camisa != "g"\
              and tamanho_camisa != "GG" and tamanho_camisa != "gg":
            tamanho_camisa = input("tamanho inválido, digite novamente:" + "\n")

        dic_aluno = {
            'Nome do aluno': nome_aluno,
            'Tamanho da camisa': tamanho_camisa.upper()
        }

        print(f"{dic_aluno['Nome do aluno']} irá vestir uma camisa de tamanho {dic_aluno['Tamanho da camisa']}", "\n")

        return dic_aluno

def fazer_pedido(lista_cadastro):

    p = 0
    m = 0
    g = 0
    gg = 0

    for alunos in lista_cadastro:

        if alunos['Tamanho da camisa'] == "P":
            p = p + 1
        elif alunos['Tamanho da camisa'] == "M":
            m = m + 1
        elif alunos['Tamanho da camisa'] == "G":
            g = g + 1
        elif alunos['Tamanho da camisa'] == "GG":
            gg = gg + 1

    print("foram encomendadas:")
    print(f"""
    {p} camisas do tamanho P
    {m} camisas do tamanho M
    {g} camisas do tamanho G
    {gg} camisas do tamanho GG """)
    print("TOTAL: ", p + m + g + gg, "Camisas", "\n")

def confere_tamanho(lista_cadastro):

    nome_aluno = input("Digite o nome do aluno que deseja verificar" + "\n")

    aluno_encontrado = False
    posicao = 0
    while not aluno_encontrado and posicao < len(lista_cadastro):
        if lista_cadastro[posicao]['Nome do aluno'].lower() == nome_aluno.lower():
            print(f"O tamanho da camisa de {nome_aluno} é {lista_cadastro[posicao]['Tamanho da camisa']}", "\n")
            aluno_encontrado = True
            break
        posicao += 1
    if not aluno_encontrado:
        print("Aluno não encontrado na lista.")


lista_alunos = []

while True:

    menu = int(input("""Escolha uma das opções abaixo:
    1 - Adicionar um aluno
    2 - Conferir alunos cadastrados
    3 - Realizar o pedido das camisas de todos os alunos
    4 - Verificar o tamanho de um aluno
    5 - Encerrar programa
    Digite uma opção:""" + "\n"))

    if menu == 1:
        recebe_aluno = cadastro_aluno()
        lista_alunos.append(recebe_aluno)
        opcao = input("Após conferir as informações, digite qualquer coisa para voltar pro menu:")

    elif menu == 2:
        print("Lista de alunos até o momento:" + "\n")
        for x in lista_alunos:
            print(f"{x['Nome do aluno']} : tamanho {x['Tamanho da camisa']}")
        print(" ")
        opcao = input("Após conferir as informações, digite qualquer coisa para voltar pro menu:")

    elif menu == 3:
        fazer_pedido(lista_alunos)
        opcao = input("Após conferir as informações, digite qualquer coisa para voltar pro menu:")

    elif menu == 4:
        confere_tamanho(lista_alunos)
        opcao = input("digite qualquer coisa para voltar pro menu:")

    elif menu == 5:
        print("Programa encerrado")
        break







