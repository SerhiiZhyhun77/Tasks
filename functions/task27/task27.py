# -*- coding: utf-8 -*-

"""ЗАДАЧА: МАТЕМАТИЧЕСКИЙ ТЕСТ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая позволяет проводить простые математические тесты. 
Она должна показать два случайных числа, которые должны быть просуммированы 
вот так:
    247
  + 129
Эта программа должна давать обучаемому возможность вводить ответ. Если ответ 
правильный, то должно быть показано поздравительное сообщение. Если ответ 
неправильный, то должно быть показано сообщение с правильным ответом. 
"""

import random

def think_of_2_numbers():
    x1 = random.randint(0, 1000)
    x2 = random.randint(0, 1000)
    return x1, x2

def inp():
    while True:
        inp = input(': ')
        try:
            answ = int(inp)
            if answ >= 0:
                return answ
        except:
            pass
        print('Please enter a positive number.')

def main():
    x1, x2 = think_of_2_numbers()
    print('Add up 2 number:')
    print(' ', x1)
    print('+', x2)
    answ = inp() # get answer

    # output
    result = x1 + x2
    print()
    if answ == result:
        print('Your answer is correct!')
    else:
        print('Your answer is not correct!')
        print(f'{x1} + {x2} = {result}')

if __name__ == '__main__':
    main()
