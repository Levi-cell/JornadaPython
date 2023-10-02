from re import findall, search

# vamos começar com um texto simples como exemplo

texto = "Estamos estudando Pithon no curso Python Pro da Mentorama"

print(findall("da", texto))

print(search("da", texto).start())  # retorna a primeira posição encontrada
print(texto.index("da"))  # é a mesma coisa

# Podemos também retirar caracteres especiais dos textos

caracteresEspeciais = "Estamos @ estudando #Python no curso 1 Python Pro da Mentorama"

palavras = findall(r"\w+", texto)  # retorna uma lista com as palavras sem caracters
print(palavras)
print(" ".join(palavras))  # agora você terá espaços e as palavras descompactadas como frase

# Quando não sabemos se um caractere está presente ou não, podemos utilizar o ponto no lugar dele

print(findall(r"P.thon", texto))

# Podemos também buscar apenas pela ocorrência inicial da palavra

padrao = r"\bpy"  # py no inicio no inicio da palavra
texto = "python é uma linguagem pythonica e os seu arquivos possuem extensão py"

print(findall(padrao, texto))

padrao = r"py\b"  # py no final da palavra
texto = "python é uma linguagem pythonica e os seu arquivos.py possuem extensão py"

print(findall(padrao, texto))