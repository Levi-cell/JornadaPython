# Handling file not found exception

try:
    file = open('texte1.txt', 'r')
except FileNotFoundError:
    print("File not found")
except:
    print("An error occurred")

print("////////////////////")
print(" ")

# Handling NameError exceptions
var1 = 10
try:
    print(var1)
except NameError:
    print("Name not defined!")
else:
    print("Try again!")
finally:  # will always be executed regardless of the exception
    print("Program finished!")

# A more complex example using the Math library

import math

number_list = [10, -5, 1.2, 'apple']

for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("Factorial is not supported for the given input type.")
    except ValueError:
        print("Factorial accepts only positive integer values, and", number, " is not a positive integer.")
    else:
        print("The factorial of ", number, "is", number_factorial)
    finally:
        print("Release all resources in use.")