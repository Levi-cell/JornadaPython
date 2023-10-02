# 1 to 10 with WHILE
print("---------------")
print("Using while from 1 to 10")
print("---------------")

i = 0
while i <= 10:
    print(i)
    i += 1

# 1 to 10 with FOR
print("---------------")
print("Using for from 1 to 10")
print("---------------")

for x in range(0, 11):
    print(x)
    x = x + 1

# Write a program to count how many even and odd numbers exist between
# 1 and 10, as well as their sum using while
print("---------------")
print("Even and odd using while")
print("---------------")

b = 0
evenNumbers = []
oddNumbers = []
while b <= 10:

    if b % 2 == 0:
        evenNumbers.append(b)
        print(b, "is even")
    else:
        oddNumbers.append(b)
        print(b, "is odd")

    b = b + 1

print("Hence:")
print('Quantity of even numbers = ', len(evenNumbers))
print('Quantity of odd numbers = ', len(oddNumbers))
print('Sum of even numbers = ', sum(evenNumbers))
print('Sum of odd numbers = ', sum(oddNumbers))
print("---------------")

# Using for now
print("Even and Odd using for")
print("---------------")

b = 0
evenNumbers = []
oddNumbers = []
for b in range(0, 11):

    if b % 2 == 0:
        print(b, "is even")
        evenNumbers.append(b)
    else:
        print(b, "is odd")
        oddNumbers.append(b)

    b = b + 1
print("Hence:")
print('Quantity of even numbers = ', len(evenNumbers))
print('Quantity of odd numbers = ', len(oddNumbers))
print('Sum of even numbers = ', sum(evenNumbers))
print('Sum of odd numbers = ', sum(oddNumbers))
print("---------------")

# Professor's method
print("Separating even and odd with user interaction")

quantityOfNumbers = int(input('Enter the quantity of numbers: '))
evenNumbers = []
oddNumbers = []
sumOfEvenNumbers = 0
sumOfOddNumbers = 0

for x in range(quantityOfNumbers):
    number = int(input('Enter a number: '))

    if number % 2 == 0:
        evenNumbers.append(number)
        sumOfEvenNumbers += number
    else:
        oddNumbers.append(number)
        sumOfOddNumbers += number

print(f'Sum of even numbers: {sumOfEvenNumbers}')
print(f'Sum of odd numbers: {sumOfOddNumbers}')

print(f'List of even numbers: {evenNumbers}')
print(f'List of odd numbers: {oddNumbers}')

# Without object-oriented approach
print("Without object-oriented approach")
print("---------------")

numbers = []
quantityOfNumbers = int(input("Enter the quantity of numbers: "))

for i in range(quantityOfNumbers):
    number = int(input(f"Enter the {i+1}th number: "))
    numbers.append(number)

# Variables to count the quantity and sum the even and odd numbers
quantityOfEvenNumbers = 0
quantityOfOddNumbers = 0
sumOfEvenNumbers = 0
sumOfOddNumbers = 0

# Separate even from odd and calculate sums
for number in numbers:
    if number % 2 == 0:
        quantityOfEvenNumbers += 1
        sumOfEvenNumbers += number
    else:
        quantityOfOddNumbers += 1
        sumOfOddNumbers += number

# Print the results
print("\nEven Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

print("\nOdd Numbers:")
for number in numbers:
    if number % 2 != 0:
        print(number)

print("\nQuantity of Even Numbers:", quantityOfEvenNumbers)
print("Quantity of Odd Numbers:", quantityOfOddNumbers)
print("Sum of Even Numbers:", sumOfEvenNumbers)
print("Sum of Odd Numbers:", sumOfOddNumbers)

# Extra code:
# Here I will ask the user to enter a list of integers,
# the program will check whether they are even or odd, and then list the numbers showing which are even and which are odd,
# stating the quantity of each, and the sum of each

print("User interaction using even and odd")
print("---------------")

print('Using object-oriented approach')
print("---------------")

def separateEvenOdd(numbers):
    evenNumbers = []
    oddNumbers = []
    sumOfEvenNumbers = 0
    sumOfOddNumbers = 0

    for number in numbers:
        if number % 2 == 0:
            evenNumbers.append(number)
            sumOfEvenNumbers += number
        else:
            oddNumbers.append(number)
            sumOfOddNumbers += number

    return evenNumbers, oddNumbers, sumOfEvenNumbers, sumOfOddNumbers

# Get the list of numbers from the user
numbers = []
quantityOfNumbers = int(input("Enter the quantity of numbers: "))

for i in range(quantityOfNumbers):
    number = int(input(f"Enter the {i+1}th number: "))
    numbers.append(number)

# Separate even from odd and calculate sums
evenNumbers, oddNumbers, sumOfEvenNumbers, sumOfOddNumbers = separateEvenOdd(numbers)

# Print the results
print("\nEven Numbers:")
for number in evenNumbers:
    print(number)

print("\nOdd Numbers:")
for number in oddNumbers:
    print(number)

print("\nQuantity of Even Numbers:", len(evenNumbers))
print("Quantity of Odd Numbers:", len(oddNumbers))
print("Sum of Even Numbers:", sumOfEvenNumbers)
print("Sum of Odd Numbers:", sumOfOddNumbers)