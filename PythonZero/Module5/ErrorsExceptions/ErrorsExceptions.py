open("C:\\Users\\levig\\Desktop\\Programação\\Mentorama\\Python\\PythonZero\\Module5\\Módulos\\MeusPacotes", 'r')

amount = 1000

try:
    installments = int(input("Number of installments: "))
    installmentValue = amount / installments
    print("Alright! In this case, the value of each installment is:", round(installmentValue, 2))
except ZeroDivisionError:
    print("Please enter a number other than 0.")
except ValueError:
    print("You can only input numbers here!")

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Oops! It's not a valid number. Please try again...")
