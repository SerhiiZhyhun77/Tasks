# -*- coding: utf-8 -*-

"""ЗАДАЧА: ПРОСТЫЕ ЧИСЛА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Простое число - это число, которое делится без остатка на само себя и 1.
Например, число 5 является простым, потому что оно делится без остатка только
на 1 и 5. Однако число 6 не является простым, потому что оно делится без
остатка на 1, 2, 3 и 6.

Напишите булеву функцию is_prime, которая в качестве аргумента принимает
целое число и возвращает истину, если аргумент является простым числом,
либо ложь в противном случае. Примените функцию в программе, которая
предлагает пользователю ввести число и затем выводит сообщение с указанием,
является ли это число простым.
"""

def is_prime(num):
    for n in range(2, abs(num)):
        if num % n == 0:
            print(f'Number is divisible by {n}')
            return False
    return True

def inp():
    while True:
        n = input('Enter integer: ')
        try:
            num = int(n)
            return num
        except Exception:
            pass
        print('Please enter integer.')

def main():
    num = inp()
    if is_prime(num):
        print(f'The number {num} is prime.')
    else:
        print(f'The number {num} is not prime.')

if __name__ == '__main__':
    main()
