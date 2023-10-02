import time
import threading

start = time.time()

def process():
    print("Process 1")

t1 = threading.Thread(target=process, args=())

# a
t1.start()
t1.join()  # Wait for the thread to finish

end = time.time()

print(f"Duration: {end - start}")

# b
print(f"Is the thread active? {t1.is_alive()}" + "\n")

# c
print(threading.enumerate())
print(f"Active thread: {threading.current_thread().name}" + "\n")  # Another way

# d
print(f"Thread identification number: {threading.get_ident()}" + "\n")  # Shows the current thread's identifier

# e
print(f"Number of active threads: {threading.active_count()}" + "\n")  # Number of active threads

# f
print(f"List of active threads: {threading.enumerate()}" + "\n")  # More convenient