'''Списки. 
Для створення порожнього списку існує два способи:'''

# my_list = list()

# empty_list = []

'''Щоб створити заповнений список:'''

# not_empty = [1, 2, 'user']
'''Приклад'''
# cars = ['VW', 'Tesla', 'BMV', 'Toyota']
# numbers = [1, 2, 56, 6]
# a = ['Hello', 55, True, True, False, 55, None, 6.11, 'n', 4.5j]
# print(cars)
# print(numbers)
# print(a)

# Перетворення в колекцію

# s = list('My string')    # на виході ['M', 'y', ' ', 's', 't', 'r', 'i', 'n', 'g']
# print(s)

'''Щоб звернутися до елемента у списку, вкажіть ім'я списку за яким слідує індекс елемента у квадратних дужках.'''
# persons = ['Jane', 'Steve', 'Moris']
# print(persons[1])  # Steve

'''Змінити значення конкретного елемента списку можна за допомогою звичайного оператора присвоєння. 
При цьому ліворуч від нього має стояти ім'я змінної, у якій зберігається список, з індексом потрібного 
елемента у квадратних дужках, а праворуч – нове значення.'''

# persons = ['Jane', 'Steve', 'Moris']
# persons[1] = 'Niv'
# print(persons)  # ['Jane', 'Niv', 'Moris']

'''Інструкція for дозволяє проходити по елементах списку, як і з будь-якою колекцією.
Функції можуть повертати списки. Як і значення інших типів, списки з функцій повертаються за допомогою 
ключового слова return.'''

# data = [4, 3, 7.5]
# sum = 0
# for value in data:
#     sum = sum + value
# print(sum)  # 14.5


'''Впорядковані контейнери. Доступ за індексом.
У Python синтаксис доступу за індексом виглядає так:
У першому рядку ми створили список з трьох перших літер англійського алфавіту.
У другому рядку ми зберегли у змінну first_letter літеру "a" — перший елемент some_iterable. 
Індекс у Python починається з 0, як і в більшості мов програмування, та індексом "a" є 0.
Третій рядок — це звернення до другого елементу some_iterable, його індекс дорівнює 1 — це літера "b" 
і ми зберігаємо її у middle_one. Четвертий рядок — це звернення до останнього елементу some_iterable, 
літери "c", ми збережемо її у last_letter і її індекс дорівнює 2.'''

# some_iterable = ["a", "b", "c"]
# first_letter = some_iterable[0]
# middle_one = some_iterable[1]
# last_letter = some_iterable[2]

'''Python підтримує індексування елементів з кінця. Для цього потрібно додати - і вказати номер елементу 
з кінця. Оскільки у Python -0 == 0, то перший елемент з кінця — це -1, другий — -2 і так далі.
Наш приклад можна переписати, використовуючи індексування з кінця, ось так:'''

# some_iterable = ["a", "b", "c"]
# first_letter = some_iterable[-3]
# middle_one = some_iterable[-2]
# last_letter = some_iterable[-1]

'''Найкориснішою властивістю списків є змінність списків, ви можете змінити значення будь-якого 
елементу списку:
В цьому прикладі ми змінили другий елемент списку some_iterable (другий елемент — це елемент з індексом 1) 
на 'Z'.'''

# some_iterable = ["a", "b", "c"]
# some_iterable[1] = "Z"
# print(some_iterable)    # ["a", "Z", "c"]

'''Зрізи у Python (Slice)
Для впорядкованих контейнерів є спеціальний синтаксис, коли нам необхідно отримати деяку послідовність 
елементів з контейнера. Наприклад, якщо ми хочемо отримати перші 5 літер рядку:
Синтаксис полягає у зазначенні індексу першого елементу зрізу, індексу, до якого (не включно) брати елементи 
в нову послідовність, та кроку, з яким брати елементи між початковим та кінцевим індексом у квадратних дужках, 
розділивши їх двокрапкою.'''

# some_str = "This is awesome string"
# first_five = some_str[0:5]       #first_five в цьому прикладі буде містити рядок 'This '.

