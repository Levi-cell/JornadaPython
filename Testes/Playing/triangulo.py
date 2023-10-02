def calcular_numero_triangular(n):
    if n == 1:
        return 1
    else:
        return n + calcular_numero_triangular(n - 1)

def imprimir_triangulo(numero_triangular, linha_atual=1):
    if linha_atual > numero_triangular:
        return
    imprimir_triangulo(numero_triangular, linha_atual + 1)
    print(" ".join([str(linha_atual)] * linha_atual))

# Solicita ao usuário um número natural N
N = int(input("Digite um número natural N: "))

# Calcula o N-ésimo número triangular
triangular = calcular_numero_triangular(N)

# Imprime o N-ésimo número triangular
print(f"O {N}-ésimo número triangular é {triangular}.")

# Imprime o triângulo equivalente ao número triangular
print(f"Triângulo equivalente:")
imprimir_triangulo(triangular)