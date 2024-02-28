# Знайти у рядку індекс першого входження символу 'a'
s = input('Enter a string: ')
index = 0

for char in s:
    print(f'char: {char}')
    if char == 'a':
        break
    index += 1
print(f'Перше входження символу а: {index}')