'''Візьмімо список чисел від 1 до 10 і збережемо окремо парні, не парні та кратні 3.
У odd_numbers ми беремо числа, починаючи з індексу 0 до 10 з кроком 2 (отримаємо [1, 3, 5, 7, 9]). 
У even_numbers ми беремо числа, починаючи з індексу 1 до 10 з кроком 2 (отримаємо [2, 4, 6, 8]) 
У three_numbers ми беремо числа, починаючи з індексу 2 до 10 з кроком 3 (отримаємо [3, 6, 9]).'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# odd_numbers = numbers[0:9:2]
# even_numbers = numbers[1:9:2]
# three_numbers = numbers[2:9:3]

'''Ви можете не вказувати початковий, кінцевий індекс або крок, пропускаючи його. За замовчуванням Python 
візьме зріз з початку до останнього елемента з кроком 1. Перепишемо попередній приклад у скороченому синтаксисі:
numbers_copy в цьому прикладі — це зріз, який бере всі елементи numbers від початку і до кінця з кроком 1.'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# odd_numbers = numbers[::2]
# even_numbers = numbers[1::2]
# three_numbers = numbers[2:9:3]

# numbers_copy = numbers[:]

'''Також важливо пам'ятати, що в зріз не входить елемент з індексом, до якого брати елементи.
В цьому прикладі елемент з індексом 3 не увійде у first_three.'''

# numbers = [0, 1, 2, 3]
# first_three = numbers[0:3]  # [0, 1, 2]

'''Отримати список `numbers` у зворотному порядку допоможе'''
# numbers[::-1]

'''Використання методів об'єктів
Доступ до методів об'єктів у Python синтаксично відбувається за допомогою символу крапки після імені об'єкту 
і зазначення імені методу або атрибуту, до якого потрібно отримати доступ.
В цьому прикладі ми використали метод append, який є у списків і він є у списку numbers. Цей метод додає новий
 елемент в кінець списку. Як аргумент цей метод отримує елемент, який потрібно додати до списку. 
 Аргументи вказуються в дужках.'''

# numbers = ['a', 'b']
# numbers.append('c')
# print(numbers)  # ['a', 'b', 'c']

'''Якщо метод не вимагає аргументів (наприклад метод clear), то дужки будуть порожніми:'''

# num = [1, 2]
# num.clear()
# print(num)  # []

'''МЕТОДИ СПИСКІВ'''
'''Додавання елементу в кінець списку: my_list.append(element)'''

# chars = ['a', 'b']
# chars.append('c')
# print(chars)  # ['a', 'b', 'c']

###

# num = [1, 3.1415, 41, 3]
# num.append(30)
# print(num)  # [1, 3.1415, 41, 3, 30]

'''Видалення елементу зі списку викличе помилку, якщо такого елементу немає в списку: my_list.remove(element)'''

# chars = ['a', 'b']
# chars.remove('b')
# print(chars)  # ['a']

###

# num = [1, 3.1415, 41, 3]
# num.remove(3.1415)
# print(num)  # [1, 41, 3]

'''Повернути i-ий елемент та видалити його зі списку i_element = my_list.pop(i). 
За замовчуванням i = -1'''

# chars = ['a', 'b']
# last = chars.pop(1)
# print(chars)  # ['a']
# print(last)  # 'b'

###

# num = [1, 3.1415, 41, 3]
# second = num.pop(1)
# print(second)  # 3.1415
# print(num)  # [1, 41, 3]

'''Розширити список a_list елементами з b_list: a_list.extend(b_list)'''

# chars = ['a', 'b']
# numbers = [1, 2]

# chars.extend(numbers)
# print(chars)  # ['a', 'b', 1, 2]

'''Вставити x на позицію з індексом i: my_list.insert(i, x)'''

# chars = ["a", "b"]
# chars.insert(1, "c")
# print(chars)  # ['a', 'c', 'b']

###

# num = [1, 3.1415, 41, 3]
# num.insert(2, 30)
# print(num)  # [1, 3.1415, 30, 41, 3]

'''Очистити список: my_list.clear()'''

# chars = ['a', 'b']
# last =  chars.clear() 
# print(chars) # []

'''Знайти індекс першого елемента у списку, що дорівнює x: index = my_list.index(x)'''

# chars = ['a', 'b', 'c', 'd']
# c_ind = chars.index('c') 
# print(c_ind) #2

'''Повернути кількість елементів у списку, що дорівнюють x: x_number = my_list.count(x)'''

# chars = ['a', 'b', 'c', 'a']
# a_count = chars.count('a')
# print(a_count) # 2

'''Відсортувати список за зростанням: my_list.sort(key=None, reverse=False)
my_list.sorted - отримуємо новий відсортований список не змінюючи старий'''

# chars = ['z', 'a', 'b']
# chars.sort()
# print(chars) # ['a', 'b', 'z']

###

# num = [1, 3.1415, 41, 3]
# new_num = sorted(num)
# print(new_num)  # [1, 3, 3.1415, 41]
# print(num)  # [1, 3.1415, 41, 3]

