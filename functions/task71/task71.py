# -*- coding: utf-8 -*-

'''ЗАДАЧА: ВИКТОРИНА СО СТОЛИЦАМИ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая создает словарь, содержащий в качестве ключей
названия американских штатов и в качестве значений - из столицы. (Список
штатов и столиц можно найти в Интернете.) Затем программа должна провести
викторину, случайным образом выводя название штата и предлагая ввести его
столицу. Программа должна провести подсчет количества правильных и
неправильных ответов.
'''

import random


def main():
    states_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }
    correct = 0
    incorrect = 0
    print('*' * 30)
    print('State capitals quiz')
    print('*' * 30)
    while True:
        rand_state = random.choice(list(states_capitals.keys()))
        rand_capital = states_capitals.get(rand_state)
        capital = input(f'Enter the state capital of {rand_state} ("q" to '
                        'finish): ')
        if capital.lower().strip() == 'q':
            exit()
        if capital.lower().strip() == rand_capital.lower():
            correct += 1
            print('Answer is correct!')
        else:
            incorrect += 1
            print('The answer is wrong!')
            print(f'The state capital of {rand_state} is {rand_capital}.')
        print()
        print('Correct answers:', correct)
        print('Incorrect answers:', incorrect)
        print()


if __name__ == '__main__':
    main()
