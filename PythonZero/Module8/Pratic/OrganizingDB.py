import sqlite3
conn = sqlite3.connect('exercicio.db')

# Criando a tabela de alunos

conn.execute("""CREATE TABLE Alunos (
cod_aluno INTEGER PRIMARY KEY NOT NULL,
Nome VARCHAR NOT NULL,
Cpf Integer NOT NULL);""")

conn.commit()

# Criando a tabela de professores

conn.execute("""CREATE TABLE Professores (
cod_professor INTEGER PRIMARY KEY NOT NULL,
Nome VARCHAR NOT NULL,
Cpf Interger NOT NULL);""")

conn.commit()

# Criando a tabela de turmas

conn.execute("""CREATE TABLE Turmas (
cod_turma INTEGER PRIMARY KEY NOT NULL,
titulo VARCHAR NOT NULL,
ano INTEGER NOT NULL);""")

conn.commit()

# Criando a tabela de disciplinas de cada Turma

conn.execute("""CREATE TABLE Disc_Turma (
cod_Disciplinas_Turmas INTEGER PRIMARY KEY NOT NULL,
cod_disciplina INTEGER NOT NULL,
cod_professor INTEGER NOT NULL,
cod_turma INTEGER NOT NULL,
horario VARCHAR NOT NULL);""")

# Criando a tabela de disciplinas de cada Histórico

conn.execute("""CREATE TABLE historico(
cod_historico INTEGER PRIMARY KEY NOT NULL,
cod_aluno INTEGER NOT NULL);""")

conn.commit()

# Criando a tabela de disciplinas de cada disciplina e nota do histórico

conn.execute("""CREATE TABLE Hist_Disci(
cod_Hist_Disci INTEGER PRIMARY KEY NOT NULL,
cod_disciplina INTEGER NOT NULL,
nota REAL NOT NULL,
cod_historico INTEGER NOT NULL);""")

conn.commit()