'''Змінити порядок елементів у списку на зворотний: my_list.reverse()'''

# chars = ['a', 'b']
# chars.reverse()
# print(chars) # ['b', 'a']

'''Повернути копію списку: copy_of_my_list = my_list.copy()'''

# chars =  ['a', 'b']
# chars_copy = chars.copy()
# chars == chars_copy # True

'''МЕТОДИ СЛОВНИКІВ'''
'''Деякі методи словників, що найчастіше використовуються:'''

'''pop(key) — повертає значення елементу і видаляє пару ключ-значення зі словника'''

# chars = {'a': 1, 'b': 2}
# b_num = chars.pop('b')
# print(chars)  # {'a': 1}
# print(b_num)  # 2

'''update(another_dict) — розширює словник значеннями з іншого словника'''

# chars = {'a': 1, 'b': 2}
# chars.update({"c": 3})
# print(chars)  # {'a': 1, 'b': 2, "c": 3}

'''clear() — очищає словник, не створюючи нового'''

# chars = {'a': 1, 'b': 2}
# chars.clear()
# print(chars)  # {}

'''copy() — повертає копію словника'''

# chars = {'a': 1, 'b': 2}
# chars_copy = chars.copy()
# chars_copy == chars  # True

'''get(key[, default]) — не викликає виключення, якщо ключа немає в словнику, повертає default, 
за замовчуванням default=None.'''

# chars = {'a': 1, 'b': 2}
# c_idx = chars.get('c', -1)
# print(c_idx)  # -1

'''ЦИКЛ ТА СЛОВНИКИ'''
'''Ітерування за словником — це блок коду, що дуже часто зустрічається, і корисно вміти це робити.
Спершу варто сказати, що словник сам по собі — це ітерований контейнер і за ним можна ітеруватися 
в циклі for без необхідності заводити якийсь зовнішній лічильник тощо. Створимо словник, в якому ключами 
будуть числа, а значеннями — числівники англійською:'''

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

'''Тепер давайте просто пройдемо словником в циклі та виведемо, що нам повертає ітератор на кожній ітерації:'''

# for key in numbers:
#     print(key)

'''У виведенні ви побачите:'''

# 1
# 2
# 3

'''Ітеруючи за словником, ви перебираєте ключі словника. Таку саму поведінку можна отримати, 
використовуючи метод keys, але так ви явно вкажете, що хочете перебрати ключі:'''

# for key in numbers.keys():
#     print(key)

'''Відповідь буде точно такою самою:'''

# 1
# 2
# 3

'''Часто необхідно перебрати саме значення словника, для цього скористаємося методом values:'''

# for val in numbers.values():
#     print(val)

'''У виведенні буде:'''

# one
# two
# tree

'''І переберемо пари ключ значення, використовуючи метод items. На кожній ітерації ми отримаємо пару 
(ключ, значення):'''

# for key, value in numbers.items():
#     print(key, value)

'''Виведення:'''

# 1 one
# 2 two
# 3 three

'''Що не можна робити, поки ітеруєтеся за словником: не можна видаляти елементи із словника, 
не можна додавати елементи у словник. Але можна перезаписувати значення, якщо ви ітеруєтеся за ключами.'''

### Перевірка скільки разів символ входить в строку та поміщення результату в словник 

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# dict_counter = {} # {'L':1, 'o':2}
# for char in text:
#     try:            # видає помилку так як при першому входженні словник порожній
#         count = dict_counter[char]  # отримаємо значення по ключу
#     except KeyError:
#         count = 0
#     count +=1
#     dict_counter[char] = count  # записуємо значення по ключу

# print(dict_counter)

### Спосіб прописаний вище можна спростити з використанням методу get

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# dict_counter = {} # {'L':1, 'o':2}
# for char in text:
#     count = dict_counter.get(char, 0) 
#     count +=1
#     dict_counter[char] = count  # записуємо значення по ключу

# print(dict_counter)


'''МНОЖИНИ'''
'''Множини — це неврегульований контейнер, який містить тільки унікальні елементи. У множину можна додавати 
тільки незмінні типи даних.
Є тільки один спосіб створити порожню множину:'''

# a = set()
# print(a)    # set()

'''Для створення заповненої множини достатньо передати будь-який об'єкт, що ітерується, в функцію set:'''

# a = set('hello')
# print(a)    # {'e', 'h', 'l', 'o'}

