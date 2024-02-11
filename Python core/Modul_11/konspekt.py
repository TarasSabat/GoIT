''' Метод init '''
'''Цей метод відповідає за ініціалізацію об'єкта. Коли ви створюєте об'єкт класу, то спочатку створюється порожній об'єкт, який містить лише обов'язкові службові атрибути. Після цього (об'єкт вже створено) автоматично викликається метод __init__, який ви можете модифікувати під ваші потреби.'''
# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

    # def say_hello(self):
    #     return f'Hello! I am {self.name}'


# bill = Human('Bill')
# print(bill.say_hello())  # Hello! I am Bill
# print(bill.age)          # 0

# jill = Human('Jill', 20)
# print(jill.say_hello())  # Hello! I am Jill
# print(jill.age)          # 20

''' В цьому прикладі ми створили клас Human, у якому визначили метод __init__. У цьому методі ми додаємо об'єктам цього класу поля name та age. Зверніть увагу, що метод __init__ може приймати аргументи позиційні та/або іменні, як і будь-який інший метод. Коли ми створюємо об'єкт класу Human, ми повинні класу передати обов'язково хоча б один аргумент, оскільки метод __init__ повинен приймати обов'язково name.
__init__ не обов'язково приймає аргументи та містить лише створення полів. Цей метод можна використовувати для реалізації будь-яких дій, які вам потрібні на етапі, коли об'єкт вже створений та його потрібно ініціалізувати.'''

###########################

''' Методи str та repr '''
''' __repr__ це метод приймає лише один аргумент (self звичайно) і повинен повертати рядок.
Якщо ви хочете виводити у випадках, коли застосунок повинен відобразити об'єкт, якусь корисну інформацію, ви можете модифікувати цей метод. Наприклад, клас точки на площині в Декартових координатах:'''
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Point ({self.x}, {self.y})'


# a = Point(1, 9)
# a

''' Дуже схожий на нього метод, який відповідає за те, як об'єкт конвертується в рядок — це метод __str__. Коли ви викликаєте функцію str та передаєте їй якийсь об'єкт, то насправді цей об'єкт викликається методом __str__.'''
# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'Hello! I am {self.name}'


# bill = Human('Bill')
# bill_str = str(bill)
# print(bill_str)  # Hello! I am Bill

''' Методи __repr__ и __str__ '''
# class Car:
#     name = 'GoIT'

#     def __init__(self, year, mark, model, color):
#         self.year = year
#         self.mark = mark
#         self.model = model
#         self.color = color

#     def __str__(self):
#         return f'{self.name}: {self.mark}.{self.model}'

#     def __repr__(self):
#         return f"Car({self.year}, '{self.mark}', '{self.model}', '{self.color}')"


# car = Car(2022, 'Toyota', 'Camry', 'Black')
# print(car)  # print(str(car))
# print(repr(car))

'''Приклад'''
# class User:
#     def __init__(self, name, last_name = None) -> None:
#         self.name = name
#         self.last_name = last_name
        
#     def __str__(self) -> str:
#         return f'Fulname: {self.name} {self.last_name}'
        
#     def __repr__(self) -> str:   # відображає як строку навіть списки і має вищий пріорітет ніж __str__ 
#         return f'Fulname: {self.name} {self.last_name}'
    
# user_1 = User('Boris', 'Johnson')
# print(user_1)

# users = []
# users.append(user_1)
# print(users)

###########################

''' Методи getitem та setitem '''
''' Коли ви хочете отримати значення, використовуючи квадратні дужки, в об'єкта викликається метод __getitem__. Для запису значення з індексом або ключем викликається метод __setitem__. Обидва ці методи приймають першим аргументом self. __getitem__ другим аргументом приймає індекс або ключ, за яким потрібно знайти елемент, а __setitem__ другим аргументом приймає ключ/індекс, а третім значення, яке потрібно записати за цим ключем/індексом. '''
# class ListedValuesDict:
#     def __init__(self):
#         self.data = {}

