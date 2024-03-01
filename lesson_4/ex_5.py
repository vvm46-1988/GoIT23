# Порахувати суму всіх чисел через рекурсію
sum = 0
# 10 + 9 + 8 + 7 + … + 1

def sum_numbers(max_num: int) -> int:
    if max_num <= 0:
        return 0
    if max_num == 1:
        return 1
    return max_num + sum_numbers(max_num - 1)


print(sum_numbers(10))
# f(10) -> 10 + f(9)
# f(9) -> 9 + f(8)
# f(8) -> 8 + f(7)
# f(7) -> 7 + f(6)
# f(6) -> 6 + f(5)
# f(5) -> 5 + f(4)
# f(4) -> 4 + f(3)
# f(3) -> 3 + f(2)
# f(2) -> 2 + f(1)
# f(1) -> 1
