# In this file, I will perform the simpler tasks

# Make a program that prints your full name on the screen
print("Levi Oliveira Pereira")

# Write a program that displays the result of 5a x 3b on a=2 and b=5
a = 2
b = 5
print((5 * a) * (3 * b))

# Adding c
c = 5
print(a + b + c)

print("""#####################################################################
################################################################################
################################################################################
#############################################################################""")

# Calculating addition, division, multiplication, and subtraction of two numbers

print("Welcome to the calculator for 4 operations of two numbers")

anotherOperation = str  # It's not mandatory to define the variable type

anotherOperation = "Yes"
# You must define the value of the variable here, as the program will stop if something else is entered.

while anotherOperation == "Yes":

    print("""We have these operations available:
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division""")
    choice = input("Which one would you like to perform? (Enter its respective number):")
    print("-" * 35, "\n")

    if choice == "1":
        x = float(input("Enter the first number for addition: "))
        y = float(input("Enter the second number for addition: "))
        result = x + y
        print("The result of adding ", x, " and ", y, " is " + str(result))
        # Using a comma also allows you to concatenate strings with integers in prints
        print("-" * 35, "\n")
        anotherOperation = input("""Type "Yes" if you want to perform another operation: """)
        print("-" * 35, "\n")

    elif choice == "2":
        x = float(input("Enter the first number for subtraction: "))
        y = float(input("Enter the second number for subtraction: "))
        result = x - y
        print("The result of subtracting ", x, " and ", y, " is " + str(result))
        print("-" * 35, "\n")
        anotherOperation = input("""Type "Yes" if you want to perform another operation: """)
        print("-" * 35, "\n")

    elif choice == "3":
        x = float(input("Enter the first number for multiplication: "))
        y = float(input("Enter the second number for multiplication: "))
        result = x * y
        print("The result of multiplying ", x, " and ", y, " is " + str(result))
        print("-" * 35, "\n")
        anotherOperation = input("""Type "Yes" if you want to perform another operation: """)
        print("-" * 35, "\n")

    elif choice == "4":
        x = float(input("Enter the first number for division: "))
        y = float(input("Enter the second number for division: "))
        while y == 0:
            y = float(input("The second number for division cannot be 0, enter another number:"))
        result = x / y
        print("The result of dividing ", x, " by ", y, " is " + str(result))
        print("-" * 35, "\n")
        anotherOperation = input("""Type "Yes" if you want to perform another operation: """)
        print("-" * 35, "\n")