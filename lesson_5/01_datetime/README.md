Клас `datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)` - комбінація дати та часу.


Обов'язкові аргументи:
`datetime.MINYEAR (1) ≤ year ≤ datetime.MAXYEAR (9999)`
`1 ≤ month ≤ 12`
`1 ≤ day ≤ кількість днів у цьому місяці та році`


Необов'язкові:
`0 ≤ minute < 60 0 ≤ second < 60 0 ≤ microsecond < 1000000`


## Методи класу datetime:
`datetime.today()` - об'єкт datetime з поточної дати та часу. Працює як і datetime.now() зі значенням tz=None.

`datetime.fromtimestamp(timestamp)` - дата із стандартного уявлення часу.

`datetime.fromordinal(ordinal)` - дата з числа, що становить кількість днів, що пройшли з 01.01.1970.

`datetime.now(tz=None)` - об'єкт datetime з поточної дати та часу.

`datetime.combine(date, time)` - об'єкт datetime з комбінації об'єктів date та time.

`datetime.strptime(date_string, format)` - перетворює рядок на datetime (так само, як і функція strptime з модуля time).

`datetime.strftime(format)` - див. функцію strftime із модуля time.

`datetime.date()` - об'єкт дати (з відсіканням часу).

`datetime.time()` - об'єкт часу (з відсіканням дати).

`datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]]]])` - повертає новий об'єкт datetime зі зміненими атрибутами.

`datetime.timetuple()` - повертає struct_time із datetime.

`datetime.toordinal()` - кількість днів, що пройшли з 01.01.0000.

`datetime.timestamp()` - повертає час у секундах з початку епохи.

`datetime.weekday()` - день тижня у вигляді числа, понеділок - 0, неділя - 6.

`datetime.isoweekday()` - день тижня у вигляді числа, понеділок - 1, неділя - 7.

`datetime.isocalendar()` - кортеж (рік у форматі ISO, ISO номер тижня, ISO день тижня).

`datetime.isoformat(sep='T')` - гарний рядок виду "YYYY-MM-DDTHH:MM:SS.mmmmmm" або, якщо microsecond == 0, "YYYY-MM-DDTHH:MM:SS"

`datetime.ctime([сек])` - перетворює час, виражений у секундах з початку епохи в рядок вигляду "Thu Sep 27 16:42:37 2012".
