MULTIPLOS 

A ideia desse projeto é conferir se o número inserido é multiplo de 5 e 7 ou apenas de um desses números. se for multiplo de ambos será printado na tela "fizzbuzz". Caso seja apenas de 5 irá printar "fizz", caso seja de 7 irá printar "buzz" e caso não seja multiplo de nenhum deles irá printar "miss"


ORGANIZAÇÃO DOS ARQUIVOS/MÓDULOS

-main.py: irá executar o código para interação 
-Multiple.py: é a função que armazena a lógica do programa
-test.py: irá verificar se a função multiple está sendo executada corretamente e irá garantir a correção da função multiple, para isso use a estrutura do pytest para realizar o teste de caaso
-Dockerfile: irá permitir que você execute o projeto sem precisar baixar todas as ferramentas que utilizei abra seu CMD e confira os comandos no Dockerfile
-requirements.txt: esse arquivo lista todas as dependências do projeto

COMO EXECUTAR:

Para usar este projeto, siga as etapas abaixo:

Clone o repositório em sua máquina local usando o seguinte comando: git clone 

Abra um terminal ou prompt de comando e navegue até o diretório do projeto.

Execute o arquivo main.py usando o interpretador Python: python main.py

Insira um número natural quando solicitado para verificar se é múltiplo de 5, 7 ou ambos. O programa exibirá a mensagem correspondente.

EXECUTANDO OS TESTES

Para executar os testes automatizados para a função multiplo, execute o seguinte comando no diretório do projeto:

pytest test.py

Os testes serão executados e os resultados serão exibidos no console.

CONTRIBUIÇÃO

Contribuições para este projeto são bem-vindas. Se você quiser contribuir, siga estes passos:

Bifurque o repositório e crie um novo branch.

Faça as alterações ou acréscimos desejados.

Certifique-se de que os testes sejam aprovados com êxito.

Confirme suas alterações com uma mensagem de confirmação descritiva.

Envie suas alterações para seu repositório bifurcado.

Envie uma solicitação pull para o repositório original.

LICENSE

Este projeto está licenciado sob a licença MIT. 

Sinta-se à vontade para modificar e usar este código para seus próprios fins. Contribuições e sugestões são sempre bem-vindas!