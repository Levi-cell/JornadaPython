# Example 1: Filling an Empty List, Interacting with the User
# Empty lists can be filled using a loop structure with the append method

numberList1 = []
quantityOfNumbers = int(input("Enter how many numbers you want to add: "))

for i in range(quantityOfNumbers):
    x = float(input("Enter the value of the %dº number: " % (i+1)))
    i += 1
    numberList1.append(x)

numberList1.sort()

print(numberList1)
print("-" * 35)

# Example 2: Without Using the Sort Function

numbers = []

quantity = int(input("Enter how many numbers you want to add to the list: "))

for i in range(quantity):
    number = float(input("Enter a number: "))
    numbers.append(number)

# Manually sort the numbers

for i in range(quantity):

    for j in range(i + 1, quantity):

        if numbers[i] > numbers[j]:

            numbers[i], numbers[j] = numbers[j], numbers[i]

print("The list in ascending order is:", numbers)