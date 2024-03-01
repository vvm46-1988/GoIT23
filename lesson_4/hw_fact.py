def factorial(n) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k) -> int:
    a = factorial(n)
    b = factorial(n - k)
    c = factorial(k)
    return int(a / (b * c))

# Cnk = n! / ((n - k)! · k!)
