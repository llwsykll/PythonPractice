from datetime import datetime,timedelta,timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2018,7,6,16,48)
print(dt)
print(dt.timestamp())

t = 1530866880.0
print(datetime.fromtimestamp(t))

cday = datetime.strptime('2018-7-9 13:58:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%a, %b %d %H:%M'))

print(now+timedelta(hours=10))

print(now+timedelta(days=10))

print(now+timedelta(days=10,hours=10))

tz_utc_8 = timezone(timedelta(hours=8))

dtNew = now.replace(tzinfo=tz_utc_8)

print(dtNew)


utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_bt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_bt)
tokyo_bt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_bt)