file = open("teste.txt", 'w+')
file.write("Linha1\n") # write
file.write("Linha2\n")
file.write("Linha3\n")
file.close()

file = open("teste.txt", 'r')
print(file.read())
file.close()