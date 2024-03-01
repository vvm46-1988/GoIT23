# Знайти індекс колонки для excel таблиці

def index_table(column_name: str) -> int:
    """
    index_table("AA"): 27
    index_table("B"): 2
    index_table("ABC"): 703
    """
    index = 0
    for item, char in enumerate(reversed(column_name)):
        index += (ord(char) - 64) * (26 ** item)
    return index

print(f'Index table: {index_table("AAA")}')
