
year = '2010'
num = '10k'
coin = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, num, coin)
print(s)

==================================================================================

year = 2010
amount = '10K'
currency = 'Bitcoin'

print('In {0}, someone paid {1} {2} for two pizzas.'.format(year, amount, currency))

===============================================================================

for i in range(26):
    print(chr(ord('A') + i))

================================================================================

На вход программе подаются два числа aa и bb. Напишите программу, которая для каждого кодового значения в диапазоне от aa до bb (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

a = int(input())
b = int(input())
for i in range(a,b+1):
    print(chr(a), end = ' ')
    a += 1

================================================================================

На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.

s = input()
for i in range(len(s)):
    print(ord(s[i]), end = ' ')

==================================================================================

В первой строке дается число n \, (1 \le n \le 25)n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

step = int(input())
s = input()
for i in range(len(s)):
    n = (ord(s[i]) - step)
    if n < 97:
        n = 122 - (96 - n)
    print(chr(n), end = '')


===================================================================================

Второе вхождение

На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.

s = input()
if (s.count('f')) == 1:
    print(-1)
if (s.count('f')) < 1:
    print('-2')
if (s.count('f')) >= 2:
    print(s.find('f',s.find('f')+1))


=================================================================================

На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».

s = input()
print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])

===============================================================================

