# count = 0
# while count <= 10:
#     if count < 5:
#         print("1Result <5 = " + str(count))
#     if count == 5:
#        print("2Result ==5 = " +  str(count))
#     if count > 6 and count <= 8:
#        print("3Result 7-8 = " +  str(count))
#     if count == 10:
#         print("4Result 10 = " + str(count))
#     print("count = " + str(count))
#     count += 1
#     print ('==================')



# count = 10
# for i in range(0, count+1):
#     print(i)

#списки
# ll = [10,12,14,15,16, 'kate']
# for i in ll:
#     print(i)
#     n = i * 2
#     print (i, '== * 2 == ',  n)

# #деление без остатка
# ll = [2,5,9,12,6,11,10,18,14,15,16,0,21]
# for i in ll:
#     if i % 2 == 0:
#         print(ll.index(i), "==", i, "%2", )      #вывод индекса числа в списке
#     elif i % 3 == 0:
#         print(ll.index(i), "==", i, "%3")

# #разделение на четные/нечетные
# ll = [2, 5, 9, 12, 6, 11, 10, 18, 14, 15, 16, 0, 21]
# even_list = []
# odd_list = []
# for i in ll:
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print("even_list", even_list)
# print("odd_list", odd_list)


# #функция
# def even_odd(n):           #переменная объявляется внутри функции и работает только в этой функции
#     if n % 2 == 0:
#         even_m = str(n) + " is even nomber"
#         return even_m
#     else:
#         odd_m = str(n) + " is odd nomber"
#         return odd_m
# print(even_odd(101))

# #запуск функции в списке
# ll = [2, 5, 9, 12, 6, 11, 10, 18, 14, 15, 16, 0, 21]
# def even_odd(n):
#     if n % 2 == 0:
#         even_m = str(n) + " is even nomber"
#         return even_m
#     else:
#         odd_m = str(n) + " is odd nomber"
#         return odd_m
# for i in ll:
#    print(even_odd(i))


# #input запуск в cmd
# import sys
# elem = int(input())
# def even_odd(n):
#     if n % 2 == 0:
#         even_m = str(n) + " is even nomber"
#         return even_m
#     else:
#         odd_m = str(n) + " is odd nomber"
#         return odd_m
# print(even_odd(elem))
