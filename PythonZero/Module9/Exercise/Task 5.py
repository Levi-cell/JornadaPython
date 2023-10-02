from datetime import *
from time import *

# a)
print("a)")

today = datetime.today()
print(today)

print(" ")

# b)
print("b)")

print(today.year)

print(" ")

# c)
print("c)")

print(today.month)

print(" ")

# d)
print("d)")

today = datetime.today()
year, week, day = today.isocalendar()

print(f"Week {week} of the year")

print(" ")

# e)
print("e)")

print(f"Today is the {day}th day of the week")

print(" ")

# f)
print("f)")

currentDate = datetime.now()

dayOfYear = currentDate.timetuple().tm_yday
print(f"Day of the year: {dayOfYear}")
print(" ")

# g)
print("g)")

print(f"Day of the month: {currentDate.timetuple().tm_mday}")

print(" ")

# h)
print("h)")

print(f"Weekday: {currentDate.timetuple().tm_wday}")

print(" ")
