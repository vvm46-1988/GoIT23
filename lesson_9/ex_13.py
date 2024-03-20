# Самостійний виклик через next
def simple_gen():
    yield 'First'
    yield 'Second'
    yield 'Third'

gen = simple_gen()

print(gen)

r = next(gen)
print(r)

r = next(gen)
print(r)

r = next(gen)
print(r)

r = next(gen)
print(r)