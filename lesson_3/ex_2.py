# swap
baz = int(input("Enter a number baz: "))
foo = int(input("Enter a number foo: "))

# if baz < foo:
#     temp = baz
#     baz = (baz + foo) / 2
#     foo = temp * foo
# else:
#     temp = foo
#     foo = (foo + baz) / 2
#     baz = temp * baz
if baz < foo:
    baz, foo = (baz + foo) / 2, baz * foo
else:
    foo, baz = (foo + baz) / 2, foo * baz

print(baz, foo)
# 4.0 15
# 4.0 15

# a = 3
# b = 5
# a,b = b,a
