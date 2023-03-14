# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу factors.py, которая запрашивает у пользователя положительное 
целое число, а затем выводит список множителей этого числа. Пример запуска 
программы с выводом результата:

Enter a positive integer: 12
1 is a factor of 12
2 is a factor of 12
3 is a factor of 12
4 is a factor of 12
6 is a factor of 12
12 is a factor of 12
"""

def get_factors(number):
    factors = [num for num in range(1, number+1) if not number % num]
    return factors
    

def main():
    number = int(input("Enter a positive integer: "))
    factors = get_factors(number)
    for factor in factors:
        print(f"{factor} is a factor of {number}")


if __name__ == '__main__':
    main()