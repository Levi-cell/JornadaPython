Esse projeto é apenas para ensinar como passar projetos Python para a Nuvem da AWS, você deve replicar esse tutorial sempre que terminar um projeto e precisar passar ele para nuvem:

---------------------------PARA USUÁRIOS DE WINDOWS---------------------------------------

//Criando Instância:

1 - Logue na sua conta AWS.

2 - Vá em Painiel EC2 e em executar instância.

3 - Escolha a instância que será usada, para esse projeto iremos utilizar ubuntu.

4 - Escolha sempres instâncias gratuitas caso não queira pagar nada.

5 - certifique-se de nomear uma chave nova, ou de usar alguma já criada.

6 - Gere uma chave .ppk se necessário para utilizar no PuTTY para não precisar converter lá na frente.

7 - Mova a chave pro diretório do seu projeto (opcional).

8 - Clique em executar instância.

9 - Em instâncias você pode conferir suas instância com status em verde, clique nela para ver mais informações.

10 - Após terminar seus projetos se certifique de encerrar a instância no site da AWS para evitar cobranças.

OBS:não delete as chaves que foram baixadas, se não você irá perder para sempre e terá que criar uma nova.

---------------------------SE CONECTANDO NA NUVEM---------------------------------------:

//Após baixar sua cheve faça o seguinte passo a passo se sua chave é do tipo.pem:

1 - Abra o PuTTyGEN, caso não tenha baixe.

2 - Vá em Conversions/Import Key e selecione a chave.pem.

3 - Após isso salve sua chave em "Save private key", você poderá nomear.

OBS: caso a chave seja do tipo .ppk não precisa fazer essa parte

//Após a conversão você deve fazer os seguintes passos no Windows:

1 - Abra o PuTTY, caso não tenha baixe.

2 - Vá em SSH/AUTH/CREDENTIALS.

3 - Após isso em private key encontre sua chave.ppk

4 - Depois disso clique em Session.

5 - Em "Host Name(or IP addrese)" Cole o Endereço de IPv4 público.

6 - Depois cliquem em Open.

7 - Clique em accept

8 - Irá abrir o terminal, você pode digitar ubuntu para acessar o projeto, depois digite cd /

9 - Agora que está conectado a nuvem se sinta a vontade para explorar o diretório com comandos como ls e cd

//Transferindo projeto python para o servidor:

1 - deixe o terminal do PuTTY aberto.

2 - Após seguir os passos de interface para navegar nos arquivos, arraste o seu projeto para o outro lado que é a nuvem.

------------INTERFACE PARA NAVEGAR NOS ARQUIVOS--------------------------------

1 - baixe o WinSCP

2 - Ao abrir ele vai abrir uma pagína de login 

3 - Vá em avançado, depois em arquivo de chave privada clique nos 3 pontos e selecione sua chave

4 - aperte em Ok

3 - depois em Host coloque o IPv4 público

4 - Em Usuário coloque ubuntu, não precisa de senha.

5 - Clique em login e aproveite a interface.

------------MEDIDAS DE SEGURANÇA OPCIONAL

1 - No Site da AWS vá em Security groups, você verá várias instâncias.

2 - Geralmente a instância que você está usando é a primeira(atual) 

3 - Confira se o "ID da VPC" é o mesmo da sua instância

4 - Vá em editar regras de entrada

5 - Customize a segurança de acordo com suas regulamentações ou da empresa


