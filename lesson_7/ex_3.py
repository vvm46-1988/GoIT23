'''
Читаємо файл за допомогою бібліотеки pathlib
'''

from pathlib import Path
folder = Path('./Temp')

try:
    with open(folder / 'temp.txt', 'r') as f:
        for line in f:
            print(line, end='')
except Exception as e:
    print('Error: ', e)
finally:
    print('Happy end')

# /Users/vova/PycharmProjects/GoIT23/lesson7/Temp/temp.txt <- linux, macOS - 99,99%
# D:\Documents\lesson7\Temp\temp.txt   <- Windows