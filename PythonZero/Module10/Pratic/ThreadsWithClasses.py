import threading
from threading import Thread
import time

class MyThread:
    def showNumbers(self):
        i = 0
        print(threading.current_thread().getName())
        time.sleep(1)
        while i < 10:
            print(i)
            i += 1

obj = MyThread()

thread1 = Thread(target=obj.showNumbers)
thread1.start()

thread2 = Thread(target=obj.showNumbers)
thread2.start()

thread3 = Thread(target=obj.showNumbers)
thread3.start()