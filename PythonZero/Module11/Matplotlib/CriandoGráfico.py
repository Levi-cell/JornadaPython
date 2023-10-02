import matplotlib.pyplot as plt
print(plt.style.available)
#Antes de começar a desenvolver o gráfico vc pode escolher estilo e tamanho do gráfico

# Escolhendo estilo
plt.style.use('Solarize_Light2')

# Definindo o tamanho de todos os gráficos a serem impressos

plt.rcParams['figure.figsize'] = (11, 7)

# Definindo os valors do eixo x e y

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


fix, ax = plt.subplots()
# primeira forma de criar um gráfico, comente uma das formas para testar
ax.plot(x, y)
# Segunda forma de criar um gráfico
plt.plot(x, y)

# Criando um título para o gráfico

plt.title('Seu Título Legal')
# alterando o nome dos eixos
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')

# Quando terminar de desenvolver o gráfico, você pode salva-lo antes de o gerar

plt.savefig('nome_da_imagem.png', transparent=True)

#  Quando terminar de desenvovler seu gráfico utilize este comando para mostra:
plt.show()
