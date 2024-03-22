def handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError:
            return "ValueError"
        except IndexError:
            return "IndexError"
    return wrapper


@handler
def add(arg, contacts):
    try:
        return arg + contacts
    except ValueError:
        print('Error')