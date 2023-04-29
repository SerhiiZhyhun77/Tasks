# -*- coding: utf-8 -*-

'''ЗАДАЧА: ПРИНТЕР ДАТ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая считывает от пользователя строковое значение,
содержащее дату в формате дд/мм/гггг. Она должна напечатать дату в формате
12 марта 2018 г.
'''

def make_date(date):
    months = {
        '01' : 'january',
        '02' : 'february',
        '03' : 'march',
        '04' : 'april',
        '05' : 'may',
        '06' : 'june',
        '07' : 'july',
        '08' : 'august',
        '09' : 'september',
        '10' : 'october',
        '11' : 'november',
        '12' : 'december'
    }
    date_parts = date.split('/')
    return f'{date_parts[0]} {months[date_parts[1]]} {date_parts[2]} y.'


def main():
    date = input('Enter date in dd/mm/yyyy format: ')
    print(make_date(date))

if __name__ == '__main__':
    main()
