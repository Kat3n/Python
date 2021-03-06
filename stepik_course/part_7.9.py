

Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:

n = int(input())
count = 1
for i in range(n):
    print()
    for j in range(i+1):
        print(count, end=' ')
        count +=1
print()


====================================================

Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:

1
121
12321
1234321
123454321


n = int(input())
for i in range(n+1):
    print()
    for i in range(1, i+1):
        print(i, end='')
    for i in range(i-1, 0, -1):
        print(i, end='')
print()


======================================================

На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит натуральное число из отрезка [a; \, b][a;b] с максимальной суммой делителей.


a, b = int(input()), int(input())
counter = 0 # счетчик подсчета суммы делителей
number = 1 # число которое будем выводить (минимум 1)
summa = 0  # тут будет сумма делителей, которую надо будет вывести
for i in range(a, b + 1):  # проверяем каждое число в [a;b]
    counter = 0 # обнуляем счетчик для каждого i
    for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
        if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
            counter += j  # создаем сумму делителей
    if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
        summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
        number = i  # число у которого делителей оказалось больше, теперь равно number
print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей


=========================================================

На вход программе подается натуральное число nn. Напишите программу, выводящую графическое изображение делимости чисел от 11 до nn включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

n = int(input())
for i in range(1, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    print(j, end='')
    print('+' * count)


============================================================

Цифровой корень
На вход программе подается натуральное число nn. Напишите программу, которая находит цифровой корень данного числа. Цифровой корень числа nn получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.

n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)


================================================================

Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.


n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)


====================================================================

На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит все простые числа от aa до bb включительно.

a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


=======================================================================


