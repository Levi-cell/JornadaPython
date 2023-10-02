def imprimir_matriz_intercalada(linhas, colunas):
    for i in range(linhas):
        linha = ""
        for j in range(colunas):
            if (i + j) % 2 == 0:
                linha += "0"
            else:
                linha += "1"
        print(linha)

# Exemplo de uso:
linhas = int(input("Digite quantas linhas você quer na matriz matriz: "))
colunas = int(input("Digite quantas colunas você quer na matriz matriz: "))
imprimir_matriz_intercalada(linhas, colunas)