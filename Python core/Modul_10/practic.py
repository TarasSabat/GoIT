''' Створення класів, конструкторів, методів '''
# class Animal:
#     def __init__(self, nickname='', age=5):
#         self.nickname = nickname                # ініціалізація змінних (обов'язково)
#         self.age = age                          # ініціалізація змінних (обов'язково)

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# animal = Animal()
# print(animal.nickname)
# print(animal.age)
# print(animal.get_info())
# animal.age = 5
# print(animal.get_info())

#####
## файл ex03.py ###

# data = {"name": "Bill", 
#         "games": [
#             {"name": "Doom", "counter": 10},
#             {"name": "WoW", "counter": 15},
#             {"name": "HeroesIII", "counter": 20}]}


# class Game:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.count = 0
    
#     def play_game(self):
#         self.count += 1
    
#     def __repr__(self) -> str:
#         return f"{self.name = }, {self.count = }"


# class Gamer:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.games = []
    
#     def add_game(self, game: Game) -> None:
#         self.games.append(game)
    
#     def play_game(self, game_name: str) -> str:
#         for g in self.games:
#             if g.name == game_name:
#                 g.play_game()
#                 return "Good game"
#         return "Bad game"
    
## файл ex04.py ###

# if __name__ == '__main__':
#     print(data["games"][0]["counter"])

# from ex03 import Game, Gamer


# g1 = Game("Doom")
# g2 = Game("CS:Go")
# g3 = Game("HeroesIII")

# gamer = Gamer("Bill")

# for g in (g1, g2, g3):
#     gamer.add_game(g)

# print(gamer.games)
# print(gamer.play_game("Doom"))
# print(gamer.games)

    
"""
Базові принципи ООП - Спадкування
Спадкування є властивістю об'єктів породжувати своїх нащадків.
Об'єкт-нащадок автоматично успадковує від батька все:
поля та методи, може доповнювати об'єкти новими полями та змінювати (перекривати) методи батька або доповнювати їх.
"""
# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

# class Cat(Animal):
#     name = ['Cat']     # mutable

#     def __init__(self, nickname, age, owner):
#         super().__init__(nickname, age)
#         self.owner = owner

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'

#     def get_info(self):
#         return 5 * 5


# cat = Cat('Borys', 3, 'Valerii')
# print(cat.nickname)
# print(cat.age)
# cat.age = 6
# print(cat.get_info())
# print(cat.sound())

# cat_2 = Cat('Jack', 2, 'Ivan')
# print(f'cat.name: {cat.name}')

# cat.name[0] = 'Test'

# print(f'cat.name: {cat.name}')
# print(f'cat_2.name: {cat_2.name}')
# print(f'Cat.name: {Cat.name}')


# class Car:
#     brand = 'TOYOTA'

# p1 = Car()
# p2 = Car()
# print(p1.brand)
# print(p2.brand)

# # Car.brand = 'Daewoo'
# # print(p1.brand)
# # print(p2.brand)
# p1.brand = 'Mazda'
# print(p1.brand)
# print(p2.brand)

# print(dir(cat))

#####

# from random import randint, choice


# class Position:
#     def __init__(self, value) -> None:
#         self.value = value
    
#     def get_salary(self):
#         return randint(500, 1500)

#     def __str__(self) -> str:
#         return self.value


# class Employee:
#     def __init__(self, name: str, position: str = None) -> None:
#         self.name = name
#         self.position = Position(position) if position else position

#     def get_rate(self) -> int:
#         if self.position:
#             return self.position.get_salary()
#         return 0



# names = ("Bill", "Gill", "Mary")

# positions = ("Manager", "CEO", "Developer", "QA")

# employees = []

# for i in range(1000):
#     employees.append(Employee(f"{choice(names)}-{i}", choice((choice(positions), None))))

# print(len(employees))

# rand_emp: Employee = employees[randint(0, 999)]

# print(rand_emp.get_rate(), rand_emp.position, rand_emp.name )

# print(len(list(filter(lambda x: x.get_rate() != 0, employees))))

"""
Базові принципи ООП - Поліморфізм
Поліморфізм - це властивість споріднених об'єктів (тобто об'єктів, що мають одного спільного батька)
вирішувати схожі за змістом проблеми різними способами.
"""
# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# class Cat(Animal):
#     def __init__(self, nickname, age, owner):
#         super().__init__(nickname, age)
#         self.owner = owner

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# class Dog(Animal):
#     def __init__(self, nickname, age, owner):
#         super().__init__(nickname, age)
#         self.owner = owner

#     def sound(self):
#         return f'{self.nickname} says Woof !!!!'

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

# cat = Cat('Borys', 4, 'Ivan')
# dog = Dog('Bella', 3, 'Petro')

# print(isinstance(dog, Animal))
# print(isinstance(dog, Cat))
# print(isinstance(dog, Dog))
# print('============')
# print(type(dog) is Animal)
# print(type(dog) is Dog)

