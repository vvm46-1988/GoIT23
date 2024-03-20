# Найпростіший генератор
def my_generator():
    yield 1
    yield 2
    yield 3

for gen in my_generator():
    print(gen)