#     def __setitem__(self, key, value):
#         if key in self.data:
#             self.data[key].append(value)
#         else:
#             self.data[key] = [value]

#     def __getitem__(self, key):
#         result = str(self.data[key][0])
#         for value in self.data[key][1:]:
#             result += ", " + str(value)
#         return result


# l_dict = ListedValuesDict()
# l_dict[1] = 'a'
# l_dict[1] = 'b'
# print(l_dict[1])    # a, b

'''У цьому прикладі ми створили власний клас, який поводиться як словник. ListedValuesDict значення зберігає у список і вже цей список зберігає як значення для ключа. Головна відмінність від словника у тому, що ListedValuesDict не дозволяє перезаписувати значення, завжди додаватиме нове значення в кінець списку. І при отриманні значення повертає рядок, складений зі значень у списку.'''

''' Методи __getitem__ i __setitem__ '''
# from collections import UserList


# class PositiveNumbers(UserList):
#     def __init__(self, data=[]):
#         super().__init__()
#         self.data = [el for el in list(filter(lambda x: x > 0, data))]

#     def __getitem__(self, item):
#         if item is None:
#             return self.data
#         return self.data[item]

#     def __setitem__(self, key, value):
#         if value > 0 and key < len(self.data):
#             self.data[key] = value

#     def append(self, item) -> None:
#         if item > 0:
#             super().append(item)


# nums = PositiveNumbers([2, 3, -4, 5, 6])
# print(nums)
# print(nums[None])
# print(nums[0])
# nums[0] = -3
# print(nums)
# nums.append(-5)
# print(nums)

########################

''' Функтори, метод call '''
''' Функтори — це об'єкти, які поводяться як функції у тому сенсі, що їх можна викликати та передавати їм аргументи. Функція у Python — це такий самий об'єкт, але у ньому реалізований метод __call__, який відповідає за синтаксис виклику з круглими дужками. 
Функтор - потрібний коли ми хочимо викликати екземпляр об'єкта як функцію
Функтор - це коли екземпляр класу може сам себе викликати '''
# class Adder:
#     def __init__(self, add_value):
#         self.add_value = add_value

#     def __call__(self, value):
#         return self.add_value + value


# two_adder = Adder(2)
# print(two_adder(5))  # 7
# print(two_adder(4))  # 6

# three_adder = Adder(3)
# print(three_adder(5))  # 8
# print(three_adder(4))  # 7

'''В цьому прикладі ми створили клас Adder, у якого є метод __call__. Тепер об'єкти цього класу можна викликати як функцію, передаючи їм аргументи. Ці виклики будуть викликати метод __call__ в об'єктів класу Adder.'''
'''
# Функтор - потрібний коли ми хочимо викликати екземпляр об'єкта як функцію
# Функтор - це коли екземпляр класу може сам себе викликати
'''
# class Count:
#     def __init__(self, init_steps):
#         self.steps = init_steps

#     def __call__(self, *args, **kwargs):
#         inc, = args  # (25,)
#         self.steps += inc


# count_step = Count(100)
# count_step(25)
# count_step(50)
# print(count_step.steps)

##########################

''' Створення власних менеджерів контексту '''
''' Менеджер контексту закриє з'єднання в будь-якому випадку. 
Для цього використовуються магічні методи, які відповідають за синтаксис with ... as ...:.
__enter__ викликається, коли інтерпретатор заходить у контекст і те, що він поверне, буде записано в змінну після as;
__exit__ викликається, коли інтерпретатор виходить із блоку менеджера контексту. Буде викликаний в будь-якому випадку.'''
# class Session:
#     def __init__(self, addr, port=8080):
#         self.connected = True
#         self.addr = addr
#         self.port = port

#     def __enter__(self):
#         print(f"connected to {self.addr}:{self.port}")
#         return self

#     def __exit__(self, exception_type, exception_value, traceback):
#         self.connected = False
#         if exception_type is not None:
#             print("Some error!")
#         else:
#             print("No problem")

'''Об'єкт класу Session буде менеджером контексту. Ми можемо створити його та використовувати повторно за потребою:'''
# localhost_session = Session("localhost")

