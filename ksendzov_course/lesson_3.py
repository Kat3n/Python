count = 0
while count <= 100:
    print('count = ', count, count <= 100)
    count += 1

---------------------------------------------------

count = 0
for i in range(0, 100):
    print('i = ', i)

--------------------------------------------------

count = 0
for i in range(0, 100, 5):
    print('i = ', i)                  #задаем шаг

---------------------------------------------------

count = 1
for i in range(0, 100, 5):
    print('count = ', count, 'i = ', i)
    count += 1

---------------------------------------------------

count = 1
test_list = [1,2,3,0,88,156,499,45,12,1,3,69,789,789,145]

for i in test_list:
    print('count = ', count, 'i = ', i)
    count += 1

---------------------------------------------------

count = 1
test_list = [1,2,3,0,88,156,499,45,12,1,3,69,789,789,145,'jghh', 'ggt88',[11,22,'hghurt'],{'jgjgj':'jgj'}]

for i in test_list:
    print('count = ', count, 'i = ', i)
    count += 1

----------------------------------------------------

count = 1
test_list = [1,2,3,0,88,156,499,4.5,12,1,3,69,True,789,145,'jghh', 'ggt88',[11,22,'hghurt'],{'jgjgj':'jgj'}]
test_list2 = []
print('test_list2 before = ', test_list2)
for i in test_list:
    print('count = ', count, 'i = ', i)
    test_list2.append(i)
    count += 1
print('test_list2 after = ', test_list2)           #добавляем значения в другой массив

----------------------------------------------------------

count = 1
test_list = [1,2,3,0,88,156,499,4.5,12,1,3,69]
test_list2 = []
print('test_list2 before = ', test_list2)
for i in test_list:
    print('count = ', count, 'i = ', i)
    test_list2.append(i + count)
    count += 1
print('test_list2 after = ', test_list2)

---------------------------------------------------------

count = 1
test_list = [1,2,3,0,88,156,499,4.5,12,1,3,69]
test_list2 = []
print('test_list2 before = ', test_list2)
for i in test_list:
    print('count = ', count, 'i = ', i)
    test_list2.append(str(i + count) + 'years')
    count += 1
print('test_list2 after = ', test_list2)

----------------------------------------------------------

                #index


count = 1
test_list = [1,2,3,0,88,156,499,4.5,12,1,3,69]
test_list2 = []
print('test_list2 before = ', test_list2)
for i in test_list:
    item_index = test_list.index(i)
    print('i = ', i, '| item_index = ', item_index)
    count += 1                                                
-----------------------------------------------------------



