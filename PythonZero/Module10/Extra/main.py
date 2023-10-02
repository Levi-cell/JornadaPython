import time
from threading import Thread

# Both functions do the same thing, the difference is in the logic
def sumNumbers1(a, b):  # Here we use range and sum
    numbers = range(a, b + 1)
    print(sum(numbers))

def sumNumbers2(a, b):  # Here we use a for loop
    totalSum = 0
    for number in range(a, b + 1):
        totalSum += number
    print(totalSum)

start = time.time()
sumNumbers1(1, 5000000)
sumNumbers2(1, 5000000)
end = time.time()

print(f"Execution time = {end - start}")