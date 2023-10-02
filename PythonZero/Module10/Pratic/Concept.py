import time
import threading

def printCube(num):
    """Function to print the cube of a given number"""

    time.sleep(5)
    print(f"Cube: {num * num * num}")

def printSquare(num):
    """Function to print the square of a given number"""
    time.sleep(10)
    print(f"Square: {num * num}")


# Creating threads
if __name__ == "__main__":  # This IF statement is optional
    thread1 = threading.Thread(target=printSquare, args=(10,))
    thread2 = threading.Thread(target=printCube, args=(10,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Done!")