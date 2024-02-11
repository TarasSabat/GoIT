'''
На технічній співбесіді претенденти на посаду одержують оцінку за тест. 
У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище. 
Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True, 
якщо кількість набраних балів буде більшою або дорівнює 83. 
В іншому випадку значення змінної дорівнює False.
'''
# is_next = 83
# num = int(input("Enter the number of points: "))
# if num >= is_next:
#     is_next = True
#     print('True')
# else:
#     is_next = False
#     print('False')

'''
У нас є три логічні змінні.
Перша визначає статус користувача is_active, яка дорівнює True або False.
Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
Третя is_permission — чи дозволено доступ, теж булевого типу.
Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.
Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.
'''
# is_active = (input("Is the user active? "))
# is_admin = (input("Is the user administrator? "))
# is_permission = (input("Does the user have access? "))

# is_active = bool(is_active) 
# is_admin = bool(is_admin)
# is_permission = bool(is_permission)

# access = is_active and is_permission or is_admin
'''
Як відомо, зазвичай розробників заведено поділяти на три категорії: 
Джун (Junior) & mdash; молодший спеціаліст, Мідл ( Middle) — основний розробник у компанії та Сеньйор 
(Senior) — старший розробник. Орієнтовно можна вважати, що до 1 року роботи включно — це Джуніор, 
понад 5 років — це Сеньйор розробник, а від одного року до 5 включно — мідл.
Є змінна work_experience, що визначає стаж роботи програміста. Залежно від стажу роботи, 
присвоїти змінній developer_type значення "Junior", "Middle" або "Senior". Використовуйте, 
якщо необхідно, булеві оператори or та and під час перевірок.
'''
# work_experience = float(input("Enter your full work experience in years: "))

# if 1 < work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1 :
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(developer_type)
'''
Перепишіть приклад із теорії, але для додатного числа перевіряйте — парне воно чи ні. 
Таким чином після перевірок змінна result повинна містити одне з чотирьох значень:
"Positive even number"
"Positive odd number"
"Negative number"
"It is zero"
Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. 
Нагадаємо, залишок від ділення можна отримати після операції %
'''
# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 0:
#         result = "Positive even number"
#     else:
#         result = "Positive odd number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)

'''
Повернемося до завдання розрахунку коренів квадратного рівняння з попереднього модуля.
Необхідно обчислити коріння квадратного рівняння.
a · x2 + b · x + c = 0
Дискримінант рівняння помістіть у змінну D
D = b2 - 4 · a · c
Коріння рівняння помістіть у змінні x1 та x2
x1 = (-b + D0.5) / (2 · a)
x2 = (-b - D0.5) / (2 · a)
Минулого разу ми просто вказали значення коефіцієнтів a, b, c. 
Тепер, коли ми вже знаємо про розгалуження, ми можемо перевіряти значення дискримінанта і, 
в залежності від того додатне чи від'ємне, провести розрахунок коренів. 
Виконайте розрахунок коренів для довільних значень коефіцієнтів a, b, c.
'''
# import math

# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c

# if D >= 0:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print(x1)
#     print(x2)
# if D < 0:
#     print('D negative')

'''
Виконайте завдання, щоб визначити парне число чи ні, за допомогою тернарного оператора.
Програма встановлює значення змінної is_even у True або False, 
залежно від того, чи є число в змінній num парним або непарним.
Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. 
Нагадаємо, залишок від ділення можна отримати після операції %
'''
# num = int(input("Enter an integer number: "))

# is_even = True if num % 2 == 0 else False
# print(is_even)
'''
Користувач вводить число від 0 до 100. Підрахуйте, використовуючи цикл while, 
суму всіх чисел від першого до введеного числа включно в num. Результат помістити в змінну sum.
Тести будуть:
Поміщати тестові значення для змінної num: 20, 10, 5, 100
І чекати суми в змінній sum: 210, 55, 15, 5050
'''
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# count = 0

# while count <= num:
#     sum += count  
#     count += 1    
# print(sum)  
'''
Рядок — це об'єкт, що ітерується, а, значить, ми можемо використовувати його в циклі for. 
Підрахуйте в заданому рядку message кількість входжень символу зі змінної search. 
Результат помістіть у змінну result.
'''
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0

