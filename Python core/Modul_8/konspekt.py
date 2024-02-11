''' datetime '''
# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime)  # 2023-10-26 12:32:36.832355

##У результаті виклику now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:

# from datetime import datetime
#
# current_datetime = datetime.now()
#
# print(current_datetime.year)        # 2023
# print(current_datetime.month)       # 10
# print(current_datetime.day)         # 26
# print(current_datetime.hour)        # 12
# print(current_datetime.minute)      # 33
# print(current_datetime.second)      # 53
# print(current_datetime.microsecond) # 644484

'''------'''
# from datetime import datetime

# date = datetime(year=2023, month=10, day=31)
# print(date)
# date = datetime(year=2023, month=10, day=31, hour=19, minute=37, second=55)
# print(date)
# print(date.date())
# print(date.time())

# print(datetime.now())
# print(datetime.today())

''' В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати): '''

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())  # 2020-10-09
# print(current_datetime.time())  # 22:13:35.053819

''' Щоб створити об'єкт datetime з будь-якою вибраною датою, можна зробити так: '''

# from datetime import datetime

# d1 = datetime(year=2012, month=1, day=7, hour=14)
# print(d1) # 2012-01-07 14:00:00

''' Щоб дізнатися день тижня, можна скористатися методом weekday: '''

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.weekday())   # 1

'''
Дні тижня у Python починаються з понеділка і він буде 0. У прикладі вище 7 Січня 2020 року було вівторком.
Щоб порівняти два об'єкти datetime, достатньо скористатися оператором порівняння:
'''

# from datetime import datetime

# current_datetime = datetime.now()

# future_month = (current_datetime.month % 12) + 1
# future_year = current_datetime.year + int(current_datetime.month / 12)
# future_datetime = datetime(future_year, future_month, 1)

# print(current_datetime < future_datetime)    # True

'''
timedelta
Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. Він відповідає за відрізок часу     
між двома датами.
'''
from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2019)


difference = seventh_day_2020 - seventh_day_2019
print(difference)                   # 365 days, 0:00:00
print(difference.total_seconds())   # 31536000.0

'''-------'''
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now.date())
# interval = timedelta(days=5)
# result_date = now + interval
# print(result_date)
# ##
# interval = timedelta(days=15)
# result_date = now - interval
# print(result_date)

''' Об'єкти timedelta можна створювати самостійно, щоб отримати дату/час віддалену від початкової: '''

# from datetime import datetime, timedelta

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)   # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)   # 2019-12-10 14:00:00

''' Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і мікросекунди: '''

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )

''' Якщо якийсь параметр не заданий, то він дорівнює 0 за замовчуванням. '''

'''
timestamp
Окремо потрібно сказати про timestamp. timestamp — це кількість секунд, що пройшло з 00 годин 00 хвилин 1 Січня 1970 року в UTC (часовий пояс Гринвіча). Це просто прийнята константа і нічого особливого вона не означає. Просто для зручності колись почали відраховувати час в секундах з цієї миті і це виявилося дуже зручно. Адже порівняти два числа завжди легше і швидше, ніж порівняти складну структуру дат і часів.
Звичайно можна з timestamp отримати дату/час і навпаки:
'''

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# ts = seventh_day_2020.timestamp()
# print(ts)   # 1578398400.0

# ts += 100_000
# print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

'''--------'''
# from datetime import datetime

# d = datetime.now()
# print(type(d.timestamp))

# Перетворення timestamp в рядок
# from datetime import datetime

# timestamp = 1625309472.357246
# d = datetime.fromtimestamp(timestamp) # отримання типу datetime з числа stamp  
# print(d)
# d_int = datetime.fromtimestamp(int(timestamp))  # переведення з datetime в int
# print(d_int)                          
# str_date = d_int.strftime('%d-%m-%Y, %H:%M:%S')  # переведення з int  в str
# print(str_date)

'''
Перетворення в рядок і з рядка
Коли потрібно перетворити дату/час в рядок, ви можете скористатися функцією str, яка перетворить datetime у рядок. Але часто формат такого перетворення незручний і в Python є окрема мінімова для опису, як перетворити дату/час в рядок:
'''

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.strftime('%A %d %B %Y')) # Tuesday 07 January 2020

