''' Створення власних менеджерів контексту '''
'''Написати Contex Manager FileReader, який пише в лог timestamp коли файл був відкритий, timestamp, коли файл був закритий, ім'я файлу, і як довго файл був відкритий з точністю до секунд.'''
# from datetime import datetime
# from time import sleep

# class FileReader:
#     log = ''
#     instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super(FileReader, cls).__new__(cls)  # cls - екземпляр класу
#         return cls.instance

#     def __init__(self, filename):
#         self.file = None
#         self.opened = False
#         self.filename = filename
#         self.timestamp = None

#     def __enter__(self):
#         self.file = open(self.filename, 'r')
#         self.opened = True
#         self.timestamp = datetime.now().timestamp()
#         message = '{:<20}|{:^15}| open \n'.format(self.timestamp, self.filename)
#         self.log += message
#         return self.file

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.opened:
#             self.file.close()
#         timestamp_closed = datetime.now().timestamp()
#         diff = timestamp_closed - self.timestamp
#         message = '{:<20}|{:^15}| closed {:>15}s \n'.format(timestamp_closed, self.filename, diff)
#         self.log += message
#         self.opened = False

# reader = FileReader('test.txt')
# with reader as file:
#     sleep(2)
#     print(file.read())

# reader = FileReader('ex_1.py')
# with reader as file:
#     sleep(1)
#     print(file.read())

# print(reader.log)

'''Сховище з паролем'''
# class KeyStore:
#     def __init__(self, name, password):
#         self.__password = None
#         self.__name = None
#         self.__secret = None
#         self.name = name
#         self.password = password

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name

#     @property
#     def password(self):
#         return 'No way to get password'

#     @password.setter
#     def password(self, value):
#         if self.__password is None:
#             self.__password = value
#         elif self.is_valid():
#             self.__password = value

#     @property
#     def secret(self):
#         if self.is_valid():
#             return self.__secret

#     @secret.setter
#     def secret(self, value):
#         if self.is_valid():
#             self.__secret = value

#     def is_valid(self):
#         old = input('Please enter the password: ')
#         if self.__password == old:
#             print("Okay")
#             return True
#         print('Wrong password')
#         return False


# k_store = KeyStore('Ivan', '123456')
# print(k_store.password)
# print(k_store.name)
# k_store.name = 'Olga'
# print(k_store.name)
# k_store.password = '56789'
# print(k_store.password)
# k_store.secret = 'Hello world'
# print(k_store.secret)

'''Напишіть клас Adder, який має метод add, який генерує виключення NotImplemented.
Потім визначте два підкласи, які реалізують метод додавання:
а) ListAdder з методом додавання, який повертає конкатенацію двох своїх аргументів списку
б) DictAdder з методом додавання, який повертає новий словник з елементами як у два його словникові аргументи
(Підійде будь-яке визначення додавання)'''
# class Adder:
#     def __add__(self, other):
#         raise NotImplemented


# class ListAdder(Adder):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value  # return [*self.value, *other.value]

# class DictAdder(Adder):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return {**self.value, **other.value}


# la1 = ListAdder([1, 2])
# la2 = ListAdder([3, 4])
# print(la1 + la2)

# da1 = DictAdder({'Volodymyr': 15, 'Olga': 25})
# da2 = DictAdder({'Roman': 3, 'Oxana': 11})
# print(da1 + da2)

# # {'Volodymyr': 15, 'Olga': 25, 'Roman': 3, 'Oxana': 11}

'''Логічні операції (__eq__, __ne__, __lt__, __gt__, __le__, __ge__)'''
# class Car:
#     store_name = 'GoIT store'

#     def __init__(self, year, mark, model, color, price):
#         self.year = year
#         self.mark = mark
#         self.model = model
#         self.color = color
#         self.price = price

#     def __str__(self):
#         return (f'{self.store_name}: {self.mark} -> {self.model}, {self.price}')

#     def __eq__(self, other):
#         return self.price == other.price

#     def __ne__(self, other):
#         return self.price != other.price

#     def __lt__(self, other):
#         return self.price < other.price

#     def __gt__(self, other):
#         return self.price > other.price

#     def __le__(self, other):
#         return self.price <= other.price

#     def __ge__(self, other):
#         return self.price >= other.price


# car_w = Car(2019, 'BMW', 'X5', 'Black', 21000)
# car_b = Car(2022, 'Toyota', 'Camry', 'White', 28000)

# print(car_w == car_b)
# print(car_w != car_b)
# print(car_w < car_b)
# print(car_w > car_b)
# print(car_w <= car_b)
# print(car_w >= car_b)

