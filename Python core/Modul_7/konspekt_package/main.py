# from konspekt_package.foo import foo
# from konspekt_package.baz.operation import mul, sum
# from konspekt_package.bar.info import log
from konspekt_package import foo, mul, sum, log, info_foo, get_value   # записуємо в такий спосіб бо імпорт
                                                                        # помістили в init


# def mul(a):
#     return a * 5


if __name__ == "__main__":
    print(foo('Natalia'))
    print(sum(1, 4))
    print(mul(5, 6))
    log('hello world')
    print(mul(5, 2))
    print(info_foo())
    print(foo('Test'))
    get_value()