''' Та ж міні-мова використовується для конвертації вже рядків в дату/час: '''

# from datetime import datetime

# s = '10 January 2020'
# print(datetime.strptime(s, '%d %B %Y')) # 2020-01-10 00:00:00 перетворення строки в datetime (потрібно
# підбирати такий же ж стиль як і у str)

'''-------'''
# from datetime import datetime
# td = '24.02.2022'
# d = datetime.strptime(td, '%d.%m.%Y') # перетворення строки в datetime (потрібно підбирати такий же ж стиль як і у str)
# print(type(d))
# print(d)
# print(d.date())
# print(d.time())
# print(d.year, d.month, d.day, d.minute)
##
# temp_replace = d.replace(month=5, day=11, minute=15) # заміна даних в об'єкті
# print(temp_replace)
##
# str_temp_replace = temp_replace.strftime('%y/%d/%m %H:%M:%S') # перетворення datetime в строку (передіємо формат який нам потрібний у строці)
# print(str_temp_replace)
# print(datetime.now().strftime('%Y %B %d')) # перетворення поточної години з datetime в строку (передіємо формат який нам потрібний у строці)
'''
Генерація випадкових чисел
Для генерації випадкових (псевдовипадкових) чисел у Python є пакет random. Він досить хороший для ряду побутових завдань, але не для криптографії. На жаль, вбудований генератор псевдовипадкових чисел досить скоро починає повторюватися і не є достатньо криптостійким. Проте, для прикладних завдань поза сферою криптографії його цілком вистачає.
Отримання випадкового цілого числа з рівномірного розподілу в інтервалі між 1 та 1000 включно:
'''
# import random

# random.randint(1, 1000)

''' Якщо потрібно отримати випадкове число в інтервалі 0, 1 включно: '''

# import random

# random.random()

###

# import random

# random.seed()
# print(random.random())
# print(random.randint(1, 10))

# for _ in range(10):
   #  print(random.randrange(1, 10), end=" ")  # 4 7 8 5 8 8 3 1 7 4 - 10 не входить
    # print(random.randint(1, 10), end=' ')  # 1 1 10 5 9 9 3 5 7 5 - 10 входить

''' Коли у вас є список об'єктів і вам потрібно перемішати порядок елементів в цьому списку на випадковий: '''

# import random

# fruits = ['apple', 'banana', 'orange']
# random.shuffle(fruits)
# print(fruits)   # ['banana', 'orange', 'apple']

###
# import random
# l = list(range(1, 40))
# print(l)
# random.shuffle(l) # перемішує елементи у рандомному порядку
# print(l)

# print(random.choice(l))      # повертає випадковий елемент з непустої послідовності
# print(random.sample(l, k = 5))   # повертає k (можна просто ввести число) випадкових елементів з непустої послідовності
# print(random.sample('Hello world, nice to meet you', 5))

''' Якщо потрібно вибрати випадковий елемент зі списку: '''

# import random

# fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))   # 'banana'

''' Щоб вибрати N випадкових елементів зі списку: '''

# import random

# fruits = ['apple', 'banana', 'orange']
# print(random.choices(fruits, k=4))   # ['banana', 'orange', 'orange', 'orange']

''' Щоб вибрати N елементів, що не повторюються, зі списку: '''

# import random

# fruits = ['apple', 'banana', 'orange']
# print(random.sample(fruits, k=2))   # ['banana', 'orange']

''' Зверніть увагу, що k не може бути більше довжини fruits. '''

'''
Контроль точності обчислень (decimal)
Комп'ютер усі обчислення робить в бінарному вигляді, а десяткові числа використовуються тільки для "спілкування" з користувачем для зручності останнього. Через це і через те, що точність обчислень в комп'ютері обмежена, виникають помилки округлення під час виконання математичних операцій.
'''

# print(0.1 + 0.2 == 0.3)     # False
# print(0.1 + 0.2)            # 0.30000000000000004

###

# from decimal import Decimal, getcontext

# f = 0.2 + 0.1 + 0.3 - 0.5
# print(f)
# result = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5') # для отримання більш точних даних
# print(result)

