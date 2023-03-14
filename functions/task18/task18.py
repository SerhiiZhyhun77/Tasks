# -*- coding: utf-8 -*-

"""ЗАДАЧА: КАКОВА СТОИМОСТЬ СТРАХОВКИ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Многие финансовые эксперты рекомендуют собственникам недвижимого имущества
страховать свои дома или постройки как минимум на 80% суммы замещения
строения. Напишите программу, которая просит пользователя ввести стоимость
строения и затем показывает минимальную страховую сумму, на которую он должен
застраховать недвижимое имущество.
"""

def insurance_calculation(cost):
    return cost * 0.8

def main():
    print('*' * 20, 'Calculation insurance', '*' * 20)
    cost = 0
    while cost == 0:
        inp = input('How much is your building cost? ')
        try:
            cost = float(inp)
            if cost < 0:
                cost = 0
                print('Enter a positive number')
        except:
            print('Enter a number')
    insurance = insurance_calculation(cost)
    print(f'The minimal amount of your insurance is {insurance:.2f}')

if __name__ == '__main__':
    main()
