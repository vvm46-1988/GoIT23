
try:
    a = '56'
    c = 45
    print(a + c)  # TypeError
except (TypeError, ValueError) as e:
    print(f'Вибачте сталась помилка: {e}')