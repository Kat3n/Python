На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом. Напишите программу, которая подсчитывает количество слов в ней.

s = input()
print(s.count(' ')+1)


=======================================================================

На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.

s = input()
s = (s.lower())
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))


=========================================================================

В первой строке подаётся число nn – количество сообщений, в последующих nn строках вводятся строки, содержащие латинские строчные буквы и цифры.

Формат выходных данных
Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.

n = int(input())
count = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        count += 1
print(count)


==========================================================================

На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.

s = input()
count = 0
for i in range(len(s)):
    if '0'<=s[i]<='9':
        count += 1
print(count)


========

n = input()
count = 0
for i in range(10):
    count += n.count(str(i))
print(count)


======

s=input()
c=0
for i in range(10):
    for j in range(len(s)):
        if str(i)==s[j]:
            c+=1
print(c)


===========================================================================
Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.

s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')


=============================================================================


Программа должна вывести символ, который появляется наиболее часто.

s = input()
num_1 = 0
num_2 = ''
for i in range(len(s)):
    if s.count(s[i]) >= num_1:
        num_1 = s.count(s[i])
        num_2 = s[i]
print(num_2)



================================================================================

На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».

s = input()
if s.count('f') == 0:
    print('NO')
if s.count('f') == 1:
    print(s.find('f'))
if s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))

==================================================================================

На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.

s = input()
n1 = s.find('h')
n2 = s.rfind('h')
s1 = (s[:n1])
s2 = (s[n2 + 1:])
print (s1+s2)

======

s = input()
print((s[:s.find('h')])+(s[s.rfind('h')+1:]))

=================================================================================


