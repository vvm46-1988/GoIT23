'''
Запис у файл байтових рядків. Робота з різними кодуваннями
'''

from pathlib import Path
message = 'Привіт світ! Hello world!'
print(message.encode())
print(message.encode('utf-16'))
print(message.encode('cp1251'))
with open('utf-8.txt', 'wb') as file:
    file.write(message.encode('utf-8'))

with open('utf-8.txt', 'rb') as file:
    print(file.read().decode('utf-8'))

with open('utf-8.txt', 'rb') as file:
    print(file.read().decode('utf-16'))


У цій ката вам буде надано рядок тексту та дійсні дужки, наприклад «h(el)lo». Ви повинні повернути рядок, перевернувши лише текст у круглих дужках, щоб "h(el)lo" перетворилося на "h(le)lo". Проте, якщо вказаний текст у дужках містить сам текст у дужках, то його також потрібно повернути назад, щоб він був спрямований у вихідному напрямку. Коли дужки перевернуті, вони повинні змінити напрямок, щоб вони залишалися синтаксично правильними (тобто "h((el)l)o" стає "h(l(el))o"). Цей шаблон має повторюватися для будь-якої кількості шарів дужок. На будь-якому рівні може бути кілька груп дужок (тобто «(1) (2 (3) (4))»), тому обов’язково врахуйте їх.

reverseInParens("h(el)lo") == "h(le)lo";
reverseInParens("a ((d e) c b)") == "a (b c (d e))";
reverseInParens("one (two (three) four)") == "one (ruof (three) owt)";
reverseInParens("one (ruof ((rht)ee) owt)") == "one (two ((thr)ee) four)";
reverseInParens("h(el)lo") == "h(le)lo";
reverseInParens("a ((d e) c b)") == "a (b c (d e))";
reverseInParens("one (two (three) four)") == "one (ruof (three) owt)";
reverseInParens("one (ruof ((rht)ee) owt)") == "one (two ((thr)ee) four)";