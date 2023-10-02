class sequenciaFibonacci:
    def __init__(self, qtdTermos):
        self.primeiro = 0
        self.segundo = 1
        self.qtdTermos = qtdTermos

    def __iter__(self):
        return self

    def __next__(self):
        if self.qtdTermos == 0:
            raise StopIteration
        else:
            resultado = self.primeiro + self.segundo
            self.primeiro = self.segundo
            self.segundo = resultado
            self.qtdTermos -= 1
            return self.segundo

def geraFibonnaci(termos):
    sequencia = sequenciaFibonacci(termos)
    return {pos: val for pos, val in enumerate(sequencia, start= 1)}

termos = int(input("Quantos termos deseja usar na sua sequência fibonacci:"))
dicionarioFibonacci = geraFibonnaci(termos)

for pos, val in dicionarioFibonacci.items():
    print(f"{pos}º termo: {val}")

if __name__ == "__main__":
    # teste de mesa pro pytest
    sequencia = 10
    sequenciaFibonacci(sequencia)  # não precisa
    print(sequencia)
    gerador = geraFibonnaci(sequencia)
    print(len(gerador))