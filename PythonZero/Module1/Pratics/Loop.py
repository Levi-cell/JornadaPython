# Repetition with while
print("exampleWithWhile:")

i = 0
while i < 5:
    print(i)
    i += 1

# Repetition with for
print("exampleWithFor:")

for x in range(5):  # range means 5 positions
    print(x)

# Example of a counter
print("exampleOfCounterWithWhile")

counter = 1
while counter <= 5:
    print(counter)
    counter = counter + 1

print("exampleOfCounterWithFor")

counter = 0
for element in range(0, 10):
    print(counter)
    counter = counter + 1

# In a counter, the increment is constant, one by one
# In an accumulator, the increment is variable and usually has a condition

# Example of accumulators
print("exampleOfAccumulatorsWithCondition:")

totalSum = 0
while True:
    value = int(input("Enter a number to add or 0 to exit:"))
    if value == 0:
        break
    totalSum = totalSum + value
    print(totalSum)

# Example of accumulator with continue
print("exampleOfAccumulatorsWithContinue")

for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")