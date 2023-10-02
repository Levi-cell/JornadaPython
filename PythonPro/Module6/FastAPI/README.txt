Antes de começar faça os seguintes comandos no terminal do seu repositório:

1 - pip install fastapi[all]
2 - pip install typing
3 - pip install requests
4 - pip install pytest
5 - pip install scanapi
6 - pip install pylint

Executando a aplicação:

1 - uvicorn main:app --reload

Gerando a documentação da API:

1 - scanapi run scanapi.yaml
