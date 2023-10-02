velocidade_km = int(input("Qual sua velocidade em km  por hora?"))

if velocidade_km > 80:
    multa = (velocidade_km - 80)*5
    print("Você foi multado no valor de %d reais" % multa)
else:
    print("Parabéns você está respeitando a lei")