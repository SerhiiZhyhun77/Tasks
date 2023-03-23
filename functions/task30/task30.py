# -*- coding: utf-8 -*-

"""ЗАДАЧА: КИНЕТЕЧЕСКАЯ ЭНЕРГИЯ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Из физики известно, что движущееся тело имеет кинетическую энергию.
Приведенная ниже формула может использоваться для определения кинетической
энергии движущегося тела:
    Ke = 1/2 mv^2
где Ke - это кинетическая энергия; m - масса тела, кг; v - скорость тела, м/с.
Напишите функцию kinetic_energy, которая в качестве аргументов принимает
массу тела (в килограммах) и его скорость (в метрах в секунду). Данная
функция должна вернуть величину кинетической энергии этого тела. Напишите
программу, которая просит пользователяввести значения массы и скорости,
а затем вызывает функцию kinetic_energy, чтобы получить кинетическую энергию
тела.
"""

def kinetic_energy(m, v):
    return 1 / 2 * m * v ** 2

def inp(msg):
    while True:
       x = input(msg)
       try:
           return float(x)
       except:
           print('Please enter a number.')

def main():
    print('This program will calculate the kinetic energy.')
    m = inp('Enter mass in kilograms: ')
    v = inp('Enter speed in meters per second: ')
    # output
    print(f'Kinetic energy = {kinetic_energy(m, v):.2f}')

if __name__ == '__main__':
    main()
