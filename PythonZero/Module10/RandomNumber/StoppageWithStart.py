
import random
import time
from threading import Thread

def generateRandomNumbers(quantity):
    totalSum = 0
    for x in range(quantity):
        number = random.randint(1, 5000000)
        totalSum += number
    print(f"Sum: {totalSum}")

startTime = time.time()

t1 = Thread(target=generateRandomNumbers, args=[5000000])  # args refers to the quantity
# Another way to declare t1:
# t1 = Thread(target=generateRandomNumbers(1000000))

t1.start()
endTime = time.time()

print(f"Execution time: {endTime - startTime}")
print(t1.is_alive())