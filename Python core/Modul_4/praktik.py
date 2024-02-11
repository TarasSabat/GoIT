'''Виводимо зі словника ключ-значення'''
 
# a = {'a':1, 'b':2, 'c':3}
# for key, value in a.items():
#     print(key, value)

'''У нас є строка: a = "lsj94ks6d231* !9#".
Потрібно створити список в якому будуть тільки цифри'''

# a = "lsj94k4s6d231* !9#"
# result_list = []
# for el in a:
#     if '0' <= el <= '9':
#         result_list.append(el)
# print(result_list)    # виводить результат СПИСКОМ  

# result_tuple = tuple(result_list)
# print(result_tuple)   # виводить результат КОРТЕЖЕМ

# result_dict = {}
# for element in result_list:
#     result_dict[element] = int(element)
# print(result_dict)     # виводить результат СЛОВНИК 

# result_set = set(result_list)
# print(result_set)      # виводить результат МНОЖИНИ  

'''Реалізувати рекурсивний прохід по дереву дирекорій.
І потрібно вивести всі папки і файли які зберігаються в середині.'''

# from pathlib import Path
# import sys

# p = Path(sys.argv[1])
###
# def parse_folder(path: Path):     # не повний підхід
#     for el in path.iterdir():
#         if el.is_dir():
#             print(f'Parse_folder: This is folder - {el.name}')
#         else:
#             print(f'Parse_folder: This is file - {el.name}')
###

# def parse_folder_recursion(path: Path):
#     for element in path.iterdir():
#         if element.is_dir():
#             print(f'Parse_folder: This is folder - {element.name}')
#             parse_folder_recursion(element)
#         else:
#             print(f'Parse_folder: This is file - {element.name}')

# if __name__ == "__main__":
#     parse_folder_recursion(p)

'''Знайти індекс колонки для excel таблиці'''

# from string import ascii_uppercase

# def find_column_index(column_name: str) -> int:
#     """
#     >>> find_column_index('AA')
#     27
#     >>> find_column_index('ABA')
#     729
#     >>> find_column_index('AAA')
#     703
#     """
#     letter_map = {}
#     for index, letter in enumerate(ascii_uppercase, 1):
#         letter_map[letter] = index  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
#     if len(column_name) > 1:
#         sum = 0
#         reverse_column_name = column_name[::-1]
#         for index, letter in enumerate(reverse_column_name):
#             sum += 26 ** index * letter_map[letter]
#         return sum
#     return letter_map.get(column_name)
# ​
# print(find_column_index('AAA'))

# '''main.py 1 2 Hi'''

# import sys
# sum = ''
# for ar in sys.argv:
#     sum = sum + ar
# print(sum)

# ###
# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}
