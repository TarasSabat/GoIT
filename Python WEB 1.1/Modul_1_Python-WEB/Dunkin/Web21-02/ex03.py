class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(name, bases, dct)
        new_obj = super().__new__(cls, name, bases, dct)
        new_obj.super_param = "This is super"
        return new_obj
    

class MyClass(metaclass=MyMeta):
    pass


mc = MyClass()

print(mc.super_param)