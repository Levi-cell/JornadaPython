anonima = lambda a, b, c: a + b + c
print(anonima(2, 5, 3))

anonima2 = lambda a, b: a + b if a > b else a - b

print(anonima2(4, 2))

print(anonima2(1, 2))