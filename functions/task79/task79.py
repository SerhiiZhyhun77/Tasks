# -*- coding: utf-8 -*-

'''ЗАДАЧА: РЕКУРСИВНОЕ УМНОЖЕНИЕ
[Начинаем программировать на Python. Тони Гэддис (2022)]
Разработайте рекурсивную функцию, которая принимает два аргумента в параметры
х и у. Данная функция должна вернуть значение произведения х на у. При этома
умножение должно быть выполнено, как повторяющееся сложение, следующим образом:
    7 * 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4.
(Для упрощения функции исходите из того, что х и у будут всегда содержать
положительные ненулевые числа.)
'''


def mult(x, y):
    if x < 1:
        return 0
    return y + mult(x - 1, y)


def main():
    x = 4
    y = 2
    print(f'{x} * {y} = {mult(x, y)}')


if __name__ == '__main__':
    main()