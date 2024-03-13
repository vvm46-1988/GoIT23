'''
Прочитати хвіст файлу останні N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
'''
NUMBER_LINES = 4
# try:
#     lines = []
#     with open('test.txt', 'r', encoding='utf-8') as f:
#         for line in f:  # те саме, що і file.readline()
#             lines.append(line)
#             if len(lines) > NUMBER_LINES:
#                 lines.pop(0)
#     print(lines)
# except OSError as err:
#     print('Помилка доступу до файлу: ', err)


with open('test.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    last_n_lines = lines[-NUMBER_LINES:]
print(last_n_lines)
