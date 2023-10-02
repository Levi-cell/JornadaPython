from datetime import datetime

dayNames = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

today = datetime.now()

# Printing in the example format

day = today.day
dayName = dayNames[today.weekday()]
month = monthNames[today.month - 1]
year = today.year

print(f"{dayName}, {month} {day}, {year}")