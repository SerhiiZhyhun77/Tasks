# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите функцию cube(), которая получает один числовой параметр и возвращает
 значение указанного числа в третьей степени. Протестируйте функцию - вызовите 
 cube() для нескольких чисел и выведите результаты."""
 
def cube(x):
    return pow(x, 3)
    

def main():
    numbers = [2,5,8,11,17,44,100]
    numbers_power = [cube(number) for number in numbers]  # to the 3 power
    #show result
    for i in range(len(numbers)):
        print(f"{numbers[i]}^3 = {numbers_power[i]}")


if __name__ == '__main__':
    main()