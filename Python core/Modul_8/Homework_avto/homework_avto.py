''' № 1
Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).
Підказки:
Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
datetime приймає аргументи типу int, використовуйте перетворення типів.
ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.
'''
# from datetime import datetime

# def get_days_from_today(date):
#     datetime_now = datetime.now()
    
#     date_datetime = datetime.strptime(date, '%Y-%m-%d')
    
#     time_delta = (datetime_now-date_datetime).days
   
#     return time_delta

# print(get_days_from_today('2020-10-09'))

''' № 2
Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.
'''
# from datetime import date

# def get_days_in_month(month, year):
   
#     if month == 12:
#         start_day = date(year, month -1, day = 1)
#         end_day = date(year, month, day = 2) 
#         day = (end_day - start_day).days
#     else:
#         start_day = date(year, month, day = 1)
#         end_day = date(year, month + 1, day = 1) 
#         day = (end_day - start_day).days
#     return day

# print(get_days_in_month(2, 2000))

''' № 3
Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику.
'''
# from datetime import datetime

# def get_str_date(date):
#     d = datetime.fromisoformat(date[:-1])
#     d_str = d.strftime('%A %d %B %Y')  
#     return d_str
   
# print(get_str_date('2021-05-27 17:08:34.149Z'))

''' № 4
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
Напишіть функцію, яка випадково підбиратиме набір чисел для лотерейного квитка. Серед цих чисел не має бути дублікатів.
Формат функції get_numbers_ticket(min, max, quantity), де параметри:
min - мінімальне значення діапазону, не може бути менше 1
max - максимальне значення діапазону, не може бути більше 1000
quantity - кількість чисел у наборі (має бути min < quantity < max)
Функція повинна повернути перелік випадкових чисел за зростанням. Якщо порушено умови обмежень на параметри функції, тоді повернути пустий список.
'''

# import random  
# from random import randrange

# def get_numbers_ticket(min, max, quantity):
#     if min < 1 or max > 1000 or quantity <= min or quantity >= max:
#         return []
    
#     list_rand = list(range(min, max+1)) 
#     return sorted(random.sample(list_rand, quantity))
    
# print(get_numbers_ticket(1, 1000, 2))

''' № 5
Ви проводите розіграш кавоварок Bosch серед зареєстрованих користувачів вашої інтернет-сторінки.
Список зареєстрованих користувачів — це словник такого типу:
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}
Ключ словника — це унікальний ідентифікатор бази даних MongoDB, а значення &mdash це email користувача. Вам необхідно випадково відібрати декілька переможців розіграшу.
Створіть функцію get_random_winners(quantity, participants), яка повертатиме список унікальних ідентифікаторів бази даних зі словника participants в кількості quantity. Це буде список переможців
Вимоги:
Отримайте перелік ключів словника. (Після виконання методу keys() використовуйте перетворення типів)
Перемішайте отриманий список за допомогою методу shuffle
Виберіть випадкових переможців, використовуючи метод sample.
Якщо передана кількість переможців більша за кількість користувачів (quantity > len(participants)) — поверніть порожній список.
Наприклад: виклик get_random_winners(2, participants) може повернути список з випадковим набором ідентифікаторів як: ['60577ce4b536f8259cc225d2', '605b89080c318d66862db390'].
'''
# import random

# def get_random_winners(quantity, participants):
#     if quantity > len(participants):
#         return []
    
#     keys_list = []
#     for i in participants.keys():
#         keys_list.append(i)
#         random.shuffle(keys_list)
#     return random.sample(keys_list, k=quantity) 
    
# print(get_random_winners(2 , {"603d2cec9993c627f0982404": "test@test.com", "603f79022922882d30dd7bb6": "test11@test.com",
                        # "60577ce4b536f8259cc225d2": "test2@test.com", "605884760742316c07eae603": "vitanlhouse@gmail.com",
                        # "605b89080c318d66862db390": "elhe2013@gmail.com",}))

''' № 6
Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. Параметр number_list — список чисел
Увага
Не забувайте приводити всі числа у списку до типу `decimal`
Приклад:
виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
'''
# from decimal import Decimal, getcontext

# def decimal_average(number_list, signs_count):
#     sum = 0
#     for i in number_list:
#         sum += Decimal(str(i))
#     ar_mean = sum/len(number_list)
#     return ar_mean

# print(decimal_average([31, 55, 177, 2300, 1.57], 9))

''' № 7
У нас є іменований кортеж для зберігання котів у змінній Cat. На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.
Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.
Якщо функція convert_list приймає у параметрі cats список іменованих кортежів
[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
То функція поверне наступний список словників:
[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
І в той же час, якщо функція convert_list приймає в параметрі cats список словників, то результатом буде зворотна операція та функція поверне список іменованих кортежів.
Для визначення типу параметра cats використовуйте функцію isinstance.
'''
# from collections import namedtuple

# Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

# def convert_list(cats):
#     if isinstance(cats, list) and all(isinstance(cat, Cat) for cat in cats):
#         return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
#     elif isinstance(cats, list) and all(isinstance(cat, dict) for cat in cats):
#         return [Cat(cat['nickname'], cat['age'], cat['owner']) for cat in cats]
#     else:
#         raise ValueError("Неправильний тип вхідного параметру cats")
    
''' № 8
Є список IP адрес:
IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.
Приклад:
{
    '85.157.172.253': 2,
    ...
}
Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.
Пример:
('66.50.38.43', 4)
'''
# from collections import Counter

# def get_count_visits_from_ip(ips):
#    ip = Counter(ips)
#    return ip

# def get_frequent_visit_from_ip(ips):
#     ip = Counter(ips)
#     mc_ip = ip.most_common(1)
#     mc_ip_tuple = mc_ip[0] 
#     return mc_ip_tuple

# print(get_count_visits_from_ip(['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236']))
# print(get_frequent_visit_from_ip(['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236']))

''' № 9
LIFO (англ. last in, first out, "останнім прийшов - першим пішов") - спосіб організації даних або іншими словами Стек (Stack). У структурованому лінійному списку, організованому за принципом LIFO, елементи можуть додаватися та вибиратися тільки з одного кінця, що називається «вершиною списку». Структура LIFO може бути проілюстрована наступним малюнком.
lifo
За допомогою колекції deque реалізуйте структуру даних LIFO. Створіть змінну lifo, що містить колекцію deque. Обмежте розмір за допомогою константи MAX_LEN. Функція push додає значення element на початок списку lifo. Функція pop дістає та повертає перше значення зі списку lifo.
'''
# from collections import deque

# MAX_LEN = 5

# lifo = deque(maxlen=MAX_LEN)


# def push(element):
#     lifo.appendleft(element)

# def pop():
#     return lifo.popleft()

''' № 10
FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних або іншими словами черга. Цей вислів описує принцип технічної обробки черги чи обслуговування конфліктних вимог шляхом впорядкування процесу за принципом: "першим прийшов - першим обслужений" (ПППО). Той, хто приходить першим, той і обслуговується першим, хто прийде наступним чекає, поки обслуговування першого не буде закінчено, і таке інше.
За допомогою колекції deque реалізуйте структуру даних FIFO. Створіть змінну fifo, що містить колекцію deque. Обмежте розмір за допомогою константи MAX_LEN. Функція push додає значення element до кінця списку fifo. Функція pop дістає та повертає перше значення зі списку fifo.
'''
# from collections import deque

# MAX_LEN = 5

# fifo = deque(maxlen=MAX_LEN)

# def push(element):
#     fifo.append(element)

# def pop():
#     return fifo.popleft()

