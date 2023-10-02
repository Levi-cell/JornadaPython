import sqlite3

#conectando e criando um banco de dados
# banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('empresa.db')

#criando um cursor para operar comandos SQL


cursor = banco.cursor()

cursor.execute("CREATE TABLE estudantes(idEstudante integer, nomeEstudante text,idade integer, email text, idDepartamento integer)")

cursor.execute("INSERT INTO estudantes VALUES(1, 'Maria', 40, 'mariadosanjos@mentorama.com', 2)")
banco.commit()

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

listaestudantes = [('2', 'Felipe', '18', 'felipe@mentorama.com', '1'),
                   ('3', 'Maria', '45', 'maria@mentorama.com', '4'),
                   ('4', 'João', '33', 'joao@mentorama.com', '4'),
                   ('5', 'Lucia', '17', 'lucia@mentorama.com', '2'),
                   ('6', 'Pedro', '32', 'pedro@mentorama.com', 'NULL'),
                   ('7', 'Izabela', '23', 'izabela@mentorama.com', '3'),
                   ('8', 'Eduardo', '59', 'eduardo@mentorama.com', '4',),
                   ('9', 'Tiago', '38', 'tiago@mentorama.com', '5'),
                   ('10', 'Ana', '25', 'ana@mentorama.com', 'NULL'),
                   ('11', 'Carol', '36', 'carol@mentorama.com', '2'),
                   ('12', 'Leonardo', '28', 'leonardo@mentorama.com', '3'),
                   ('13', 'Vanessa', '45', 'vanessa@mentorama.com', '4'),
                   ('14', 'João', '43', 'joaopedro@mentorama.com', '5'),
                   ('15', 'Mari', '25', 'mari@mentorama.com', '6')]
#
cursor.executemany("""INSERT INTO estudantes VALUES(?,?,?,?,?)""", listaestudantes)
print("Dados inseridos com sucesso!")
banco.commit()

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

#Atualizar o registro

sql = """
UPDATE estudantes
SET nomeEstudante = 'Diego'
WHERE nomeEstudante = 'Felipe'
"""

cursor.execute(sql)
banco.commit()
print("Registros atualizados com sucesso!")

cursor.execute("Select * FROM estudantes")
print(cursor.fetchall())

#Deletando registros

sql = """
DELETE FROM estudantes
WHERE nomeEstudante = 'Maria'
"""

cursor.execute(sql)
banco.commit()
print("Registros deleteados com sucesso")

cursor.execute("SELECT * FROM ESTUDANTES")
print(cursor.fetchall())

# # Deletando uma tabela
#
sql = """
DROP TABLE estudantes"""

cursor.execute(sql)
banco.commit()
print("Tabela deletada com sucesso!")

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

#Where

cursor.execute("""SELECT * FROM estudantes
WHERE idade == '33'""")

print(cursor.fetchall())

cursor.execute("""SELECT * FROM estudantes
WHERE nomeEstudante = 'Diego'
""")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

cursor.execute("""SELECT * FROM estudantes
WHERE nomeEstudante = 'Diego' AND idade = '18' """)

print(cursor.fetchall())

cursor.execute("SELECT * FROM estudantes WHERE nomeEstudante = 'Maria' OR idade = '18'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM estudantes WHERE NOT nomeEstudante = 'Maria' OR idade = '18'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM estudantes WHERE NOT nomeEstudante = 'Maria' AND idade = '18'")
print(cursor.fetchall())

#Order by

cursor.execute("SELECT nomeEstudante, idade FROM estudantes ORDER BY idade ASC")
print(cursor.fetchall())

#Group by

cursor.execute("SELECT nomeEstudante, idDepartamento FROM estudantes GROUP BY nomeEstudante")
print(cursor.fetchall())

#COUNT/AVG/SUM

sql = """SELECT COUNT(nomeEstudante)
FROM estudantes
WHERE nomeEstudante = 'Maria'"""
cursor.execute(sql)
print(cursor.fetchall())

sql = """SELECT AVG(idade)
FROM estudantes
WHERE idade > '18'"""
cursor.execute(sql)
print(cursor.fetchall())

sql = """SELECT SUM(idade)
FROM estudantes
WHERE idade > '18'"""
cursor.execute(sql)
print(cursor.fetchall())

#INNER JOIN

cursor.execute("CREATE TABLE departamentos(idDepartamento integer PRIMARY KEY, nomeDepartamento text)")
print("Tabela criada com sucesso!")

listaDepartamento = [('1', 'TI'),
                     ('2', 'Fisica'),
                     ('3', 'Matemática'),
                     ('4', 'Engenharia'),
                     ('5', 'Biologia'),
                     ('6', 'História')]

cursor.executemany("""INSERT INTO departamentos VALUES (?,?)""", listaDepartamento)
print("Dados inseridos com sucesso!")
banco.commit()

cursor.execute("SELECT * FROM departamentos")
print(cursor.fetchall())

sql = """SELECT
  e.nomeEstudante,
  d.nomeDepartamento
FROM departamentos d
INNER JOIN Estudantes e ON e.idDepartamento = d.idDepartamento"""
cursor.execute(sql)
print(cursor.fetchall())

#Left join

sql = """SELECT
  e.nomeEstudante,
  d.nomeDepartamento
FROM Estudantes e
LEFT JOIN departamentos d ON e.idDepartamento = d.idDepartamento
"""
cursor.execute(sql)
print(cursor.fetchall())

#Cross join #Faz uma combinação com todos os nome da outra tabela,
#Cada elemento da tabela A se combina com cada elemento da tabela B

sql = """SELECT
  e.nomeEstudante,
  d.nomeDepartamento
FROM Estudantes e
CROSS JOIN departamentos d"""
cursor.execute(sql)
print(cursor.fetchall())
