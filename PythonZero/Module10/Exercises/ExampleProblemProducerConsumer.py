import threading
import time

buffer = []  # Shared area between producer and consumer
MAX_SIZE = 5  # Maximum buffer size
empty = threading.Semaphore(MAX_SIZE)  # Controls empty spaces in the buffer
full = threading.Semaphore(0)  # Controls occupied spaces in the buffer
mutex = threading.Lock()  # Ensures exclusive access to the buffer

def producer():
    while True:
        item = produceItem()  # Generate a new item
        empty.acquire()  # Wait for an empty space in the buffer
        mutex.acquire()  # Get mutual exclusion to access the buffer
        buffer.append(item)  # Insert the item into the buffer
        mutex.release()
        full.release()  # Signal that the buffer has an available item
        time.sleep(1)  # Simulate production

def consumer():
    while True:
        full.acquire()  # Wait for an item in the buffer
        mutex.acquire()  # Get mutual exclusion to access the buffer
        item = buffer.pop(0)  # Remove the item from the buffer
        mutex.release()
        empty.release()  # Signal that there's an empty space available
        processItem(item)  # Process the item
        time.sleep(2)  # Simulate consumption

# Thread initialization
producerThread = threading.Thread(target=producer)
consumerThread = threading.Thread(target=consumer)

# Start the threads
producerThread.start()
consumerThread.start()