import sqlite3
# Não adicionei dados, preguiça, ninguém merece
# Minha preguiça é bem justificada fiz o curso de SQL, essa era a única parte Chata kkkk

banco = sqlite3.connect('empresa.db')


# Criando a tabela de funcionarios

# banco.execute("""CREATE TABLE funcionarios (
# id INTEGER PRIMARY KEY NOT NULL,
# primeiro_nome VARCHAR NOT NULL,
# segundo_nome VARCHAR NOT NULL,
# ultimo_nome VARCHAR NOT NULL,
# data_nasci VARCHAR NOT NULL,
# CPF VARCHAR NOT NULL,
# RG VARCHAR NOT NULL,
# Endereco VARCHAR NOT NULL,
# CEP VARCHAR NOT NULL,
# cidade VARCHAR NOT NULL,
# Telefone VARCHAR NOT NULL,
# codigo_departamento INTEGER NOT NULL,
# Funcao VARCHAR NOT NULL,
# Salario INTERGER NOT NULL);""")
#
# banco.commit()

# banco.execute("""CREATE TABLE departamentos (
# id INTEGER PRIMARY KEY NOT NULL,
# nome VARCHAR NOT NULL,
# localizacao VARCHAR NOT NULL,
# codigo_funcionario_gerente);""")
#
# banco.commit()

cursor = banco.cursor()
# a)
consulta = """
SELECT primeiro_nome, segundo_nome
FROM funcionarios
ORDER BY segundo_nome ASC"""

cursor.execute(consulta)
print(cursor.fetchall())

# b)

cursor.execute("""SELECT * FROM funcionarios
ORDER BY cidade""")
print(cursor.fetchall())

# c)

cursor.execute("""SELECT * FROM funcionarios
WHERE salario > 1000
ORDER BY 2,3,4""")
print(cursor.fetchall())

# d)

cursor.execute("""SELECT data_nasci, primeiro_nome
FROM funcionarios
ORDER BY data_nasci ASC""")
print(cursor.fetchall())

# e)

cursor.execute("""SELECT SUM(Salario) FROM funcionarios""")
print(cursor.fetchall())

# f)

cursor.execute(
    """SELECT f.primeiro_nome,
                         d.nome,
                         f.Funcao
    FROM funcionarios f
    INNER JOIN departamentos d on d.id = f.codigo_departamento""")

print(cursor.fetchall())

# g)

cursor.execute(
    """SELECT count(id) From funcionarios"""
)
print(cursor.fetchall())

# f)

cursor.execute("""SELECT 
d.nome,
f.primeiro_nome
FROM funcionarios f 
INNER JOIN departamentos d on f.codigo_departamento = d.id
ORDER BY d.id and f.id""")

print(cursor.fetchall())
#outra forma
cursor.execute("""SELECT 
d.nome,
f.primeiro_nome
FROM funcionarios f 
INNER JOIN departamentos d on f.codigo_departamento = d.id
ORDER BY d.id,f.id""")

print(cursor.fetchall())

#mais outra forma

cursor.execute("""SELECT 
d.nome,
f.primeiro_nome
FROM funcionarios f 
INNER JOIN departamentos d on f.codigo_departamento = d.id
ORDER BY 1,2""")

print(cursor.fetchall())