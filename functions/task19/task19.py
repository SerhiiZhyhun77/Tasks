# -*- coding: utf-8 -*-

"""ЗАДАЧА: РАСХОДЫ НА АВТОМОБИЛЬ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая просит пользователя ввести месячные расходы на
следующие нужды, связанные с его автомобилем: платеж по кредиту, страховка,
бензин, машинное масло, шины и техобслуживание. Затем программа должна
показать общую месячную стоимость и общую годовую стоимость этих расходов.
"""

def get_amount(msg=''):
    amount = None
    while amount is None:
        inp = input(msg)
        try:
            amount = float(inp)
            if amount < 0:
                amount = None
        except:
            print('\tEnter a positive number!')
    return amount

def main():
    print('Enter the data related to the vehicle:')
    amount_dict = {}
    amount_dict['loan'] = get_amount('\t- monthly loan payment: ')
    amount_dict['insurance'] = get_amount('\t- monthly insurance: ')
    amount_dict['gasoline'] = get_amount('\t- amount of gasoline per month: ')
    amount_dict['engine_oil'] = get_amount('\t- engine oil per month: ')
    amount_dict['tires'] = get_amount('\t- tires per month: ')
    amount_dict['maintenance'] = get_amount('\t- maintenance per month: ')
    # calculation
    amount_per_month = sum(amount_dict.values())
    amount_per_year = amount_per_month * 12
    # output
    print()
    print(f'Total monthly cost {amount_per_month:,.2f}')
    print(f'Total yearly cost of spending {amount_per_year:,.2f}')

if __name__ == '__main__':
    main()
