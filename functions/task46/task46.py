# -*- coding: utf-8 -*-

'''ЗАДАЧА: СТАТИСТИКА ДОЖДЕВЫХ ОСАДКОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Разработайте программу, которая позволяет пользователю занести в список общее
количество дождевых осадков за каждый из 12 месяцев. Программа должна
вычислить и показать суммарное количество дождевых осадков за год, среднее
ежемесячное количество дождевых осадков и месяцы с самым высоким и самым
низким количеством дождевых осадков.
'''

import datetime
import statistics

def get_month_name(month):
    date = datetime.date(2023, month, 1)
    return date.strftime('%B')

def main():
    max = 0
    min = 1000000
    amount_of_precipitation_lst = []
    for i in range(12):
        while True:
            precipitation = input('Enter the amount of precipitation in '
                                  f'{get_month_name(i + 1)}: ')
            if precipitation.isnumeric():
                break
            else:
                print('Please enter positive integer.')
        precipitation = int(precipitation)
        # check max / min
        if precipitation > max:
            max = precipitation
        if precipitation < min:
            min = precipitation
        # add precipitation to list
        amount_of_precipitation_lst.append(precipitation)
    # output
    print()
    # amount of rainfall
    print(f'Amount of rainfall for the year: {sum(amount_of_precipitation_lst)}')
    # average rainfall
    print('Average monthly rainfall: '
          f'{statistics.mean(amount_of_precipitation_lst):.0f}')
    # highest rainfall month
    print('Months with the highest rainfall: ', end='')
    month_lst = []
    for i, precipitation in enumerate(amount_of_precipitation_lst):
        if max == precipitation:
            month_lst.append(get_month_name(i + 1))
    print(', '.join(month_lst))
    # lowest rainfall month
    print('Months with the lowest rainfall: ', end='')
    month_lst = []
    for i, precipitation in enumerate(amount_of_precipitation_lst):
        if min == precipitation:
            month_lst.append(get_month_name(i + 1))
    print(', '.join(month_lst))

if __name__ == '__main__':
    main()
