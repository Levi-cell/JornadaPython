# ESTRUTURA DO DICT COMPREHENSION

letras = {k + 1: v for k, v in enumerate("avsakclkjerigbaweeopapoxciv")}
for posicao, letras in letras.items():
    print(f"{posicao}:{letras}")
# pode fazer k + 1 para não usar o 0, caso queira usar o 0 só usar k:
print("-----------------------")

letras = {k + 1: v for k, v in enumerate("avsakclkjerigbaweeopapoxciv") if v not in ("a", "e", "i", "o", "u")}

for posicao, letras in letras.items():
    print(f"{posicao}:{letras}")

# perceba que ele pula as posições