from datetime import datetime, timedelta

now = datetime.now()

dayBeforeYesterday = now - timedelta(days=2)

dayAfterTomorrow = now + timedelta(days=2)

difference = dayAfterTomorrow - dayBeforeYesterday

print(difference)