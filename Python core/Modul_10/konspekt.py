''' Визначення та створення класу '''
''' Клас - це свого роду креслення або шаблон по якому будуть робитись реальні об'єкти (instanse він же ж  екзеспляр він же ж об'єкт)'''
# class User:
#     name = 'UserName'
#     age = 15

''' Створення об'єктів '''

# class User:
#     name = None             # атребути (поля, властивості, методи)
#     age = None               
#     phone = None 
    
#     def greeting(self):
#         return f'I am {self.name} my self {self}'
            
# user_1 = User()            # створюємо екземпляр класу User
# user_1.name = 'Taras'      # передаємо атрибуту name екземпляра user_1 значення Taras 
# user_1.age = 42            # передаємо атрибуту name екземпляра user_1 значення 42
# user_1.phone = 53521       # передаємо атрибуту name екземпляра user_1 значення 35321

# print(user_1.name, user_1.age, user_1.phone)   # Taras 42 53521 
# print(user_1.greeting())   # I am Taras my self <__main__.User object at 0x00000220C51D2C50>
# print(user_1)                                 # <__main__.User object at 0x00000220C51D2C50>

#####
# class User:
#     name = 'UserName'     # атребути (поля, властивості, методи)
#     age = 15              # атребути (поля, властивості, методи)

# user1 = User()            # екземпляр класу User
# print(user1.name)   # 'UserName'
# print(user1.age)    # '15'

# user2 = User()            # екземпляр класу User
# user2.name = "John"
# user2.age = 90

# print(user2.name)   # 'Jhon'
# print(user2.age)    # '90'


''' Атрибути класу (поля та методи) '''
# class User:
#     name = 'UserName'
#     age = 15

#     def say_name(self):
#         print(f'Hi! I am {self.name} and I am {self.age} years old.')

#     def set_age(self, age):
#         self.age = age


# bob = User()
# bob.name = 'Bob'

# bob.say_name()  # Hi! I am Bob and I am 15 years old.

# bob.set_age(25)
# bob.say_name()  # Hi! I am Bob and I am 25 years old.

### У цьому прикладі ми додали два методи класу User: say_name та set_age. say_name виводить у консоль рядок привітання від користувача. Для формування цього рядку використовуються поля name та age.

### Метод set_age приймає на вхід число та записує його в поле age.

# class Human:
#     name = ""

#     def hello(self, val):
#         if self.name:
#             return f"Hello {val}! I am {self.name}."
#         return f"Hello {val}!"

# bill = Human()
# print(bill.hello("John"))   # Hello John!

# bill.name = "Bill"
# print(bill.hello("John"))   # Hello John! I am Bill.

''' Конструктор класу '''
''' Інкапсуляція - це здатність об'єктів приховувати частину свого стану та поведінки від інших об'єктів, надаючи зовнішньому світу лише певний інтерфейс взаємодії із собою. '''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greeting(self):
#         return f"Hi {self.name}"


# p = Person("Boris", 34)
# print(p.name)  # Boris
# print(p.age)  # 34
# print(p.greeting())  # Hi Boris

''' Наслідування '''
'''Основна сила об'єктно-орієнтованого програмування полягає саме в можливості наслідування класів. Наслідування дає можливість створювати нові класи, що містять атрибути батьківських класів.'''
# class Person():
#     name = None
    
#     def greeting(self):
#         print(f'I am {self.name}')
        
# class Developer(Person):              # наслідується від Person (отримує атрибути)
#     def do_job(self):
#         print(f'I am writting code now...')

# class Manager(Person):
#     def manage(self):
#         print('Deadline is coming, hurry up!')
        
# class TeamLead(Developer, Manager):
#     def manage(self):                
#         print('I am tem lead')
#         return super().manage()       # доповнює функцію def manage класу Manager
    
               
# team_lead = TeamLead()
# team_lead.name = 'Bob'
# team_lead.greeting()            # I am Bob
# team_lead.do_job()              # I am writting code now...    
# team_lead.manage()              # Deadline is coming, hurry up!

# junior = Developer()
# junior.name = 'Taras'

# junior.greeting()           # I am Taras
# junior.do_job()             # I am writting code now...


#####
# class Human:
#     name = ''
#     def voice(self):
#         print(f"Hello! My name is {self.name}")


# class Developer(Human):
#     field_description = "My Programming language"
#     language = ""
#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"


# class PythonDeveloper(Developer):
#     value = "Python"


# class JSDeveloper(Developer):
#     value = "JavaScript"


# p_dev = PythonDeveloper()
# p_dev.name = 'Bob'
# p_dev.voice()   # Hello! My name is Bob
# p_dev.make_some_code()  # My Programming language is Python


