
import datetime

currentDateTime = datetime.datetime.now()
onlyTime = currentDateTime.time()
print(onlyTime)

# QUESTION 4

modifiedHour = datetime.time(hour=int(onlyTime.hour - 3),
                             minute=onlyTime.minute,
                             second=onlyTime.second)

print(modifiedHour)
