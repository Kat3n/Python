# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

# input_data = int(input('enter_your_money_in_ BYN   '))
# if input_data > 0:
#     print('Your_money == ', input_data)
#     print('Your_money_in_USD == ', input_data/2.8304)
# else:
#     print("You don't have money?")


# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.



# input_data = int(input('Enter_your_money_in_ BYN   '))
# if input_data > 0:
#     print('Your_money == ', input_data, ' BYN')
#     print('Your_money_in_USD == ', input_data/3.31433)
#     print('Your_money_in_EUR == ', input_data /3.59837)
#     print('Your_money_in_СHF == ', input_data /3.55654)
#     print('Your_money_in_GBR == ', input_data /4.31395)
#     print('Your_money_in_CNY == ', input_data /0.52033)
# else:
#     print("You don't have money?")



# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
# 3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
# 4.Валюту пользователя определите сами.

def main():
    input_money = function_input_money()
    conversion_money = function_conversion_money(input_money)
    cond_mon = function_condition_2(input_money)

def function_input_money():                                      #funcyion_1
    input_data = input('Enter_your_money_in_ BYN   ')
    return input_data

def function_conversion_money(conv_money):                       #function_2
    if int(conv_money) > 0:
        print('Your_money_in_USD == ', int(conv_money)/3.31433)
        print('Your_money_in_EUR == ', int(conv_money) /3.59837)
        print('Your_money_in_СHF == ', int(conv_money) /3.55654)
        print('Your_money_in_GBR == ', int(conv_money) /4.31395)
        print('Your_money_in_CNY == ', int(conv_money) /0.52033)
        return (conv_money)

def function_condition_2(money_1):
    if int(money_1) < 0:
        print('Enter positive number')
    elif int(money_1) == 0:
        print("it's very little")
        return (money_1)
main()


