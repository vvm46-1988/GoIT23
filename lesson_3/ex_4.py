# # Знайти у рядку індекс останнього входження символу 'a'
s = input('Enter a string: ')
index = -1
count = 0
for char in s:
    if char == 'a':
        index = count
    count += 1

print(index)
