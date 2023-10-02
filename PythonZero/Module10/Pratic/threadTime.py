from threading import Thread
import threading
import time

def process1():
    for x in range(1, 11):
        print("Process 1 - Task", x)
        time.sleep(2)
        x += 1

def process2():
    for x in range(1, 11):
        print("Process 2 - Task", x)
        time.sleep(1)
        x += 1

thread1 = Thread(target=process1).start()
thread2 = Thread(target=process2).start()

print(threading.enumerate())
print(threading.current_thread())
print(threading.active_count())
print(threading.get_ident())
