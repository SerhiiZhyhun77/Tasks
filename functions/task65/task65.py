# -*- coding: utf-8 -*-

'''ЗАДАЧА: САМЫЙ ЧАСТОТНЫЙ СИМВОЛ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая предоставляет пользователю возможность ввести
строковое значение и выводит на экран символ, который появляется в нем наиболее
часто.
'''


def rep_rate_analysis(text):
    rep_letter = {}
    for symb in text:
        if symb.isalpha():
            num = rep_letter.setdefault(symb, 0)
            rep_letter[symb] = num + 1
    max_num = max(rep_letter.values())
    letters = [l for l, r in rep_letter.items() if r == max_num]
    return max_num, letters


def main():
    text = input('Enter string value: ')
    if text:
        max_num, letters = rep_rate_analysis(text)
        # Output
        if len(letters) <= 1:
            print(f'The letter {",".join(letters)} is', end='')
        else:
            print(f'The letters {",".join(letters)} are', end='')
        print(f' repeated most often - {max_num} times.')


if __name__ == '__main__':
    main()
