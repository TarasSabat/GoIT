'''Це рекурсивна реалізація алгоритму для задачі лісеняння сходів, де на кожному кроці можна крокувати на один або два сходинки.'''
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# res = Solution()
# print(res.climbStairs(5))

'''Для застосування динамічного програмування і покращення швидкодії алгоритму можна використовувати підхід з мемоізацією (зберіганням проміжних результатів) або нижнім підходом з динамічним програмуванням.'''

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}  # Словник для зберігання проміжних результатів

#         def climb(n):
#             if n == 0 or n == 1:
#                 return 1
#             if n not in memo:
#                 # Якщо результат для n ще не збережено, обчислюємо його та зберігаємо
#                 memo[n] = climb(n-1) + climb(n-2)
#             return memo[n]

#         return climb(n)


# res = Solution()
# print(res.climbStairs(5))

'''Застосування нижнього підходу з динамічним програмуванням:'''

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1

#         # Створюємо список для зберігання проміжних результатів
#         dp = [0] * (n + 1)
#         dp[0], dp[1] = 1, 1  # Базові випадки

#         for i in range(2, n + 1):
#             # Обчислюємо та зберігаємо результат для кожного n
#             dp[i] = dp[i-1] + dp[i-2]

#         return dp[n]


# res = Solution()
# print(res.climbStairs(5))
