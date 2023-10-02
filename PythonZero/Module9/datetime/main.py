import datetime

aDate = datetime.date(2021, 2, 8)
print(aDate.year)

print(datetime.datetime(2021, 1, 2, 4, 20, 34, 565))

today = datetime.date.today()

# Printing dates

print(today.day)
print(today.weekday())  # Monday = 0, Sunday = 6
print(today.isoweekday())  # Monday = 1, Sunday = 7

# Assigning current date and time to the object y
y = datetime.datetime.now()

# Oops... printing the year, month, and day

print(y.year)
print(y.month)
print(y.day)

# Defining the step size in days
dayDelta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 5 * dayDelta

for i in range((end_date - start_date).days):
    print(start_date + i * dayDelta)

# Calculating the difference between days

diff1 = datetime.timedelta(days=25)
diff2 = datetime.timedelta(days=15)

diff3 = diff1 - diff2
print(diff3)
print(type(diff3))
