import sqlite3

conn = sqlite3.connect('exercise.db')
#
# # Criando a tabela de alunos
# conn.execute('''CREATE TABLE Alunos (
#    cod_aluno INTEGER PRIMARY KEY NOT NULL,
#    Nome VARCHAR NOT NULL ,
#    Cpf Interger NOT NULL );''')
#
# conn.commit()
#
# # Criando a tabela de professores
# conn.execute('''CREATE TABLE Professores (
#    cod_professor INTEGER PRIMARY KEY NOT NULL,
#    Nome VARCHAR NOT NULL ,
#    Cpf Interger NOT NULL );''')
#
# conn.commit()
#
# # Criando a tabela de disciplinas
# conn.execute('''CREATE TABLE Disciplinas (
#    cod_disciplinas INTEGER PRIMARY KEY NOT NULL,
#    nome VARCHAR NOT NULL,
#    cargaHoraria TEXT NOT NULL);''')
#
# conn.commit()
#
# # Criando a tabela de turmas
# conn.execute('''CREATE TABLE Turmas (
#    cod_turma INTEGER PRIMARY KEY NOT NULL,
#    titulo VARCHAR NOT NULL,
#    ano INTEGER NOT NULL);''')
#
# conn.commit()
#
# # Criando a tabela de disciplinas de cada Turma
# conn.execute('''CREATE TABLE Disc_Turma (
#    cod_Disciplinas_Turmas INTEGER PRIMARY KEY NOT NULL,
#    cod_disciplina INTEGER NOT NULL,
#    cod_professor INTEGER NOT NULL,
#    cod_turma INTEGER NOT NULL,
#    horario VARCHAR NOT NULL);''')
#
# # Criando a tabela de disciplinas de cada Histórico
# conn.execute('''CREATE TABLE historico (
#    cod_historico INTEGER PRIMARY KEY NOT NULL,
#    cod_aluno INTEGER NOT NULL);''')
#
# conn.commit()
#
# # Criando a tabela de disciplinas de cada disciplina e nota do Histórico
# conn.execute('''CREATE TABLE Hist_Disci (
#    cod_Hist_Disci INTEGER PRIMARY KEY NOT NULL,
#    cod_disciplina INTEGER NOT NULL,
#    nota REAL NOT NULL,
#    cod_historico INTEGER NOT NULL);''')
#
# conn.commit()
cursor = conn.cursor()
conn.execute("INSERT INTO Alunos (Nome, Cpf) VALUES ('João Pedro Pereira', 112778908965);")
conn.execute("INSERT INTO Alunos (Nome, Cpf) VALUES ('Maria Luiza Costa', 122000908778);")

comando = conn.execute("SELECT * FROM Alunos ;")

print(comando.fetchall())

conn.execute("INSERT INTO Professores (Nome, Cpf) VALUES ('José da Silva', 1028890908900);")
conn.execute("INSERT INTO Professores (Nome, Cpf) VALUES ('Lúcia Cristina Viana', 115000908666);")
conn.execute("INSERT INTO Professores (Nome, Cpf) VALUES ('Maria Passos Araújo', 103010608686);")

comando=conn.execute("SELECT * FROM professores ;")

print(comando.fetchall())

conn.execute("INSERT INTO disciplinas (nome, cargaHoraria) VALUES ('Matemática', '30:00');")
conn.execute("INSERT INTO disciplinas (nome, cargaHoraria) VALUES ('Portugês', '20:00');")

comando=conn.execute("SELECT * FROM disciplinas ;")

print(comando.fetchall())

conn.execute("INSERT INTO turmas (titulo, ano) VALUES ('primeiro ano A', 2022);")
conn.execute("INSERT INTO turmas (titulo, ano) VALUES ('primeiro ano B', 2019);")
conn.execute("INSERT INTO turmas (titulo, ano) VALUES ('segundo ano A', 2023);")

comando=conn.execute("SELECT * FROM turmas ;")

print(comando.fetchall())

conn.execute("INSERT INTO Disc_Turma (cod_turma, cod_disciplina, horario, cod_professor) VALUES (1, 1, 'segunda e quarta de 10:00 às 10:50', 1);")
conn.execute("INSERT INTO Disc_Turma (cod_turma, cod_disciplina, horario, cod_professor) VALUES (1, 2, 'segunda e quarta de 08:00 às 08:50', 2);")

conn.execute("INSERT INTO Disc_Turma (cod_turma, cod_disciplina, horario, cod_professor) VALUES (2, 1, 'terça e quinta de 10:00 às 10:50',1);")
conn.execute("INSERT INTO Disc_Turma (cod_turma, cod_disciplina, horario, cod_professor) VALUES (2, 2, 'terça e quinta de 08:00 às 08:50',2);")

conn.execute("INSERT INTO Disc_Turma (cod_turma, cod_disciplina, horario,cod_professor) VALUES (3, 1, 'terça  de 08:00 às 09:40',1);")
conn.execute("INSERT INTO Disc_Turma (cod_turma, cod_disciplina, horario,cod_professor) VALUES (3, 2, 'terça  de 08:00 às 09:40',3);")

comando=conn.execute("SELECT * FROM Disc_Turma ;")

print(comando.fetchall())

comando=conn.execute("SELECT turmas.titulo, Professores.nome, Disciplinas.nome, horario  FROM Disc_Turma JOIN turmas ON Disc_Turma.cod_turma = turmas.cod_turma  JOIN Professores ON Disc_Turma.cod_professor=Professores.cod_professor JOIN disciplinas ON Disc_Turma.cod_disciplina=disciplinas.cod_disciplinas ;")

print(comando.fetchall())

conn.execute("INSERT INTO historico (cod_aluno) VALUES (1);")
conn.execute("INSERT INTO historico (cod_aluno) VALUES (2);")

comando=conn.execute("SELECT * FROM historico ;")
print(comando.fetchall())


conn.execute("INSERT INTO Hist_Disci (cod_disciplina, nota, cod_historico) VALUES (1, 98.7, 1);")
conn.execute("INSERT INTO Hist_Disci (cod_disciplina, nota, cod_historico) VALUES (2, 88.5, 1);")

conn.execute("INSERT INTO Hist_Disci (cod_disciplina, nota, cod_historico) VALUES (1, 78.0, 2);")
conn.execute("INSERT INTO Hist_Disci (cod_disciplina, nota, cod_historico) VALUES (2, 89.1, 2);")

comando=conn.execute("SELECT * FROM Hist_Disci ;")
print(comando.fetchall())

comando=conn.execute("SELECT * FROM historico JOIN Hist_Disci ON historico.cod_historico = Hist_Disci.cod_historico  WHERE historico.cod_aluno==1 ;")
print(comando.fetchall())

comando=conn.execute("SELECT alunos.nome, disciplinas.nome, Hist_Disci.nota  FROM Hist_Disci JOIN historico ON Hist_Disci.cod_historico = historico.cod_historico JOIN alunos ON alunos.cod_aluno=historico.cod_aluno JOIN disciplinas ON Hist_Disci.cod_disciplina=disciplinas.cod_disciplinas WHERE historico.cod_aluno==1 ;")

print(comando.fetchall())