# -*- coding: utf-8 -*-

'''ЗАДАЧА: ГРАФИК ЕЖЕНЕДЕЛЬНЫХ ЦЕН НА БЕНЗИН ЗА 1994 ГОД
[Начинаем программировать на Python. Тони Гэддис (2022)]

Вам дан файл 1994_Weekly_Gas_Averages.txt, он содержит среднюю цену бензина в
течение каждой недели 1994 года. (В файле 52 строки.) Используя пакет
matplotlib, напишите программу, которая считывает содержимое файла и затем
строит линейный график. Не забудьте показать содержательные метки вдоль осей
х и у, а также метки делений.
'''

import matplotlib.pyplot as plt

# read data from file to list
def get_data():
    price_lst = []
    try:
        f = open('1994_Weekly_Gas_Averages.txt', 'r')
        for price in f:
            price_lst.append(float(price.strip()))
    except Exception as err:
        print(err)
    else:
        f.close()
    return price_lst

def main():
    # read data
    price_lst = get_data()
    # create chart
    plt.plot(list(range(1,53)), price_lst)
    # add title
    plt.title('CHART OF WEEKLY PETROL PRICES FOR 1994')
    # sign the coordinate axes
    plt.xlabel('Weeks')
    plt.ylabel('Gasoline price')
    # set a limit
    plt.xlim(xmin=1, xmax=52)
    # show grid
    plt.grid(True)
    # show chart
    plt.show()

if __name__ == '__main__':
    main()
