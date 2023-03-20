# -*- coding: utf-8 -*-

"""ЗАДАЧА: МЕСЯЧНЫЙ НАЛОГ С ПРОДАЖ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Розничная компания должна зарегистрировать отчет о месячном налоге с продаж с
указанием общего налога с продаж за месяц и взимаемых сумм муниципального и
федерального налогов с продаж. Федеральный налог с продаж составляет 5%,
муниципальный налог с продаж - 2.5%. Напишите программу, которая просит
пользователя ввести общий объем продаж за месяц. Из этого значения приложение
должно рассчитать и показать:
- сумму мунициального налога с продаж;
- сумму федерального налога с продаж;
- общий налог с продаж (муниципальный плюс федеральный).
"""

def federal_tax(amount):
    return amount * 0.05

def municipal_tax(amount):
    return amount * 0.025

def main():
    amount = None
    while amount is None:
        inp = input('Enter the amount of sales per month: ')
        try:
            amount = float(inp)
        except:
            print('Please enter a number.')

    # calculation
    m_tax = municipal_tax(amount)
    f_tax = federal_tax(amount)
    total_tax = m_tax + f_tax

    # output
    print()
    print('Calculation:'.rjust(35,'_'))
    print(f'Municipal tax: {m_tax:>20,.2f}')
    print(f'Federal tax: {f_tax:>22,.2f}')
    print('-' * 35)
    print(f'Total tax: {total_tax:>24,.2f}')

if __name__ == '__main__':
    main()
