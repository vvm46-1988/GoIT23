from datetime import datetime
from datetime import timedelta

birth_day = datetime(1988, 5, 20)
now = datetime.now()
# res = now + timedelta(birth_day)
# res = now + birth_day
# Чому ми не змогли додати дві дати між собою?
# Ми маємо використати операцію, яка має сенс в контексті об'єктів дати.
# У випадку додавання дати до дати, ми зазвичай додаємо часовий інтервал до першої дати.
# Тобто вираз: 1988.05.20 + 2024.03.06 немає сенсу.
# Якщо нам потрібно додати до певної дати якесь змщення, ми маємо використовувати timedelta
# Приклад: res = now + timedelta(days=365)
