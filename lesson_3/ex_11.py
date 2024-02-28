# Напишіть програму яка по введеному значенню буде повертати день тижня
days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
while True:
    i = input('Enter a day, "q" for exit: ')
    try:
        value = int(i)
        print(days.get(value, 'Такого дня немає'))
    except ValueError:
        if i == 'q':
            break
        print('Потрібно ввести число')
