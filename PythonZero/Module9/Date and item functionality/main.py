import datetime
import time

# Creating an object named date, representing the date 01/29/2012
exampleDate = datetime.date(year=2012, month=1, day=29)

print(exampleDate)

print(exampleDate.day)

day = exampleDate.day
month = exampleDate.month
year = exampleDate.year

print(f"{day}/{month}/{year}")

today = datetime.date.today()

print(today)

exampleTime = datetime.time(hour=12, minute=55, second=1)
print(exampleTime)

hour = exampleTime.hour
minute = exampleTime.minute
second = exampleTime.second

print(f"hour: {hour}")
print(f"minute: {minute}")
print(f"second: {second}")

now = datetime.datetime.now()

print(now)
print(now.date())