# for search2 in message:
#     if search2 == search:
#         result += 1
# print(result)
# print(search2)
'''
На співбесідах часто люблять запитувати про алгоритми. Наприклад, розрахуйте найбільший спільний дільник 
(НД) двох додатних чисел. НСД — це найбільше число, на яке без залишку діляться обидва числа.
Є кілька алгоритмів знаходження НСД, але ми розберемо циклічний алгоритм. Хай є два початкових числа 
first та second. Виберемо менше з них та привласнимо значення змінній gcd. Поки first або second не діляться
на gcd без залишку, треба виконувати цикл, в якому зменшуємо змінну gcd на одиницю. Коли цикл закінчиться 
в змінній gcd буде НСД для чисел first та second 
Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.
Примітка: Для умови циклу в пункті 3 необхідно пам'ятати, що цикл while виконується за умови True, 
а наш цикл повинен закінчитися, тільки якщо gcd поділив обидва числа без залишку.
'''
# Варіант 1
# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = 0

# if first < second:
#     gcd = first
# else:
#     gcd = second

# while second % gcd != 0 or first % gcd != 0:
#     gcd -= 1

# print(gcd)

'''
Напишіть два цикли, вкладені один в один. У першому циклі while ми постійно запитуємо ціле число, 
а у другому з допомогою циклу for складаємо суму чисел від 0 до введеного числа включно 
і додаємо до змінної sum. Змінна sum накопичує суми, що утворюються при кожному введенні числа. 
Вихід з першого циклу здійснюємо, якщо ми ввели число 0.
Тести використовують дві тестові послідовності чисел:
10, 13, 73, 0 і чекають на суму 2847
1, 2, 3, 4, 0 і чекають на суму 20
'''
# num = int(input("Enter integer (0 for output): "))
# sum = 0

# while num != 0:
#     for i in range(num + 1):
#         sum += num
#         num -= 1
#     num = int(input("Enter integer (0 for output): "))
# print(sum)
'''
Перепишіть попередній приклад, але використовуючи оператор break.
Напишіть два подвійні цикли. У першому циклі while ми постійно запитуємо ціле число, 
а у другому за допомогою циклу for обчислюємо суму чисел від 0 до введеного числа. 
Вихід з першого циклу здійснюємо, якщо ввели число 0, за допомогою оператора break.
Тести використовують дві тестові послідовності чисел:
10, 13, 73, 0 і чекають на суму 2847
1, 2, 3, 4, 0 і чекають на суму 20
'''
# sum = 0

# while True:    
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     else:        
#         for i in range(num + 1):
#             sum = sum + i
#             i -= 1
# print(sum)
'''
Повернемося знову до нашого попереднього завдання.
Напишіть два подвійні цикли. У першому циклі while ми постійно запитуємо ціле число, 
а у другому за допомогою циклу for обчислюємо суму парних чисел від 0 до введеного числа. 
Вихід з першого циклу здійснюємо, якщо ввели число 0 за допомогою оператора break.
Тести використовують дві тестові послідовності чисел:
10, 13, 73, 0 і чекають на суму 1404
1, 2, 3, 4, 0 і чекають на суму 10   
'''
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2 == 1:
#             continue
#         sum = sum + i
# print(sum)
'''
Код Цезаря
ord('a') # 97
chr(118) # 'v'

pos = ord(v) - ord('a) # 21 # позиція символу 'a' відносно символу 'v'

pos = ord('v') - ord('a')  # 21
pos = (pos + 33) % 26  # 2  # з врахуванням зсуву н.п. 33

Залишився останній крок, отримати новий символ:
pos = ord('v') - ord('a')  # 21
pos = (pos + 33) % 26  # 2
new_char = chr(pos + ord("a"))  # 'c'

Тести перевіряють та кодують наступні рядки:
"Hello my little friends!", offset = 37,
"Hello world!", offset = 7
'''
# # Result 1
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         if ch.islower():
#             pos = ord(ch) - ord('a')
#             pos = (pos + offset) % 26  
#             new_char = chr(pos + ord("a"))
#             encoded_message += new_char
#         else:
#             pos = ord(ch) - ord('A')
#             pos = (pos + offset) % 26  
#             new_char = chr(pos + ord("A"))
#             encoded_message += new_char
#     else:
#         encoded_message += ch
# print(encoded_message, end = ' ')
         
