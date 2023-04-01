# -*- coding: utf-8 -*-

"""ЗАДАЧА: ИГРА В УГАДЫВАНИЕ СЛУЧАЙНОГО ЧИСЛА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая генерирует случайное число в диапазоне от 1 до
100 и просит пользователя угадать это число. Если догадка пользователя больше
случайного числа, то программа должна вывести сообщение "Слишком много,
попробуйте еще раз". Если догадка меньше случайного числа, то программа
должна вывести сообщение "Слишком мало, попробуйте еще раз". Если
пользователь число угадывает, то приложение должно поздравить пользователя и
сгенерировать новое случайное число, чтобы возобновить игру.

Необязательное улучшение: улучшите игру, чтобы она вела подсчет попыток
угадать, которые делает пользователь. Когда пользователь угадывает случайное
число правильно, программа должна показать количество попыток.
"""

import random

def pick_number():
    return random.randint(1, 100)

def start():
    # new number
    guess_number = pick_number()
    # show message
    print('I picked a number between 1 and 100. Guess!')
    print('Enter "Q" for quit.')
    return guess_number

def inp():
    while True:
        n = input('Enter your number: ')
        # for quit
        if n.lower() == 'q':
            return 'q'
        try:
            num = int(n)
            if num < 1 or num > 100:
                print('Please enter positive integer between 1 and 100')
            else:
                return num
        except Exception:
            print('Please enter integer between 1 and 100')

def main():
    guess_number = start()
    attempts = 0
    while True:
        num = inp()
        attempts += 1
        #  if q - exit
        if num == 'q':
            print('Game over!')
            exit()
        # if few
        elif num < guess_number:
            print('Too few, try again')
        # if much
        elif num > guess_number:
            print('Too much, try again')
        # if guess right
        else:
            # show congrats
            print()
            print(f'Congratulations, you guessed right in {attempts} attempts!')
            print('-' * 40)
            guess_number = start()  # pick new number 
            attempts = 0  # reset attempts

if __name__ == '__main__':
    main()
