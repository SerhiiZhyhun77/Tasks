# -*- coding: utf-8 -*-

'''ЗАДАЧА: ДАННЫЕ О НАСЕЛЕНИИ
[Начинаем программировать на Python. Тони Гэддис (2022)]

У вас есть файл USPopulation.txt. В нем хранятся данные о среднегодовой
численности населения США в тысячах с 1950 по 1990 год. Первая строка в файле
содержит численность населения в 1950 году, вторая строка - численность
населения в 1951 году и т.д.

Напишите программу, которая считывает содержимое файла в список. Программа
должна показать приведенные ниже данные:
    - среднегодовое изменение численности населения в течение указанного
    периода времени;
    - год с наибольшим увеличением численности населения в течение указанного
    периода времени;
    - год с наименьшим увеличением численности населения в течение указанного
    периода времени.
'''

def analysis(population_lst):
    # initial values
    population_change = 0
    counter = 0
    year = 1951
    max_change = 0
    min_change = 1000000
    max_change_year = 0
    min_change_year = 0
    # determination of the average increase
    for i in range(len(population_lst) - 1):
        difference = population_lst[i + 1] - population_lst[i]
        population_change += difference
        counter += 1
        year += 1
        # reviewing max an min
        if difference > max_change:
            max_change = difference
            max_change_year = year
        if difference < min_change:
            min_change = difference
            min_change_year = year
    # average annual increase
    average_population_change = round(population_change / counter)
    # output
    print(f'Average annual population change: {average_population_change}')
    print(f'The largest increase in population was in {max_change_year} '
          f'- {max_change} people.')
    print(f'The smallest increase in population was in {min_change_year} '
          f'- {min_change} people.')

# read data from file to list
def get_data():
    population_lst = []
    try:
        f = open('USPopulation.txt', 'r')
        for population in f:
            population_lst.append(int(population))
    except Exception as err:
        print(err)
    return population_lst

def main():
    population_lst = get_data()
    analysis(population_lst)

if __name__ == '__main__':
    main()
