# -*- coding: utf-8 -*-

'''ЗАДАЧА: РЕКУРСИВНЫЙ МЕТОД ВОЗВЕДЕНИЯ В СТЕПЕНЬ
[Начинаем программировать на Python. Тони Гэддис (2022)]
Разработайте функцию, в которой рекурсия применяется для возведения числа в
степень. Данная функция должна принимать два аргумента: число, которое будет
возведено в степень, и показатель степени. Исходите из того, что показатель
степени является неотрицательным целым числом.
'''


def pow_num(n, p):
    if p == 1:
        return n
    return n * pow_num(n, p - 1)


def main():
    n = 2
    p = 10
    print(f'{n} ** {p} = {pow_num(n, p)}')


if __name__ == '__main__':
    main()
