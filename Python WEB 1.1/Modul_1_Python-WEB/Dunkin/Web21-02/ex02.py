class Foo:
    pass


foo = Foo()


print(foo.__class__)
print(type(Foo))


Bar = type("Bar", (int,), {})

bar = Bar()

print(isinstance(bar, int))