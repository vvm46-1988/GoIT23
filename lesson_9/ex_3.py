# Створення Decimal із дійсних чисел

from decimal import Decimal
num1 = 1.37
num2 = 1.5
first = Decimal.from_float(num1)
second = Decimal.from_float(num2)
print(first, second)
first = Decimal(str(1.45))
second = Decimal(str(1.5))
print(first, second)
