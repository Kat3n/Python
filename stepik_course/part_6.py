числовые типы данных
---------------------

n = int('12345')  # преобразование строки в целое число
n = float('1.2345')  # преобразование строки к числу с плавающей точкой

Обратите внимание, что преобразование чисел с плавающей точкой в целое производится с округлением в сторону нуля, то есть int(1.7) = 1, int(-1.7) = -1.

--------------------------------------------------------------------

a = float(input())
if a !=0:
    a = 1 / a
    print(a)
else:
    print('Обратного числа не существует')

-------------------------------------------------------------------

У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

f = float(input())
c = 5/9*(f - 32)
print(c)

--------------------------------------------------------------------

На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.

a = float(input())
if a <= 2:
    a = a * 10.5
    print(a)
else:
    a = 2 * 10.5 + (a - 2) * 4
    print(a)

---------------------------------------------------------------------

Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

n = float(input())
n = n * 10
n = int(n)
n = n%10
print(n)

--------------------------------------------------------------------

Дано положительное действительное число. Выведите его дробную часть.

n = float(input())
n = n%1
print(n)

--------------------------------------------------------------------

Для определения соответственно минимального или максимального значения используются функции min() и max(). Аргументов у этих функций может быть любое количество, главное, чтобы они все были одного типа.

Для нахождения модуля (абсолютной величины) числа в Python используется функция abs().

---------------------------------------------------------------------

Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
num1 = max(a,b,c,d,e)
num2 = min(a,b,c,d,e)
print('Наименьшее число =', num2)
print('Наибольшее число =', num1)

---------------------------------------------------------------------
Напишите программу, которая упорядочивает три числа от большего к меньшему.

num1 = max(a,b,c)
num2 = min(a,b,c)
num3 = (a+b+c)- (num1 + num2)
print(num1)
print(num3)
print(num2)

--------------------------------------------------------------------

Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

n = int(input())
a = n//100                    #первое число
b = (n//10)%10                #второе число
c = n%10                      #третье число
a1 = max(a,b,c)                #max
b1 = min(a,b,c)                #min
c1 = (a+b+c) - (a1+b1)         #среднее
if a1 - b1 == c1:
    print('Число интересное')
else:
    print('Число неинтересное')

------------------------------------------------------------------------

Даны пять чисел a_1, \, a_2, \, a_3, \, a_4, \, a_5a,  Напишите программу, которая вычисляет сумму их модулей

a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
n = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(n)

--------------------------------------------------------------------------

Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.

На плоскости манхэттенское расстояние между двумя точками 

p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
n = (abs(p1 - q1)) + (abs(p2 - q2))
print(n)

--------------------------------------------------------------------------

Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для проведения вычислений с вещественными числами (числами с плавающей точкой).
Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:

    import math

num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз


from math import *

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз



from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))

print(floor(12.8))  # приведет к ошибке, так как функция floor не подключена

---------------------------------------------------------------------------------------------------------

Список наиболее часто используемых функций модуля math:

Функция	Описание
Округления
int()	Округляет число в сторону нуля
round(x)	Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа
round(x, n)	Округляет число x до n знаков после точки
floor(x)	Округляет число x вниз («пол»)
ceil(x)	Округляет число x вверх («потолок»)
abs(x)	Модуль числа x (абсолютная величина)
Корни, логарифмы, степени и факториал
sqrt(x)	Квадратный корень числа x
pow(x, n)	Возведение числа x в степень n
log(x)	Натуральный логарифм числа x. Основание натурального логарифма равно числу e
log10(x)	Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
log(x, b)	Логарифм числа x по основанию b
factorial(n)	Факториал натурального числа n
Тригонометрия
degrees(x)	Преобразует угол x, заданный в радианах, в градусы
radians(x)	Преобразует угол x, заданный в градусах, в радианы
cos(x)	Косинус угла x, задаваемого в радианах
sin(x)	Синус угла x, задаваемого в радианах
tan(x)	Тангенс угла x, задаваемого в радианах
acos(x)	Возвращает угол в радианах от 00 до \piπ, cos которого равен x
asin(x)	Возвращает угол в радианах от - \frac{\pi}{2}− 

-----------------------------------------------------------------------------------------

На плоскости евклидово расстояние между двумя точками

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
from math import *
a = pow((x1 - x2), 2)
b = pow((y1 - y2), 2)
n = sqrt(a + b)
print(n)

------------------------------------------------------------

Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.

n = float(input())
from math import *
s = pi * pow(n, 2)
c = 2 * pi * n
print(s)
print(c)

------------------------------------------------------------

В математике выделяют следующие средние значения:
    среднее арифметическое чисел
    среднее геометрическое чисел
    среднее гармоническое чисел
    среднее квадратичное чисел

-----------------------------------------------------------

Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

a, b = float(input()), float(input())
from math import *
num1 = (a + b) /2
num2 = sqrt(a * b)
num3 = (2 * a * b) / (a + b)
num4 = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(num1)
print(num2)
print(num3)
print(num4)

------------------------------------------------------------

Напишите программу, вычисляющую значение тригонометрического выражения

sinx+cosx+tan2x

x = float(input())
from math import *
x = radians(x)
x = sin(x) + cos(x) + pow(tan(x), 2)
print(x)

-------------------------------------------------------------


x = float(input())
from math import *
x1 = floor(x)
x2 = ceil(x)
n = x1 + x2
print(n)

----------------------------------------------------------

Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения

a, b, c = float(input()), float(input()), float(input())
from math import *
d = pow(b, 2) - 4 * a * c
if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')

------------------------------------------------------------

Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны aa и количеством сторон nn вычисляется по формуле:

n = int(input())
a = float(input())
from math import * 
s = (n * pow(a, 2)) / (4 * tan( pi / n))  
print(s)

--------------------------------------------------------------
Длиной строки называется количество символов из которых она состоит. Чтобы посчитать длину строки используем встроенную функцию len() (от слова length – длина

При подсчете длины строки считаются все символы, включая пробелы.

Строки, как и числа, можно складывать. Операция сложения строк называется конкатенацией или сцеплением

В Python так же можно умножать строку на число. Такой оператор повторяет строку указанное количество раз.

----------------------------------------------------------------

Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

a, b, c = input(), input(), input()
from math import *
num_max = (max(len(a), len(b), len(c)))
num_min = (min(len(a), len(b), len(c)))
if len(a) == num_min:
    print(a)
elif len(b) == num_min:
    print(b)
elif len(c) == num_min:
    print(c)
if len(a) == num_max:
    print(a)
elif len(b) == num_max:
    print(b)
elif len(c) == num_max:
    print(c)

--------------------------------------------------------------

Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

a, b, c = len(input()), len(input()), len(input())
from math import *
if (2 * b-c-a) * (2 * c-b-a) * (2 * a-b-c) == 0:
    print('YES')
else:
    print('NO')

---------------------------------------------------------------

В Python есть специальный оператор in, который позволяет проверить, что одна строка находится внутри другой.

s = input()
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')

----------------------------------------------------------------

s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')

------------------------------------------------------------------

Примечание. Если строка s1 содержится в строке s2, то говорят, что строка s1 является подстрокой для строки s2. Другими словами, оператор in определяет является ли одна строка подстрокой другой.

----------------------------------------------------------------

Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

n = input()
if 'синий' in n:
    print('YES')
else:
    print('NO')

----------------------------------------------------------------------

Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

n = input()
if 'суббота' in n or 'воскресенье' in n:
    print('YES')
else:
    print('NO')

---------------------------------------------------------------------


        