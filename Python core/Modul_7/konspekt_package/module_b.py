import module_a


def bar():
    print('Function `bar` from module_b')


if __name__ == "__main__":
    bar()
    module_a.foo()
