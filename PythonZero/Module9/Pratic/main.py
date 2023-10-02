import time

# Help
help(time.localtime())

# Defining an epoch
print(time.gmtime(0))

# Time in seconds as a floating-point number
seconds = time.time()
print("Seconds since the epoch:", seconds)

# Time in seconds as a string representing the local time
localTime = time.ctime(seconds)
print("Local time:", localTime)

print("Local time:", time.asctime())

print(time.localtime())

timeStruct = time.localtime()
print(timeStruct[0])

print(time.strftime("%Y-%m-%d-%H.%M.%S"), time.localtime())

print("This is printed immediately")
time.sleep(5)  # Delay execution
print("This is printed after 5 seconds")

# We can create a timer to execute the statement at a scheduled time
startExec = time.time()

def hello():
    time.sleep(5)
    print("Hello, world!")

hello()
endExec = time.time()
print("Total execution time:", endExec - startExec)