'''Або ж скористатися синтаксисом з фігурними дужками (як у словниках), але елементи у фігурних дужках 
просто перелічити через кому без двокрапок:'''

# b = {1, 2, 3, 4}

'''Унікальність має на увазі, що якщо множина вже містить такий елемент, то спроба додати ще один такий 
самий нічого не змінить.'''

# numbers = {1, 2, 3, 1, 2, 3}
# print(numbers)    # {1, 2, 3}

'''Математичні операції над множинами
Давайте детальніше розглянемо, які корисні математичні операції можна робити над множинами. 
Спершу створимо множини a та b:'''

# a = set('hello')
# print(a)    # {'e', 'h', 'l', 'o'}

# b = set('hi there!')
# print(b)    # {'r', ' ', 'i', 'e', '!', 'h', 't'}

'''Щоб знайти загальні елементи для двох множин, виконаємо над ними операцію & (AND):'''

# a & b   # {'e', 'h'}

'''Знайдемо усі елементи з двох множин, окрім загальних, за допомогою оператора ^ (XOR):'''

# a ^ b   # {' ', '!', 'i', 'l', 'o', 'r', 't'}

'''Об'єднання множин, або просто усі елементи з обох множин знаходяться за допомогою оператора | (OR):'''

# a | b   # {' ', '!', 'e', 'h', 'i', 'l', 'o', 'r', 't'}

### Відокремимо елементи англійського алфавіту за допомогою множини

# text = "The best employees of a month get a special bonus: they can have an extra day off once a week during the following month. Also, you can take a day off if you work overtime. Actually, you don't have to work overtime, but if you do, you can either get money for it or an extra day off work."

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# char_set = set()
# symdol_set = set()

# for el in text:
#     if el.lower() in alphabet:
#         char_set.add(el)
#     else:
#         symdol_set.add(el)

# print(f'Chars {char_set}')
# print(f'Symbols {symdol_set}')


'''РЯДКИ'''
'''Для того щоб створити змінну типу "рядок", необхідно певний набір символів взяти в лапки.
Варіант 1. Одинарні лапки (апостроф) 'some text'
Варіант 2. Подвійні лапки "some text".
Різні варіанти використання лапок обумовлені тим, що при використанні одинарних лапок, можна в рядку вказати 
подвійні і навпаки.'''

# game_string = 'My "Game"'

'''Впорядкована послідовність означає, що до елементів рядку можна звертатися за індексом:'''

# s = "Hello world!"
# print(s[0])   # H
# print(s[-1])  # !

'''Незмінна послідовність означає, що якщо рядок вже створений, то змінити його не можна, можна тільки 
створити новий.'''

# s = "Hello world!"
# s[0] = "Q" # Тут буде викликано виняток (помилка) TypeError

'''Малі методи
Для того, щоб усі літери рядка перевести у верхній регістр, використовується метод upper:'''

# s = "Hello"
# s.upper()
# print(s)    # Виведе 'HELLO'

'''Для переведення в нижній регістр використовується метод lower():'''

# s = "Some Text"
# print(s.lower())    # Виведе 'some text'

'''Щоб перевірити, що рядок починається з підрядка, є метод startswith:'''

# s = "Bill Jons"
# print(s.startswith("Bi"))   # Виведе True

'''Щоб перевірити, що рядок закінчується підрядком, використовується метод endswith:'''

# s = "hello.jpg"
# print(s.endswith("jpg"))    # Виведе True

'''Цей метод зручно використовувати для перевірки розширення файлів.'''

'''Метод для розбивання строки на слова зі знаком пробіл і отримання списку слів - text.split()'''

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# worlds = text.split()
# print(worlds)   # ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 
                                                                          #'typesetting', 'industry.']
### Ітерація строки та виведення поелементного (політерах) списку строки

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# for char in text:
#     print(char) #L o r e m  I p s u m  i s  s i m p l y  d u m m y  t e x t  o f  t h e  p r i n t i n g  a n d  t y p e s e t t i n g  i n d u s t r y .

### Ітерація строки та виведення поелементного (політерах) списку строки з індексами

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# for index, char in enumerate(text):
#     print(index, char)

### Ітерація строки та здійснення перевірки чи є символ літерою алфавіту (тільки малі літери)

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# for index, char in enumerate(text):
#     if char in alphabets:
#         print(index, char)

### Ітерація строки та здійснення перевірки чи є символ літерою алфавіту (малі і великі літери)

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# for index, char in enumerate(text):
#     if char.lower() in alphabets:
#         print(index, char)

