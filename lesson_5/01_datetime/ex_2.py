from datetime import timedelta, datetime
delta = timedelta(
    days=10,
    seconds=27,
    minutes=5,
    hours=8,
    weeks=2
)
now = datetime.now()

result = now + delta
print(result)