# n = Decimal('1') / Decimal('3')
# print(n)
# print(type(n))
# getcontext().prec = 6     # встановлення кількості знаків числа без врахування 0 перед комою (прийнято 4 знаки після коми)
# n = Decimal('1') / Decimal('3')
# print(n)
# n = Decimal('100') / Decimal('3')
# print(n)

###

# Створення Decimal із дійсних чисел

# from decimal import Decimal

# print(0.1 + 0.2)                             # 0.30000000000000004
# print(Decimal(0.1) + Decimal(0.2))           # 0.3000000000000000166533453694 (ніколи не передавати в Decimal число з плаваючою крапкою)
# print(Decimal(str(0.1)) + Decimal(str(0.2))) # 0.3 (потрібно перевести до строки тоді робити Decimal)  

'''
Перший вираз може збити вас з пантелику, оскільки математика стверджує однозначно, що 0.1 + 0.2 = 0.3. Але помилка округлення під час виконання обчислювальних операцій з дійсними числами у двійковій системі обчислення призводить до такої неоднозначності.
Проблема точності обчислень так і не розв'язана остаточно, і математика продовжує розвиватися в цьому напрямі.
Щоб контролювати точність обчислень більш явно, у Python є пакет decimal.
'''

# from decimal import Decimal, getcontext

# getcontext().prec = 6
# Decimal(1) / Decimal(7)  # Decimal('0.142857')

# getcontext().prec = 28
# Decimal(1) / Decimal(7) # Decimal('0.1428571428571428571428571429')

### У цьому прикладі ми вирахували вираз 1 / 7 з точністю до 6 знаків після коми і до 28 знаків. Щоб встановити точність обчислення, ми скористалися функцією getcontext, яка повертає поточні налаштування точності, та встановили налаштування prec у 6 та 28 відповідно.

### Об'єкти Decimal поводяться так само, як float, але їх і не можна використовувати в одному виразі разом. Виконання виразу на кшталт Decimal(0.1) + 0.2 призведе до помилки.

''' Повертаючись до нашого прикладу із додаванням 0.1 та 0.2: '''

# from decimal import Decimal, getcontext

# getcontext().prec = 6
# float(Decimal(0.1) + Decimal(0.2)) == 0.3   # True

'''
На жаль, Decimal має ще ту особливість, що при створенні Decimal із float його точність береться максимальною для цієї платформи, а не з налаштувань getcontext.
Саме тому:
'''

# Decimal(0.2) + Decimal(0.1) == Decimal(0.3) # False

# але

# Decimal(0.2) + Decimal(0.1) == Decimal(0.3)  + Decimal(0.0) # True

'''
Можливості пакетів math, cmath
Для математичних обчислень у Python доданий пакет math. Цей пакет містить ряд часто використовуваних математичних функцій та констант:
тригонометричні функції
sin / asin
cos / acos
tan / atan
hypot, обчислення відстані Евкліда між точками
Перетворення кутів та радіанів:
degrees
radians
Гіперболічні функції:
sinh / asinh
cosh / acosh
tanh / atanh
степеневі функції:
exp
pow (перетворить аргументи в float, на відміну від вбудованої pow)
sqrt
log2
log10
log логарифм із основою e, якщо основа не задана або із заданою основою.
константи:
pi - чмсло пі
e
tau
inf, нескінченність
nan, не число
'''

# import math

# math.sin(math.pi / 4)       # 0.7071067811865475
# math.degrees(math.pi / 4)   # 45.0

'''
Якщо вам потрібна комплексна математика, то можна скористатися пакетом cmath. Він надає той самий API, але вміє працювати з комплексними числами.
'''

# import cmath

# cmath.sqrt(-4)  # 2j

''' Collections
У Python є пакет з додатковими колекціями, які можуть дуже знадобитися розробнику-початківцю і сильно розширяти його арсенал.
   Іменовані кортежі
Використання кортежів у Python для передачі даних між обробниками — це хороша та поширена практика. Але є одна незручність у кортежів, вам необхідно пам'ятати індексацію елементів у кортежі і не плутати їх порядок. Це не завжди зручно і для ситуацій, коли в кортежі є 2 або більше елементів, такий підхід ускладнює читабельність коду:

person = ('Mick', 'Nitch', 35, 'Boston', '01146')

Після створення person там, де ви його використовуєте, вам потрібно пам'ятати, що ім'я на першому місці, а вік — на третьому. Щоб не плутатися, доведеться постійно повертатися до коду, де створюється person. Це незручно і спеціально для таких випадків додали іменовані кортежі:'''

