from datetime import datetime, timedelta

# This approach was proposed by ChatGPT
# Define start and end dates
startDate = datetime(1987, 10, 16)
endDate = datetime(1987, 10, 25)

# Calculate the total number of days in the range
numDays = (endDate - startDate).days + 1

# Create a list to store the dates
dateList = [startDate + timedelta(days=day) for day in range(numDays)]

# Print the dates from the list
for date in dateList:
    print(date.strftime("%d/%m/%Y"))

# A simpler and more readable approach:

start = datetime(1987, 10, 16)
end = datetime(1987, 10, 25)

oneDayStep = timedelta(days=1)
dateList = []

currentDate = start
while currentDate <= end:
    dateList.append(currentDate)
    currentDate += oneDayStep

for date in dateList:
    print(date.strftime("%d/%m/%Y"))