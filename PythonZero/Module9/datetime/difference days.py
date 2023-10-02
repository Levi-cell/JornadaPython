from datetime import datetime, timedelta

# Calculating the difference between days between a specified date and the current date


now = datetime.now()

then = datetime(2019, 5, 23)
delta = now - then
print(delta)


