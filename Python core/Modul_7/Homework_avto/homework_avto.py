''' № 1
Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict), яка буде викликати функцію setup з параметрами зі словника args_dict.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
# from setuptools import setup


# def do_setup(args_dict):
#     setup(
#         name=args_dict['name'],
#         version=args_dict['version'],
#         description=args_dict['description'],
#         url=args_dict['url'],
#         author=args_dict['author'],
#         author_email=args_dict['author_email'],
#         license=args_dict['license'],
#         packages=args_dict['packages'],
#     )
   
# print(do_setup({
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }))

''' № 2
Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами зі словника args_dict та параметром install_requires, який набуває значення requires.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
# from setuptools import setup


# def do_setup(args_dict, requires):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires = requires)
    
''' № 3
Продовжуємо модифікувати приклад. Для функції do_setup необхідно передбачити третій параметр, який буде словником, де ми можемо вказати список "точок входу" для ключа console_scripts.
Функція do_setup(args_dict, requires, entry_points) повинна викликати функцію setup з параметрами словника args_dict та параметром install_requires, який набуває значення requires. Третій параметр entry_points приймає словник, де ми можемо вказати список "точок входу" для ключа console_scripts.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
# from setuptools import setup


# def do_setup(args_dict, requires, entry_points):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,
#           entry_points={'console_scripts':entry_points['console_scripts']}
#           )
''' № 4
Далі підуть завдання на повторення та закріплення матеріалу. Можна використовувати будь-які техніки, з якими ви зіткнулися у процесі навчання. І почнемо ми з функцій.
У Python існує рядкова функція isdigit(). Ця функція повертає True, якщо всі символи в рядку є цифрами, і є принаймні один символ, інакше — False. Напишіть функцію з ім'ям is_integer, яка розширюватиме функціональність isdigit(). При перевірці рядка необхідно ігнорувати початкові та кінцеві прогалини в рядку. Після виключення зайвих прогалин рядок вважається таким, що представляє ціле число, якщо:
її довжина більша або дорівнює одному символу
вона повністю складається з цифр
передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри
'''
# import re

# def is_integer(s):
#     s = s.strip().removeprefix('-').removeprefix('+')
#     r = re.search('\D+', s) is None     
#     if len(s) <= 0:
#         return False
#     else:
#         return r

    
# print(is_integer('      '))

''' № 5 
Дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало масовим явищем в еру мобільних. пристроїв. Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом і повертатиме рядок з відновленими великими літерами.
Функція повинна:
зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини
'''
# def capital_text(s):  
#     result = ""
#     capitalize_next = True
#     for char in s:
#         if capitalize_next and char.isalpha():
#             result += char.upper()
#             capitalize_next = False
#         else:
#             result += char
#         if char in [".", "!", "?"]:
#             capitalize_next = True
#     return result
    

# print(capital_text('  зробити великою. першу літеру! в рядку? попри прогалини  '))

''' № 6 
Параметри функції:
riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
'''
# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     if reverse:
#         riddle = riddle[::-1]
#         word_start = riddle.find(start_letter)
#         word = riddle[word_start: word_start+word_length] 
        
#     else:        
#         word_start = riddle.find(start_letter)
#         word = riddle[word_start: word_start+word_length] 
        
#     return word

# print(solve_riddle('terpower1im', 5, 'p', reverse=False))

''' № 7
У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.
При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. Напишіть функцію data_preparation, яка приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).
Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи. Після видалення даних з кожного списку необхідно злити їх разом в один список, відсортувати його за зменшенням та повернути отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
'''
# Варіант 1
# def data_preparation(list_data):
#     list_end = []
#     for el in list_data:
#         if len(el) > 2:
#             el.sort()
#             el.pop(0)
#             if len(el) > 2:
#                 el.pop(-1)
#                 list_end.extend(el)
#                 continue
#             list_end.extend(el)
#             continue
#         else:
#             list_end.extend(el)
#             continue
#     list_end.sort()
#     list_end.reverse()
#     return list_end

# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))

## Варіант 2
# def data_preparation(list_data):
#     list_end = []
#     for el in list_data:
#         if len(el) > 2:
#             el.remove(min(el))
#             if len(el) > 2:
#                 el.remove(max(el))
#                 list_end.extend(el)
#                 continue
#             list_end.extend(el)
#             continue
#         else:
#             list_end.extend(el)
#             continue
#     list_end.sort()
#     list_end.reverse()
#     return list_end

# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))

'''№ 8
Підсумкове завдання модуля два було на обчислення арифметичного виразу. У задачі на повторення ми підемо трохи іншим       
шляхом і виконаємо схоже завдання, одночасно закріпивши знання роботи зі рядками та списками. Розбиття рядка на 
лексеми є процес перетворення вихідного рядка в список з підрядків, званих лексемами (token).
В арифметичному виразі лексемами є: оператори, числа та дужки. Операторами у нас будуть такі символи: *, /, 
- та +. Оператори та дужки легко виділити у рядку — вони складаються з одного символу і ніколи не є частиною інших 
лексем. Числа виділити складніше, оскільки ці лексеми можуть складатися з кількох символів. Тому будь-яка безперервна                                        
послідовність цифр — це одна числова лексема.
Напишіть функцію, яка приймає параметр рядок, що містить математичний вираз, і перетворює його в список лексем.   
Кожна лексема має бути або оператором, або числом, або дужкою.
Приклад:
"2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
З метою спрощення вважаємо, що числа можуть бути тільки цілими, і вхідний рядок завжди міститиме математичний вираз, 
що складається з дужок, чисел та операторів.
Зверніть увагу, що лексеми можуть відокремлюватися один від одного різною кількістю прогалин, а можуть і не   
відокремлюватися зовсім. Прогалини не є лексемами та до підсумкового списку потрапити не повинні.
'''
# import re
# def token_parser(s):
#     # s = s.replace(" ", "") може і не бути
#     tokens = re.findall(r'\d+|[-+*/()]', s)
#     return tokens
#
# print(token_parser("2+ 34-5 * 3"))

'''№ 9
Підсписком (sublist) називають список, що є складовою більшого списку. Підсписок може містити один елемент, множину елементів або бути порожнім.
Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4] не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.
Порожній список є підсписком будь-якого списку.
Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.
Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].
Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].
'''
# def all_sub_lists(data):
#     if not data:
#         return [[]]
    
#     new_sublist = [[]]
#     for length in range(1, len(data) + 1):
#         for i in range(0, len(data) - length + 1):
#             new_sublist.append(data[i: i + length])

#     return new_sublist
        
# print(all_sub_lists([1, 2, 3]))

'''№ 10
При роботі веб-сервісів спілкування, за протоколом HTTP, найчастіше відбувається в форматі JSON. І надсилання даних на сервер при запиті POST - це необхідність використовувати словник, оскільки структура формату JSON ідентична словнику Python.
Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у вигляді словника. Дана функція make_request(keys, values) приймає два параметри у вигляді списків. Функція повинна створити словник із ключами з списку keys та значеннями зі списку values.
Порядок відповідності збігається з індексами списків keys та values.
Якщо довжина keys та values не збігаються, поверніть порожній словник.
'''
## Варіант 1
# def make_request(keys, values):
#     if len(keys) != len(values):
#         return {}
    
#     dict_end = {}
#     for k, v in zip(keys, values):
#         dict_end[k] = v
               
#     return dict_end

# print(make_request([1,2,3], ['one', 'twu', 'three']))

## Варіант 2
# def make_request(keys, values):
#     key_t = []
#     dict_end = {}
#     n = 0
#     if len(keys) != len(values):
#         return {}
        
#     for key in keys:
#         key_t.append(key)
           
#     for value in values:
#         dict_end[key_t[0+n]] = value
#         n+=1
       
#     return dict_end

# print(make_request([1,2,3], ['one', 'twu', 'three']))

'''№ 11
Як ви знаєте, раніше телефони були з кнопками, та й зараз вони є подекуди у вжитку. Тоді текстові повідомлення набиралися за допомогою цифрових кнопок. Як інженери телефонів створили набір тексту? Рішення було в тому, що одна кнопка була асоційована одночасно з декількома літерами, а вибір залежав від кількості натискань на кнопку. Одноразове натискання призводило до появи першої літери у відповідному цій кнопці списку, наступні натискання змінювали її на наступну.
Символи, що відповідають кнопкам на телефонах
Кнопка	Символи
1	. , ? ! :
2	A B C
3	D E F
4	G H I
5	J K L
6	M N O
7	P Q R S
8	T U V
9	W X Y Z
0	Пробіл
Напишіть функцію sequence_buttons, що показує послідовність кнопок, яку необхідно натиснути, щоб на екрані телефону з'явився текст, введений користувачем.
Створіть словник, який відповідає символам з кнопками, які потрібно натиснути.
Приклад: якщо функції sequence_buttons передати рядок "Hello, World!", функція повинна повернути "4433555555666110966677755531111".
Вимоги:
функція коректно обробляє малі та великі літери.
функція ігнорує символи, що не входять до зазначеного списку
'''
# def sequence_buttons(string):
    
#     num_str = ""

#     NUMVAL_DICT = {
#         '.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111,
#         'A': 2, 'B': 22, 'C': 222,
#         'D': 3, 'E': 33, 'F': 333,
#         'G': 4, 'H': 44, 'I': 444,
#         'J': 5, 'K': 55, 'L': 555,
#         'M': 6, 'N': 66, 'O': 666,
#         'P': 7, 'Q': 77, 'R': 777, 'S': 7777,
#         'T': 8, 'U': 88, 'V': 888,
#         'W': 9, 'X': 99, 'Y': 999, 'Z': 9999,
#         ' ': 0
#     }
#     string = string.upper()
#     for k in string:
#         num_str += str(NUMVAL_DICT[k])
#     return num_str       
        
    
# print(sequence_buttons("Hello, World!"))

'''№ 12
Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), яка додає додаткову інформацію в файл на шляху path з параметра additional_info, і після цього повертає рядок з позиції start_pos довжиною count_chars.
Вимоги:
функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
записувати в кінець файлу рядок additional_info
після запису функція має відкрити той самий файл для читання
прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read.
'''
# def file_operations(path, additional_info, start_pos, count_chars):
#     with open(path, 'a') as file_a:
#         file_a.write(additional_info)
#     with open(path, 'r') as file_r:
#         file_r.seek(start_pos)
#         file_r.read(count_chars)

'''№ 13
Є файл зі списком працівників компанії. У кожному рядку файлу записано інформацію лише одного співробітника. Формат запису, в межах навчання приймемо спрощений, такий як: ім'я співробітника, символ пропуску та його посада, тобто, ким він працює.
John courier
Pipe cook
Створіть функцію get_employees_by_profession(path, profession). Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)
Вимоги:
відкрийте файл за допомогою with для читання
отримайте рядки з файлу за допомогою методу readlines()
за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
об'єднайте всі ці рядки в списку в один рядок за допомогою методу join (пам'ятайте про символ перенесення рядків '\n' та зайві прогалини, які треба прибрати)
приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
поверніть отриманий рядок із файлу
'''
# def get_employees_by_profession(path, profession):
#     file_list = []
    
#     with open(path, 'r') as file_r:
#         lines = file_r.readlines()
#         for line in lines:
#             if line.find(profession) != -1:
#                 file_list.append(line.strip('\n'))

#     result = ''.join(file_list).replace(profession, '')
#     result = result.strip()
#     return result
    
# print(get_employees_by_profession('D:\IT\GoIT\Modul_7\\test.txt', 'courier' ))

'''№ 14
Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.
Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.
Нумерація рядків іде від 0.
'''
# def to_indexed(source_file, output_file):
#     with open(source_file, 'r') as file_r, open(output_file, 'w') as file_w:
#         for idx, line in enumerate(file_r, start = 0):
#             file_w.write('{}: {}'.format(idx, line))

# print(to_indexed('test.txt', 'test_2.txt'))

'''№ 15
Рекурсія добре підходить до задачі flatentening. Це процес вирівнювання списків, який полягає в позбавленні вкладеної структури. Наприклад список вигляду [1, 2, [3, 4, [5, 6]], 7] має бути перетворений на плоский (flat) список [1, 2, 3, 4, 5, 6, 7]
Напишіть функцію flatten, яка приймає на вхід список, рекурсивно вирівнюватиме цей список і повертатиме пласку версію списку.
Для виконання завдання можна дотримуватися наступного алгоритму:
Якщо вхідний список порожній, то:
  Повертаємо порожній список
