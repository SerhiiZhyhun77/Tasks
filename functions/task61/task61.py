# -*- coding: utf-8 -*-

'''ЗАДАЧА: АЛФАВИТНЫЙ ПЕРЕВОДЧИК НОМЕРА ТЕЛЕФОНА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Многие компании используют телефонные номера наподобие 555-GET-FOOD,
чтобы клиентам было легче запоминать эти номера. На стандартном телефоне
буквы алфавита поставлены в соответствие числа следующим образом:
    A, B и C = 2
    D, E и F = 3
    G, H и I = 4
    J, K и L = 5
    M, N и O = 6
    P, Q, R и S = 7
    T, U и V = 8
    W, X, Y и Z = 9

Напишите программу, которая просит пользователя ввести 10-символьный номер
телефона в формате ХХХ-ХХХ-ХХХХ. Приложение должно показать номер телефона,
в котором все буквенные символы в оригинале переведены в их числовой
эквивалент. Например, если пользователь вводит 555-GET-FOOD, то приложение
должно вывести 555-438-3663.
'''

def symb_to_num(s):
    symb_num_dict = {
        ('A', 'B', 'C') : '2',
        ('D', 'E', 'F') : '3',
        ('G', 'H', 'I') : '4',
        ('J', 'K', 'L') : '5',
        ('M', 'N', 'O') : '6',
        ('P', 'Q', 'R', 'S') : '7',
        ('T', 'U', 'V') : '8',
        ('W', 'X', 'Y', 'Z') : '9'
    }
    for key in symb_num_dict:
        if s.upper() in key:
            return symb_num_dict[key]
    return s

def main():
    tel_num = input('Enter a 10-character phone number in the format '
                    'XXX-XXX-XXXX: ')
    dig_num = ''
    # Make a digital number by replacing letters with numbers
    for s in tel_num:
        dig_num += symb_to_num(s)
    # Output
    print('Numeric equivalent:', dig_num)

if __name__ == '__main__':
    main()
