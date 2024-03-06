from datetime import datetime

t = '05.03.2024'

d = datetime.strptime(t, '%d.%m.%Y')
print(d.date())
print(d.day, d.month, d.year)
print(type(d))


other = d.replace(month=4, day=1, hour=14, minute=55)
print(other)
a = other.strftime('%Y/%m/%d')
print(a)
