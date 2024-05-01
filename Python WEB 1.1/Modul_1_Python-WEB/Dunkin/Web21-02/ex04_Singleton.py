from random import randint

class SomeClass:
    def __init__(self) -> None:
        self.param = randint(1, 10)


class SingleMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            obj = super().__call__(*args, **kwargs)
            cls._instances[cls] = obj
        return cls._instances[cls]


class SomeSingleClass(metaclass=SingleMeta):
    def __init__(self) -> None:
        self.param = randint(1, 10)


for i in range(10):
    sc = SomeClass()
    print(f"{sc.param = }")
    
    single_class = SomeSingleClass()
    print(f"{single_class.param = }")