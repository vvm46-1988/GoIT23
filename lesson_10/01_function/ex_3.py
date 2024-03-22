# Функція може бути повернена з функції як результат

def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def ops(operator: str):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        return "Operator not supported"

f_mul = ops('*')  # f_mul = mul
print(f_mul(3, 5))

f_add = ops('+')  # f_add = add
print(f_add(3, 5))


# f_sub = ops('-')  # f_sub = sub
# print(f_sub(3, 5)) str(3, 5) - Exeption