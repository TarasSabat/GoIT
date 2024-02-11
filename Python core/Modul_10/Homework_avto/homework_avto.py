'''№1
Створіть клас Animal. Також створіть екземпляр класу Animal (замість реалізації класу можете використовувати pass) і привласніть змінній animal.
'''
# class Animal:
#     pass

# animal = Animal()

'''№2
Створіть клас Animal. Також створіть екземпляр класу Animal та привласніть змінній animal. Для класу Animal у конструкторі створіть дві властивості: nickname - кличка тварини та weight - вага тварини. Реалізуйте також метод класу say. При реалізації методу можна використати оператор pass, поки що головне - це визначення, а не конкретна реалізація.
'''
# class Animal:
#     def __init__(self, nickname=None, weight=None) -> None:
#         self.nickname = nickname
#         self.weight = weight
    
#     def say(self):
#         pass
  
# animal = Animal()

'''№3
Для попереднього завдання реалізуйте в класі Animal метод change_weight, який має змінювати вагу тварини.
Викличте функцію change_weight(12) для об'єкта animal та змініть значення початкової ваги з 10 на 12 одиниць.
'''
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass
    
#     def change_weight(self, weight):
#         self.weight = weight
        

# animal = Animal("Simon", 10)
# animal.change_weight(12)

'''№4
Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', і метод change_color, який повинен змінювати значення змінної класу color.
Створіть екземпляри об'єкта: first_animal та second_animal
Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal та змініть значення змінної класу color на "red".
'''
# class Animal:
#     color = "white"

#     def __init__(self, nickname=None, weight=None):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight
        
#     def change_color(self, color):
#         self.color = color
#         Animal.color = self.color
        
# first_animal = Animal()
# second_animal = Animal()

# first_animal.change_color('red')

'''№5
Створіть клас Cat, батьківським класом якого є клас Animal. У класі Cat виконайте перевизначення методу say, щоб він повертав рядок "Meow" для екземплярів класу Cat.
Фактично ми виконуємо при цьому поліморфізм. Поліморфізм - це здатність програми вибирати різні реалізації при виклику операцій з однією і тією ж назвою. Тобто при виклику методу say в екземпляра класу Cat викликається нова реалізація, а не успадкована від класу Animal
Створіть також змінну cat, яка буде екземпляром класу Cat. При створенні змінної cat ім'я кота має бути "Simon", а вага - 10 одиниць.
'''
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Cat(Animal):
#     def say(self):
#         return "Meow"
        
# cat = Cat('Simon', 10)
# cat.say()

'''№6
Створіть клас Dog, батьківським класом якого є клас Animal. У класі Dog виконайте перевизначення методу say, щоб він повертав рядок "Woof" для екземплярів класу Dog.
У конструкторі класу Dog введіть нову властивість breed - порода, при цьому повинні залишитись всі властивості, успадковані від класу Animal.
Створіть у коді наступний екземпляр класу Dog.
dog = Dog("Barbos", 23, "labrador")
'''
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed
#     def say(self):
#         return "Woof"
    
# dog = Dog("Barbos", 23, "labrador")

# print(dog.say)
# print(dog.nickname)
# print(dog.weight)

'''№7
Для минулого завдання додамо клас Owner — власника собаки. У класу є три атрибути: ім'я — name, вік — age та адреса — address. Також необхідно реалізувати метод info, який повертає словник з ключами 'name', 'age' і 'address', та значення яких дорівнюють відповідним властивостям екземпляра класу.
Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner. Додати до класу Dog метод who_is_owner, який повертає результат виклику методу info екземпляра класу Owner, тобто це словник з ключами name, age та address власника.
'''
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def info(self):
#             return {'name': self.name, 'age': self.age, 'addres': self.address}

# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)
    
#     def say(self):
#         return "Woof"
    
#     def who_is_owner(self):
#         return self.owner.info()
             

# owner = Owner('Bill', '20', 'Lviv')   

'''№8
 Створіть два класи: CatDog та DogCat. Ці класи повинні наслідуватись від двох класів відразу: Cat та Dog. Після успадкування в екземпляра класу CatDog, батьківський метод say повинен повертати "Meow", а у класу DogCat — "Woof". Для обох зазначених класів реалізуйте метод info, який повертає рядок у наступному форматі f"{self.nickname}-{self.weight}".
 ''' 
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

# class Cat(Animal):
#     def say(self):
#         return "Meow"

# class Dog(Animal):
#     def say(self):
#         return "Woof"

# class CatDog(Cat, Dog):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"
        
# class DogCat(Dog, Cat): 
#     def info(self):
#         return f"{self.nickname}-{self.weight}"
    