# js_dev = JSDeveloper()
# js_dev.make_some_code()  # My Programming language is JavaScript

### У цьому прикладі ми створили батьківський клас Human, який визначив, що у всіх є ім'я та метод voice.

''' Method Resolution Order (MRO). '''
'''MRO у Python працює наступним чином:
1) Шукає атрибут серед атрибутів самого класу. Саме завдяки цьому ви можете "перевизначати" батьківські атрибути.
2) Шукає атрибут у першого з батьків (той, що вказаний першим у списку батьків).
3) Шукає атрибут у наступного батька у списку батьків, доки такі є.
4) Шукає атрибут у батьках першого батька.
5) Повторює п.4 для всіх батьків.
6) Викликає виняток, що атрибут не знайдено.
Пошуки закінчуються, як тільки атрибут знайдено.'''

# class A:
#     x = 'I am A class'

# class B:
#     x = 'I am B class'
#     y = 'I exist only in B'

# class C(A, B):
#     z = "This exists only in C"

# c = C()
# print(c.z)  # This exists only in C
# print(c.y)  # I exist only in B
# print(c.x)  # I am A class

### З цього прикладу видно, що у класі C поле x береться з A класу. Якщо ж в цьому самому прикладі змінити список батьків, то отримаємо:

# class A:
#     x = 'I am A class'

# class B:
#     x = 'I am B class'
#     y = 'I exist only in B'

# class C(B, A):
#     z = "This exists only in C"

# c = C()
# print(c.z)  # This exists only in C
# print(c.y)  # I exist only in B
# print(c.x)  # I am B class

### Тепер у класі C поле x береться з B класу.

#####
# class Foo:
#     field = "foo"
    

# class Baz:
#     field = "baz"
    

# class Bar(Baz, Foo):
#     pass


# bar = Bar()

# print(bar.field)  # baz

''' Контейнери, створені за допомогою наслідування (UserList, UserDict, UserString). '''
'''Правильний спосіб отримати модифікований контейнер — це використовувати пакет collections та класи UserList, UserDict, UserString, які в ньому є.
Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, що самі дані лежать у полі data у цих класів і ви можете використовувати це поле на свій розсуд.'''

# from collections import UserDict

# class ValueSearchableDict(UserDict):
#     def has_in_values(self, value):
#         return value in self.data.values()

# as_dict = ValueSearchableDict()
# as_dict['a'] = 1
# as_dict.has_in_values(1)    # True
# as_dict.has_in_values(2)    # False

### У цьому прикладі ми створили клас, який поводиться як словник, але в ньому є додатковий метод, який перевіряє наявність деякого value серед значень у цьому словнику.

# from collections import UserList

# class CountableList(UserList):
#     def sum(self):
#         return sum(map(lambda x: int(x), self.data))

# countable = CountableList([1, '2', 3, '4'])
# countable.append('5')
# countable.sum()     # 15

### У цьому прикладі ми створили клас, який поводиться як список, але в ньому є метод sum , який повертає суму всього вмісту цього класу, при цьому перетворюючи рядки на цілі числа.

# from collections import UserString

# class TruncatedString(UserString):
#     MAX_LEN = 7
#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]

# ts = TruncatedString('abcdefghjklmnop')
# ts.truncate()
# print(ts)   # abcdefg

### Останній приклад показує модифікований рядок з методом truncate, який обмежує розмір рядка до MAX_LEN символів.

''' Власні винятки '''
'''У Python широко використовується механізм винятків (Exceptions) для того, щоб дати зрозуміти коду, що викликає, що саме пішло не так і що з цим робити. На винятках також будують розгалуження коду, наприклад, ми очікуємо, що користувач введе саме число, але він може ввести що завгодно:'''

# def input_number():
#     while True:
#         try:
#             num = input("Enter integer number: ")
#             return int(num)
#         except:
#             print(f'"{num}" is not a number. Try again')

# num = input_number()

### У цьому прикладі функція input_number вийде з нескінченного циклу тільки, коли користувач введе ціле число. Це приклад використання винятків у Python з метою управління потоком виконання.

# import string

# class NameTooShortError(Exception):
#     pass

# class NameStartsFromLowError(Exception):
#     pass

# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError
#     if name[0] not in string.ascii_uppercase:
#         raise NameStartsFromLowError

# while True:
#     try:
#         name = enter_name()
#         break
#     except NameTooShortError:
#         print('Name is too short, need more than 3 symbols. Try again.')
#     except NameStartsFromLowError:
#         print('Name should start from capital letter. Try again.')

