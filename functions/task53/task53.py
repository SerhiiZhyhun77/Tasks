# -*- coding: utf-8 -*-

'''ЗАДАЧА: ЧЕМПИОНЫ МИРОВОЙ СЕРИИ
[Начинаем программировать на Python. Тони Гэддис (2022)]

У вас есть файл WorldSeriesWinners.txt. Он содержит хронологический список
команд-победителей Мировой серии по бейсболу с 1903 по 2009 год. (Первая
строка в файле является названием команды, которая победила в 1903 году,
а последняя строка - названием команды, которая победила в 2009 году.
Обратите внимание, что Мировая серия не проводилась в 1904 и 1994 годах.)

Напишите программу, которая позволяет пользователю ввести название команды и
затем выводит количество лет, когда команда побеждала в Мировой серии в
течение указанного периода времени с 1903 по 2009 год.
'''

# read data from file to list
def get_teams():
    teams_lst = []
    try:
        f = open('WorldSeriesWinners.txt', 'r')
        for name in f:
            teams_lst.append(name.strip().lower())
    except Exception as err:
        print(err)
    else:
        f.close()
    return teams_lst

def main():
    # get teams from file
    teams_lst = get_teams()
    # get team from user
    team = input('Enter baseball team name: ')
    # output
    print()
    print(f'The {team} won the World Series in during \nthe specified time '
          f'period'
          f' from 1903 to 2009 {teams_lst.count(team.lower())} times.')

if __name__ == '__main__':
    main()
