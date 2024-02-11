'''У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. 
Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. 
Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення 
та повертає суму платежу наприкінці місяця.'''

# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum += value
#     return sum  
    
# print(amount_payment([1, -3, 4]))

'''При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати 
з даними далі. Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, 
сортує його в порядку зростання і повертає змінений список як результат.'''
    
# def prepare_data(data):
#     res = sorted(data)
#     res.pop(0)
#     res.pop()

#     return res

# print(prepare_data([4, 1, 3, 5, 2]))

'''Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, 
а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar

Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів 
["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з його елементів 
в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.'''

# def format_ingredients(items):
#     if len(items) > 2:
#         items_1 = ', '.join(items[: -1])
#         items_2 = ''.join(items[-1])
#         items_f = (f"{items_1} {'and'} {items_2}")
#         return items_f
    
#     elif len(items) == 0:
#         items_f = ''.join(items)
#         return items_f
    
#     else:
#         items = items[0]
#         items_f = ''.join(items)
#         return items_f
    
# print(format_ingredients([]))

'''Сучасна система оцінок в університеті має такий вигляд:

Оцінка	Бали	Оцінка ECTS     Пояснення
1	    0-34	    F	        Unsatisfactorily
2	    35-59	    FX	        Unsatisfactorily
3	    60-66	    E	        Enough
3	    67-74	    D	        Satisfactorily
4	    75-89	    C	        Good
5	    90-95	    В	        Very good
5	    96-100	    A	        Perfectly
Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії, get_grade приймає ключ у вигляді оцінки ECTS, і має повертати відповідну п'ятибальну оцінку (перший стовпчик таблиці). Друга get_description теж приймає ключ у вигляді оцінки ECTS, але повертатиме пояснення оцінки в текстовому форматі (останній стовпчик таблиці) і буде використана в електронній заліковій книжці студента. На відсутній ключ функції повинні повертати значення None.'''

# def get_grade(key):
#     ects_rating = {'F':1, 'FX':2, 'E':3, 'D':3, 'C':4, 'B':5, 'A':5}
#     return ects_rating.get(key)
    
# def get_description(key):
#     ects_rating = {'F':'Unsatisfactorily', 
#                    'FX':'Unsatisfactorily', 
#                    'E':'Enough', 
#                    'D':'Satisfactorily', 
#                    'C':'Good', 
#                    'B':'Very good', 
#                    'A':'Perfectly'
#                    }
#     return ects_rating.get(key)

# key = 'D'
# print(get_grade(key))
# print(get_description(key))

'''Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику. Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти. Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо.'''

# def lookup_key(data, value):
#     my_list =[]
#     for key, val in data.items():
#         if val == value:
#             my_list.append(key)
#     return my_list

'''У нас є список показників студентів групи – це список з отриманими балами з тестування. Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку та ділить його на два списки. У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.'''

# def split_list(grade):
#     if len(grade) == 0:
#         return [], []
#     else:    
#         avg = sum(grade) / len(grade)
#         list_1 = []  
#         list_2 = []
#         for value in grade:
#             if value <= avg:
#                 list_1.append(value)
#             else:
#                 list_2.append(value)
#         list = [list_1, list_2]
#         return tuple(list)

# print(split_list([1, 12, 3, 24, 5]))

'''Є чотирикутна схема польотів дронів з координатами (0, 1, 2, 3). У нас є словник points, ключі якого — кортежі, точки польоту між координатами чотирикутника, вигляду (1, 2). Значення словника — це відстані між вказаними точками.
Приклад:
points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
Напишіть функцію calculate_distance, яка на вхід приймає список координат чотирикутника зі словника виду [0, 1, 3, 2, 0]. Функція повинна підрахувати, використовуючи вказаний словник, яку загальну відстань пролетить дрон, рухаючись між точками польоту.
Примітки:
коли беремо у словника points значення, у ключі кортежі завжди має бути першою координата з меншим значенням — (2, 3), але не (3, 2);
для порожнього списку та списку з однією координатою функція calculate_distance має повертати 0.'''

# Варіант чужий 2
# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }


# def calculate_distance(coordinates):
#     distanse = 0
      
#     for point in range(len(coordinates)-1):
#         if len(coordinates) <=1:
#             return 0
        
#         point_next = [coordinates[point], coordinates[point+1]]
#         distanse += points[(min(point_next), max(point_next))]
#     return distanse
        
'''Потрібно написати функцію реалізації наступного ігрового алгоритму. На вхід функції game подається два аргументи: список, що складається зі списків, та початкове значення power - енергія гравця. Внутрішні списки — це списки з числовим значенням енергії, які може поглинути гравець, якщо вони менші або дорівнюють його енергії. Після поглинання елементу списку він рухається за списком далі та, або поглинає список повністю до кінця, або, якщо знаходить енергію вище за власну, залишає його і переходить до наступного списку. Наприкінці обходу всіх списків функція повинна повернути загальну отриману енергію гравця.
Приклад списку:
[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
Для цього списку і початкової енергії рівної 1 гравець поглине з першого списку перші два значення і залишить його, зустрівши значення 5, через те, що на цей момент матиме енергію в 3. Другий список пропустить відразу, а третій повністю поглине та отримає остаточну енергію в 6.'''

