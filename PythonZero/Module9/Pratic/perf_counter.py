from time import perf_counter

print("Enter two integer values")

n, m = map(int, input().split())

t1Start = perf_counter()

for i in range(n):
    print("Enter an integer value")
    t = int(input())  # User enters input n times
    if t % m == 0:
        print(t)

# Stop the stopwatch / counter

t1Stop = perf_counter()

print("Elapsed time", t1Stop, t1Start)
print("Elapsed time throughout the program, in seconds", t1Stop - t1Start)