# Значення за замовчуванням
def seconds(seconds=0, minutes=0, hours=0, days=0):
    number_seconds_in_minutes = 60
    number_seconds_in_hours = 60 * number_seconds_in_minutes
    number_seconds_in_days = 24 * number_seconds_in_hours

    return seconds + minutes * number_seconds_in_minutes + \
        hours * number_seconds_in_hours + \
        days * number_seconds_in_days


print(seconds(minutes=5, days=1, seconds=6))