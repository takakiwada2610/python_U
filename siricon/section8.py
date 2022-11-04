import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y'))

today = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(today)

print(now)
# d =datetime.timedelta(weeks=1)
d =datetime.timedelta(days=365)

print(now - d)

import time
# print('###')
# time.sleep(2)
# print('###')

print(time.time())
