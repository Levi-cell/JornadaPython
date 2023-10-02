import time
from datetime import datetime

# a)
print("a)")
text = '2021-02-08'

parsedDate = datetime.strptime(text, '%Y-%m-%d')
print(parsedDate)
print(" ")

# b)
print("b)")
print(time.gmtime(40))
seconds = time.time()
print("Seconds since epoch:", seconds)
print("  ")

# c)
print("c)")
print(datetime.now())
print("  ")

# d)
print("d)")
localTimeObj = time.localtime()
print(time.strftime("%H.%M.%S"))
print("  ")

# e)
import time
print("e)")
# Get information about the local time
currentHour = time.localtime()

# Check if Daylight Saving Time is active
if currentHour.tm_isdst > 0:
    print(time.strftime("%Y-%m-%d, %H hours %M minutes and %S seconds"))
    print("We are in Daylight Saving Time.")

else:
    print(time.strftime("%Y-%m-%d, %H hours %M minutes and %S seconds"))
    print("We are not in Daylight Saving Time.")
print("  ")






