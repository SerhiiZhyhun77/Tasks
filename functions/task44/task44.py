# -*- coding: utf-8 -*-

'''ЗАДАЧА: СРЕДНЕЕ КОЛИЧЕСТВО ШАГОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Браслет для занятий спортом - это носимое устройство, которое отслеживает
вашу физическую активность, количество сожженных калорий, сердечный ритм,
модели сна и т.д. Одним из самых распространенных видов физической
активности, который отслеживает большинство таких устройств, является
количество шагов, которые вы делаете каждый день.

Среди исходного кода вы найдете файл steps.txt. Этот файл содержит количество
шагов, которые человек делал каждый день в течение года. В файле 365 строк,
и каждая строка содержит количество шагов, сделанных в течении дня. (Первая
строка - это число шагов, сделанных 1 января, вторая строка - число шагов,
сделанных 2 января, и т.д.)
Напишите программу, которая читает файл и затем выводит среднее количество
шагов, сделанных в течение каждого месяца. (Данные были записаны в год,
который не был высокосным, и поэтому февраль имеет 28 дней.)
'''

import datetime
import statistics

def main():
    year = 2001
    month = 1
    # make start date
    date = datetime.date(year, month, 1)
    date_before = date
    #make stepday
    one_day = datetime.timedelta(days=1)
    # list for steps pet month
    steps_per_month_lst = []

    try:
        f = open('steps.txt', 'r')
        print('Average steps taken:')
        for steps in f:
            steps_per_month_lst.append(int(steps.strip()))
            date += one_day
            # if next month
            if date.month != month:
                print(f'{date_before.strftime("%B")}'.ljust(10),
                      f'{statistics.mean(steps_per_month_lst):.0f}')
                date_before = date
                steps_per_month_lst.clear()
                month = date.month
    except Exception as err:
        print(err)
    else:
        f.close()

if __name__ == '__main__':
    main()
