# n = 5

# for i in range(1, n+1):
#     print(i, end = '')

# # 12345

#####

'''Завдання. Ви менеджер супермаркету. У вас є список товарів разом із цінами, які споживачі купували в певний день. Ваше завдання — надрукувати кожне item_name і net_price у порядку їх першого входження.

item_name = назва елемента.
net_price = кількість проданого товару, помножена на ціну кожного товару.

Формат введення
Перший рядок містить кількість елементів, .
Наступні рядки містять назву та ціну товару, розділені пробілом.

Формат виводу
Виведіть item_name і net_price у порядку першої появи.

Зразок введення
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20'''
# from collections import OrderedDict


# def main():
#     n = int(input().strip())
#     items_dict = OrderedDict()

#     for _ in range(n):
#         item_info = input().split()
#         item_name = ' '.join(item_info[:-1])
#         price = int(item_info[-1])

#         if item_name in items_dict:
#             items_dict[item_name] += price
#         else:
#             items_dict[item_name] = price

#     for item_name, net_price in items_dict.items():
#         print(f"{item_name} {net_price}")


# if __name__ == "__main__":
#     main()
'''Давайте дізнаємося про розуміння списків! Вам дано три цілі числа x, y і z, що представляють розміри кубоїда, а також ціле число n. Надрукуйте список усіх можливих координат (i, j, k) на тривимірній сітці, де сума i+j+k не дорівнює n. Тут 0<=i<=x; 0<=j<=y; 0<=k<=z. Будь ласка, використовуйте розуміння списків, а не кілька циклів, як навчальну вправу.
приклад
х=1
y=1
z=2
n=3

Усі перестановки i,j,k:
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[ 1,0,0],[1,0,1],[1,0,2],[1,1,0]...

Надрукуйте масив елементів, сума яких не дорівнює n=3.
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[ 1,0,0],[1,0,1],[1,1,0],[1,1,2]

Формат введення
Чотири цілі числа x,y,z і n, кожне в окремому рядку.

Jбмеження
Надрукуйте список у лексикографічному порядку зростання.

Зразок введення 0
1
1
1
2

Зразок результату 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Пояснення 0
Кожна змінна x,y та z матиме значення 0 або 1. Усі перестановки списків у формі [i,j,k]=[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1][1, 1, 0][1, 1, 1]].
Видаліть усі масиви, сума яких дорівнює n=2, щоб залишити лише дійсні перестановки.

Зразок введення 1
2
2
2
2

Зразок результату 1
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2]'''

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

# # Функція для генерації списку комбінацій (i, j, k) з заданими обмеженнями
# def generate_combinations(x, y, z):
#     return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

# # Функція для фільтрації комбінацій за умовою суми не дорівнює n
# def filter_combinations(combinations, n):
#     return [comb for comb in combinations if sum(comb) != n]

# # Генерація всіх можливих комбінацій
# combinations = generate_combinations(x, y, z)

# # Фільтрація за умовою суми
# result = filter_combinations(combinations, n)

# # Виведення результату
# print(result)

##############
'''Виведення зі списку другого по величині числа''' 
# через ітерування 
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     bals_list = []
    
#     for i in arr:
#         bals_list.append(i)
#     bals_unical = set(bals_list)
#     bals_list = []
#     for i in bals_unical:
#         bals_list.append(i)
#     bals_list.sort()
#     print(bals_list)
#     print(bals_list[-2])
    
##############
# сподобалось найбільше
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     # Перетворіть введені дані на список і видаліть дублікати
#     scores = list(set(arr))

#     # Відсортуйте список у порядку спадання
#     sorted_scores = sorted(scores, reverse=True)

#     # Оцінка, яка посіла друге місце, є другим елементом у відсортованому списку
#     runner_up_score = sorted_scores[1]

#     print(runner_up_score)

###############
# # те саме через функцію
# def find_runner_up_score(n, scores):
#     # Перетворіть рядок балів, розділених пробілами, на список цілих чисел
#     scores_list = list(map(int, scores.split()))

