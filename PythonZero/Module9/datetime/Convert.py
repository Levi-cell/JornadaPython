# Converte String no formato data e tempo

from datetime import datetime
from datetime import timedelta

text = '2021-02-08'

y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()

diff = z - y
print(diff)