# for element in (cat, dog):
#     print(element.sound())

"""
Асоціація
Це коли один клас включає інший клас як один з полів. Асоціація описується словом "має".
Тварина має господаря.
Виділяють два окремі випадки асоціації: композицію та агрегацію.
Композиція
Це коли господар не існує окремо від вихованця. Він створюється при створенні вихованця і повністю управляється вихованцем.
КОМПОЗИЦІЯ - це якщо цикл життя одного об'єкта нерозривно зв'язаний з циклом життя іншого об'єкта.
Агрегація
АГРЕГАЦІЯ - це якщо цикл життя одного об'єкта не пов'язаний з циклом життя іншого об'єкта але взаємодіє з ним. 
"""

# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f'{self.name}- {self.phone}'

# class Cat(Animal):
#     def __init__(self, nickname, age, name, phone):
#         super().__init__(nickname, age)
#         self.owner = Owner(name, phone)  # композиція

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'

# cat = Cat('Alex', 3, 'Petro', '0951234567')
# print(cat.owner.info())

"""
Агрегація
Це коли екземпляр господаря створюється десь в іншому місці коду, і передається в конструктор вихованця як параметр
Так є правильно. Так завди і робити.
"""

# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f'{self.name}- {self.phone}'


# class Cat(Animal):
#     def __init__(self, nickname, age, owner: Owner):
#         super().__init__(nickname, age)
#         self.owner = owner  # агрегація

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'


# owner = Owner('Petro', '0951233455')
# cat = Cat('Alex', 3, owner)
# print(cat.owner.info())

"""
Method Resolution Order (MRO).
MRO в Python працює наступним чином:
1. Шукає атрибут серед атрибутів самого класу. Саме завдяки цьому ви можете "перевизначати"
батьківські атрибути.
2. Шукає атрибут у першого з батьків (той, що зазначено першим у списку батьків).
3. Шукає атрибут у наступного батька у списку батьків, доки такі є.
4. Шукає атрибут у батьках першого з батьків.
5. Повторює п.4 всім батьків.
6. Викликає виняток, що атрибут не знайдено.
"""

# class A:
#     def hi(self):
#         print('A')

# class B(A):
#     def hi(self):
#         print('B')

# class C(A):
#     def hi(self):
#         print('C')

# class D(B, C):
#     def hi_(self):
#         print(55)

# d = D()
# d.hi()
# print(D.__mro__)   # магічний метод який показує де буде відбуватись пошук атрибутів

# #####

# class Human:
#     pass


# class Developer(Human):
#     field_description = "My Programming language"
#     language = ""
#     value = ''
#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"

#     def test(self):
#         return 25


# class PythonDeveloper(Developer):
#     value = "Python"

#     def make_some_code(self):
#         res = self.test()
#         return f"{self.field_description} is {self.value}. Result is: {res}"


# class JSDeveloper(Developer):
#     value = "JavaScript"


# a = PythonDeveloper()
# print(a.make_some_code())

# dev = Developer()
# dev.value = 'Python'
# print(dev.make_some_code())

''' Контейнери списки UserList '''

# from collections import UserList
# from random import randint

# class MyList(UserList):
#     info = 'This is my list class'

#     def get_positive(self):
#         return list(filter(lambda x: x > 0, self.data))

#     def get_negative(self):
#         return list(filter(lambda x: x < 0, self.data))

#     def get_info(self):
#         return self.info

# r = []
# for _ in range(0, 35):
#     r.append(randint(-10, 10))

# result = MyList(r)
# print(result)

# result.append(5555)
# print(result)
# print(result.get_positive())
# print(result.get_negative())
# print(result.get_info())

'''Контейнери словники UserDict'''
# from collections import UserDict

# contacts = [
#    {
#        "name": "Allen Raymond",
#        "email": "nulla.ante@vestibul.co.uk",
#        "phone": "(992) 914-3792",
#        "favorite": False,
#    },
#    {
#        "name": "Chaim Lewis",
#        "email": "dui.in@egetlacus.ca",
#        "phone": "(294) 840-6685",
#        "favorite": False,
#    },
#    {
#        "name": "Kennedy Lane",
#        "email": "mattis.Cras@nonenimMauris.net",
#        "phone": "(542) 451-7038",
#        "favorite": True,
#    },
#    {
#        "name": "Wylie Pope",
#        "email": "est@utquamvel.net",
#        "phone": "(692) 802-2949",
#        "favorite": False,
#    },
#    {
#        "name": "Cyrus Jackson",
#        "email": "nibh@semsempererat.com",
#        "phone": "(501) 472-5218",
#        "favorite": True,
#    },
# ]

# class Customer(UserDict):
#     def get_phone(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def get_email(self):
#         return f"{self.get('name')}: {self.get('email')}"