'''№9
У четвертому модулі ми реалізували функцію lookup_key для пошуку всіх ключів за значенням у словнику. Першим параметром у функцію ми передавали словник, а другим – значення, яке хотіли знайти. Результатом був список ключів або порожній список, якщо ми нічого не знаходили.
def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Створіть клас LookUpKeyDict, батьком якого буде клас UserDict. Зробіть функцію lookup_key методом класу LookUpKeyDict.
'''
# from collections import UserDict


# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         keys = []
#         for key in self.data:
#             if self.data[key] == value:
#                 keys.append(key)
#         return keys
        
'''№10
Перепишемо завдання розрахунку заборгованостей з комунальних послуг за допомогою класу UserList.

payment = [1, -3, 4]
def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг наприкінці місяця, список payment. Заборгованості можуть бути від'ємними — у нас переплата, або додатними, якщо потрібно сплатити за рахунками.
Створіть клас AmountPaymentList, успадковуйте його від класу UserList. Зробіть функцію amount_payment методом класу AmountPaymentList.
'''      
# from collections import UserList


# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         result_1 = list(filter(lambda x: x > 0, self.data))
#         return sum(map(lambda x: int(x), result_1))

'''№11
Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.
'''
# from collections import UserString


# class NumberString(UserString):
#     def number_count(self):
#         digit_count = 0
#         for char in self.data:
#             if char.isdigit():
#                 digit_count += 1
#         return digit_count

'''№12
Створіть клас IDException, який успадковуватиме клас Exception.
Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.
Функція add_id буде викликати власне виключення IDException, якщо employee_id не починається з '01', інакше employee_id буде додано до списку id_list.
'''
# class IDException(Exception):
#     def __init__(self, message="Invalid employee ID"):
#         self.message = message
#         super().__init__(self.message)

# def add_id(id_list, employee_id):
#     if not employee_id.startswith('01'):
#         raise IDException("Employee ID must start with '01'")
#     id_list.append(employee_id)
#     return id_list

'''№13
Як ми вже говорили, поліморфізм - це здатність програми вибирати різні реалізації при виклику операцій з однією і тією ж назвою.
Але поліморфізм - це також здатність об'єктів прикидатись чимось іншим. У наведеному вище прикладі Chupakabra прикидалася собакою та кішкою.
Для коду із завдання вам необхідно реалізувати клас CatDog, не використовуючи успадкування від класу Animal, але щоб екземпляр класу CatDog поводився як і, як екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.
'''
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Cat(Animal):
#     def say(self):
#         return "Meow"

# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#         self.cat_dog = Cat(nickname, weight)
        
#     def say(self):
#         return self.cat_dog.say()
    
#     def change_weight(self, weight):
#         self.cat_dog.change_weight(weight)
        
'''№14
Реалізуйте клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.
list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts
Клас Contacts містить змінну класу current_id. Ми будемо використовувати її при додаванні нового контакту як унікального ідентифікатора контакту. Коли ми додаємо новий контакт, то передаємо такі аргументи в метод add_contacts: name, phone, email та favorite. Метод повинен створити словник із зазначеними ключами та значеннями параметрів функції. Також необхідно додати до словника новий ключ id, значенням якого є значення змінної класу current_id.
Приклад отриманого словника:

    {
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}
Вказаний словник ми додаємо до списку contacts. Не забуваймо збільшувати змінну current_id на одиницю після кожного виклику методу add_contacts для збереження унікальності ключа id для словника.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''
# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts
        

#     def add_contacts(self, name, phone, email, favorite):
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.favorite = favorite
#         self.contacts.append({"id": Contacts.current_id, 'name': self.name, 'phone': self.phone, 'email': self.email, "favorite": self.favorite})
#         Contacts.current_id += 1
        
# contacts = Contacts()

'''№15
Продовжуємо розширювати функціональність класу Contacts. На цьому етапі ми додамо до класу метод get_contact_by_id. Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''
# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

#     def get_contact_by_id(self, id):
#         for i in range(len(self.contacts)):
#             if id == self.contacts[i]['id']:
#                 return self.contacts[i]
            
# con = Contacts()
# con.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# print(con.get_contact_by_id(1))   

'''№16     
Завершуємо функціональність класу Contacts. На цьому етапі ми додамо до класу метод remove_contacts. Метод винен видаляти контакт по унікальному id у списку contacts. Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''
# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

#     def get_contact_by_id(self, id):
#         result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
#         return result[0] if len(result) > 0 else None

#     def remove_contacts(self, id):
#         result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
#         self.contacts.remove(result[0])
#         return self.contacts
    
# con = Contacts()
# con.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# con. remove_contacts(1)