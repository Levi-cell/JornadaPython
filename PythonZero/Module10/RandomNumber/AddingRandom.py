import random
import time

totalSum = 0

startTime = time.time()
for x in range(1000000):
    randomNumber = random.randint(1, 1000)
    print(randomNumber)
    totalSum += randomNumber
endTime = time.time()

print(totalSum)
print(f"Execution time: {endTime - startTime}")