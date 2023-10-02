Execute os seguintes comandos no terminal do seu diretório antes de começar:

1 - pip install django

2 - django-admin (consultar comados)

3 - django-admin startproject meuprojeto

4 - cd meuprojeto

4 - python manage.py startapp main (o nome é de sua preferência, não precisar ser main)

5 - python manage.py runserver


Executando as migrações e criando banco de dados:

1 - cd meuprojeto

2 - python manage.py makemigrations

3 - python manage.py sqlmigrate main 0001 (criará o banco de dados definido em main/models)

4 - python manage.py migrate

Criando Usuário

1 - cd meuprojeto

2 - python manage.py createsuperuser

Acessando as linhas de comando do shell do Django:

1 - cd meuprojeto

2 - python manage.py shell

No shell faça os seguintes blocos de código(aconselho usar o windows PowerShell):

1 - from main.models import ProjetoDjango as pd
    from datetime import datetime as dt

2 - pd(titulo = "titulo", descricao = "descricao", numero_de_modulos = 0, data = dt.now()).save()

3 - pd.objects.filter(titulo="Python Pro")

4 - pd.objects.exclude(titulo="Python Pro")

5 - pd.objects.get(pk=1)

6 - [print(p) for p in pd.objects.raw("select 1 id, titulo from main_ProjetoDjango")]

7 - pd.objects.filter(titulo="Python do Zero ao Pro").delete()

CURIOSIDADE DO TÓPICO ANTERIOR

1 - curso = pd.objects.get(pk=1)
2 - print(curso)


