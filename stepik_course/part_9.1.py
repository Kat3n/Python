Программа должна вывести «YES», если слово является палиндромом и «NO» в противном случае.

s = input()
if s[::1] == s[::-1]:
    print('YES')
else:
    print('NO')


==========================================================

На вход программе подается одна строка. Напишите программу, которая выводит:

общее количество символов в строке;
исходную строку повторенную 3 раза;
первый символ строки;
первые три символа строки;
последние три символа строки;
строку в обратном порядке;
строку с удаленным первым и последним символом.

s = input()
print(len(s))
print(s*3)
print(s[:1])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])


===============================================================

На вход программе подается одна строка. Напишите программу, которая выводит:

третий символ этой строки;
предпоследний символ этой строки;
первые пять символов этой строки;
всю строку, кроме последних двух символов;
все символы с четными индексами;
все символы с нечетными индексами;
все символы в обратном порядке;
все символы строки через один в обратном порядке, начиная с последнего.

s = input()
print(s[2:3])
print(s[-2:-1])
print(s[:5])
print(s[0:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[-1::-2])

=================================================================

На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.

s = input()
#s1 = s[0:len(s)-len(s)//2]
#s2 = s[len(s)-len(s)//2:]
#print(s2+s1)
print((s[len(s)-len(s)//2:])+(s[0:len(s)-len(s)//2]))

===================================
