'''Написати програму розв'язання лінійного рівняння а * х + b = 0 (а≠0). (a і b вводяться користувачем)'''

# a = float(input('Please enter a: '))
# b = float(input('Please enter b: '))
# x = -b / a
# print(x)

'''Скласти програму обчислення площі та гіпотенузи прямокутного трикутника, якщо відомі його катети (вводяться користувачем)'''

# a = float(input('Please enter a: '))
# b = float(input('Please enter b: '))
# c = (a ** 2 + b ** 2) ** 0.5
# S = a * b / 2
# print(f'Гіпотенуза дорівнює: {(a ** 2 + b ** 2) ** 0.5}')
# # print(f'Гіпотенуза дорівнює: {c}')
# print(f'Площа прямокутного трикутника: {S}')

'''Дано радіус кола r (вводяться користувачем). Скласти програму знаходження довжини кола та площі кола'''

# import math
# r = float(input('Radius r: '))
# l = 2 * math.pi * r
# S = math.pi * r ** 2
# print(f'довжини кола: {l}')
# print(f'площа кола: {S}')

'''Скласти програму обчислення суми модулів трьох дійсних чисел'''

# a = float(input('Please enter a: '))
# b = float(input('Please enter b: '))
# c = float(input('Please enter c: '))
# sum_modules = (abs(a) + abs(b) + abs(c)) 
# print(sum_modules)

'''Скласти програму, яка отримує із клавіатури чотиризначне число і виводить на екран середнє арифметичне його цифр.'''

# x = int(input('Введіть чотирьох значне число: '))
# x4 = x % 10
# x3 = x // 10 % 10
# x2 = x // 100 % 10
# x1 = x // 1000 % 10
# average = (x1 + x2 + x3 + x4) / 4
# print(average)

'''Скласти програму, яка вводить з клавіатури тризначне число і виводить на екран:
- суму останньої та передостанньої цифри
- суму останньої та першої цифри'''

# x = int(input('Введіть тризначне значне число: '))
# x3 = x % 10
# x2 = x // 10 % 10
# x1 = x // 100 % 10
# print(f'x3: {x3}, x2: {x2}, x1: {x1}')
# result1 = x2 + x3
# result2 = x1 + x3
# print(f'суму останньої та передостанньої цифри: {result1}')
# print(f'суму останньої та першої цифри: {result2}')

'''Результат пошуку згенерував n записів (вводиться користувачем). Скільки сторінок потрібно для відображення цих записів, якщо на 1 сторінку виводиться 10 записів.'''

# import math

# n = int(input('Введіть кількість записів '))
# pages = n / 10
# print(f'Потрібна кількість сторінок: {math.ceil(pages)}')

'''Скласти програму, яка переводить час із секунд, визначаючи повну кількість годин, хвилин і секунд (наприклад, час 5000 секунд це 1 година 23 хвилини 20 секунд 5000=1*3600+23*60+20).'''

# sekonds1 = int(input('Введіть кількість секунд: '))
# hours = sekonds1 // 3600
# minutes = (sekonds1 - hours * 3600) // 60
# sekonds2 = ((sekonds1 - hours * 3600) - minutes * 60)
# print(f'Введена кількість секунд це: {hours} год. {minutes} хв. {sekonds2} сек.')

'''В Інтернет-магазині зроблено 4 покупки: на $34.34, $12.01, $17.42, $4.93. Зі скількох доларів і центів складатиметься підсумкова сума.'''

# price1 = 34.34
# price2 = 12.01
# price3 = 17.42
# price4 = 4.93

# cost = price1 + price2 + price3 + price4
# dollar = int(cost)
# # cent = float(cost - dollar)
# cent = int((cost - int(cost)) * 100)
# print(f'Sum: {cost}')
# print(f'Dollar: {dollar}')
# print(f'Cent: {cent}')

'''В Інтернет-магазині зроблено 4 покупки: на суми які вводяться користувачем. Зі скількох доларів і центів складатиметься підсумкова сума.'''

# price1 = float(input('Перша сума: '))
# price2 = float(input('Друга сума: '))
# price3 = float(input('Третя сума: '))
# price4 = float(input('Четверта сума: '))
# cost = price1 + price2 + price3 + price4
# cost = (round(cost, 2))
# dollar = int(cost)
# cent = int((cost % dollar) * 100)
# print(f'Сума: {cost}')
# print(f'Доларів: {dollar}')
# print(f'Центів: {cent}')

'''Для кава-брейків на конференції закуплено: х круасанів, у стаканчиків, z упаковок кави. Ціна круасана $1.04, ціна стаканчика - $0.34, ціна упаковки кави $4.42. Скласти програму, яка обчислює, скільки повних доларів пішло на закупівлю їжі для кава-брейків, і яка її вартість у центах.'''

# x = float(input("Введіть кількість круасанів: "))
# y = float(input("Введіть кількість стаканчиків: "))
# z = float(input("Введіть кількість упаковок кави: "))
# price_x = 1.04
# price_y = 0.34
# price_z = 4.42
# sum_dollars = int(price_x * x + price_y * y + price_z *z)
# sum_cents = int((price_x * x + price_y * y + price_z *z) * 100)
# print(f'Повних доларів: {sum_dollars}')
# print(f'Вартість у центах: {sum_cents}')

