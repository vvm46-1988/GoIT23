# match case
res = ('/', 5, 5)
match res:
    case ("+", x, y):
        print(x + y)
    case ("-", x, y):
        print(x - y)
    case ("*", x, y):
        print(x * y)
    case ("/", x, 0):
        print("Ділити на 0 не можна")
    case ("/", x, y):
        print(x / y)
    case _:
        print("Невідомий оператор")
