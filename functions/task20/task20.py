# -*- coding: utf-8 -*-

"""ЗАДАЧА: НАЛОГ НА НЕДВИЖИМОЕ ИМУЩЕСТВО
[Начинаем программировать на Python. Тони Гэддис (2022)]

Муниципальный округ собирает налоги на недвижимое имущество на основе
оценочной стоимости имущества, составляющей 60% его фактической стоимости.
Например, если акр земли оценен в 10000 долларов, то его оценочная стоимость
составит 6000 долларов. В этом случае налог на имущество составит 72 цента за
каждые 100 долларов оценочной стоимости. Налог на акр, оцененный в 6000
долларов, составит 43,20 долларов. Напишите программу, которая запрашивает
фактическую стоимость недвижимого имущества и показывает оценочную стоимость
и налог на имущество.
"""

def calculation(cost):
    estimated_cost = cost * 0.6
    tax = estimated_cost * 0.72
    return estimated_cost, tax

def main():
    cost = None
    while cost is None:
        inp = input('Enter the value of the property: ')
        try:
            cost = float(inp)
            if cost < 0:
                cost = None
                print('Please enter a positive number!')
        except:
            print('Error! Enter a number.')
    estimated_cost, tax = calculation(cost)
    print('\nResult:')
    print(f'\tValue of the property: {cost:,.2f}')
    print(f'\tEstimated cost: {estimated_cost:,.2f}')
    print(f'\tProperty tax: {tax:,.2f}')

if __name__ == '__main__':
    main()