# customers = [Customer(contact) for contact in contacts]
# print(customers)

# for customer in customers:
#     print(customer.get_email())
#     print(customer.get_phone())

#####

# from collections import UserDict


# class Box(UserDict):
#     def add_if_not_exist(self, key, item):
#         if self.data.get(key):
#             return None
#         self.data[key] = item
#         return item


# box = Box()

# box.add_if_not_exist("food", "banana")

# print(box)

# box.add_if_not_exist("food", "kiwi")

# print(box)

''' Контейнери строки UserString'''
# from collections import UserString

# template = [
#     "Ви можете досягти всього. Варто лише трохи постаратися і запастися книгами.",
#     "Цей смартфон - справжня знахідка. Великий і яскравий екран, потужний процесор - все це в невеликому гаджеті.",
#     "Зібрати камені нескінченності легко, якщо ви природжений герой.",
#     "Освоїти верстку нескладно. Візьміть книгу нову книгу і закріпіть усі вправи на практиці.",
#     "Боротися з прокрастинацією нескладно. Просто дійте. Маленькими кроками.",
#     "Програмувати не настільки складно, як про це говорять.",
#     "Прості щоденні вправи допоможуть досягти успіху."
# ]


# # for item, text in enumerate(template):
# #     print("|{:^5}|{:<15}".format(item, text))

# class Text(UserString):
#     def set_limit_text(self, limit=15):
#         return (f'{self.data[:limit]}...')


# text = [Text(text) for text in template]
# for item, text in enumerate(text):
#     print("|{:^5}|{:<15}".format(item, text.set_limit_text(35)))

''' Власні винятки '''
# class MyException(Exception):
#     def __init__(self, x):
#         self.x = x


# def foo(number):
#     if number < 0:
#         raise MyException(f'Value is equal {number} and lower then 0')
#     else:
#         return "Hello world!"

# try:
#     print(foo(-100))
# except MyException as e:
#     print(e)

# print(foo(-34))

#####

# class LaptopNameError(Exception):...


# class Laptop:
#     def __init__(self, name: str) -> None:
#         if len(name) < 2:
#             raise LaptopNameError("Name must be grater then 1 symbols")
#         self.name = name

# try:
#     lp1 = Laptop("H")
# except LaptopNameError as e:
#     print(e)

#####
# from collections import UserDict, UserList


# class Phones(UserList):
#     def set_phone(self, phone):
#         if len(phone) == 12:
#             new_phone = '+' + phone
#         elif len(phone) < 12:
#             new_phone = '+38' + phone
#         self.data.append(new_phone)
        
#     def get_phones(self):
#         return self.data
   
# отримуємо словник за номерами телефонів {'name: ім'я', 'phones': [phone, phone, phone]} 
# class User(UserDict):
#     def set_name(self, name):
#         self.data['name'] = name
        
#     def get_name(self):
#         return self.data.get('name')
    
#     def set_phone(self, phone):
#         phone_list = self.data.get('phones', Phones())
#         phone_list.data.append(phone)
#         self.data['phones'] = phone_list
        
#     def get_phone(self):
#         return self.data.get('phones')

# user_1 = User()
# user_1.set_name('Bill')
# user_1.set_phone('0989008080')
# user_1.set_phone('380938009090')
# print(user_1.get_name(), user_1.get_phone())

""" Качина типізація
Неявна типізація, латентна типізація або качина типізація (англ. Duck typing) в ООП мовах - визначення факту реалізації певного інтерфейсу об'єктом без явної вказівки або наслідування цього інтерфейсу, а просто реалізації повного набору методів.
"""

# class Dog:
#     def speak(self):
#         return 'Woof'

# class Cat:
#     def speak(self):
#         return 'Meow'

# class Duck:
#     def speak(self):
#         return 'Quack'

# def animal(animal):
#     return animal.speak()

# dog = Dog()
# cat = Cat()
# duck = Duck()

# print(animal(dog))
# print(animal(cat))
# print(animal(duck))

#####

# class Duck:
#     def swim_quack(self):
#         print("I'm duck, and I can swim and quack")

# class RobotDuck:
#     def swim_quack(self):
#         print("I'm robot duck, and I can swim and quack")

# class Fish:
#     def swim(self):
#         print("I'm a fish, and I can swim but can't quack")


# def animal(animal):
#     return animal.swim_quack()

# animal(Duck())
# animal(RobotDuck())
# animal(Fish())

#####

# class Laptop:
#     def __init__(self) -> None:
#         self.color = "Black"

#     def get_color(self) -> str:
#         return self.color


# class Bird:
#     def __init__(self) -> None:
#         self.color = "Brown"
        
#     def get_color(self) -> str:
#         return self.color


# lp = Laptop()
# bird = Bird()

# for i in (lp, bird):
#     print(i.get_color())