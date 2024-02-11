import module_b


def foo():
    print('Function `foo` from module_a')


# module_b.bar()  # помилка зацикленості модулів partially initialized module 'module_b' has no attribute 'bar'
# (most likely due to a circular import)


if __name__ == "__main__":
    foo()
    module_b.bar()