# with localhost_session as session:
#     print(session is localhost_session)     # True
#     print(localhost_session.connected)      # True

# print(localhost_session.connected)          # False

'''Коли інтерпретатор всередині менеджера контексту __enter__ вже викликаний та self.connected == True. Зверніть увагу, session is localhost_session повертає True, оскільки метод __enter__ повертає self. Ви можете створювати об'єкт Session всередині виразу with ... as ...::'''
# with Session("localhost") as session:
#     print(session.connected)      # True

'''Метод __exit__ буде викликаний при виході з контексту помилково або штатно. __exit__ обов'язково повинен приймати аргументи exception_type, exception_value, traceback, окрім self. Це тип винятку, значення та увесь traceback помилки. Зверніть увагу, що __exit__ не дозволяє перехоплювати помилку, але він дає можливість щось виконати, незалежно від того, чи виникла помилка. Якщо контекст завершився без помилок, то в цих аргументах буде None.'''

'''Наприклад, покажемо ситуацію, коли менеджер контексту завершився з помилкою.'''
# with Session("host", "port") as session:
#     raise Exception("OH NO!")

'''В результаті в консолі буде виведено:'''
# connected to host:port
# Some error!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     raise Exception("OH NO!")
# Exception: OH NO!

'''На виході з контексту обов'язково буде виконано __exit__ і, навіть якщо помилка трапилася, ми можемо щось зробити (наприклад, встановити self.connected = False).
Метод __exit__ не дозволяє перехоплювати винятки, він потрібен лише для того, щоб правильно завершити контекст (закрити відкриті файли та з'єднання, повернути ресурси системі тощо).'''


"""
Для того, щоб об'єкт можна було використовувати в конструкції with... as...: в об'єкті повинні бути визначені два
методи: __enter__, __exit__.
__enter__ - метод, який приймає лише один аргумент self. Якщо метод щось повертає, його результат буде
записаний у змінну val у конструкції with context_manager as val:.
__exit__ - обов'язково приймає 4 аргументи: self, exception type, exception value, exception traceback.
Ці аргументи необхідні коректної обробки винятків всередині __exit__.
"""
# class FileWriter:
#     def __init__(self, filename):
#         self.file = None
#         self.opened = False
#         self.filename = filename

#     def __enter__(self):
#         self.file = open(self.filename, 'w')
#         self.opened = True
#         return self.file

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.opened:
#             self.file.close()
#         self.opened = False


# if __name__ == "__main__":
#     with FileWriter('test.txt') as file:
#         file.write('Hello world!\n')
#         file.write('Lesson 11\n')

''' Декоратор contextmanager'''
# from contextlib import contextmanager
# from datetime import datetime

# @contextmanager
# def managed_resource(*args, **kwargs):
#     log = ''
#     timestamp = datetime.now().timestamp()
#     message = '{:<20}|{:^15}| open \n'.format(timestamp, args[0])
#     log += message
#     file_handler = open(*args, **kwargs)
#     try:
#         yield file_handler
#     finally:
#         timestamp_closed = datetime.now().timestamp()
#         diff = timestamp_closed - timestamp
#         message = '{:<20}|{:^15}| closed {:>15}s \n'.format(timestamp_closed, args[0], diff)
#         log += message
#         file_handler.close()
#         print(log)

# with managed_resource('test.txt', 'r') as f:
#     print(f.read())

''' Декоратор contextmanager'''
# from contextlib import contextmanager

# @contextmanager
# def managed_resource(*args, **kwargs):
#     file_handler = open(*args, **kwargs)
#     try:
#         yield file_handler
#     finally:
#         file_handler.close()


# with managed_resource('test.txt', 'r') as f:
#     print(f.read())
    
##########################

