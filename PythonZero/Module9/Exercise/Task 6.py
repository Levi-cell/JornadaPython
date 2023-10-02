from datetime import datetime

text = '2021-01-01-13-53'

converted = datetime.strptime(text, '%Y-%m-%d-%H-%M')

print(converted)