# def game(terra, power):
#     player_power = power
#     for layer in terra:
#         for line in layer:
#             if player_power >= line:
#                 player_power += line
#             else:
#                 break
#     return player_power

# print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))

'''Всім відомо, що для доступу до кредитної картки банку потрібний пін-код. Класично склалося, що це поєднання чотири цифри. Нам необхідно вирішити наступне програмістське завдання. Є підготовлений перелік пін-кодів. Напишіть функцію is_valid_pin_codes, яка буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр і повертати логічне значення — валідний список чи ні. Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, всі вони зберігаються у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.
Приклад аргументу для функції is_valid_pin_codes:
['1101', '9034', '0011']
Якщо список відповідає всім поставленим умовам, функція повертає логічне значення True. Якщо хоч одну з умов порушено, повертається значення — False. Передбачити перевірку на порожній список в аргументі функції та повернути при цьому значення False.'''

# def is_valid_pin_codes(pin_codes):
#     if not pin_codes:    # пустий pin_codes це False а not False дає True і if виконується       
#         return False                    
    
#     seen_pins = set()
    
#     for pin in pin_codes:  # присвоєння значення для pin відбувається блоками '1101' потім '9034' і '0011'
#         if len(pin) != 4 or not pin.isdigit() or pin in seen_pins:
#             return False
#         seen_pins.add(pin)
    
#     return True 

# print(is_valid_pin_codes(['1101', '9034', '0011']))

'''Браузер Chrome пропонує нам згенеровані випадкові паролі для сайтів та вебзастосунків. Ми потренуємось розв'язувати подібні завдання. Розіб'ємо завдання на три етапи. Перший етап — створіть функцію get_random_password, яка буде генерувати випадковий рядок пароля.
Вимоги:
у пароля має бути 8 символів.
для шифрування пароля будемо використовувати наступний набір символів:
()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
Ці символи лежать у межах від 40 до 126 коду в таблиці ASCII включно, і доступ до них можна отримати за допомогою функції chr.
chr(40)  # (
chr(126)  # ~
Щоб отримати випадкове ціле значення із заданого діапазону, ми використовуємо стандартний модуль Python random та його функцію randint. Вона має виклик виду randint(A, B) і повертає випадкове ціле число N, A ≤ N ≤ B.
from random import randint
random_num = randint(40, 126)
Після виконання коду в змінній random_num буде знаходитися випадкове ціле число від 40 до 126 включно.
Таким чином функція get_random_password має випадковим чином вибрати із запропонованого діапазону 8 символів та повернути згенерований пароль у вигляді рядка.'''

# from random import randint

# def get_random_password():
#     result = ''
#     count = 0
#     while count < 8:
#         result += chr(randint(40, 126))
#         count += 1
#     return result

# print(get_random_password())

'''Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.
Критерії надійного пароля:
Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.'''

### Варіант 1
# def is_valid_password(password):
#     if len(password) != 8:
#         return False
#     if any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password) and any(ch.islower() for ch in password):
#         return True
#     else:
#         return False
    
# print(is_valid_password('S|1QY(Cb'))

### Варіант 2 
# def is_valid_password(password):
#     if len(password) != 8:
#         return False

#     has_upper = False
#     has_lower = False
#     has_num = False

#     for ch in password:
#         if has_upper and has_lower and has_num:
#             return True
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_num = True
    
#     return has_upper and has_lower and has_num   

'''І, нарешті, третій, останній етап. Використовуючи рішення із попередніх двох завдань, напишіть функцію get_password, яка згенерує нам випадковий надійний пароль та поверне його. Алгоритм простий — ми генеруємо пароль за допомогою функції get_random_password і, якщо він проходить перевірку на надійність функцією is_valid_password, повертаємо його, якщо ні — повторюємо ітерацію знову.
Примітка: Хорошою практикою буде обмежити кількість спроб (наприклад, до 100), щоб не отримати нескінченний цикл.'''

# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result


# def is_valid_password(password):
#     if len(password) != 8:
#         return False

#     has_upper = False
#     has_lower = False
#     has_num = False

#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_num = True

#     return has_upper and has_lower and has_num


# def get_password():
#     flag = True
#     current = 0

#     while flag:
#         my_pas = get_random_password()
#         flag = False if is_valid_password(my_pas) else True
#         current += 1 
#         if current == 100:
#             break
    
#     return my_pas

'''Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. Функція повинна просканувати директорію path та повернути кортеж із двох списків. Перший — це список файлів усередині директорії, другий — список директорій.
Приклад виводу функції:
(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 'module-06', 'module-07',
  'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])'''

# from pathlib import Path

# def parse_folder(path):
#     files = []
#     folders = []

#     for el in path.iterdir():
#         if el.is_dir():
#             folders.append(el.name)
#         else:
#             files.append(el.name)

#     return files, folders

# p = Path('d:/IT/GoIT/Modul_3')
# print(parse_folder(p))

'''Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, розділених пробілами. Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція parse_args повинна повернути рядок наступного виду 'first second'.'''

# import sys

# def parse_args():
#     result = " ".join(sys.argv[1:])

#     return result