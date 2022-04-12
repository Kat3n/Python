            #break
            ------

count = 1
while True:
    count += 1
    print('count == ', count)
    if count == 100:
        break

-------------------------------------------------------

count = 1
while True:
    count += 1
    if count > 100 and count < 130:
        time.sleep(.200)
        print('sleep == ', count)
        continue
    print('count > 100 and count < 150 ======= ', count)
    print('count == ', count)
    if count > 250:
        break

-------------------------------------------------------

while True:
    input_data = int(input('enter money'))
    if input_data < 0:
        print('enter money above 0')
        continue
    bun_to_usd = int(input_data) / 3.0
    print('USD = ', bun_to_usd)

--------------------------------------------------------

import time, random
created_list = [value for value in range(0, random.randint(10,30))]
print('created_list', created_list)


--------------------------------------------------------

import time, random
created_list = [value for value in range(0, random.randint(10,30))]
second_list = []
random_and_of_list_values = random.randint(10,40)
for i in range(0, random_and_of_list_values):
    second_list.append(i)
print('created_list', created_list)
print('sec-list', second_list)


----------------------------------------------------------

def main():
    input_money = get_money()
    usd_money = exchange(input_money)
    print('usd_money = ', usd_money)
def get_money():
    input_data = input('Enter UAH amount:')
    return input_data
def exchange(money):
    int_money = int(money) / 2.5
    return int_money
main()

--------------------------------------------------------



def say_my_name(name):
    hello_string = 'Hello ' + name
    return hello_string
name_1 = say_my_name('kate')
name_2 = say_my_name('alex')
name_3 = say_my_name('julia')
print(name_1)
print(name_2)
print(name_3)

---------------------------------------------------------


