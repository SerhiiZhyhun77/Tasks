# -*- coding: utf-8-*-

import random

"""Напишите функцию roll(), которая использует randint() для моделирования 
броска симметричного кубика, возвращающего случайное целое число от 1 до 6.

Напишите программу, которая моделирует 10000 бросков игрального кубика и 
выводит среднее значение из тех, что выпали."""

def roll():
    return random.randint(1, 6)


def main():
    NUMBER_OF_THROWS = 10_000
    summ = 0
    for i in range(NUMBER_OF_THROWS):
        summ += roll()
    average = summ / NUMBER_OF_THROWS
    print(f'Average over {NUMBER_OF_THROWS} trows: {average}')


if __name__ == '__main__':
    main()
