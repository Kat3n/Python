Списки

Структура данных (data structure) — программная единица, позволяющая хранить и обрабатывать множество однотипных и/или логически связанных данных.

mylist = []       # пустой список
mylist = list()   # пустой список


numbers = list(range(5))
Во время исполнения этого кода происходит следующее:

Вызывается функция range(), в которую в качестве аргумента передается число 5;
Эта функция возвращает последовательность чисел 0, 1, 2, 3, 4;
Последовательность чисел 0, 1, 2, 3, 4 передается в качестве аргумента в функцию list();
Функция list() возвращает список [0, 1, 2, 3, 4];
Список [0, 1, 2, 3, 4] присваивается переменной numbers.


===========================================

На вход программе подается одно число nn. Напишите программу, которая выводит список [1, 2, 3, ..., n].

n = int(input())
num = list(range(1,n+1))
print(num)

==============================================

На вход программе подается одно число nn. Напишите программу, которая выводит список, состоящий из nn букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

n = int(input())
mylist = []
for i in range(97, n+97):
    s = chr(i)
    mylist += s
print(mylist)

==================================================


