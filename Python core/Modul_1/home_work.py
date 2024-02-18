# № 1 Створіть змінну name та привласніть їй ваше ім'я, наприклад 'Данило' Створіть змінну age і надайте їй значення свого віку
name = 'Данило'
age = 42

# № 2 Нехай нам необхідно розрахувати послуги споживання електрики. У змінній rate у нас знаходиться тариф за електроенергію 1.68, а в змінній value — значення показання лічильника, задайте для неї розумне ціле число в кіловатах. Розрахуйте та помістіть у змінну payment рахунок за електрику.
rate = 1.68
value = 50
payment = rate * value

# № 3 Повернемося до попереднього завдання. У змінній rate у нас знаходиться тариф за електроенергію — 1.68. Але тепер нам потрібно вести розрахунок денного та нічного тарифу. Нічний тариф розраховується як половина денного, тобто. rate треба поділити на 2. У змінній value_day — денні показання лічильника, а в змінній value_night — нічні. Знову ж таки, задайте для них розумне ціле число кіловат. Розрахуйте та помістіть у змінну payment рахунок за електрику, але вже з урахуванням денного та нічного тарифів.
rate = 1.68
value_day = 50
value_night = 20
payment = (value_day * rate) + (value_night * (rate/2))

# № 4 Знову повернемося до попереднього завдання. Додамо перед обчисленням змінної payment пояснювальний коментар. Закоментуйте текст 'Payment for electricity for the current month', щоб код став робочим.
rate = 1.68
value_day = 358
value_night = 103
# Payment for electricity for the current month
payment = rate * value_day + rate / 2 * value_night

# № 5 При покупці квитків нам завжди необхідно знати ім'я та прізвище покупця. Оголосимо дві рядкові змінні: first_name, яка містить ім'я, та змінну last_name, в яку помістимо прізвище користувача. Створіть ці дві змінні та привласніть їм своє ім'я та прізвище.
first_name = 'Taras'
last_name = 'Sabat'

# № 6 При покупці квитків нам завжди необхідно знати ім'я та прізвище покупця. Оголосимо дві рядкові змінні: first_name, яка містить ім'я, та змінну last_name, в яку треба помістити прізвище покупця квитка. Створіть ці дві змінні та надайте їм своє ім'я та прізвище.
first_name = "Taras"
last_name = "Sabat"
full_name = first_name + " " + last_name

# № 7 На цю мить у нас є три змінні: first_name, last_name та full_name
# Додамо змінну message, яка фактично буде прототипом шаблонного листа користувачеві, який купив квиток. Цю змінну ми сформуємо за допомогою f-рядка. У змінну message ми, за допомогою f-рядка, помістимо рядок наступного змісту:
# "Dear <підставляємо first_name>, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at <підставляємо full_name>. We are looking forward to seeing you!"
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"

# № 8 Змінна length містить довжину, а змінна width — ширину кімнати. Необхідно зробити розрахунок площі кімнати та результат помістити в змінну area. Додайте змінну show, в яку помістіть рядок з наступним шаблоном: 'With width <значення ширини> and length <значення довжини> of the room, its area is equal to <значення площі>'.
length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"

# № 9 Необхідно виконати додавання двох комплексних чисел (нагадаємо, що комплексні числа підтримують не всі математичні операції та не всі операції порівняння).
# Перша змінна a дорівнює -2 + 3j і друга змінна b дорівнює 4 + 2.1j. Результат необхідно помістити у змінну result.
a = -2 + 3j
b = 4 + 2.1j
result = a + b

# № 10 Необхідно обчислити корені квадратного рівняння.
# a · x2 + b · x + c = 0
# Задайте змінні коефіцієнти a, b, c зі значеннями -2, 7, -6 відповідно
# Дискримінант рівняння помістіть у змінну D
# D = b2 - 4 · a · c
# Корені рівняння помістіть у змінні x1 та x2, відповідно.
# x1 = (-b + D0.5) / (2 · a)
# x2 = (-b - D0.5) / (2 · a)
import math

a = -2
b = 7
c = -6
D = b ** 2 - 4 * a * c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

# № 11 Булевий тип часто використовують, щоб позначити стан об'єкта. Наприклад, змінна is_active може вказувати, чи активний обліковий запис користувача чи ні. Також акаунти користувачів часто не видаляють із бази даних, а просто встановлюють їм властивість is_delete – це називають soft delete (м'яке видалення). Тож встановіть змінній is_active істинне значення, а змінній is_delete — хибне.
is_active = True
is_delete = False

# № 12 Заведіть чотири змінні різного типу та надайте їм значення відповідного типу.
# name — рядкова змінна
# age — числова змінна
# is_active — булева змінна
# subscription — встановити значення None  
name = "Taras"
age = 42
is_active = True
subscription = None

# № 13 Повернімося до завдання з пункту 8 для розрахунку площі. Ширина та висота задані у рядковому вигляді. Необхідно, як і раніше, розрахувати площу, але потрібно рядковий тип перетворити на чисельний (float) при розрахунку площі area. Не забудьте також додати до змінної show рядок з наступним шаблоном: 'With width <значення ширини> and length <значення довжини> of the room, its area is equal to <значення площі>'.
length = "2.75"
width = "1.75"       
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"

# № 14 Програмісти часто працюють із геоданими. Попрацюємо і ми з ними. Нам необхідно написати програму, в якій ми розрахуємо відстань між двома точками на поверхні Землі.
# Рахуватимемо відстань між двома містами: Києвом та Лондоном
# Координати Києва в градусах:
# Широта lat1 = 50.45
# Довгота lon1 = 30.523
# Координати Лондона в градусах:
# Широта lat2 = 51.5072
# Довгота lon2 = -0.1275
# Радіус Землі приймемо 6371.01 км. Відстань у кілометрах між містами з урахуванням викривленості планети можна знайти за такою формулою:
# distance = 6371.01 · arccos(sin(lat1) · sin(lat2) + cos(lat1) · cos(lat2) · cos(lon1 - lon2))
# Пам'ятайте, що тригонометричні функції в Python оперують радіанами. Тобто величини із градусів необхідно перекласти у радіани, перш ніж обчислювати відстань між точками. Для цього в модулі math є функція radians
# <радіани> = math.radians(<градуси>)
# Також:
# arccos(x) — це math.acos(x)
# sin(x) — це math.sin(x)
# cos(x) — це math.cos(x)
# Обчисліть distance за вказаною формулою за допомогою запропонованих методів модуля math.
import math

RADIUS = 6371.01

lat1 = math.radians(50.45)
lon1 = math.radians(30.523)

lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)

distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

# № 15 При заповненні анкети на сайті нам необхідно через функцію input присвоїти відповідним змінним значення:
# name - ваше ім'я, тип рядок
# email - ваша електронна пошта, тип рядок
# age - ваш вік, тип число int
# height - ваш зріст, тип число float
# is_active - чи бажаєте ви отримувати повідомлення від сайту, тип булевий
name = input("Your name? ")
email = input("Your emei? ")
age = int(input("Age? "))
height = float(input("Height? "))
is_active = True

# № 16 Використовуючи приведення типів і input, розв'яжіть задачу для розрахунку площі. Ширина та висота задані за допомогою функції input. Необхідно, як і раніше, розрахувати площу, але потрібно рядковий тип перетворити на чисельний (float) при отриманні значення через input. Змінну show створювати не треба.
length = float(input ("Lenght? "))
width = float(input ("Widght? "))
area = length * width