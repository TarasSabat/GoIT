"""
Метод search()
"""
# string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), " \
#          "і Еллен Адлер (1860-1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
#          "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного " \
#          "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826-1878) і Дженні Рафаел (1830-1902) " \
#          "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

# import re
# pattern = r'[0-9]+'             # те шо потрібно знайти, pattern завжди має бути з r 
# result = re.search(pattern, string)  
# print(result.span())            # повертає кортеж з індексами для зрізу

# first_index, second_index = result.span()
# print(string[first_index:second_index])  #  або print(result.group())

# print(result.group())

"""
Метод: findall шукає усі входження
"""

# import re

# string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), " \
#          "й Еллен Адлер (1860--1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
#          "на Нобелівську премію з фізіології або медицини[63]. Мати була донькою впливового та вельми заможного " \
#          "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826--1878) і Дженні Рафаел (1830--1902) " \
#          "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

# # Знайти всі цифри і їх кількість
# result = re.findall(r'\d', string)
# print(result)
# print(len(result))

# # Знайти всі числа і їх кількість
# result = re.findall(r'\d+', string)
# print(result)
# print(len(result))

# # Знайти всі роки
# result = re.findall(r'\d{4}', string)    # шукає числа з чотирма знаками
# print(result)
# result = re.findall(r'\d{2,4}', string)  # шукає числа з двома та чотирма знаками
# print(result)

"""
Метод: compile
Ми використаємо функцію compile щоб скомпілювати попередньо визначений патерн.
Потрібно, якщо використовуємо його часто в різних місцях програми.
"""

# import re

# string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), " \
#          "й Еллен Адлер (1860--1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
#          "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного " \
#          "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826--1878) і Дженні Рафаел (1830--1902) " \
#          "із британської єврейської банкірської династії Raphael Raphael & sons."

# # Знайти всі слова з великої літери
# pattern = re.compile(r'[А-ЯA-Z]\w*')
# result = pattern.findall(string)
# print(result)

# # Знайти всі слова
# pattern = re.compile(r'\w+')
# result = pattern.findall(string)
# print(result)

# # Знайти слово на початку строки
# pattern = re.compile(r'^[А-ЯA-Z]\w*')
# result = pattern.findall(string)
# print(result)

# # Знайти слово в кінці строки
# pattern = re.compile(r'\w+\.$')
# result = pattern.findall(string)
# print(result)

"""
Метод: split
​
Напишемо універсальну функцію get_parameters, яка повертатиме словник з даними.
Оскільки в першому рядку розділювачем є символ `;` а в другому `&`,
тому тут вдало підійде випадок (a|b - відповідає a або b)
"""

# import re

# url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;

# url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"  # &
# url = "data=value*data_1=value_1"
# ur2 = "dadddddddta=vaddddddlue%daddddta_1=valdddddue_1"

# def get_parameters(data: list) -> dict:
#     obj_query = {}
#     for element in data:
#         key, value = element.split('=')
#         obj_query.update({key: value.replace('+', ' ')})
#     return obj_query

# data = re.split(r';|&', url_query)
# print(data)

# data = re.split(r';|&|\*|%', url_search)
# print(data)

# data = re.split(r';|&|\*|%', url)
# print(data)
# data = re.split(r';|&|\*|%', ur2)
# print(data)
# # ['20850=ot-25-mp-do-47-mp', '23777=6-6-5', '38435=8-gb', '41404=16gb']
# # ['q=Cat+and+dog', 'ie=utf-8', 'oe=utf-8', 'aq=t']
# # ['data=value', 'data_1=value_1']

"""
Метод: sub => re.sub(pattern, repl, string, count=0, flags=0); Заміняє елемент
"""
# import re

# string = "The best language is Java and Java"
# print(re.sub(r'java', 'Python', string, 1, flags=re.IGNORECASE))
# # print(re.sub(r'java', 'Python', string, 1))

"""
Метод: sub
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
"""
# import re

# string = "Виключити із цієї [рядки групи] символів, [розташовані між] дужками [, ]."
# print(re.findall(r'\[.*?\]', string))

# s_string = re.sub(r'\[.*?\]', '', string)  # позбуваємось з цього рядка групи символів між дужками [, ]
# print(s_string)

# s_string = re.sub(r'\[|\]', '', string)  # позбуваємось скобок [, ]
# print(s_string)

# s_string = re.sub(r'\[.*?\]', '[]', string)  # видаляємо вміст у скобках
# print(s_string)

"""
Задача(ділить кожне слово по дві літери, знайт: перші дві букви кожного слова, пари років, групування)
"""""
# import re

# string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), " \
#          "й Еллен Адлер (1860-1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
#          "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного " \
#          "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826-1878) і Дженні Рафаел (1830-1902) " \
#          "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

# # ділить кожне слово по дві літери
# result = re.findall(r'[А-Яа-яa-zA-Zіїє]{2}', string)
# print(result)

# # Знайти перші дві букви кожного слова
# result = re.findall(r'\b[А-Яа-яa-zA-Zіїє]{2}', string)
# print(result)

# # Знайти пари років хххх-хххх
# result = re.findall(r'\d{4}-\d{4}', string)
# print(result)

# # Групування
# result = re.findall(r'(\d{4})-\d{4}', string)   # виводить ту частину яка в дужках
# print(result)

