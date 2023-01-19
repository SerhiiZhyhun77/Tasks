# -*- coding: utf-8 -*-

"""При помощи модуля random и использования условной логики можно построить 
модель выбборов, в которых участвуют два кандидата.

Допустим, два кандидата А и В, претендуют на должность мэра города, в котором 
три избирательных участка. Последние опросы показывают, что кандидат А имеет 
следующие шансы на победу в каждом участке.

- Участок 1: 87%
- Участок 2: 65%
- Участок 3: 17%

Напишите программу, которая моделирует выборы 10000 раз и выводит процент 
выборов, когда победил кандидат А.

Для простоты считайте, что кандидат одержал верх на выборах, если он победил 
как минимум на двух из трех участков."""

import random


NUMBER_OF_POLLING_STATION = 3
NUMBER_OF_ELECTIONS = 10_000


def result_voting_polling_station():
    votes_a = random.randint(0, 100)
    votes_b = 100 - votes_a
    if votes_a > votes_b:
        return 'a'  # candodate A won
    elif votes_a < votes_b:
        return 'b'  # candidate B won
    else:
        return 0  # re-elections


def round_of_election():
    wins_a = 0
    wins_b = 0
    for i in range(NUMBER_OF_POLLING_STATION):
        result = 0
        while not result:
            result = result_voting_polling_station()
        if result == 'a':
            wins_a += 1
        else:
            wins_b += 1
    if wins_a > wins_b:
        return 'a'
    else:
        return 'b'


def main():
    wins_a = 0
    wins_b = 0
    for i in range(NUMBER_OF_ELECTIONS):
        if round_of_election() == 'a':
            wins_a += 1
        else:
            wins_b += 1
    percent_a = wins_a / NUMBER_OF_ELECTIONS
    percent_b = wins_b / NUMBER_OF_ELECTIONS
    print(f'Elections were held {NUMBER_OF_ELECTIONS} times')
    print(f'Probabiliti of winning candidate A: {percent_a:.2%},' \
          f'candidate B: {percent_b:.2%}')


if __name__ == '__main__':
    main()
