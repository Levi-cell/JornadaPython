# Equação de baskara
import math # na linha 46 uso a função sqrt.
print((-2)**2) # testando

print("-------------------")
print("Questão de Bhaskara")
print("-------------------")
#criando menu interativo com varáveis de interação
continuar_usando = "Sim"

while continuar_usando == "Sim":
    interacao = str(input("Seja bem vindo  a calculadora de bhaskara, digite qualquer tecla para continuar:"))
    print("-" * 35)
    print("""O que deseja fazer ?
             1 -Fazer sua própria equação
             2 -Conferir exemplo 1
             3 -Conferir exemplo 2
             4 -Conferir exemplo 3
             5 -Conferir exemplo 4
             6 -Conferir exemplo 5""")
    print("-" * 35,)
    Menu = int(input("Digete o número da opção que deseja:"))
    print("-" * 35,)

    if Menu == 1:
        delta = float
        interacao1 = str(input("Vamos começar calculando o seu delta, digite qualquer tecla para continuar: "))
        print("-" * 35)
        a = float(input("digite o valor da constante a:"))
        print("-" * 35)
        b = float(input("digite o valor da constante b:"))
        print("-" * 35)
        c = float(input("digite o valor da constante c:"))
        print("-" * 35)

        delta = ((b) ** 2) - (4 * a * c)

        interacao2 = str(input("Vamos agora conferir as condições do seu Delta, digite qualquer tecla para continuar:"))
        print("-" * 35)
        if (delta > 0) or ((a<0 or c<0) and ((b)**2>4*a*c)): # essa condições não são obrigatórias, é apenas curiosidade
            #logo depois do delta você pode comentar caso prefira
            print("Uhmm o seu delta é", delta," e por ser maior que zero, teremos duas raízes")
            interacao3 =  input("digite qualquer tecla para continuar:")
            print("-" * 35)

            x1 = float
            x2 = float
            raiz = math.sqrt(delta)
            x1 = (-b + raiz)/2*a
            x2 = (-b - (delta)**(1/2))/2*a

            interacao4 = str(input("""Já temos suas duas raízes com valores distintos
            digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da primeira raiz é ", x1, "e da segunda raiz é ", x2)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-"*35)

        if (delta == 0) or ((b == 0 and (a == 0 or c == 0))) or ((b) ** 2 == 4 * a * c):
            # essa condições não são obrigatórias, é apenas curiosidade
            #logo depois do delta você pode comentar caso prefira
            print("Uhmm o seu delta é 0, por isso teremos uma única raiz")
            interacao5 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            xO = float
            x0 = (-b + (delta)**(1/2))/2*a

            interacao6 = str(input("""Já temos a  raíz única digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da raiz única é:", x0)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)

        if (delta < 0) or ((a > 0 and c > 0) and((b)**2)<4*a*c) or ((a < 0 and c < 0) and((b)**2)<4*a*c):
            # essa condições não são obrigatórias, é apenas curiosidade
            # logo depois do delta você pode comentar caso prefira
            print("seu delta é ", delta, " por ser negativo as raízes são inexistentes, não tem :/ ")
            continuar_usando = input("""Quer continuar usando e encontra um delta positivo ? 
            Digite "Sim" caso queira continuar:""")
            print("-" * 35)


    if Menu == 2:
        delta = float
        a = float(1)
        b = float(-5)
        c = float(6)

        print("Neste exemlo o valor de a é:", a)
        print("Neste exemlo o valor de b é:", b)
        print("Neste exemlo o valor de c é:", c)

        interacao7 = str(input("Vamos começar calculando o delta, digite qualquer tecla para continuar: "))

        delta = ((b) ** 2) - (4 * a * c)

        interacao2 = str(input("Vamos agora conferir as condições do Delta, digite qualquer tecla para continuar:"))
        print("-" * 35)
        if (delta > 0) or ((a < 0 or c < 0) and ((b) ** 2 > 4 * a * c)):
            print("Uhmm o delta é", delta, " e por ser maior que zero, teremos duas raízes")
            interacao3 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            x1 = float
            x2 = float
            x1 = (-b + (delta) ** (1 / 2)) / 2 * a
            x2 = (-b - (delta) ** (1 / 2)) / 2 * a

            interacao4 = str(input("""Já temos as duas raízes com valores distintos
            digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da primeira raiz é ", x1, "e da segunda raiz é ", x2)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)
        if (delta == 0) or ((b == 0 and (a == 0 or c == 0))) or ((b) ** 2 == 4 * a * c):
            print("Uhmm o delta é 0, por isso teremos uma única raiz")
            interacao5 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            xO = float
            x0 = (-b + (delta)**(1/2))/2*a

            interacao6 = str(input("""Já temos a  raíz única digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da raiz única é:", x0)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)

        if (delta < 0) or ((a > 0 and c > 0) and ((b) ** 2) < 4 * a * c) or ((a < 0 and c < 0) and ((b) ** 2)<4*a*c):
            print("o delta é ", delta, " por ser negativo as raízes são inexistentes, não tem :/ ")
            continuar_usando = input("""Quer continuar usando e encontra um delta positivo ? 
            Digite "Sim" caso queira continuar:""")
            print("-" * 35)

    if Menu == 3:
        delta = float
        a = float(1)
        b = float(0)
        c = float(-9)

        print("Neste exemlo o valor de a é:", a)
        print("Neste exemlo o valor de b é:", b)
        print("Neste exemlo o valor de c é:", c)

        interacao7 = str(input("Vamos começar calculando o delta, digite qualquer tecla para continuar: "))

        delta = ((b) ** 2) - (4 * a * c)

        interacao2 = str(input("Vamos agora conferir as condições do Delta, digite qualquer tecla para continuar:"))
        print("-" * 35)
        if (delta > 0) or ((a < 0 or c < 0) and ((b) ** 2 > 4 * a * c)):
            print("Uhmm o delta é", delta, " e por ser maior que zero, teremos duas raízes")
            interacao3 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            x1 = float
            x2 = float
            x1 = (-b + (delta) ** (1 / 2)) / 2 * a
            x2 = (-b - (delta) ** (1 / 2)) / 2 * a

            interacao4 = str(input("""Já temos as duas raízes com valores distintos
            digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da primeira raiz é ", x1, "e da segunda raiz é ", x2)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)
        if (delta == 0) or ((b == 0 and (a == 0 or c == 0))) or ((b) ** 2 == 4 * a * c):
            print("Uhmm o delta é 0, por isso teremos uma única raiz")
            interacao5 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            xO = float
            x0 = (-b + (delta)**(1/2))/2*a

            interacao6 = str(input("""Já temos a  raíz única digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da raiz única é:", x0)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)

        if (delta < 0) or ((a > 0 and c > 0) and ((b) ** 2) < 4 * a * c) or ((a < 0 and c < 0) and ((b) ** 2)<4*a*c):
            print("o delta é ", delta, " por ser negativo as raízes são inexistentes, não tem :/ ")
            continuar_usando = input("""Quer continuar usando e encontra um delta positivo ? 
            Digite "Sim" caso queira continuar:""")
            print("-" * 35)

    if Menu == 4:
        delta = float
        a = float(5)
        b = float(-45)
        c = float(0)

        print("Neste exemlo o valor de a é:", a)
        print("Neste exemlo o valor de b é:", b)
        print("Neste exemlo o valor de c é:", c)

        interacao7 = str(input("Vamos começar calculando o delta, digite qualquer tecla para continuar: "))

        delta = ((b) ** 2) - (4 * a * c)

        interacao2 = str(input("Vamos agora conferir as condições do Delta, digite qualquer tecla para continuar:"))
        print("-" * 35)
        if (delta > 0) or ((a < 0 or c < 0) and ((b) ** 2 > 4 * a * c)):
            print("Uhmm o delta é", delta, " e por ser maior que zero, teremos duas raízes")
            interacao3 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            x1 = float
            x2 = float
            x1 = (-b + (delta) ** (1 / 2)) / 2 * a
            x2 = (-b - (delta) ** (1 / 2)) / 2 * a

            interacao4 = str(input("""Já temos as duas raízes com valores distintos
            digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da primeira raiz é ", x1, "e da segunda raiz é ", x2)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)
        if (delta == 0) or ((b == 0 and (a == 0 or c == 0))) or ((b) ** 2 == 4 * a * c):
            print("Uhmm o delta é 0, por isso teremos uma única raiz")
            interacao5 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            xO = float
            x0 = (-b + (delta)**(1/2))/2*a

            interacao6 = str(input("""Já temos a  raíz única digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da raiz única é:", x0)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)

        if (delta < 0) or ((a > 0 and c > 0) and ((b) ** 2) < 4 * a * c) or((a < 0 and c < 0) and ((b) ** 2) < 4*a*c):
            print("o delta é ", delta, " por ser negativo as raízes são inexistentes, não tem :/ ")
            continuar_usando = input("""Quer continuar usando e encontra um delta positivo ? 
            Digite "Sim" caso queira continuar:""")
            print("-" * 35)

    if Menu == 5:
        delta = float
        a = float(1)
        b = float(-1)
        c = float(-12)

        print("Neste exemlo o valor de a é:", a)
        print("Neste exemlo o valor de b é:", b)
        print("Neste exemlo o valor de c é:", c)

        interacao7 = str(input("Vamos começar calculando o delta, digite qualquer tecla para continuar: "))

        delta = ((b) ** 2) - (4 * a * c)

        interacao2 = str(input("Vamos agora conferir as condições do Delta, digite qualquer tecla para continuar:"))
        print("-" * 35)
        if (delta > 0) or ((a < 0 or c < 0) and ((b) ** 2 > 4 * a * c)):
            print("Uhmm o delta é", delta, " e por ser maior que zero, teremos duas raízes")
            interacao3 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            x1 = float
            x2 = float
            x1 = (-b + (delta) ** (1 / 2)) / 2 * a
            x2 = (-b - (delta) ** (1 / 2)) / 2 * a

            interacao4 = str(input("""Já temos as duas raízes com valores distintos
            digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da primeira raiz é ", x1, "e da segunda raiz é ", x2)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)
        if (delta == 0) or ((b == 0 and (a == 0 or c == 0))) or ((b) ** 2 == 4 * a * c):
            print("Uhmm o delta é 0, por isso teremos uma única raiz")
            interacao5 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            xO = float
            x0 = (-b + (delta)**(1/2))/2*a

            interacao6 = str(input("""Já temos a  raíz única digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da raiz única é:", x0)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)

        if (delta < 0) or ((a > 0 and c > 0) and ((b) ** 2) < 4 * a * c) or((a < 0 and c < 0) and ((b) ** 2) < 4*a*c):
            print("o delta é ", delta, " por ser negativo as raízes são inexistentes, não tem :/ ")
            continuar_usando = input("""Quer continuar usando e encontra um delta positivo ? 
            Digite "Sim" caso queira continuar:""")
            print("-" * 35)

    if Menu == 6:
        delta = float
        a = float(1)
        b = float(-6)
        c = float(10)

        print("Neste exemlo o valor de a é:", a)
        print("Neste exemlo o valor de b é:", b)
        print("Neste exemlo o valor de c é:", c)

        interacao7 = str(input("Vamos começar calculando o delta, digite qualquer tecla para continuar: "))

        delta = ((b) ** 2) - (4 * a * c)

        interacao2 = str(input("Vamos agora conferir as condições do Delta, digite qualquer tecla para continuar:"))
        print("-" * 35)
        if (delta > 0) or ((a < 0 or c < 0) and ((b) ** 2 > 4 * a * c)):
            print("Uhmm o delta é", delta, " e por ser maior que zero, teremos duas raízes")
            interacao3 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            x1 = float
            x2 = float
            x1 = (-b + (delta) ** (1 / 2)) / 2 * a
            x2 = (-b - (delta) ** (1 / 2)) / 2 * a

            interacao4 = str(input("""Já temos as duas raízes com valores distintos
            digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da primeira raiz é ", x1, "e da segunda raiz é ", x2)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)
        if (delta == 0) or ((b == 0 and (a == 0 or c == 0))) or ((b) ** 2 == 4 * a * c):
            print("Uhmm o delta é 0, por isso teremos uma única raiz")
            interacao5 = input("digite qualquer tecla para continuar:")
            print("-" * 35)

            xO = float
            x0 = (-b + (delta)**(1/2))/2*a

            interacao6 = str(input("""Já temos a  raíz única digite qualquer tecla para conferir:"""))
            print("-" * 35)

            print("O valor da raiz única é:", x0)
            print("-" * 35)
            continuar_usando = input("""Quer continuar usando ? Digite "Sim" caso queira continuar:""")
            print("-" * 35)

        if (delta < 0) or ((a > 0 and c > 0) and ((b) ** 2) < 4 * a * c) or((a < 0 and c < 0) and ((b) ** 2) < 4*a*c):
            print("o delta é ", delta, " por ser negativo as raízes são inexistentes, não tem :/ ")
            continuar_usando = input("""Quer continuar usando e encontra um delta positivo ? 
            Digite "Sim" caso queira continuar:""")
            print("-" * 35)