from threading import Thread

# Does something
def task1():
    for x in range(1, 11):
        print("Process 1 - Task", x)
        x += 1

# Does something
def task2():
    for x in range(1, 11):
        print("Process 2 - Task", x)
        x += 1

thread1 = Thread(target=task1).start()
thread2 = Thread(target=task2).start()