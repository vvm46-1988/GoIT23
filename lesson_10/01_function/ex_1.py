# Функція може бути збережена у змінній чи структурі даних

def mul(a, b):
    return a * b


f = mul  # збереження ф-ції у змінній
print(f)
result = f(2, 3)
print(result)

field = {
    "a": 2,
    "b": 3,
    "operation": f
}

test = field.get("operation")
print(test)
result = field.get("operation")(field.get('a'), field.get('b'))
print(result)

result = field.get("operation")(3, 4)
print(result)