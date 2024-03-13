'''
Створення директорій pathlib
'''
from pathlib import Path

new_dir = Path('ABC')
new_dir.mkdir(parents=True, exist_ok=True)
new_dir.rmdir()
