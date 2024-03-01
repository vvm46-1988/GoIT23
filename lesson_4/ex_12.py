# Область видимості
# x = 50
#
# def test_global():
#     global x
#     print(f'x is equal {x}')
#     x = 2  # this is local var
#     print(f'x was changed to {x}')
#
#
# test_global()
# print(x)

def outer():
    x = 'Hello World!'

    def inner_func():
        nonlocal x
        x = 'nonlocal var x'
        print(f'Inner func: {x}')

    inner_func()
    print(f'Outer func: {x}')

outer()
# Inner func: nonlocal var x
# Outer func: Hello World!

# Inner func: nonlocal var x
# Outer func: nonlocal var x
