'''
Введення пін-кода (3 спроби)
Через while
'''
# pin = '0123'
# n = 0
# max_tries = 3

# while n < max_tries:

#     user_pin = input('Enter your pin: ')

#     if len(user_pin) >= 4:
#         if pin == user_pin:

#             amount = input('How much: ')

#             if amount > 0:

#                 print(f'Take your {amount}')
#                 break

#         else:

#             print('Sorry, wrong pin. Try again please!')
#             print(f'You have {max_tries - n - 1} tries.')
#             n += 1

#     else:

#         print('Pin should be 4 or more digits.')
#         print(f'You have {max_tries - n - 1} tries.')
#         n += 1

# print('Good bye!')
'''
Через for
'''
# pin = '0123'
# for i in range(3):
#     user_pin = input('Enter your pin: ')
#     if len(user_pin) == 4 or len(user_pin) == 6:
#         if pin == user_pin:
#             print("Here's your money")
#             break
#         else:
#             print('Sorry, wrong pin. Try again please!')
#     else:
#         print('Pin should be 4 or 6 digits.')
# print('Good bye!')
'''
Перевірка чи 3-и значне чичсло поліндром (зліва направа і зправа на ліво читається однаково)
'''
# num = int(input('Number: '))

# n1 = num // 100
# n2 = num % 10

# if n1 == n2:
#     print('Yes')

# else:
#     print('No')
'''
Перевірити чи в 3-х значному числі всі цифри різні? І чи є тільки 2 однакових числа?
'''
# num = input("Number: ")

# if len(num) != 3:
#     print('Please enter 3 digits')
# else:
#     n1 = int(num[0])
#     n2 = int(num[1])
#     n3 = int(num[2])

#     if n1 != n3 and n2 != n3 and n1 != n2:
#         print('Усі цифри різні')

#     elif (n1 == n3 or n2 == n3 or n2 == n1) and not (n1 == n2 and n1 == n3):
#         print('Є тільки дві однакові цифри')
'''
Скласти програму, яка вводить цілі k, l.
Якщо вони не рівні, то менше з них замінюється більшим, інакше обидва замінюються на 0.
'''
# k = int(input("Введіть число k: "))
# l = int(input("Введіть число l: "))

# if k != l:
#     if k < l:
#         k = l
#     else:
#         l = k
# else:
#     l = 0
#     k = 0
# print(k, l)
'''
# # swap (заміна місцями змінних)
'''
# baz = int(input("Enter a number: "))
# foo = int(input("Enter a number: "))

# if baz < foo:
#     temp = baz
#     baz = (baz + foo) / 2
#     foo = temp * foo
# else:
#     temp = foo
#     foo = (foo + baz) / 2
#     baz = temp * baz

# # print(foo, baz)
# # Enter a number: 3
# # Enter a number: 11
# # 33 7.0

# if baz < foo:
#     baz, foo = (baz + foo) / 2, baz * foo
# else:
#     foo, baz = (foo + baz) / 2, foo * baz

# # print(foo, baz)
# # Enter a number: 3
# # Enter a number: 11
# # 33 7.0

# # зміна значень змінних
# a = 4
# b = 6

# temp = a
# a = b
# b = temp

# a, b = b, a
# print(f'a: {a}, b: {b}')
'''
Знайти у рядку номер першого входження символу 'a'
'''
# string = input("Введіть строку: ")

# count = 0
# # hello and
# for char in string:
#     if char == 'a':
#         break
#     count += 1

# print(f"a: {count}")
'''
Знайдемо індекс останнього входження символу 'а'
'''
# string = input('String: ')

# count = 0
# index = -1
# for ch in string:
#     if ch == 'a':
#         index = count
#     count += 1

# print(f'The latest a is: {index}')
'''
Визначити до якої пори року відноситься місяць
'''
# month = 11

# match month:
#     case 3 | 4 | 5:
#         season = 'весна'
#     case 6 | 7 | 8:
#         season = 'літо'
#     case 9 | 10 | 11:
#         season = 'осінь'
#     case 12 | 1 | 2:
#         season = 'зима'
# print(season)
'''
У банк поклали 100 доларів під 5 % річних.
Скласти програму обчислення кількості грошей на рахунку через 10 років. (складні щомісячні відсотки)
'''
# deposit = 100
# percent = 0.05
# T = 10

# for year in range(1, T + 1):
#     new_deposit = deposit * (1 + percent / 12) ** 12
#     deposit = new_deposit
# print(deposit)
# # 164.700949769028
# # 164.700949769028
# # print(deposit * (1 + percent / 12) ** (12 * 10))
'''
Розрахуємо найбільший спільний дільник для двох цілих чисел з використанням циклу
'''
# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = min(first, second)
# while not (first % gcd == 0 and second % gcd == 0):
#     gcd = gcd - 1
# print(gcd)
'''
# Визначити, чи є введений користувачем рядок паліндромом (пробіли не враховуємо)
'''
# Варіант 1
# word= input("Введіть рядок: ")
# word2 = word[::-1]
# if word == word2:
#     print(True)
# else:
#     print(False)

# Варіант 2
# word = input("Enter word: ")
# print(word == ''.join(reversed(word)))

# Варіант 3
# word = input("Please enter word: ").lower()
# while True:
#     word = input("Please enter word: ").lower()
#     if len(word) % 2 == 0:
#         print ("This word cant be polindrom")
#         continue
#     for i, d in enumerate(word):
#        #print(word[i], word[-i -1], i)
#         if word[i] != word[-i -1]:
#            pol = False
#     break

# Варіант 4
# pol = True
# while True:
#     word = input("Please enter word: ").lower()
#     if len(word) % 2 == 0:
#         print ("This word cant be polindrom")
#         continue
#     for i  in  range(len(word)):
#        #print(word[i], word[-i -1], i)
#         if word[i] != word[-i -1]:
#            pol = False
#     break
# print(pol)

##
# number = 100
# figure = 63
# c = figure % 2 == 0
# if c:
#     for i in range(0,number+1,2):
#         if i == figure:
#             print("Parne", i)
#             break
# else:
#     for i in range(1,number+1,2):
#         if i == figure:
#             print(i)
#             break

'''Побудова трикутника'''
# n = 6

# for i in range (1, n+1):
#     if i % 2 == 1:
#         print(' ' * ((n-i) // 2), end = '')
#         print('#' * i)
'''Визначення парне/непарне'''
# number = 100
# figure = int(input('Enter number: '))
# a = figure % 2 == 0
# if a:
#     for i in range(0, number + 1, 2):
#         if i == figure:
#             print(f'Parne {i}')
#             break
# else:
#     for i in range(1, number + 1, 2):
#         if i == figure:
#             print(f'Ne parne {i}')
#             break
