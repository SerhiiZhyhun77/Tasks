# -*- coding: utf-8 -*-

"""ЗАДАЧА: КАЛОРИИ ЗА СЧЕТ ЖИРОВ И УГЛЕВОДОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Диетолог работает в спортивном клубе и дает рекомендации клиентам в отношении
диеты. В рамках своих рекомендаций он запрашивает у клиентов количество
граммов жиров и углеводов, которые они употребили за день. Затем на основе
приведенной ниже формулы он вычисляет количество калорий, которые получаются
в результате употребления жиров:
        калории от жиров = граммы жиров * 9
Затем на основе еще одной формулы он вычисляет количество коларий, которые
получаются в результате употребления углеводов:
        калориии от углеводов = граммы углеводов * 4
Диетолог просит вас написать программу, которая выполнит эти расчеты.
"""

def calculation_calories(fat, carbohydrates):
    calories_from_fat = fat * 9
    calories_from_carbohydrates = carbohydrates * 4
    return calories_from_fat, calories_from_carbohydrates

def inp(msg):
    num = -1
    while num < 0:
        inp = input(msg)
        try:
            num = int(inp)
        except:
            print('Please enter a positive integer.')
    return  num

def main():
    fat = inp('How many grams of fat did you eat per day? ')
    carbohydrates = inp('How many grams of carbohydrates did you eat per day? ' )
    calories_from_fat, calories_from_carbohydrates = calculation_calories(
        fat, carbohydrates)
    print('\nResult:')
    print(f'\tCalories from fat: {calories_from_fat:,d}')
    print(f'\tCalories from carbohydrates: {calories_from_carbohydrates:,d}')

if __name__ == '__main__':
    main()
