#curiosidade 1
import os

infos = [
    "Joao",
    "Paulo",
    "Brasil",
    "Desempregado",
    "Solteiro",
    "Ensino Superior",
    "25"
]


nome, sobrenome, *_, ensino, idade = infos

print(f"{nome} {sobrenome} está no {ensino} e tem {idade} anos")

lista = [
    "pica",
    "pica"
]
for palava in lista:
    print(palava.removeprefix('p'))


#String no python são imutaveis, tem que atribuir a elas de novo

texto = "   Python  "

texto = texto.strip() #strip remove espaços
texto = texto.replace("y", "ai ")
texto = texto.replace("h", "a ")

print(texto)

