import time

def increase(number, limit, interval):
    print(number)
    time.sleep(interval)
    number += 1

    if number <= limit:
        increase(number, limit, interval)
        if number == limit:
            print("Fire!!")

increase(1, 100, 0.05)