# import time
# from functools import cache

# def timer(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# @timer
# def hello():
#     print("Hello user...")
#     time.sleep(1)

# @cache
# def fibo(n):
#     if n < 2:
#         return n
#     return fibo(n - 1) + fibo(n - 2)

# # hello()

# result = fibo(40)
# print(result)

# # 0 1 1 2 3 5 8 13 21 34 55 89 144



# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, new_age):
#         if new_age <= 0:
#             raise ValueError("Age cannot be 0 or less")
#         self._age = new_age


# hossein = Person("Hossein", 23)
# print(hossein.age)

# hossein.age = 25
# print(hossein.age)


# class Math:
#     @staticmethod
#     def add(num1, num2):
#         print(num1 + num2)


# Math.add(1, 5)

from dataclasses import dataclass

@dataclass
class APIs:
    weather_api = "https://djkhslf"
    price_api = "fadshfalskd;"


APIs.price_api