''' Створення об'єкта ітератора/генератора '''
'''Протокол ітератора у Python реалізований за допомогою методу __iter__. Цей метод повинен повертати ітератор. Ітератором може бути будь-який об'єкт, у якого є метод __next__, який за кожного виклику повертає значення. Щоб створити ітератор, достатньо реалізувати метод __next__.
Генератор - це ітератор по якому можні ітеруватися тільки один раз так як вони на зберігають ссвої значення в пам'яті.
Наприклад, створимо клас, яким можна ітеруватися Iterable та клас ітератор:'''
# class Iterable:
#     MAX_VALUE = 10
#     def __init__(self):
#         self.current_value = 0

#     def __next__(self):
#         if self.current_value < self.MAX_VALUE:
#             self.current_value += 1
#             return self.current_value
#         raise StopIteration


# class CustomIterator:
#     def __iter__(self):
#         return Iterable()


# c = CustomIterator()
# for i in c:
#     print(i)

'''Зверніть увагу, що метод __next__ повинен викликати виняток StopIteration, щоб вказати, що ітерування завершено, інакше цикл for за таким об'єктом буде нескінченний.'''

'''Приклад'''
# from random import randint

# class RandIterator:
#     def __init__(self, start, end, quantity):
#         self.start = start
#         self.end = end
#         self.quantity = quantity
#         self.count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.count += 1
#         if self.count > self.quantity:
#             raise StopIteration
#         else:
#             return randint(self.start, self.end)


# my_random_list = RandIterator(0, 200, 10)

# for random_range in my_random_list:
#     print(random_range, end=' ')

# a = [1, 3, 4]
# print(type(a))
# b = list()

#############################

''' Інкапсуляція у Python (property, setter). '''
'''У Python неможливо інкапсулювати (зробити недоступними) атрибути класу. Ви завжди можете отримати доступ до будь-якого атрибуту. Щоб якось вказати розробнику, що доступ до атрибута напряму небажаний, прийнято називати такі поля або методи, починаючи з одного нижнього підкреслення. Якщо ж назвати атрибут так, що спочатку буде два нижні підкреслення, то включиться механізм "приховування" імен. Це не означає, що доступ до цього поля буде закрито, просто дещо ускладнений.'''
# class Secret:
#     public_field = 'this is public'
#     _private_field = 'avoid using this please'
#     __real_secret = 'I am hidden'

# s = Secret()
# print(s.public_field)           # this is public
# print(s._private_field)         # avoid using this please
# print(s._Secret__real_secret)   # I am hidden

''' Інкапсуляція у Python (property, setter). '''
# class A:
#     def _protected(self):    # атрибути з одним _ чи двома __ нижніми підкресленнями призначені тільки для використання в середині класу    
#         print('This is protected method')
        
# a = A()
# a._protected()

# class B:
#     def __private(self):     # атрибути з одним _ чи двома __ нижніми підкресленнями призначені тільки для використання в середині класу    
#         print('This is private method')
        
# b = B()
# b._B__private()
# # b.__private()

'''Як видно з цього прикладу, доступу за допомогою s.__real_secret немає, але можна отримати доступ до цього самого поля через s._Secret__real_secret, що загалом нічого не захищає.

Цей механізм можна використовувати для реалізації механізму setter та getter. Буває виникає необхідність перевірити, що користувач хоче записати в поле. Для цього можна написати окремий метод, який буде перед збереженням значення в полі реалізовувати перевірку, але саме поле, як і раніше, залишиться доступним. Можна ж скористатися декоратором setter. Для обчислення значення "на льоту" або як пару для setter можна скористатися декоратором property, який перетворює будь-який метод на поле. Наприклад, ми хочемо перевірити, що користувач вводить лише додатні числа.'''
# class PositiveNumber:
#     def __init__(self):
#         self.__value = None

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, new_value):
#         if new_value > 0:
#             self.__value = new_value
#         else:
#             print('Only numbers greater zero accepted')


# p = PositiveNumber()
# p.value = 1
# print(p.value)  # 1
# p.value = -1    # Only numbers greater zero accepted
# p._PositiveNumber__value = -1
# print(p.value)  # -1s

