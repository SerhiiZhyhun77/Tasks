# -*- coding: utf-8 -*-

"""ЗАДАЧА: СИДЯЧИЕ МЕСТА НА СТАДИОНЕ
[Начинаем программировать на Python. Тони Гэддис (2022)]

На стадионе имеется три категории сидячих мест. Места класса А стоят 20
долларов, места класса В - 15 долларов, места класса С - 10 долларов.
Напишите программу, которая запрашивает, сколько билетов каждого класса было
продано, и затем выводит сумму дохода, полученного от продажи билетов.
"""

def inp(msg):
    while True:
        inp = input(msg)
        if inp.isdigit():
            return int(inp)
        else:
            print('Please enter a positive integer!')

def calculation(a, b, c):
    seats_cost = {
        'a' : 20,
        'b' : 15,
        'c' : 10
    }
    sum = a * seats_cost['a'] + b * seats_cost['b'] + c * seats_cost['c']
    return sum

def main():
    a = inp('How many class A seats sold? ')
    b = inp('How many class B seats sold? ')
    c = inp('How many class C seats sold? ')
    sum = calculation(a, b, c)
    print('\nResult:')
    print(f'The amount of income received from ticket sales: {sum:,d}')

if __name__ == '__main__':
    main()
