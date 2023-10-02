# Defining a function with a string
print("Defining a function with a string")
print("-" * 35)

def hello(myName):
    print('Hello', myName)  # myName is declared as a string

hello('Felipe' + "\n")  # performing the process and defining the value of myName

# Another way
print("Another way")
print("-" * 35)

def hello1(myName1):
    print('Hello', myName1)

myName1 = 'Tiago'
hello1(myName1 + "\n")

# Defining a function that adds two numbers
print("Defining a function that adds two numbers")
print("-" * 35)

def addNumbers(a, b):  # addNumbers function takes two variable arguments
    print(a + b)  # Process

addNumbers(2, 5)
addNumbers(0, 4)
addNumbers(-1, 9)
addNumbers(1.5, 2.8)
print(" ")

# Note that the addNumbers function prints something on the screen because it has a print statement in its process, so it's not necessary to use print

# Defining a function that adds two numbers with the print outside the function
print("Defining a function that adds two numbers with the print outside the function")
print("-" * 35)

def addNumbers1(a, b):
    result = a + b  # result is a variable and not the function
    return result  # return a + b

print(addNumbers1(2, 8))
sumResult = 2 + 5
print(sumResult, "\n")

# Determining if a value is even or not
print("Determining if a value is even or not")
print("-" * 35)

def isEven(x):
    return x % 2 == 0  # return the result of x modulo 2
print(isEven(2))
print(isEven(3))
print(isEven(-2), "\n")

# Reusing the isEven function in another function
print("Reusing the isEven function in another function")
print("-" * 35)

def isEven1(x):
    return x % 2 == 0
def evenOrOdd(x):
    if isEven1(x):
        return "even"
    else:
        return "odd"
print(evenOrOdd(3))
print(evenOrOdd(6))