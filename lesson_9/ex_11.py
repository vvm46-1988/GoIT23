"""
defaultdict: Зручно, якщо ми розбиваємо на різні списки набори телефонних операторів
"""

from collections import defaultdict, namedtuple

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636',
                 '0509993637', '0639993636', '0509993632', '0339993632']

phone_operator_numbers = defaultdict(list)

for ph in phone_numbers:
    if ph.startswith('050') or ph.startswith('095'):
        phone_operator_numbers['Vodafone'].append(ph)
    elif ph.startswith('067') or ph.startswith('096'):
        phone_operator_numbers['Kyivstar'].append(ph)
    elif ph.startswith('063') or ph.startswith('093'):
        phone_operator_numbers['lifecell'].append(ph)
    else:
        phone_operator_numbers['Unknown'].append(ph)

# print(phone_operator_numbers)

# Point = namedtuple('Point', ['x', 'y'])
# t = (5, 4)
# x = t[0]
# y = t[1]
# res = x + y
# print(res)
# point1 = Point(5, 4)
# res = point1.x + point1.y
# print(res)