Якщо перший елемент списку є списком, то:
  Отримуємо перший список, рекурсивно викликавши функцію з першим елементом списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків
Якщо перший елемент списку не є списком, то:
  Отримуємо перший список із першого елемента списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків
'''
## Варіант 1
# def flatten(data):
#     if not data: 
#         return []
#     result = []
#     for i in data:
#         if isinstance(i, list):
#             result.extend(flatten(i))
#         else:
#             result.append(i)
#     return result

## Варіант 1
# def flatten(data): 
#     if not data: 
#         return []
#     if isinstance(data[0], list): 
#         return flatten(data[0]) + flatten(data[1:]) 
#     else: 
#         return [data[0]] + flatten(data[1:]) 

'''№ 16
Розберемо просту техніку кодування та декодування на основі серій. Наприклад, у нас є список із повторюваними спостереженнями якоїсь величини, вона може приймати значення X, Y або Z. Значення з'являються у довільному порядку та зберігаємо ми їх у списку ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] або рядку "XXXZZXXYYYZZ".
Внаслідок чого ми можемо зменшити обсяг інформації, що зберігається? Стиснення можна досягти заміною групи повторюваних значень на одноразове значення та лічильник повторів: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
Напишіть рекурсивну функцію decode для декодування списку, закодованого цим способом. Як аргумент функція приймає закодований список. Функція має повернути розшифрований список елементів.
'''
# def decode(data):
#     if len(data) == 0:
#         return []
#     key = data[0]
#     value = data[1]
#     return ([key] * value) + decode(data[2:])


# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

'''№ 17
Повернемося до попереднього завдання та виконаємо зворотне. Напишіть рекурсивну функцію encode для кодування списку або рядка. Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''
## Варіант № 1
# def encode(data):
#     if not data:
#         return []
    
#     current = data[0]
#     count = 0
    
#     for i in data:
#         if i == current:
#             count += 1
#         else:
#             break

#     if count > 1:
#         return [current, count] + encode(data[count:])
#     else:
#         return [current, count] + encode(data[1:])


# print(encode(["X", "X", "X", "X", "X", "Z", "X", "Y", "Y", "Y", "Y", "Z", "Z"]))

## Варіант № 2
# def encode(data):
#     if not data:
#         return []
    
#     current = data[0]
#     count = 1
    
#     for i in range(1, len(data)): 
#         if data[i] == current:      
#             count += 1
#         else:
#             break

#     if count > 1:
#         return [current, count] + encode(data[count:])
#     else:
#         return [current, count] + encode(data[count:])


# print(encode(["X", "X", "X", "X", "X", "Z", "X", "Y", "Y", "Y", "Y", "Z", "Z"]))