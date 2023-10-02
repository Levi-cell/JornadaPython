import time
import threading

def process1():
    print("Process 1")
    time.sleep(5)

def process2():
    print("Process 2")
    time.sleep(30)

start = time.time()

if __name__ == "__main__":
    thread1 = threading.Thread(target=process1)
    thread2 = threading.Thread(target=process2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(thread1.is_alive())
    print(thread2.is_alive())

    end = time.time()
    print(f"Duration: {end - start}")