# import collections

# Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# person.name         # 'Mick'
# person.post_index   # '01146'
# person.age          # 35
# person[3]           # 'Boston'

'''
Тепер, використовуючи Person, ви можете створювати кортежі, які обов'язково повинні містити 5 елементів і у таких кортежів, окрім індексів, є атрибути. Звертатися до елементів такого кортежу можна як за індексом, так і за ім'ям. За такого підходу вам достатньо один раз визначити Person і більше не повертатися до нього, щоб згадати, який елемент за що відповідає.
'''

''' Counter
Часто вам потрібно підрахувати кількість елементів у певній послідовності. Для цього зручно скористатися словником.
'''

# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1
# print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}

''' Таке завдання зустрічається досить часто і, щоб не писати одні й ті самі 6 рядків коду постійно, у collections додали спеціальний словник Counter: '''

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})

''' Але на цьому корисні властивості Counter не закінчуються. Він може вивести елементи за частотою появи: '''

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts.most_common(1))  # [(4, 4)]
# print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]

''' Ще Counter може відняти кількість елементів одного Counter від другого поелементно: '''

# from collections import Counter


# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)
# print(c)    # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

''' Counter. Підрахунок кількості кожного символа у строці. Результат повернути у форматі словника '''

# count_letter = {}
# for ch in input():
#     count_letter[ch] = count_letter.get(ch, 0) + 1
# print(count_letter)

# ### те саме за допомогою Counter

# from collections import Counter

# print(f'{dict(Counter(input()))}')

'''
defaultdict
Це спеціальний словник, який створює значення для ключів, яких в словнику не було за запитом. Наприклад, у вас є список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова.
'''

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

# У консолі ми побачимо:

# {
#     'a': ['apple', 'appendix'],
#     'z': ['zoo'],
#     'l': ['lion', 'lama'],
#     'b': ['bear', 'bet'],
#     'w': ['wolf']
# }

'''
Таким чином ми можемо отримати всі слова із words, що починаються на якусь літеру. Подібні завдання зустрічаються досить часто. Щоб не перевіряти, чи є список на цю літеру в словнику grouped_words, ми можемо скористатися defaultdict із collections та задати значенням за замовчуванням порожній список:
'''

# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

'''
Результат виконання буде ідентичний. defaultdict приймає у якості аргументу функцію, яка буде використовуватися для створення значення за замовчуванням. В цьому прикладі ми використали list, але ви можете передати будь-яку функцію, яка викликається без аргументів.
'''
'''
   deque
Списки у Python реалізовані таким чином, що вибір елемента за індексом відбувається за константний час (дуже швидко) і додавання/видалення елементу в кінець списку теж відбувається дуже швидко. Але ось додавання елементу в будь-яке інше місце в списку змушує Python перерахувати індекси усіх елементів списку до кінця. Для великих списків це може бути дуже невигідно. Щоб швидко додавати елементи на початок списку, в Python в пакеті collections є така колекція як deque:
'''

# from collections import deque

# d = deque()
# d.append('last')
# d.appendleft('first')
# d.insert(1, 'middle')
# print(d)            # deque(['first', 'middle', 'last'])

# print(d.pop())      # 'last'
# print(d.popleft())  # 'first'
# print(d)            # deque(['middle'])

'''
Окрім додавання на початок за допомогою appendleft, у deque є і швидке видалення першого елементу popleft.
Ще однією особливістю deque є можливість обмежити розмір deque:
'''

# from collections import deque

# d = deque(maxlen=5)
# for i in range(10):
#     d.append(i)

# print(d)            # deque([5, 6, 7, 8, 9], maxlen=5)

'''
Як видно з прикладу, нові елементи витісняють старіші, але розмір залишається незмінним.
В іншому deque веде себе точно як список Python.
'''

'''  Comprehensions
Часто потрібно створити колекцію і відразу заповнити її елементами. Зробити це одним виразом не можна, доводиться писати цикл. Наприклад, створимо список квадратів чисел від 1 до 5:
'''
# sq = []
# for i in range(1, 5+1):
#     sq.append(i**2)

