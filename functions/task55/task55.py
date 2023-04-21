# -*- coding: utf-8 -*-

'''ЗАДАЧА: ГЕНЕРАЦИЯ ПРОСТОГО ЧИСЛА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Натуральное (целое положительное) число является простым, если оно не имеет
делителей кроме 1 и самого себя. Натуральное (целое положительное) число
является составным, если оно не является простым. Напишите программу, которая
просит пользователя ввести целое число больше 1 и затем выводит все простые
числа, которые меньше или равны введенному числу. Программа должна работать
следующим образом:
    - после того как пользователь ввел число, программа должна заполнить
    список всеми целыми числами начиная с 2 и до введенного значения;
    - затем программа должна применить цикл, чтобы пройти по списку. Каждый
    элемент должен быть в цикле передан в функцию, которая определяет и
    сообщает, что элемент является простым числом или составным числом.
'''

def is_prime_number(num):
    for number in range(2, num):
        if num % number == 0:
            return False
    return True

def inp():
    while True:
        s = input('Enter a positive integer greater then 1: ')
        if s.isnumeric():
            return int(s)
        print('Please enter a positive integer.')

def main():
    # get num from user
    num = inp()
    # make num list
    num_lst = [n for n in range(2, num + 1)]
    # check for prime number
    print()
    print('These are prime numbers between 2 and the number you specify:')
    for num in num_lst:
        if is_prime_number(num):
            print(num, end=' ')
    print()
    
if __name__ == '__main__':
    main()