#     # Видаліть дублікати та відсортуйте список у порядку спадання
#     unique_scores = list(set(scores_list))
#     unique_scores.sort(reverse=True)

#     # Оцінка, яка посіла друге місце, буде другою за значенням у відсортованому списку
#     runner_up_score = unique_scores[1]

#     return runner_up_score

# # Читання введення та виклик функції
# n = int(input())
# scores = input()
# result = find_runner_up_score(n, scores)
# print(result)

'''Маємо імена та оцінки для кожного учня в класі з N учнів, збережіть їх у вкладеному списку та надрукуйте імена будь-якого учня (учнів), які мають другий найнижчий бал.
Примітка. Якщо є кілька студентів із другою найнижчою оцінкою, упорядкуйте їхні імена в алфавітному порядку та друкуйте кожне ім’я з нового рядка.'''
# if __name__ == '__main__':
#     name_score_dict = {}
    
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         name_score_dict.update({name: score})
#     sorted_name_score = sorted(name_score_dict.items(), key=lambda x:x[1])
        
#     def name_sec_score():
#         n = 0
#         while sorted_name_score[0][1] == sorted_name_score[1+n][1]:
#             n += 1
#         return sort_name_score(n+1) 
    
#     def sort_name_score(n):
#         name_second_score = []
       
#         while n != len(sorted_name_score) - 1 and sorted_name_score[n][1] == sorted_name_score[n+1][1]:
#             name_second_score.append(sorted_name_score[n][0])
#             n += 1
                       
#         name_second_score.append(sorted_name_score[n][0])
#         name_second_score.sort()
#         return print(*name_second_score, sep='\n')
           
#     name_sec_score()
# 4
# Rachel
# -50
# Mawer
# -50
# Sheen
# -50
# Shaheen
# 51

'''Наданий фрагмент коду читатиметься в словнику, що містить пари ключ/значення ім’я:[знаки] для списку студентів. Надрукуйте середнє значення масиву оцінок для наданого імені студента, показуючи 2 знаки після коми.'''
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     result = (sum(student_marks.get(query_name)))/3
#     print("{:.2f}".format(result))
    
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

'''Малюємо килимок'''
# def draw_welcome_pattern(N, M):
    
#     # Верхня частина малюнка
#     for i in range(N // 2):
#         pattern = ".|." * (2 * i + 1)
#         print(pattern.center(M, "-"))

#     # Центральний рядок "WELCOME"
#     print("WELCOME".center(M, "-"))

#     # Нижня частина малюнка (відзеркалення верхньої частини)
#     for i in range(N // 2 - 1, -1, -1): # ітерація у зворотньому порядку
#         pattern = ".|." * (2 * i + 1)
#         print(pattern.center(M, "-"))

# # Приклад виклику функції з висотою N
# N_M = input()
# N, M = map(int, N_M.split())
# draw_welcome_pattern(N, M)

'''Дано ціле число i,від 1 до n, надрукуйте наступні значення для кожного цілого числа:
Десятковий
Вісімкова
Шістнадцяткове (з великої літери)
Двійковий'''
# def print_formatted(n):
#     width = len(bin(n)[2:])

#     for i in range(1, n + 1):
#         decimal = str(i)
#         octal = oct(i)[2:]
#         hexadecimal = hex(i)[2:].upper()
#         binary = bin(i)[2:]

#         print("{:>{width}} {:>{width}} {:>{width}} {:>{width}}".format(
#             decimal, octal, hexadecimal, binary, width=width))


# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

'''Створення візеруг Ранголі. Число N це розмір візерунка. Літера "а" має бути в центрі візерунку'''
# def print_rangoli(size):
#     n = size
#     width = 4 * n - 3
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     lines = []
#     for i in range(n):
#         s = '-'.join(alphabet[n-1:i:-1] + alphabet[i:n])
#         lines.append((s.center(width, '-')))
        
#     # Виведення візерунка
#     print('\n'.join(lines[::-1] + lines[1:]))

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

