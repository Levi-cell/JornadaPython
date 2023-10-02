def gerador():
    yield 10 ** 10
    yield 10 ** 2
    yield 10 ** 3


for g in gerador():
    print(g)