'''У цьому прикладі поле __value можна вважати прихованим, воно певною мірою інкапсульовано. Проте значення в цьому полі може бути отримане і модифіковане напряму. Ще декоратор property зручний, коли значення у полі потрібно обчислювати у момент звернення.'''

'''getter, setter'''
# class Animal:
#     def __init__(self, nickname, age, weight):
#         self.__nickname = None
#         self.__age = None
#         self.__weight = None
#         # Setter
#         self.name = nickname
#         self.age = age
#         self.weight = weight

#     @property
#     def name(self):
#         return self.__nickname

#     @name.setter
#     def name(self, nickname):
#         if len(nickname) > 0:
#             self.__nickname = nickname
#         else:
#             raise ValueError('Тварина має мати імя')

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         self.__age = age
        

#     @property
#     def weight(self):
#         return self.__weight

#     @weight.setter
#     def weight(self, weight):
#         if weight > 0:
#             self.__weight = weight
#         else:
#             raise ValueError('Не вірна вага для тварини')


# class Turtle(Animal):
#     def __init__(self, nickname, age, weight):
#         super().__init__(nickname, age, weight)
    
#     @Animal.age.setter
#     def age(self, age):               
#         if age in list(range(0, 150)):
#             Animal.age.fset(self, age)
#         else:
#             raise ValueError('Не вірний вік для тварини')
        
 

# turtle = Turtle('Leo', 149, 100)
# print(turtle.name, turtle.age, turtle.weight)

# a = Animal('Boris', 12, 1500)
# print(a.name, a.age, a.weight)

# a = Animal('Boris', -2, 1500)
# print(a.name, a.age, a.weight)
# a.age = -15
# print(a.name, a.age, a.weight)

'''Приклад'''
# class User:
#     def __init__(self, name, age):
#         self.__private_name = None
#         self.__private_age = None
#         self.name = name
#         self.age = age
        
#     @property 
#     def name(self):
#         return self.__private_name
      
#     @name.setter  
#     def name(self, value: str):
#         if value.isalpha():
#             self.__private_name = value
#         else:
#             raise Exception('Wrong name')
        
#     @property
#     def age(self):
#         return self.__private_age
    
#     @age.setter
#     def age(self, value):
#         if int(value) >= 18:
#             self.__private_age = int(value)
#         else:
#             raise Exception('Wrong age')
        
# user_1 = User('Boris', 20)
# print(user_1.name, user_1.age)

#############################

'''Перевизначення математичних операторів'''
'''Усі математичні оператори можна перевизначити. Для цього є методи, відповідальні за кожний оператор:
__add__ додавання
__sub__ віднімання
__mul__ множення
__div__ ділення
__pow__ піднесення до степеня
та інші. Перевизначення математичних операторів може стати зручним інструментом. Наприклад, створимо клас словників, які підтримують операції додавання та віднімання:'''
# from collections import UserDict

# class MyDict(UserDict):
#     def __add__(self, other):
#         self.data.update(other)
#         return self


#     def __sub__(self, other):
#         for key in self.data:
#             if key in other:
#                 self.data.pop(key)
#         return self


# d1 = MyDict({1: 'a', 2: 'b'})
# d2 = MyDict({3: 'c', 4: 'd'})


# d3 = d1 + d2
# print(d3)   # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# d4 = d3 - d2
# print(d4)   # {1: 'a', 2: 'b'}

'''Синтаксис простий і код досить виразний, але потрібно бути акуратним з перевизначенням математичних операторів, зазвичай така поведінка неочевидна і може навпаки заплутати.'''

#############################

''' Перевизначення операцій порівняння '''
'''Операції порівняння, як і інші оператори, мають свої "магічні" методи:
__eq__(self, other) — визначає поведінку під час перевірки на відповідність (==).
__ne__(self, other) — визначає поведінку під час перевірки на невідповідність. !=.
__lt__(self, other) — визначає поведінку під час перевірки на менше <.
__gt__(self, other) — визначає поведінку під час перевірки на більше >.
__le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <=.
__ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >=.
Якщо вам потрібно, щоб ваш об'єкт був порівнянний, ви можете реалізувати ці шість методів і тоді будь-яка перевірка на порівняння працюватиме:'''
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __ne__(self, other):
#         return self.x != other.x or self.y != other.y

