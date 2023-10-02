# matriz de notas de 3 alunos em 4 provas

matriz = [[25.0, 20.0, 19.3, 15.9],
          [18.7, 24.5, 17.8, 19.9],
          [22.4, 19.2, 15.9, 23.8]]

print(matriz)

# FORMA COMUM

novaMatriz = []

for linha in matriz:
   listaNotas = []
   for elemento in linha:
      listaNotas.append(elemento*2)
   novaMatriz.append(listaNotas)

print(novaMatriz)

# Com list Comprehension

novaMatriz = [[elemento*2 for elemento in linha] for linha in matriz]

print(novaMatriz)