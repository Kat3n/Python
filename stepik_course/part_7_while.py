циклы, повторяющиеся до наступления определенного события (while, условные циклы)

# используем for
for i in range(0, 100, 3):
    print(i)

# используем while
i = 0
while i < 100:
    print(i)
    i += 3

------------------------------------------------------------------------------------

Не всегда, однако удается заменить цикл while с помощью цикла for. Если заранее не известно количество итераций, то необходимо использовать цикл while и только его.

---------------------------------------------------------------------------------------


text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()
print('Сумма чисел равна', total)


----------------------------------------------------------------------------------------

Бесконечный цикл


i = 0
total = 0
while i < 10:
    total += i


-------------------------------------------------------------------------------------

На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек). Напишите программу, которая выводит члены данной последовательности.

text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()

----------------------------------------------------------------------------------------

На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены данной последовательности.

text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()

-----------------------------------------------------------------------------------------

На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу, которая выводит общее количество членов данной последовательности.

text = input()
count = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    count += 1
    text = input()
print(count)

---------------------------------------------------------------------------------------

На вход программе подается последовательность целых чисел делящихся на 77, каждое число на отдельной строке. Концом последовательности является любое число не делящееся на 77. Напишите программу, которая выводит члены данной последовательности.

n = int(input())
while n%7 == 0:
    print(n)
    n = int(input())


---------------------------------------------------------------------------------------

На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.

n = int(input())
count =0
while n >= 0:
    count += n
    n = int(input())
print(count)


-------------------------------------------------------------------------------------------

На вход программе подается последовательность целых чисел от 11 до 55, характеризующее оценку ученика, каждое число на отдельной строке. Концом последовательности является любое отрицательное число, либо число большее 55. Напишите программу, которая выводит количество пятерок.

n = int(input())
count = 0
while 0 < n <= 5:
    if n == 5:
        count += 1
    n = int(input())
print(count)


----------------------------------------------------------------------------------------------

Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, \, 5, \, 10, \, 251,5,10,25.

price = int(input())
count = 0
while price > 0:
        if price >= 25:
            count += 1
            price -= 25
        if 10 <= price < 25:
            count += 1
            price -= 10
        if 5 <= price < 10:
            count += 1
            price -= 5
        if 0 < price < 5:
            count +=1
            price -= 1
print(count)

--------------------------------------------------------------------------------------------

Напишем программу, которая считывает натуральное число (целое положительное) и обрабатывает его цифры.

n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    # код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа


Цикл while работает до тех пор пока в числе есть необработанные цифры. Тело цикла содержит:

процедуру получения последней цифры last_digit = n % 10;
код обработки последней цифры;
процедуру удаления последней цифры из числа n = n // 10.

В качестве процедуры обработки может быть все, что угодно: вывод цифр, нахождение суммы, произведения цифр, нахождение наибольшей или наименьшей цифры, подсчет цифр удовлетворяющих некоторому условию и т.д.

-----------------------------------------------------------------------------------

Что покажет приведенный ниже фрагмент кода?

num = 12345
product = 1
while num != 0:
    last_digit = num % 10
product = product * last_digit
    num = num // 10
print(product)

120

-------------------------------------------------------------------------------------

Что покажет приведенный ниже фрагмент кода?
num = 123456789
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit > 4:
        total += 1
    num = num // 10
print(total)

5
---------------------------------------------------------------------


Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

n = int(input())
while n > 0:
    number = n%10
    n = n // 10
    print(number)


------------------------------------------------------------------------

n = int(input())
while n > 0:
    number = n%10
    n = n // 10
    print(number, end='')


------------------------------------------------------------------------

Дано натуральное число n, \, (n \ge 10)n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

n = int(input())
num = n%10
num_max = num
num_min = num
while n != 0:
    num = n%10
    if num >= num_max and num !=0:
        num_max = num
    if num <= num_min:
        num_min = num
    n = n//10
print('Максимальная цифра равна', num_max)
print('Минимальная цифра равна', num_min)

-------------------------------------------------------------------------------

Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.

n = int(input())
sum_number = 0
count_number = 0
multi_number = 1
multi_number2 = 1
sum2_number = 0
last_number = n%10
while n != 0:
    number = n%10
    n = n//10
    sum_number += number
    count_number += 1
    multi_number = multi_number * number
    multi_number2 = sum_number/count_number
sum2_number = number + last_number
print(sum_number)
print(count_number)
print(multi_number)
print(multi_number2)
print(number)
print(sum2_number)

---------------------------------------------------------------------------

Дано натуральное число n \, (n > 9)n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

n = int(input())
while n//10 > 9:
    n = n//10
a = n%10
print(a)

-------------------------------------------------------------------------

Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

n = int(input())
number1 = n%10
counter = 0
while n > 0:
    number2 = n%10
    n = n//10
    if number1 != number2:
        counter += 1
if counter > 0:
    print('NO')
else:
    print('YES')


------------------------------------------------------------------------------

Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

n = int(input())
a = 0
flag = True
while n > 9:
    a = n%10
    n = n//10
    b = n%10
    if b < a:
        flag = False
if flag == False:
    print('NO')
else:
    print('YES')

-------------------------------------------------------------------------------

На вход программе подается число n > 1n>1. Напишите программу, которая выводит его наименьший отличный от 11 делитель.

n = int(input())
num = 2
while n != 0:
    if n%num == 0:
        print(num)
        break
    else:
        num += 1

-----------------------------------------------------------------------

