# -*- coding: utf-8 -*-

"""ЗАДАЧА: ИГРА "КАМЕНЬ, НОЖНИЦЫ, БУМАГА"
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая дает пользователю возможность поиграть с
компьютером в игру "Камент, ножницы, бумага". Программа должна работать
следующим образом.
1. Когда программа запускается, генерируется случайное число в диапазоне от 1
до 3. Если число равняется 1, то компьютер выбрал камень. Если число
равняется 2, то компьютер выбрал ножницы. Если число равняется 3,
то компьютер выбрал бумагу.
(Пока не показывайте выбор компьютера.)
2. Пользователь вводит на клавиатуре выбранный вариант "камень", "ножницы"
или "бумага".
3. Выбор компьютера выводится на экран.
4. Победитель выбирается согласно следующим правилам:
    - если один игрок выбирает камень, а другой игрок выбирает ножницы,
    то побеждает камень (камень разбивает ножницы);
    - если один игрок выбирает ножницы, а другой игрок выбирает бумагу,
    то побеждают ножницы (ножницы режут бумагу);
    - если один игрок выбирает бумагу, а другой игрок выбирает камень,
    то побеждает бумага (бумага заворачивает камень);
    - если оба игрока делают одинаковый выбор, то для определения победителя
    нужно сыграть повторный раунд.
"""

import random

subjects = {
    1 : 'stone',
    2 : 'scissors',
    3 : 'paper'
}

def comp_choice():
    return random.randint(1, 3)

def info():
    print('The computer has made its choice')
    print('Enter your subject (stone, scissors or paper).')

def user_choice():
    while True:
        subj = input(': ')
        subj = subj.lower()
        if subj not in subjects.values():
            print('You entered something wrong.')
            print('You can only enter words "stone", "scissors" or "paper".')
        else:
            # get subject code
            for code, subj_name in subjects.items():
                if subj == subj_name:
                    return code

def show_choice(comp_subj, user_subj):
    print(f'You choosed: {subjects[user_subj]}, computer choosed: '
          f'{subjects[comp_subj]}.')

def main():
    win = False
    print('-' * 40)
    print('Game: "Stone, scissors, paper"')
    info()
    while not win:
        # get the choice of computer and user
        comp_subj = comp_choice()
        user_subj = user_choice()
        # determine the result
        print()
        print('-' * 40)
        print('Result:')
        # if a draw
        if comp_subj == user_subj:
            show_choice(comp_subj, user_subj)
            print('You and the computer made the same choice.')
            print('To determine the winner you need to play a second round.')
            print('-' * 40)
            info()
        # if computer won
        elif (comp_subj == 1 and user_subj == 2) or \
                (comp_subj == 2 and user_subj == 3) or \
                (comp_subj == 3 and user_subj == 1):
            print('Computer won!')
            win = True
        # else user won
        else:
            print('You won!')
            win = True
    # show choice computer and user
    show_choice(comp_subj, user_subj)

if __name__ == '__main__':
    main()
