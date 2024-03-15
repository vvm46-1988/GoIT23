def foo():
    import module_b  # local import
    module_b.bar()
    print('function foo from module a')


if __name__ == '__main__':
    foo()
