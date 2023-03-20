# -*- coding: utf-8 -*-

"""ЗАДАЧА: ФУТЫ В ДЮЙМ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Один фут равняется 12 дюймам. Напишите функцию feet_to_inches, которая в
качестве аргумента принимает количество футов и возвращает количество дюймов
в этом количестве футов. Примените эту функцию в программе, которая
предлагает пользователю ввести количество футов и затем показывает количество
дюймов в этом количестве футов.
"""

# calculation inches
def feet_to_inches(feet):
    return feet * 12

def main():
    while True:
        inp = input('Enter number of feet: ')
        try:
            feet = float(inp)
            if feet >= 0:
                break
        except:
            pass
        print('Please enter a positive number')
    # output
    print(f'{feet:,.2f} feet equals {feet_to_inches(feet):,.2f} inches')

if __name__ == '__main__':
    main()
