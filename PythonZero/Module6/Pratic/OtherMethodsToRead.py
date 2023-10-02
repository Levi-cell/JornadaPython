file = open('teste.txt', 'r')
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
file.close()
##other method
file = open('teste.txt', 'r')
print(file.readlines())
file.close()