"""Завдання №1:
Створіть абстрактний клас Shape, який буде представляти геометричну фігуру. В цьому класі
створіть абстрактний метод area(), який буде повертати площу) фігури. Створіть два підкласи цього
абстрактного класу: Circle і Rectangle. У кожному з цих підкласів реалізуйте метод area() для обчислення
площі фігури.Потім створіть екземпляри обох підкласів, обчисліть їх площу та виведіть результат."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2


class Rectangle(Shape):
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def area(self):
        return self.h * self.v
