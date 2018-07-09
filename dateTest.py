import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str, tz_str):
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    if list(tz_str)[3] == '+':
        ztime = 8 - int(re.match(r'^UTC(\+|-)(1[0-2]|[0-9]|0[0-9])\:00$',tz_str).group(2))
    else:
        ztime = 8 + int(re.match(r'^UTC(\+|-)(1[0-2]|[0-9]|0[0-9])\:00$', tz_str).group(2))
    date = date + timedelta(hours=ztime)
    print(date.timestamp())

to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')