'''Зміна перших літер імен та прізвищ на великі'''
# def solve(s):
#     # Розділити рядок на слова та пробіли
#     words = s.split(' ', maxsplit=len(s))
    
#     # Застосувати умовні перетворення
#     edited_tokens = []
#     for token in words:
#         if token and not token[0].isdigit():
#             # Велика перша літера для слів, які не починаються з цифри
#             edited_tokens.append(token.capitalize())
#         else:
#             # Залишити слово або пробіл незмінним, якщо воно починається з цифри
#             edited_tokens.append(token)

#     # Склеїти відредаговані слова та пробіли
#     result = ' '.join(edited_tokens)

#     print(result)
#     return result

# if __name__ == '__main__':
import textwrap
    # s = input()

    # result = solve(s)

'''Задача на виконання методів списку'''
# import copy

# if __name__ == '__main__':
#     N = int(input())
#     arr_1 = []
#     arr_2 = []
    
        
#     for _ in range(N):
#         inputs = input().split()
#         command = inputs[0]
#         args = list(map(int, inputs[1:]))
        
#         if command == 'insert':
#             arr_1.insert(args[0], args[1])
#         elif command == 'append':
#             arr_1.append(args[0])
#         elif command == 'sort':
#             arr_1.sort()
#         elif command == 'remove':
#             arr_1.remove(args[0])
#         elif command == 'pop':
#             arr_1.pop()
#         elif command == 'reverse':
#             arr_1.reverse()
#         elif command == 'print':
#             arr_2.append(copy.deepcopy(arr_1))

#     for inner_list in arr_2:
#         print(inner_list)
     
# # Введення  
# # 12
# # insert 0 5
# # insert 1 10
# # insert 0 6
# # print
# # remove 6
# # append 9
# # append 1
# # sort
# # print
# # pop
# # reverse
# # print
'''Задача не хешування '''
# n = int(input())
# t = tuple(map(int, input().split()))
 
# print(hash(t))
'''Поміняти регістри (малі букви на великі і навпаки)'''
# def swap_case(s):
#     result = s.swapcase()
#     return result

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

'''Роз'єднання строки за пробулами на окремі слова та з'єднання слів через дефізи'''
# def split_and_join(line):
#     line_split = line.split(' ')
#     result = '-'.join(line_split)
#     return result

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
'''Друкування f-стрінги'''
# def print_full_name(first, last):
#     return print(f'Hello {first} {last}! You just delved into python.')

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)
'''Заміна літери в тексті маючи текст, позицію та нову літеру'''
# Варіант 1
# def mutate_string(string, position, character):
#     string_list = list(string)
#     string_list[position] = character
#     string = ''.join(string_list)
#     return string

# Варіант 2
# def mutate_string(string, position, character):
#     string = string[:position] + character + string[position+1:]
#     return string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)
'''Шукаємо кількість входжень підрядка у рідок'''
# def count_substring(string, sub_string):
#     n = 0
#     counter = 0
#     while string.find(sub_string, n) != -1:
#         counter += 1
#         n = string.find(sub_string, n) + 1
#     return counter


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)

# # ABCDCDC
# # CDC
# # 2
'''Перевірка рядка, чи рядок містить: буквено-цифрові символи, букви, цифри, малі та великі літери .'''
# if __name__ == '__main__':
#     s = input()
    
#     print(any(el.isalnum() for el in s))
#     print(any(el.isalpha() for el in s))
#     print(any(el.isdigit() for el in s))
#     print(any(el.islower() for el in s))
#     print(any(el.isupper() for el in s))

'''Вирівнювання рядків. Створення логотипу "H"'''
# # Замінити усі пропуски на rjust, ljust або center.

# thickness = int(input())  # Це має бути непарне число
# c = 'H'

# # Верхній конус (Top Cone)
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
# # Верхні стоввпці (Top Pillars)
# for i in range(thickness + 1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
# # Середній пояс (Middle Belt)
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
# # Нижні стовпи (Bottom Pillars)
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
# # Нижній конус (Bottom Cone)
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c +
#           (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

''''''
import textwrap

def wrap(string, max_width):
    return


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
