# -*- coding: utf-8 -*-

'''ЗАДАЧА: КРУГОВАЯ ДИАГРАММА РАСХОДОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Создайте текстовый файл costs.txt, который содержит ваши расходы за прошлый
месяц по приведенным ниже статьям:
    - арендная плата;
    - бензин;
    - продукты питания;
    - одежда;
    - платежи по автомашине;
    - прочие.

Напишите программу, которая считывает данные из файла и использует пакет
matplotlib для построения круговой диаграммы, показывающей, как вы тратите
свои деньги.
'''

import matplotlib.pyplot as plt

# read data from file
def get_data():
    expense_items = []
    costs = []
    try:
        f = open('costs.txt','r')
        for line in f:
            expense, cost = line.strip().split(':')
            expense_items.append(expense)
            costs.append(cost)
    except Exception as err:
        print(err)
    else:
        f.close()
    return expense_items, costs

def main():
    # get data from file
    expense_items, costs = get_data()
    # create pie diagram
    plt.pie(costs, labels=expense_items)
    # add title
    plt.title('PIE DIAGRAM OF EXPENSES')
    # show diagram
    plt.show()

if __name__ == '__main__':
    main()