# result = re.findall(r'\d{4}-(\d{4})', string)   # виводить ту частину яка в дужках
# print(result)

"""
Завдання: Пошук email
- алфавіт, який використовується для назви email, - англійська
- префікс (все, що знаходиться до символу @) починається з латинської літери і може містити будь-яке число або літеру,
 включаючи нижнє підкреслення та символ крапки, складається щонайменше з двох символів
- суфікс почти (все, що знаходиться після символу @) складається тільки з букв англійського алфавіту,
складається з двох частин, розділених крапкою, і доменне ім'я верхнього рівня не може бути менше двох символів
 (все, що після крапки)
"""

# import re

# text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
#        "abc111@test.com 12Fool1@iana.org"
# result = re.findall(r'[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', text)
# print(result)
# ['Ima.Fool@iana.org', 'Fool1@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com', 'Fool1@iana.org']

"""
Задача: Пошук по url
"""

# import re

# text_url = "The main search site in the world is https://www.google.com The main social network for people in the " \
#            "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
#            "they share their code. some url to check https://www..facebook.com www.facebook.com " \
#            "https://www.app.facebook.com My site: https://localhost.info  https://api.io"

# # result = re.findall(r'https?:\/\/\w{3}\.?(?:\w+\.)*\w{2,5}', text_url)
# result = re.findall(r'https?:\/\/\w{3}\.?(?:\w+\.)+\w{2,5}', text_url)
# print(result)


'''
Задача: Пошук phone
Метод: match - шукає тільки на початку строки!!! аналог search
шаблон наступний: +380(67)777-7-777 або +380(67)777-77-77
'''

# import re

# phones = ['+380(66)964-0-547', '+06(37)306465', '+380(96)193-51-71', '+63264-3-973',
#           '+50832-52-00', '+000000000', '+487(30)283-9-18', '(98)622-35-75', '+380(29)794-7963']

# pattern = r'\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{}-\d{4}'

## або

# from re import search

# regexp = r'^\+?(38)?8?[ ]?[-(]?0\d{2}[- ) ]?[ ]?\d{3}[- ]?\d{2}[- ]?\d{2}$'
# phone_nombers = ['+380681231234', '12345', '0681231234', '380681231234', '38068 123 12 34', '+38 (068) 1231234', '+38 (068) 123 12 34', '068 123 12 34', '068-123-12 34', '068-123-12-34', '1 2 3', '1-2', '1 2-3', '+380681231234123', '+390681231234', '+30681231234']

# for number in phone_nombers:

#     result = search(regexp, number)

#     if result is None:
#         print(f'Negative - {number}')
#     else:
#         print(f'Positive - {result.group()}')

'''
Відфільтровування поганих слів НЕ ПРАЦЮЄ
'''
# bad_words = ['bad', 'mad', 'vodka']

# while True:
#     user_input = input()

#     for word in bad_words:
#         user_input = user_input.replace(word, '*' * len(word))

#     print(f'Me: {user_input}')    

'''Робота з текстами'''
# from re import  

# text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

# reg_exp = r'[^a-zA-Z0-9 ]' 
# normalized_text = text.lower()
# normalized_text = sub(reg_exp, '', normalized_text)

# words_list = normalized_text.split()
# unique_words_list = set(words_list)
# n_words = len(words_list)
# n_unique_words = len(unique_words_list)

# words_quantity = {}

# for word in unique_words_list:
#     words_quantity[word] = normalized_text.count(word)

# words_quantity_list = list(words_quantity.items())

# def sort_by_quantity(element):
#     return element[1]

# words_quantity_list.sort(key=sort_by_quantity, reverse=True)

# # print(n_words)              
# print(words_quantity_list)   # виведення відсортованого теексту з кількістю повторюваності 

'''
Робота регулярних виразів
'''
# from re import search
## Якра (anchor)
# result = search('^Hello', 'Hello world') # якщо ^ стоїть на початку значить ми шукаємо строку, яка починається з  Hello
# result = search('world$', 'Hello world') # якщо $ стоїть в кінці строки шукаємо строку, яка закінчується на world
# result = search('^world$', 'Hello world') # якщо на початку є ^ а в кінці строки $ шукаємо строку яка складається з world
# result = search('world', 'Hello world') # якщо немає якорів ^ чи $ шукає усі строки які містять слово world

## Квантіфаєри (quantifiers)
# result = search('l*', 'Hello world') # якщо в строці є 0 або більше символів l
# result = search('worlds*', 'Hello world') # якщо в строці є worlds або world
# result = search('worlds+', 'Hello world') # якщо в строці є worlds хотя б один раз
# result = search('worlds?', 'Hello worldsss') # якщо в строці є 0 або 1 worlds в строці

# result = search('worlds{3}', 'Hello world') # якщо в строці є worlds p 3-ма символами s
# result = search('worl(ds)?', 'Hello world') # групування поля дії квантіфаєра, ?  діє на символи в дужках
# result = search('world (s|e)?', 'Hello world') # якщо в кінці строки буде або s або e
# result = search('world [se]', 'Hello world') # аналогічно |, можуть бути дапазони [a-d], [1-3], [^1-3] - заперечення (тільки не символ [1-3])


