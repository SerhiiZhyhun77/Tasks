# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу temperature.py, которая определяет две функции.
1. convert_cel_to_far() получает один параметр float, представляющий температуру
 по шкале Цельсия, и возвращает значение float, представляющее ту же температуру
 по шкале Фвренгейта. Преобразование выполняется по следующей формуле:
 
 F = C * 9 / 5 + 32

2. convert_far_to_cel() получает один параметр float, представляющий температуру
 по шкале Фвренгейта, и возвращает значение float, представляющее ту же
 температуру по шкале Цельсия. Преобразование выполняется по следующей
 формуле:
 
 C = (F - 32) * 5 / 9
 
Программа должна делать следующее.
 
1. Запрашивать у пользователя температуру в градусах по шкале Фвренгейта, а
 затем выводить температуру, преобразованную к шкале Цельсия.
 
2. Запрашивать у пользователя температуру в градусах по шкале Цельсия, а затем
 выводить температуру, преобразованную к шкале Фаренгейта.
 
3. Выводить все преобразования температуры, округленные до двух знаков в дробной
 части.

Пример выполнения программы:

Enter a temperature in degrees F: 72
72 degrees F = 22.22 degrees C

Enter a temperature in degrees C: 37
37 degrees C = 98.60 degrees F
"""

def convert_cel_to_far(c):
    f = c * 9 / 5 + 32
    return f


def convert_far_to_cel(f):
    c = (f - 32) * 5 / 9
    return c
    
    
def main():
    # F to C
    f = float(input("Enter a temperature in degrees F: "))
    c = convert_far_to_cel(f)
    print(f"{f} degrees F = {c:.2f} degrees C")
    print()
    
    # C to F
    c = float(input("Enter a temperature in degrees C: "))
    f = convert_cel_to_far(c)
    print(f"{c} degrees C = {f:.2f} degrees F")
    print()
    
if __name__ == '__main__':
    main()