"""
Необхідність використання. Налаштування точності
"""
from decimal import Decimal, getcontext

f = 0.2 + 0.1 + 0.3 - 0.5
print(f)

dec_f = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(dec_f)
temp = Decimal('1') / Decimal('3')
print(temp)
getcontext().prec = 6
temp = Decimal('1') / Decimal('3')
print(temp)
temp = Decimal('11') / Decimal('3')
print(temp)
getcontext().prec = 6

temp = Decimal('1') / Decimal('200')
print(temp)