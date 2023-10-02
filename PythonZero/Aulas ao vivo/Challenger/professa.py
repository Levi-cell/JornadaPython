def cadastraCamisa():
  nome=input('Informe o nome')
  tamanho=input('Informe o tamanho da camisa')

  dic={'nome': nome, 'tamanho':tamanho}
  return dic


def fazerPedidoCamisa(listaAluno):

  p=0
  m=0
  g=0
  gg=0
  for x in listaAluno:
    if x['tamanho']=='p' or x['tamanho']=='P':
      p+=1
    elif x['tamanho']=='m' or x['tamanho']=='M':
      m+=1
    elif x['tamanho']=='g' or x['tamanho']=='G':
      g+=1
    else:
      gg+=1

  print(f'P-{p}')
  print(f'M-{m}')
  print(f'G-{g}')
  print(f'GG-{gg}')



def verificaTamanho(listaAluno):

  nome=input('Informe um nome')

  posicao=0
  while True:

    if listaAluno[posicao]['nome']==nome:
      print(listaAluno[posicao]['tamanho'])
      break


    posicao+=1



informar='S'
listaAluno=[]
while informar=='S':

  menu=int(input('O que deseja fazer? Digite 1 para cadastrar aluno, 2 para fazer pedido, 3 para verificar tamanho'))

  if menu==1:
    listaAluno.append(cadastraCamisa())
  elif menu==2:
    fazerPedidoCamisa(listaAluno)
  else:
    verificaTamanho(listaAluno)


  informar=input('Deseja continuar no programa? Digite S para sim ou N para não')