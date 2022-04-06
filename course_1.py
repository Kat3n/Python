lesson 1

# while True:
#     name = input()
#     print("Your input word = ", name)

# вывод тип данных
# a = 2
# b = 5.5
# print("type a = ", type(a))
# print("type b = ", type(b))
# print(a+b, type(a+b))

# #вывод списка массива
# a, b, c = 5, 8, 0
# name_list = [a, b, c]
# for i in name_list:
#     print("nomber = ", i)

# param_1 = 7
# param_2 = 2
# param_3 = param_1/param_2
# param_4 = param_1//param_2         #целочисленное деление
# param_5 = param_1 % param_2        #остаток от деления
# param_6 = 3+4*5**2+7               #приоритетность выполнения
# print('param_3 =',param_3, type(param_3))
# print('param_4 =', param_4, type(param_4))
# print('param_5 =', param_5, type(param_5))
# print('param_6 =', param_6, type(param_6))

# #операции с присвоением
# param_1 = 7
# param_1 += 2
# print('param_1 =',param_1, type(param_1))

# #подсчет элементов в массиве
# name_list = ['hkjhj', 'hggg', 'hgjhgjh', 'sggrd', 'rgsga', 'grrgrrh']
# count = 0
# for i in name_list:
#     print('count = ', count, '--i', i, type(i))
#     count += 1

--------------------------------------------------------------
Homework_1

#Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
param_string = 'Kate'
print('1_param_string = ', type(param_string))
param_int = 13
print('2_param_int = ', type(param_int))
param_float = 13.3
print('3_param_float = ', type(param_float))
param_bytes = b'1f'
print('4_param_bytes = ', type(param_bytes))
param_list = ['ffj', 'hf','645']
print('5_param_list = ', type(param_list))
param_tuple = ('ghhg',)
print('6_param_tuple = ', type(param_tuple))
param_set = {'a', 'b', 'c'}
print('7_param_tuple = ', type(param_set))
param_frozenSet = frozenset('hbgjberj')
print('8_param_tuple = ', type(param_frozenSet))
param_dict = {'key': 'hh', 'key2': 5}
print('9_param_dict = ', type(param_dict))

#Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a = 'Hello '
b = 'world!'
c = a + b
print(c)

#Создать 2 переменные Integer, сумма,деление, умножение. Вывести в консоль.
a = 11
b = 5
c= a+b
print(c)
c = a/b
print(c)
c = a//b
print(c)
c = a*b
print(c)
c = a % b
print(c)


