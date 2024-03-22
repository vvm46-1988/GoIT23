# Декоратори з параметрами
def repeat_n_times(n):
    def decorator(original_func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                original_func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(5)
def greet(name):
    print(f'Hello {name}')


greet("Vova")