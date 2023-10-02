Caso comece o projeto do zero digite os seguintes comandos no terminal do seu diretório:

1 - pip install djangopython manage.py runserver
2 - django-admin startproject meusFilmes
3 - cd meusFilmes
4 - python manage.py startapp main

Executando o projeto:

1 - python manage.py runserver

2 - acesse no navegador as seguintes rotas: http://127.0.0.1:8000/ ou /observacao ou /admin

Após adaptar o arquivo models.py faça a migração:

1 - python manage.py makemigrations

2 - python manage.py sqlmigrate main 0001 (verificar as tabelas criadas)

3 - python manage.py migrate

4 - python manage.py createsuperuser

Caso queira manipular o banco de dados siga esse passo a passo:

1 - cd meusFilmes

2 - python manage.py shell

3 - from main.models import ProjetoDjango as pd

4 - pd(filme = "filme", descricao = "descricao").save()

5 - pd.objects.filter(filme="Speed Racer")

6 - pd.objects.exclude(filme="Speed Racer")

7 - pd.objects.get(pk=1)

8 - [print(p) for p in pd.objects.raw("select 1 id, filme from main_ProjetoDjango")]

9 - pd.objects.filter(filme="Speed Racer").delete()

CURIOSIDADE DO TÓPICO ANTERIOR

1 - filme = pd.objects.get(pk=1)
2 - print(filme)

Caso queira usar o docker faça essas configurações do docker, no seu terminal faça os seguintes comandos:

1 - docker build -t my-django-app:v1 .
2 - docker run -d -p 8000:8000 my-django-app:v1

Caso esteja usando windows baixe o aplicativo docker vá em images clique em my-django-app em seguida clique em Run e vá em optional settings e adicione 8000 em host port e depois clique em Run

Caso queira conhecer melhor: https://vimeo.com/865760796/d1dac92a56
