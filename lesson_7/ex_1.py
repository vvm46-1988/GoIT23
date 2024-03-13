'''
Прочитати перші N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
'''

import sys
NUMBER_LINES = 4

print(sys.argv)

try:
    # file = open(sys.argv[1], 'r', encoding='utf-8')  # sys.argv[1] == test.txt
    file = open("test.txt", 'r', encoding='utf-8')  # sys.argv[1] == test.txt
    line = file.readline()
    count = 0
    while count < NUMBER_LINES and line != '':
        line = line.strip()
        count += 1
        print(line)
        line = file.readline()
    # file.close()
except OSError as err:
    print('Помилка доступу до файлу: ', err)
finally:
    file.close()
