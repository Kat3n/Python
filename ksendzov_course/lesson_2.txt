# b_true = True
# b_false= False
# #операторы сравнения
# v_1 = 3
# v_2 = 3
# print(v_1 == v_2)
# print(v_1 != v_2)
# print(v_1 > v_2)
# print(v_1 < v_2)
# print(v_1 >= v_2)
# print(v_1 <= v_2)

#составные условные операторы and, or, not
# age = 30
# weight = 60
# qa = True
#
# result = age == 31 and weight > 50
# print(result)
# result = not age == 30 and weight > 50
# print(result)

# #if, else
# age = 30
# weight = 60
# qa = True
#
# if age == 15 or age > 29:
#     print('condition_1')
#     if weight > 60:
#             print('>60')
#     else:
#             print('<=60')
# elif age > 29 and weight == 61:
#     print('age > 29')
# else:
#     print('condition_2')

# #Homework_1
# name = ('kate')
# work = ('qa')
# age = 34
# weight = 29
# growth = 168
#
#
# if growth < 200 or weight < 100:
#     print('type')
#     if age < 18:
#         print('child')
#     if age > 18:
#         print('man')
# if name == 'kate' or work != 'qa':
#     if work == 'qa':
#         print('is kate')
# if growth >= 168:
#     if growth == 168:
#         print('growth=168')


# # Сделать скрипт используя функцию input().
# #     1. Функция должна на вход принимать целое число.
# #     2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
# n = int(input())
# if n > 30:
#     print('Вы ввели число =', n, ', которое > 30')
# if n == 30:
#     print('Вы ввели число =', n, ', которое = 30')
# if n < 30:
#     print('Вы ввели число =', n, ', которое < 30')


# Внутри функции должно сгенерироваться рандомное целое число
n = int(input())
import random
x = (random.randint(1, 100))
y = (random.randint(1, 100))
if n < x and n < y:
    print('Вы ввели число =', n, ', которое <', x, 'и', y)
if n > x and n > y:
    print('Вы ввели число =', n, ', которое >', x, 'и', y)
if n < x and n > y:
    print('Вы ввели число =', n, ', которое <', x, 'и >', y)
if n > x and n < y:
    print('Вы ввели число =', n, ', которое >', x, 'и <', y)
if n == x and n == y:
    print('Вы ввели число =', n, ', которое =', x, 'и', y)
if n == x or n == y:
    print('Вы ввели число =', n, ', которое =', x, 'или', y)
else:
    print('попробуй еще')
