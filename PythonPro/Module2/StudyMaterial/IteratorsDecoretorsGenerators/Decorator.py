def decor(func): # decor recebe uma função como argumento
    def wrapper(): # definimos outra função dentro de decor
        frase = " ".join(func())  # a variavel frase irá receber a função do argumento só que com espaços entre as letras
        return frase  # a função de dentro irá retornar a frase modificada
    return wrapper   # e por sua vez a função de fora "decor" irá retornar a funçao de dentro

decor("teste")


"""o @  é como charmar a função decor e tudo que estiver adiante será o seu embrulhamento"""
# é a forma de vc aplicar o que você viu logo acima
@decor
def vamosFalar():
    return "Python Pro Mentorama"

# perceba que aqui ela já foi modificada
print(vamosFalar())