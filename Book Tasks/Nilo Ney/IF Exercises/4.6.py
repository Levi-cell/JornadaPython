distancia = float(input("Qual distancia deseja percorrer em KM?"))

if distancia <= 200:
    preco = distancia*0.50
    print(f" O preço da passagem é {preco}")
else:
    preco = distancia*0.45
    print(f"O preço da passagem é {preco}")
