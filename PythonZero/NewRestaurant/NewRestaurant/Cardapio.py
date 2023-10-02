def cardapio():
    pratos_dic = {
    }
    while True:
        nome_prato = input("digite o nome do prato ou da bebida:" + "\n")

        while not nome_prato.replace(" ", "") or not nome_prato[:5].isalpha() or len(nome_prato) <= 2:
            nome_prato = input("digiete o nome do prato novamente:" + "\n")

        while True:
            try:
                preco = float(input("Digite o preço do prato ou da bebida: " + "\n"))
                break
            except ValueError:
                print("Entrada inválida." + "\n")

        pratos_dic[nome_prato] = preco

        arquivoCardapio = open("Cardapios.txt", 'a')
        arquivoCardapio.write(f"prato: {nome_prato}, valor: {preco}" + "\n")

        print("Cardápio atualizado:", "\n")
        for x in pratos_dic:
            print(f"{x} : R$ {pratos_dic[nome_prato]}")
        print(" ")
        opcao = input("Deseja adicionar mais algum prato? Digite S ou N:" + "\n")
        if opcao == "N":
            arquivoCardapio.close()
            break

    return pratos_dic