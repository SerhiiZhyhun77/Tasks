# -*- coding: utf-8 -*-

"""ЗАДАЧА: КОНВЕРТЕР КИЛОМЕТРОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая просит пользователя ввести расстояние в
километрах и затем это расстояние преобразует в мили. Формула преобразования:
    мили = километры х 0.6214
"""

def kilometers_to_miles(k):
    return k * 0.6214

def main():
    print('The program converts kilometers into miles')
    print('For quit enter "q"')
    while True:
        inp = input('Enter the value in kilometers (or "q"): ')
        if inp == 'q':
            exit()
        try:
            kilometers = float(inp)
            miles = kilometers_to_miles(kilometers)
            print(f'{kilometers} kilometers = {miles:.2f} miles')
        except Exception:
            print('Enter a number or "q"!')

if __name__ == '__main__':
    main()