#     def __lt__(self, other):
#         return self.x < other.x and self.y < other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __le__(self, other):
#         return self.x <= other.x and self.y <= other.y

#     def __ge__(self, other):
#         return self.x >= other.x and self.y >= other.y


# Point(0, 0) == Point(0, 0)  # True
# Point(0, 0) != Point(0, 0)  # False
# Point(0, 0) < Point(1, 0)   # False
# Point(0, 0) > Point(0, 1)   # False
# Point(0, 2) >= Point(0, 1)  # True
# Point(0, 0) <= Point(0, 0)  # True

#############################

''' Метод __new__ '''
'''Метод __new__ завжди виконується першим '''
# class Foo:  # class Foo(object):
#     def __new__(cls, *args, **kwargs):
#         print('Method new Foo class')
#         print(args)
#         instance = super(Foo, cls).__new__(cls)
#         return instance

#     def __init__(self, value):
#         print('__init__ Foo class')
#         self.value = value


# class Baz(Foo):
#     def __init__(self, value):
#         super().__init__(value)

# baz = Baz(10)
# foo = Foo(20)

# print(baz.value, foo.value)
# print(baz, foo)
# print(isinstance(baz, Baz))
# print(isinstance(foo, Baz))

###########################

''' Singleton '''
'''Одинак — це породжуючий патерн, який гарантує існування тільки одного об’єкта певного класу, а також дозволяє    
дістатися цього об’єкта з будь-якого місця програми.
Одинак має такі ж переваги та недоліки, що і глобальні змінні. Його неймовірно зручно використовувати, 
але він порушує   модульність вашого коду.
Ви не зможете просто взяти і використовувати клас, залежний від одинака, в іншій програмі. Для цього доведеться   
емулювати там присутність одинака. Найчастіше ця проблема проявляється при написанні юніт-тестів.'''
# class Singleton:
#     instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super(Singleton, cls).__new__(cls)  # cls - екземпляр класу
#         return cls.instance

#     def __init__(self, value):
#         self.value = value


# foo = Singleton(10)
# baz = Singleton(20)
# bar = Singleton(30)

# print(foo.value, baz.value, bar.value)
# print(foo, baz, bar)
# # 0x7fe6002c8f10
# # 0x7fe6002c8f10
# # 0x7fe6002c8f10

########################

"""
Розбираємо різницю між: звичайним методом, @classmethod и @staticmethod
Якщо не звертаэшся до self тоді його можна прибрати і зробити метод @staticmethod
"""
# class Compare:
#     a = 5

#     def doubler(self, x):  # self = test (тобто назва екземпляра класу)
#         print('Mul on 2')
#         return x * 2

#     @staticmethod
#     def triples(x):
#         print('Mul on 3')
#         return x * 3

#     @classmethod
#     def quad(cls, x):  # cls = Compare (клас)
#         print('Mul on 4')
#         return x * 4

# test = Compare()
# print('Екземпляри класу')
# print(test.doubler(5))
# print(test.triples(5))
# print(test.quad(5))
# print('Виклик через клас')
# # print(Compare.doubler(6))
# print(Compare.triples(6))
# print(Compare.quad(6))

############################

''' Декоратори класів '''
# def method_decorator(func):
#     def wrapper(self, *args):
#         print('--Decorator func run--')
#         result = func(self, *args)
#         print('--Decorator func end--')
#         return result
#     return wrapper


# def class_decorator(cls):
#     print('---Decorator class---')
#     new_cls = cls
#     new_cls.value = 55
#     return new_cls


# @class_decorator
# class TestClass:
#     name = 'GoIT'

#     @method_decorator
#     def info(self, user):
#         return f'Hello: {user}'


# t = TestClass()
# print(t.info('Ivan'))
# print(t.value)
# t.value = "Hello world"
# print(t.value)
# print('=====')
# print(TestClass.value)
