# -*- coding: utf-8 -*-

"""ЗАДАЧА: КОТЫ В ШЛЯПАХ
У вас сто котов. Однажды вы решаете рассадить всех своих котов в большой круг. 
Изначально ни один из них не носит шляпы. Вы сто раз обходите круг,всегда 
начиная с первого кота (кот №1). Каждый раз, когда вы останавливаетесь рядом с 
котом, вы проверяете, есть ли на нем шляпа. Если шляпы нет,то вы надеваете 
шляпу на кота, а если есть - снимаете ее.
    
    1. На первом круге вы останавливаетесь у каждого кота и надеваете на него 
    шляпу.
    2. На втором круге вы останавливаетесь у каждого второго кота (№2, №4, №6, 
    №8 и т.д.)
    3. На третьем круге вы останавливаетесь у каждого третьего кота (№3, №6, 
    №9, №12 и т.д.)
    4. Процесс продолжается до тех пор, пока вы не обойдете круг сто раз. При 
    последнем обходе вы останавливаетесь только у кота №100.

Напишите программу, которая выводит, на каких котах будут шляпы после всех 
обходов."""


NUMBER_OF_CATS = 100
REPEAT = 100


def change_hat_status(status):
    return False if status else True


# if you want to show hats - call this function
def show_hats(num, lst):
    print(num, ':', sep='')
    for i in range(len(lst)):
        if lst[i]:
            print('1', end = '')
        else:
            print('0', end = '')
        if i > 0 and not (i + 1) % 10:
            print()
    print()
    print('-' * 20)


def show_result(lst):
    print('*' * 30)
    print('Result:')
    for i in range(len(lst)):
        if lst[i]:
            print(f'Cat #{i + 1} in a hat')
    print('*' * 30)


def main():
    hats = [False for i in range(NUMBER_OF_CATS)]
    for step in range(REPEAT):
        for i in range(step, NUMBER_OF_CATS, step + 1):
            hats[i] = change_hat_status(hats[i])
        # show_hats(step + 1, hats)  # for show result every step
    show_result(hats)


if __name__ == '__main__':
    main()
