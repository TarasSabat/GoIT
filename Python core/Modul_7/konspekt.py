''' Структура пакету: 
Припустимо у вас є пакет useful. У цьому пакеті є модулі some_code.py та another_code.py. У цих модулях знаходиться код, який виконує корисну роботу.
Щоб ваш пакет можна було встановити, вам варто розмістити сам пакет всередині папки, яка називається так само:
'''
# useful/
#     useful/
#         __init__.py
#         some_code.py
#         another_code.py
#     setup.py
'''
Поряд з самим пакетом варто розмістити модуль з інструкціями зі встановлення — setup.py. До вмісту setup.py ми повернемося трохи пізніше, а поки що продовжимо розгляд структури пакету.
Python за замовчуванням проігнорує під час встановлення усі файли, які не закінчуються на .py Якщо у вашому пакеті не буде __init__.py, то вміст useful/useful/ теж буде проігноровано (сподіваюся це виправлять в наступних версіях). Назва пакету повинна відповідати вимогам до імен змінних Python.
'''

''' setup.py
Модуль, що містить інструкції зі встановлення, викликає функцію setup з пакету setuptools. Функція setup здійснює встановлення пакету в системі і містить параметри, що конфігурують встановлення.
Детальні інструкції з написання setup.py ви можете отримати на сторінці документації.
Приклад вмісту setup.py:'''

# from setuptools import setup

# setup(name='useful',
#       version='1',
#       description='Very useful code',
#       url='http://github.com/dummy_user/useful',
#       author='Flying Circus',
#       author_email='flyingcircus@example.com',
#       license='MIT',
#       packages=['useful'])
'''
В цьому прикладі ми викликаємо setup з додатковими інформаційними параметрами, які будуть доступні користувачам. А саме, ми вказали ім'я пакету, версію, короткий опис пакету, адресу, де можна подивитися початковий код, ім'я автора, його email, ліцензію, набір пакетів, які містяться у постачанні.
Що, якщо наш пакет досить великий і прописувати вручну усі модулі packages незручно, та існує ризик помилитися? Тоді у setuptools є функція find_namespace_packages, яка допоможе знайти всі модулі і не пропустити нічого:'''

# from setuptools import setup, find_namespace_packages

# setup(
#     name='useful',
#     version='1',
#     description='Very useful code',
#     url='http://github.com/dummy_user/useful',
#     author='Flying Circus',
#     author_email='flyingcircus@example.com',
#     license='MIT',
#     packages=find_namespace_packages()
# )
'''
Такий пакет можна опублікувати на PyPi і тоді його можна буде встановити за допомогою pip, або опублікувати початковий код, і тоді можна буде встановити з початкових кодів.
Щоб встановити цей пакет з початкового коду, виконайте в консолі pip install . або pip install -e . у папці, де лежить setup.py.'''

'''
Додавання не py файлів у пакет
Коли вам потрібно додати до пакету на .py файл (зображення, README.md тощо) варто пам'ятати, що setuptools проігнорує всі не .py файли. Потрібно явно вказати додати файли в пакет, якщо вам це потрібно. Один зі способів додати файли в постачання — це вказати параметр include_package_data=True у виклику setup та прописати, які файли потрібно додати у постачання у MANIFEST.in.
MANIFEST.in — це файл поряд з setup.py, і в ньому вказуються шляхи до всіх файлів, які потрібно додати у постачання. Приклад MANIFEST.in для додавання файлу README.md:'''

# include README.md

# І структура пакету буде:

# useful/
#     useful/
#         __init__.py
#         some_code.py
#         another_code.py
#     setup.py
#     MANIFEST.in
#     README.md

'''
Тепер файл README.md буде доданий до пакету і буде доступний. Шлях до файлів, які потрібно включити у постачання, може бути будь-яким відносно пакету.
Управління залежностями пакету
Якщо в нашому пакеті є залежності, щоб він запрацював, потрібно встановити додаткові пакети, потрібно їх всі прописати в параметрі install_requires:'''

# from setuptools import setup, find_namespace_packages

# setup(
#     name='useful',
#     version='1',
#     description='Very useful code',
#     url='http://github.com/dummy_user/useful',
#     author='Flying Circus',
#     author_email='flyingcircus@example.com',
#     license='MIT',
#     packages=find_namespace_packages(),
#     install_requires=['markdown'],
# )

'''
В цьому прикладі наш пакет буде вимагати встановити спочатку пакет markdown перед встановленням. Порядок встановлення залежностей визначає сам менеджер пакетів (pip наприклад).
Консольний скрипт як пакет
Якщо наш пакет містить застосунок, який можна викликати з консолі, зручно буде додати можливість виклику цього застосунку у будь-якому місці нашої системи з консолі. Для цього у виклику setup додамо ще один параметр — entry_points. Цей параметр приймає словник, де ми можемо вказати список "точок входу" для ключа console_scripts.
Наприклад, в нашому пакеті у модулі some_code.py є функція hello_world, яка виводить у консоль повідомлення Hello World!. Після встановлення пакету ми зможемо в будь-якому місці нашої системи виконати в консолі команду: helloworld і отримаємо у відповідь Hello World!.
Щоб це працювало в системі, Python повинен викликатися при виклику файлів з розширенням .py та setup.py повинен бути змінений:'''

# from setuptools import setup, find_namespace_packages

# setup(
#     name='useful',
#     version='1',
#     description='Very useful code',
#     url='http://github.com/dummy_user/useful',
#     author='Flying Circus',
#     author_email='flyingcircus@example.com',
#     license='MIT',
#     packages=find_namespace_packages(),
#     install_requires=['markdown'],
#     entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
# )
'''
У списку точок входу console_scripts можуть бути файли, що виконуються (.exe), скрипти Bash, cmd, PowerShell і будь-який інший файл, який операційна система зможе виконати.'''