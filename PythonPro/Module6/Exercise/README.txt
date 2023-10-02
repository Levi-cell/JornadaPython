Faça os seguinte comandos no terminal do projeto caso a execução dê errado:

1 - pip install fastapi[all]
2 - pip install typing
3 - pip install requests
4 - pip install pytest
5 - pip install scanapi
6 - pip install pycodestyle

Executando a aplicação:

1 - uvicorn main:app --reload

Gerando a documentação da API:

1 - Você pode acessar a documentação de outra forma acessando a rota http://127.0.0.1:8000/docs

2 - Não há necessidade de usar Scanapi

Execute os seguinte comandos para verificar os padrões de código

1 - python -m pylint arquivoDesejado.py

2 - python -m pycodestyle arquivoDesejado.py

Como manipular a API:

1 - acesse o seguinte link para acessar a calculadora: http://127.0.0.1:8000/docs
2 - abra o metódo POST que está em verde
3 - Clique em Try it out
4 - Coloque os valores que deseja e digite a operação escolhida
5 - Clique em Execute e verifique o resultado logo abaixo
OBSERVAÇÃO: A operação deve estar tudo em miniscúlo e bem acentuado

Executar os testes e requisicao:

1 - python test.py

2 - python requisicao.py

PYLINT SCORE:

calculadora.py - 9.17/10 (Pylint não entendeu que os returns são necessários para a aplicação funcionar)

test.py - 10/10 

requisicao.py - 10/10

api.py - 10/10