### У цьому прикладі ми створили власні винятки, наслідуючи батьківський клас для всіх винятків у Python — клас Exception. Далі у коді коректно обробили два випадки, коли користувач ввів занадто коротке ім'я, або коли ім'я починається не з великої літери.

''' Поліморфізм / Качина типізація '''
'''Качина типізація — це механізм властивий Python, який дозволяє використовувати будь-які об'єкти один замість іншого, аби в обох були потрібні методи та поля. Качиною ця типізація називається від приказки: "Якщо крякає як качка, плаває як качка і літає як качка, — це качка". '''

# class Mammal:
#     phrase = ''
#     def voice(self):
#         return self.phrase

# class Dog(Mammal):
#     phrase = 'Bark!'

# class Cat(Mammal):
#     phrase = 'Meow!'

# class Chupakabra:
#     def voice(self):
#         return 'Whooooo!!!'

# class Recorder:
#     def record_animal(self, animal):
#         voice = animal.voice()
#         print(f'Recorded "{voice}"')

# r = Recorder()
# cat = Cat()
# dog = Dog()
# strange_animal = Chupakabra()

# r.record_animal(cat)            # Recorded "Meow!"
# r.record_animal(dog)            # Recorded "Bark!"
# r.record_animal(strange_animal) # Recorded "Whooooo!!!"

### В цьому прикладі ми створили батьківський клас Mammal, у якого є метод voice та два дочірніх до нього Dog та Cat. Клас Record приймає на вхід методу record_animal об'єкт animalта викликає в нього метод voice, щоб вивести результати виконання voice у консоль. При цьому є клас Chupakabra, у якого також є метод voice, та хоч він і не наслідується від Mammal, але об'єкти цього класу так само можна передавати в record_animal. Головне, щоб атрибут називався так само і приймав ті самі аргументи (якщо це метод).


#################
'''Урок Борода'''
# class Character:
#     name = None         # дефолтні атребути (поля, властивості, методи)
#     x = None            # дефолтні атребути (поля, властивості, методи)
#     y = None            # дефолтні атребути (поля, властивості, методи)
#     hp = 100            # дефолтні атребути (поля, властивості, методи)
#     mp = 100            # дефолтні атребути (поля, властивості, методи)
                          # усе разом це класові характристики 
#     def move():
#         print('I am moving')

# char = Character()      # створення екземпляр класу Character
# char_1 = Character()    # створення екземпляр класу Character
# char_2 = Character()    # створення екземпляр класу Character

# print(char_1.hp)        # 100

# char_1.name = 'Taras'   # переприсвоєння імені для char_1
# print(char_1.name)      # Taras

# char_2.name = 'Gabriel' # переприсвоєння імені для char_2
# print(char_1.name)  

# Character.mp = 300      # зміна дефолтного значення атребуту (поля, властивості, методи) і це вплине на усі     об'єкти, якщо вони не були переприсвоєні як в прикладі з char_1.name = 'Taras' і char_2.name = 'Gabriel'
#####
# class Character:
#     name = None          
#     x = None            
#     y = None             
#     hp = 100           
#     mp = 100            

#     def move(self):              # метод классу приймає в якості першого аргумента екземпляр і тому аргумент прийнято називати self
#         print('I am moving')

#     def identify(self):          # метод классу приймає в якості першого аргумента екземпляр і тому аргумент прийнято називати self
#         print(self.name)

# робота з персонажами
# char_1 = Character('Alex', 0, 0)   # створення екземпляр класу Character
# char_2 = Character('Grek', 1, 1)   
# char_1.move()
# char_2.move()
# char_1.identify()
# char_2.identify()

'''Урок Борода. Конструктори (композиція та агрегація)'''
# class Character:
    
#     count = 0           
#     hp = 100           
#     mp = 100            

#     def __init__(self, name, x=0, y=0):        # задаємо конструктор класа і викликається при виклику класа, в конструктор можна передати аргументи
#         Character.count += 1  
#         self.left_hand = None # якщо = Weapon() тобто у персонажа замість руки меч і це буде називатись КОМПОЗИЦІЯ так як цикл життя об'єкта Weapon() нерозривно зв'язаний з циклом життя об'єкта Character()
#         self.right_hand = None
#         self.name = name
#         self.x = x
#         self.y = y
     
#     def pick_weapon(self, weapon):      # метод підіймання зброї
#         if self.left_hand is None:
#             self.left_hand = weapon
#         elif self.right_hand is None:
#             self.right_hand = weapon
#         else:
#             print('I am full')
#     def show_weapon(self):
#         return self.left_hand, self.right_hand
      