# print(sq)   # [1, 4, 9, 16, 25]

'''
Подібні операції, які ми робимо зі змінюваними колекціями (list, dict, set) у циклі for, ми можемо виконати одним виразом за допомогою конструкції comprehension.
comprehensions — це синтаксична конструкція Python, створена спеціально, щоб зменшити кількість коду, коли потрібно для кожної ітерації циклу for додати один елемент у нову колекцію.
Суть синтаксису comprehensions: всередині дужок (для list — квадратні, для dict та set — круглі) записується вираз (тільки один), який потрібно виконати з кожним елементом циклу for та сам цикл, але без двокрапки у кінці.
Найпростіше зрозуміти цю конструкцію на прикладах.
   list конструкція (expression for element in iterable if condition)
Щоб записати до списку числа від 1 до 5 за допомогою comprehensions:
'''

# numbers = [i for i in range(1, 5+1)]

''' Попередній приклад із квадратами чисел від 1 до 5 можна переписати за допомогою comprehension: '''

# sq = [i ** 2 for i in range(1, 5+1)]

'''
   set
Для множин ситуація абсолютно аналогічна. Збережімо множини квадратів чисел зі списку:
'''

# numbers = [1, 4, 1, 3, 2, 5, 2, 6]
# sq = {i ** 2 for i in numbers}
# print(sq)   # {1, 4, 36, 9, 16, 25}

'''
    dict
Для словників синтаксис comprehension трохи відрізняється, оскільки потрібно явно вказати ключ та значення:
'''

# numbers = [1, 4, 1, 3, 2, 5, 2, 6]
# sq = {i: i ** 2 for i in numbers}
# print(sq)   # {1: 1, 4: 16, 3: 9, 2: 4, 5: 25, 6: 36}

'''
В цьому прикладі ми записали в словник sq числа від 1 до 5 у якості ключів, а їх квадрати як значення. Основна відмінність за синтаксисом — це двокрапка між ключем і значенням в лівій частині виразу
'''

"""
Метод isoformat() використовується для перетворення об'єкта дати і часу в рядок у форматі ISO 8601,
він має наступний вигляд: YYYY-MM-DDTHH:MM:SS.ssssss
де:
YYYY представляє рік (наприклад, "2023").
MM представляє місяць (наприклад, "10" для жовтня).
DD представляє день (наприклад, "23").
T є роздільником між датою та часом.
HH представляє години (від 00 до 23).
MM представляє хвилини (від 00 до 59).
SS представляє секунди (від 00 до 59).
ssssss представляє мікросекунди (опціонально).
"""
# from datetime import datetime
# now = datetime.now()
# iso_date_time = now.isoformat()
# print(iso_date_time)
# iso_date_time_timezone = now.isoformat() + now.astimezone().strftime('%z')
# print(iso_date_time_timezone)

''' Округлення чисел '''

"""
Згідно з офіційною документацією:

- ROUND_FLOOR: число округлюється до негативної нескінченності.
- ROUND_CEILING: число округлюється до нескінченності або позитивної нескінченності.
- ROUND_HALF_DOWN: числа округлюються до найближчого числа. Якщо є нічия, число округлюється до нуля. Зв'язки - це рівновіддалені числа, які можна округляти як у більшу, так і меншу сторону. Наприклад, таке число, як 4,25 можна округлити як у бік 4,2, так і 4,3.
- ROUND_HALF_UP: числа округлюються до найближчого числа. Якщо є нічия, число округлюється від нуля.
- ROUND_UP: число округлюється від нуля.
- ROUND_DOWN: число округлюється до нуля.
- ROUND_HALF_EVEN: числа округлюються до найближчого числа. Будь-які зв'язки округлюються до найближчого парного цілого числа.
- ROUND_05UP: числа округлюються від нуля, якщо останнє число дорівнює 0 або 5. Якщо ні, числа округлюються до нуля.

За замовчуванням округлення описується константою ROUND_HALF_EVEN
"""
# from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP

# num = Decimal('1.45')
# print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN))  # по замовчуванню від 6 by default 
# print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP))  # заокруглює по правилу від 5 

# print(Decimal('3.14159').quantize(Decimal('1.0')))