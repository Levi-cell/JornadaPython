# Estrutura do loop for da list comprehension

contagem = [n for n in range(1, 11)]  # 1 é incluso, 11 é não incluso
print(contagem)
print("-----------")
# Diferente da estrutura comum, você não precisa utilizar append
# e não precisa criar uma lista

contagem = [n for n in range(1, 11) if n % 2 == 0]
print(contagem)
print("-----------------------")
