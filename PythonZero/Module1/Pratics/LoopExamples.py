# Using for loop for string list
print("example1:")
fruits = ["Banana", "apple", "orange", "starfruit"]

for x in fruits:
    print(x)

print(" ")
print("example2:")

for x in "starfruit":
    print(x)

# Using for loop for integers
print(" ")
print("example3:")

for x in range(5):
    print(x)

# Using while loop with a counter
print(" ")
print("example4:")

i = 0
while i < 5:
    print(i)
    i += 1

# Using for loop with a counter
print(" ")
print("example5:")

counter = 0
for element in range(0, 10):  # 10 positions, not from 0 to 10
    print(counter)
    counter = counter + 2

# Using while loop with a counter
print(" ")
print("example6:")

counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 2

# Using while loop with an accumulator
print(" ")
print("example7:")

n = 1
totalSum = 0
while n <= 10:
    x = int(input("Enter the %dº number:" % n))
    totalSum = totalSum + x
    n = n + 1
print("Sum: %d" % totalSum)

# Using break
print(" ")
print("example8:")

counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1
    break  # The break only allows 1 loop, repetition stops after the first time.

# Using break
# The continue command interrupts the execution of the command immediately below
# the block, not executing it
print(" ")
print("example9:")
n = 1
totalSum = 0
while n <= 10:
    x = int(input("Enter the %dº number:" % n))
    totalSum = totalSum + x
    n = n + 1
    break
print("Sum: %d" % totalSum)

# Using for loop with continue
print(" ")
print("example10:")

for val in "string":
    if val == "i":
        continue  # The loop will not be executed when val is equal to "i"
    print(val)
print("The end")