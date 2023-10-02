class contador:  # criando uma classe iterator
    def __iter__(self):
        self.var = 0

        return self

    def __next__(self):
        self.var += 1

        if self.var > 10:
            raise StopIteration

        return self.var

# Primeira forma de se utilizar:

count = contador()
gerarNumeros = iter(count)  # Iterator
x = next(count)
print(x)
x = next(count)
print(x)
print("---------------------------")
# Segunda forma de se utilizar

count1 = contador()
gerarNumeros1 = iter(count1)

for x in range(1, 11):
    d = next((count1))
    print(d)
print("---------------------------")
# Terceira forma de se utilizar

count2 = contador()
gerarNumeros2 = iter(count2)

for c in gerarNumeros2:
    print(c)  # Iterable

