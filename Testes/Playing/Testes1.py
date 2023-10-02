#enumarate

produtos = [
    "iphone",
    "ipad",
    "airpod",
    "macbook"
]
print(" ")
for item in produtos:
    print(item)

print(" ")
for i in range(len(produtos)):
    print(i,produtos[i])

print(" ")
i = 0
for item in produtos:
    print(i, item)
    i += 1
print(" ")
print("Usando enumarete")
print(" ")
for i, item in enumerate(produtos):
    print(i,item)