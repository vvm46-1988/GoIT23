'''
Завдання: Сортування файлів у папці.
Копіювати файли із зазначеної папки та покласти в нову папку з розширенням цього файлу.
'''

import argparse
from pathlib import Path
from shutil import copyfile

output_folder = Path('dist')

def read_folder(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():  #  перевіряємо чи елемент є папкою
            read_folder(element)  # Рекурсивно викликаємо функцію з новим шляхом
        else:  # Тоді це файл
            copy_file(element)  # Функція для копіювання файлів


def copy_file(file: Path) -> None:
    ext = file.suffix  # Отримуємо розширення з файлів: .JPG, .PNG, .SVG, etc.
    new_path = output_folder / ext  # Будуємо новий шлях
    new_path.mkdir(parents=True, exist_ok=True)  # Створюємо папку за новим шляхом
    copyfile(file, new_path / file.name)  # Копіюємо файл

read_folder(Path('picture'))