#     def die(self):          # створення новогої характеристики екземпляра яка не являється класовою
#         return self.left_hand, self.right_hand

# робота зі зброєю
# class Weapon:               # створення класу Weapon який не зв'язаний з класом class Character але взаємодіє з ним. Така комбінація називається АГРЕГАЦІЯ

#     def __init__(self):
#         self.type = 'sword'
#         self.damage = 10

# char = Character('char')   # Opening a chest
# sword_1 = Weapon()
# char.pick_weapon(sword_1)
 
# '''Урок Борода. Наслідування'''

# class Character:
    
#     count = 0           
#     hp = 100           
#     mp = 100            

#     def __init__(self, name, x=0, y=0):        # задаємо конструктор класа і викликається при виклику класа, в конструктор можна передати аргументи
#         Character.count += 1  
#         self.left_hand = None # якщо = Weapon() тобто у персонажа замість руки меч і це буде називатись КОМПОЗИЦІЯ так як цикл життя об'єкта Weapon() нерозривно зв'язаний з циклом життя об'єкта Character()
#         self.right_hand = None
#         self.name = name
#         self.x = x
#         self.y = y
     
#     def pick_weapon(self, weapon):      # метод підіймання зброї
#         if self.left_hand is None:
#             self.left_hand = weapon
#         elif self.right_hand is None:
#             self.right_hand = weapon
#         else:
#             print('I am full')
#     def show_weapon(self):
#         return self.left_hand, self.right_hand
      
#     def die(self):          # створення новогої характеристики екземпляра яка не являється класовою
#         return self.left_hand, self.right_hand

# клас зброї
# class Weapon:                

#     def __init__(self):
#         self.damage = 10

#     def kick_ass(self):
#         return self.damage

# class Knife(Weapon):  # Knife(Weapon) - синтаксис наслідування класом Knife методів класу Weapon, якщо вони не вказані  
#     def __init__(self):
#         self.damage = 5
    
#     def throw(self):
#         return self.damage - 2
        

# class Sword(Weapon):
#     def __init__(self):
#         self.damage = 15

# class Axe(Weapon):
#     def __init__(self):
#         self.damage = 20

# char = Character('char')   # Opening a chest
# sword_1 = Weapon()
# char.pick_weapon(sword_1)

'''Урок Борода. Поліморфізм. Качина типізація'''

# class Weapon:                

#     def __init__(self):
#         self.damage = 10

#     def kick_ass(self):
#         return self.damage

# class Knife(Weapon):   
#     def __init__(self):
#         self.damage = 5
    
#     def throw(self):
#         return self.damage - 2
    
#     def kick_ass(self):             # поліморфізм - при одинаковому методу будуть різні способи реалізації методу
#         print('Chik-chik') # качина типізація - образно, якщо об'єкт має метод kick_ass то це зброя (клас Weapon) якщо ні
#         return self.damage
        

# class Sword(Weapon):
#     def __init__(self):
#         self.damage = 15
    
#     def kick_ass(self):             # поліморфізм - при одинаковому методу будуть різні способи реалізації методу
#         print('Slash-slash')# качина типізація - образно, якщо об'єкт має метод kick_ass то це зброя (клас Weapon) якщо ні значить ні
#         return self.damage

# class Axe(Weapon):
#     def __init__(self):
#         self.damage = 20
    
#     def kick_ass(self):             # поліморфізм - при одинаковому методу будуть різні способи реалізації методу
#         print('Herak')     # качина типізація - образно, якщо об'єкт має метод kick_ass то це зброя (клас Weapon) якщо ні
#         return self.damage

# class Gun(Weapon):
#     def __init__(self):
#         self.damage = 50
    
#     def kick_ass(self):             # поліморфізм - при одинаковому методу будуть різні способи реалізації методу
#         print('Baaam')     # качина типізація - образно, якщо об'єкт має метод kick_ass то це зброя (клас Weapon) якщо ні
#         return self.damage

''' Функця super 
надає можливість посилатись на батьківський клас '''

# class A():
#     def __init__(self) -> None:
#         print('Hello, I am A')
        
# class B(A):
#     def __init__(self) -> None:
#         super().__init__()   # в дужках після функції super можна вкзати який батьківський клас ми викликаємо
#         print('Hello I am B')
        
# b = B()   # Hello, I am A; Hello I am B

#####

# class Motherboard:
#     def __init__(self, brand: str) -> None:
#         self.brand = brand


# class Laptop(Motherboard):
#     def __init__(self, brand: str, ram_size: int) -> None:
#         super().__init__(brand)
#         self.ram = ram_size


# lp = Laptop("Dell", 32)