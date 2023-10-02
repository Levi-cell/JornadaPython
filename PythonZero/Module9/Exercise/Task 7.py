from datetime import datetime, timedelta

text = '2021-01-25'

converted = datetime.strptime(text, '%Y-%m-%d')
converted -= timedelta(days=8)
print(converted)