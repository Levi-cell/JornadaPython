import random
import time

startTime = time.time()
for x in range(1000):
    numbers = random.randint(1, 1000)
endTime = time.time()

print(f"Execution time: {endTime - startTime}")