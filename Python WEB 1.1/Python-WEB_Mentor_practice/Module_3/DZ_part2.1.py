"""Модуль 3: Друга частина ДЗ для процесів
Напишіть реалізацію функції factorize, яка приймає список чисел та повертає список чисел, на які числа з
вхідного списку поділяються без залишку.Реалізуйте синхронну версію та виміряйте час виконання.
Потім покращіть продуктивність вашої функції, реалізувавши використання кількох ядер процесора для
паралельних  обчислень і замірьте час виконання знову. Для визначення кількості ядер на машині
використовуйте  функцію cpu_count() з пакета multiprocessing.
Для перевірки правильності роботи алгоритму самої функції можете скористатися тестом:"""
# def factorize(*number):
#     # YOUR CODE HERE
#     raise NotImplementedError() # Remove after implementation
#
#
# a, b, c, d  = factorize(128, 255, 99999, 10651060)
#
# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
# 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

from multiprocessing import Pool, current_process, cpu_count
import time
import logging
import concurrent.futures


# Синхронне виконання
def factorize(numbers: list) -> list:
    result_list = []
    for number in numbers:
        temp_list = []
        for num in range(1, number + 1):
            if number % num == 0:
                temp_list.append(num)
        result_list.append(temp_list)
    print(result_list)
    return result_list


# Виконання: Pool звичайний"
def factorize_multi(number: int) -> list:
    result_list = []
    for num in range(1, number + 1):
        if number % num == 0:
            result_list.append(num)
    return result_list


if __name__ == "__main__":
    lst = [128, 25500, 999990, 106510600]
    # Синхронне виконання
    start_time = time.time()

    a, b, c, d = factorize(lst)

    end_time = time.time()
    print(f"Sync time is: {end_time - start_time}")

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
    #              1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("Success synchron")

    "Логгер"
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    core_count = cpu_count()
    start_time_multi = time.time()

    # Виконання: Pool звичайний"
    with Pool(processes=core_count) as pool:
        logger.debug(pool.map(factorize_multi, lst))
    end_time_multi = time.time()
    print(f"Sync Multi_pool time is: {end_time_multi - start_time_multi}")

    # Виконання: PoolExecutor"
    start_time_multi2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(core_count) as executor:
        executor.map(factorize_multi, lst)
    end_time_multi2 = time.time()
    print(f"Sync PoolExecutor time is: {end_time_multi2 - start_time_multi2}")

""
