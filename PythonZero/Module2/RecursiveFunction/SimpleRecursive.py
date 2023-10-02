# Função recursiva
def decrease(number):
    print(number)
    number -= 1

    if number >= 1:
        decrease(number)

input_number = int(input("Enter a number: "))
decrease(input_number)