A ideia desse projeto é você aprender a criar instâncias pelo próprio Python Utilizando a biblioteca BOTO3, dessa forma você não precisará manusear o site, pois os mesmos comandos que você faria no site agora você irá fazer pelo python, não irá somente criar instâncias, também poderá alterar  informações e deletar a instância se quiser.

Se certifique de fazer esse tutorial tanto com o BOTO3 quanto com o Troposphere

No terminal do diretório do seu projeto faça os seguintes comandos:

1 - pip install awscli

2 - pip install boto3

3 - aws configure

4 - pip install Troposphere


Agora no site AWS:

1 - Acesso painel IAM

2 - Clique no número 0 de usuários

3 - Clique em criar usuários

4 - Clique em quero criar um usário do IAM, coloque o nome do usuario

5 - depois selecione AdministratorAcess antes de continuar

6 - Depois do usuario criado clique no nome do usuário

7 - clique em criar uma chave de acesso

8 - copie esta chave de acesso para colar no termrinal

9 - faça o mesmo com a chave secreta, os outros campos você não precisa preencher

OBS: Os arquivos csv que você baixar devem estar no diretório do projeto python
