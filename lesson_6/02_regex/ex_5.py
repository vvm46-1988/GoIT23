# якщо буде час!!!

"""
Метод: split

Напишемо універсальну функцію get_parameters, яка повертатиме словник з даними.
Оскільки в першому рядку розділювачем є символ `;` а в другому `&`,
тому тут вдало підійде випадок (a|b - відповідає a або b)
"""


import re

url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;
url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"  # &
url = "data=vale*data_1=value_2"  # *
ur_1 = "data=vale%data_1=value_2"  # %