# Result 2
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         is_upper = ch.isupper()
#         ch = ch.lower()
#         pos = ord(ch) - ord('a')
#         new_pos = (pos + offset) % 26
#         new_ch = chr(new_pos + ord('a'))
#         if is_upper:
#             new_ch = new_ch.upper()
#         encoded_meisssage += new_ch
#     else:
#         encoded_message += ch
# print(encoded_message, end = ' ')

# # Result 3
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         if ch.isupper():
#             pos = ord(ch) - ord('A')
#             pos = (pos + offset) % 26  
#             new_char = chr(pos + ord("A"))
#             encoded_message += new_char
#         else:
#             pos = ord(ch) - ord('a')
#             pos = (pos + offset) % 26  
#             new_char = chr(pos + ord("a"))
#             encoded_message += new_char
#     else:
#         encoded_message += ch
# print(encoded_message, end = ' ')

# # Result 4
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if "a" <= ch <= "z":
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message = encoded_message + new_char
#     elif "A" <= ch <= "Z":
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A"))
#         encoded_message = encoded_message + new_char
#     else:
#         encoded_message = encoded_message + ch
'''
Ситуація проста, вам необхідно вирахувати кількість SMS, які треба надсилати в одному пакеті 
розсилки потенційним покупцям. Всього на день виділяється 1000 платних SMS для кампанії маркетингу 
pool=1000. Співробітник відділу маркетингу вводить кількість розсилок quantity, 
і ви обчислюєте розмір пакета chunk = pool // quantity. Опрацюйте помилку поділу на нуль.
'''
# #Мій варіант
# pool = 1000
# quantity = int(input("Enter the number of mailings: "))

# while True:
#     if quantity > 0:
#         chunk = pool // quantity
#         print(chunk)
#         break
#     try:
#         chunk = pool // quantity
#     except ZeroDivisionError:
#         quantity = int(input('Division by zero is impossible.! Enter a number greater than zero: '))

## Правильний варіант
# pool = 1000
# quantity = int(input("Enter the number of mailings: "))

# try:
#     chunk = pool // quantity
#     print(chunk)

# except ZeroDivisionError:
#     print('Divide by zero completed!')
'''
Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, 
приймаючи від користувача операнди (числа) та оператор.
Умови для цієї задачі
Додаток працює з цілими та дійсними числами.
Додаток вміє виконувати такі математичні операції:
ДОДАВАННЯ (+)
ВІДНІМАННЯ(-)
МНОЖЕННЯ (*)
ДІЛЕННЯ (/)
Програма приймає один операнд або один оператор за один цикл запит-відповідь.
Всі операції програма виконує в порядку надходження — одну за одною.
Програма виводить результат обчислень, коли отримує від користувача символ =.
Додаток закінчує роботу після того, як виведе результат обчислення.
Користувач по черзі вводить числа та оператори.
Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
Додаток коректно опрацьовує ситуацію некоректного введення (exception).
Початкові змінні:
result = None
operand = None
operator = None
wait_for_number = True
result — сюди поміщаємо підсумковий результат operand — завжди зберігає поточне число 
operator — рядковий параметр, може містити чотири значення, "+", "-", "*", "/" 
wait_for_number — прапорець, який вказує, що очікують на вводі оператор (operator) 
або операнд (operand)
Приклад виконання програми:
>>> 3
>>> +
>>> 3
>>> 2
2 is not '+' or '-' or '/' or '*'. Try again
>>> -
>>> -
'-' is not a number. Try again.
>>> 5
>>> *
>>> 3
>>> =
Result: 3.0
Тестові послідовності:
Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0
'''
## Варіант викладача
# result = None
# operand = None
# operator = None
# wait_for_number = True

# while True:
#     user_input = input(">>> ")
#     if user_input == "=":
#         break

#     if wait_for_number:
#         try:
#             operand = float(user_input)
#         except ValueError:
#             print(f'{user_input} is not a number')
#             continue
#         wait_for_number = False
#         if result is None:
#             result = operand
#         else:
#             if operator == "+":
#                 result += operand
#             elif operator == "-":
#                 result -= operand
#             elif operator == "*":
#                 result *= operand
#             elif operator == "/":
#                 if operand == 0:
#                     print('Division by zero')
#                     continue
#                 result /= operand
#     else:
#         if user_input in "+-*/":
#             operator = user_input
#             wait_for_number = True
#         else:
#             print(f'{user_input} is not "+", "-", "*", "/"')           
      
# print(result) 