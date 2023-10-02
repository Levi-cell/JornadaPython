from time import perf_counter
import time

started = perf_counter()

i = 0
while i <= 5:
    print("Hello world")
    time.sleep(3)

    i += 1

finished = perf_counter()

print("Elapsed time in seconds during program execution:", finished - started)

# Great job, I only started to understand by doing it.
