# Свій генератор range
def my_range(limit):
    value = 0
    while value < limit:
        yield value  # return
        value += 1

gen = my_range(10)


# for value in my_range(5):
#     print(value)

while True:
    try:
        r = next(gen)
        print(r)
    except StopIteration:
        break
