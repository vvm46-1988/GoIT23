# Порахувати суму всіх аргументів
def sum(start, *args):
    sum = start
    for element in args:
        sum += element
    return sum


print(sum(5, 3, 3, 4, 5, 0, 1))