# ## Ітерація строки, здійснення перевірки, та виведення символі які не є літерою алфавіту

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# for index, char in enumerate(text):
#     if not char.lower() in alphabets:
#         print(index, char)

## Ітерація строки, відокремлення слів в строці 

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# words = []
# start = 0
# for index, char in enumerate(text):
#     if not char.lower() in alphabets:
#         word = text[start:index]
#         words.append(word.strip())  # очищення від пробілів
#         start = index
# print(words)

'''Перевірка на входження
Будь-яка колекція дозволяє перевірити, чи містить колекція цей елемент (чи є там такий самий). 
Для цього використовується оператор in.
Наприклад, перевірка на те, що користувач не використовує простий пароль і в паролі не зустрічається 
послідовність "qwerty" або "123":'''

# password = "qwerty123"
# if "qwerty" in password or "123" in password:
#     print("This password is too weak!")

'''Оператор in перевіряє наявність елементу ('qwerty', '123') у контейнері (password) 
та повертає True або False.'''

# prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# is_prime = 3 in prime_numbers

'''Перевірка на те, що число 3 присутнє у множині перших дев'яти простих чисел prime_numbers.
Із словниками перевірка на входження перевіряє, що елемент присутній серед ключів словника.'''

# user = {
#     "name": "Bill",
#     "surname": "Bosh",
#     "age": 22
# }

# if "age" in user:
#     print(f"User is {user['age']} years old.")

'''Кількість елементів
Будь-яка колекція дозволяє дізнатися кількість елементів у ній за допомогою функції len.'''

# password = input("Password: ")
# if len(password) < 8:
#     print("Your password is too short")

# '''Наприклад, перевірка довжини пароля введеного користувача може бути реалізована за допомогою функції len.'''

# '''Перебір усіх елементів колекції в циклі for'''

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char)

'''По будь-якій колекції можна пройти за допомогою циклу for і на кожній ітерації в циклі буде отриманий 
один з елементів цієї колекції. У прикладі літери алфавіту з alphabet виводяться в консоль по черзі в циклі for.
Давайте проітеруємо список some_iterable у циклі та виведемо в консоль, що ми отримуємо на кожній ітерації:'''

# some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)

# У консолі ми побачимо:

# a
# b
# c

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)

# Код з цього прикладу виведе в консоль квадрати перших п'яти непарних чисел.

# Приклади взаємодії словника з циклом for.

# a = {'a':1, 'b':2, 'c':3}
# for i in (a):
#     print(i) # a b c

###
# a = {'a':1, 'b':2, 'c':3}
# for i in a.values():
#     print(i) # 1 2 3

###
# a = {'a':1, 'b':2, 'c':3}
# for i in a.items():
#     print(i)      # ('a', 1) ('b', 2) ('c', 3)

###
# a = {'a':1, 'b':2, 'c':3}
# for key, values in a.items():
#     print(key, values)       # a 1   b 2   c 3

# Приклади взаємодії списка з циклом for.

# my_list = ['a', 'b', 'c', 'd', 'f']
# for i in my_list:
#     print(i)  # a b c d f

### отримуємо індекси

# my_list = ['a', 'b', 'c', 'd', 'f']
# for i in range(len(my_list)):
#     print(i)  #  0 1 2 3 4

### отримуємо елементи

# my_list = ['a', 'b', 'c', 'd', 'f']
# for i in range(len(my_list)):
#     print(my_list[i])  #  a b c d f

### отримуємо впорядковану колекцію х індексів і елементів

# my_list = ['a', 'b', 'c', 'd', 'f']
# for index, element in enumerate(my_list):
#     print(index, element)  #  0 a  1 b  2 c  3 d  4 f

### ітерування даних в зворотному напрямку

# my_list = ['a', 'b', 'c', 'd', 'f']
# for i in reversed(my_list):
#     print(i)  #  f  b  c  d  a

### ітерування і сортування

# my_list = ['d', 'b', 'a', 'c', 'f']
# for i in sorted(my_list):
#     print(i)  #  a b c d f

# Передача списку в функцію

# def func(my_list):
#     return my_list

# print(func([1, 2, 3, 4]))  #  [1, 2, 3, 4]

# або 

# def func(my_list):
#     print(my_list)
#     return my_list

# func([1, 2, 3, 4])  #  [1, 2, 3, 4]

# або 

# def func(my_list):
#     print(my_list)
#     return my_list

# a = [1, 2, 3, 4]
# func(a)             #  [1, 2, 3, 4]

'''Аргументи командроно рядка'''

import sys

def main():
    print(sys.argv)












