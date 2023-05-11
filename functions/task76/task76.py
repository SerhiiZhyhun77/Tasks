# -*- coding: utf-8 -*-

'''ЗАДАЧА: ПОБЕДИТЕЛИ МИРОВОЙ СЕРИИ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Дан файл WorldSeriesWinners.txt, он содержит хронологический список
команд-победителей Мировой серии по бейсболу с 1903 по 2009 год. (Первая
строка в файле является названием команды, которая победила в 1903 году,
последняя строка - названием команды, которая победила в 2009 году. Обратите
внимание, что Мировая серия не проводилась в 1904 и 1994 годах. В файле
имеются указывающие на это пометки.)

Напишите программу, которая читает этот файл и создает словарь, в котором
ключи - это годы, а связанные с ними значения - названия команд, которые
побеждали в том году.

Программа должна предложить пользователю ввести год в диапазоне между 1903 и
2009 годами и вывести название команды, которая выиграла Мировую серию в том
году и количество побед команды в Мировой серии.
'''


def main():
    # Read data from file
    winning_teams = read_file('WorldSeriesWinners.txt')
    # Get year from user
    year = inp()
    # Output
    winning_team = winning_teams.get(year)
    # World Series Played
    if winning_team.find('Not Played') < 0:
        print(f'Team winning the World Series in {year}: {winning_team}.')
        # Count wins
        counter = 0
        for team in winning_teams.values():
            if team == winning_team:
                counter += 1
        print(f'This team has won the World Series {counter} times.')
    # World Series Not Played
    else:
        print(winning_team)


def inp():
    while True:
        year = input('Enter a year between 1903 and 2009: ')
        if year.isnumeric():
            year = int(year)
            if 1903 <= year <= 2009:
                return year
        print('Please enter positive integer within the specified range.')


def read_file(file_name):
    winning_teams = {}
    year = 1903
    try:
        with open(file_name, 'r') as f:
            for team in f:
                winning_teams[year] = team.strip()
                year += 1
    except Exception as err:
        print(err)
    return winning_teams


if __name__ == '__main__':
    main()
