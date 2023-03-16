# -*- coding: utf-8 -*-

"""ЗАДАЧА: ОЦЕНЩИК МАЛЯРНЫХ РАБОТ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Малярная компания установила, что на каждые 10 квадратных метров поверхности
стены требуется 5 литров краски и 8 часов работы. Компания взимает за работу
2000 руб в час. Напишите программу, которая просит пользователя ввести
площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски.
Программа должна показать следующие данные:
    - количество требуемых емкостей краски;
    - количество затраченных рабочих часов;
    - стоимость краски;
    - стоимость работы;
    - общая стоимость малярных работ.
"""

def inp(msg):
    while True:
        inp = input(msg)
        try:
            num = float(inp)
            if num >=0:
                return num
            else:
                raise Exception
        except:
            print('Please enter a positive number!')

def main():
    # input data
    surface = inp('Enter the surface area of the wall to be painted: ')
    paint_cost = inp('Enter the cost of a 5 liter container of paint: ')
    # calculation
    num_container_of_paint = surface / 10
    work_time = surface / 10 * 8
    all_paint_cost = num_container_of_paint * paint_cost
    cost_of_work = work_time * 2000
    total_cost = all_paint_cost + cost_of_work
    # output
    print('\nOrder:')
    print(f'Surface: {surface:>30,.2f}')
    print(f'Paint cost: {paint_cost:>27,.2f}')
    print(f'Number of containter of paint: {num_container_of_paint:>8,.2f}')
    print(f'Work time: {work_time:>28,.2f}')
    print(f'All paint cost: {all_paint_cost:>23,.2f}')
    print(f'Cost of work: {cost_of_work:>25,.2f}')
    print('-' * 40)
    print(f'Total cost: {total_cost:>27,.2f}')

if __name__ == '__main__':
    main()
