# -*- coding: utf-8 -*-

'''ЗАДАЧА: ЦЕНЫ НА БЕНЗИН
[Начинаем программировать на Python. Тони Гэддис (2022)]

Вам дан файл GasPrices.txt. Этот файл содержит еженедельные средние цены за
галлон бензина в США, начиная 5 апреля 1993 года и заканчивая 26 августа 2013
года. Каждая строка в файле содержит среднюю цену за галлон бензина в
указанный день и отформатирована следующим образом:
    ММ-ДД-ГГГГ:Цена
где ММ - двузначный месяц; ДД - двузначный день; ГГГГ - четырехзначный год;
Цена - это средняя цена галлона бензина в указанный день.

В рамках этого задания необходимо написать одну или несколько программ,
которые считывают содержимое данного файла и выполняют приведенные ниже
вычисления.
    - Средняя цена на год: вычисляет среднюю цену бензина за год для каждого
    года в файле. (Данные файла начинаются апрелем 1993 года и заканчиваются
    августом 2013 года. Используйте данные, предоставленные за период с 1993
    по 2013 год.)
    - Средняя цена за месяц: вычисляет среднюю цену в каждом месяце в файле.
    - Наибольшая и наименьшая цены в году: в течение каждого года в файле
    определяет дату и величину самой низкой и самой высокой цены.
    - Список цен, упорядоченный по возрастанию: генерирует текстовый файл,
    в котором даты и цены отсортированы в возрастающем порядке.
    - Список цен, упорядоченный по уменьшению: генерирует текстовый файл,
    в котором даты и цены отсортированы в убывающем порядке.

Для выполнения всех этих вычислений можно написать одну программу или
несколько разных программ, по одной для каждого вычисления.
'''

from statistics import mean


def main():
    # Read data
    gas_prices = read_data()
    # Output
    # Average price for each year
    aver_price_each_year = average_price_each_year(gas_prices)
    print('Average price for each year:')
    for year, price in aver_price_each_year:
        print(f'{year} -> {price:.3f}')
    print()
    # Average price for each month
    aver_price_each_month = average_price_each_month(gas_prices)
    print('Average price for each month:')
    for month, year, price in aver_price_each_month:
        print(f'{month:02}-{year} -> {price:.3f}')
    print()
    # Max/min price
    max_min_price = max_min_price_each_year(gas_prices)
    print('Max/min price for each year:')
    year = max_min_price[0][0]
    print(year, ':')
    for p in max_min_price:
        if year != p[0]:
            year = p[0]
            print(year, ':')
        print(*p[1:])
    print()
    # Sorted ascending and write to a file
    sort_in_ascending_order(gas_prices)
    print()
    # Sorted descending and write to a file
    sort_in_descending_order(gas_prices)
    print()


def sort_in_descending_order(gas_prices):
    print('Sort the price of gas in descending order...')
    gas_prices.sort(key=lambda x: x[3], reverse=True)
    print('Writing to the file "gas_prices_sorted_descending.txt"...')
    try:
        with open('gas_prices_sorted_descending.txt', 'w') as f:
            for p in gas_prices:
                line = f'{p[0]:02}-{p[1]:02}-{p[2]}:{p[3]}\n'
                f.write(line)
        print('Done!')
    except Exception as err:
        print(err)


def sort_in_ascending_order(gas_prices):
    print('Sort the price of gas in ascending order...')
    gas_prices.sort(key=lambda x: x[3])
    print('Writing to the file "gas_prices_sorted_ascending.txt"...')
    try:
        with open('gas_prices_sorted_ascending.txt', 'w') as f:
            for p in gas_prices:
                line = f'{p[0]:02}-{p[1]:02}-{p[2]}:{p[3]}\n'
                f.write(line)
        print('Done!')
    except Exception as err:
        print(err)


def max_min_price_each_year(gas_prices):
    def format_entry(entry):
        return entry[3], f'{entry[0]:02}-{entry[1]:02}-{entry[2]}'

    max_min_price = []
    gas_prices.sort(key=lambda x: x[2])
    min_price = max_price = format_entry(gas_prices[0])
    year = gas_prices[0][2]
    for p in gas_prices:
        if year == p[2]:
            if p[3] > max_price[0]:
                max_price = format_entry(p)
            if p[3] < min_price[0]:
                min_price = format_entry(p)
        else:
            max_min_price.append([year, 'max'] + list(max_price))
            max_min_price.append([year, 'min'] + list(min_price))
            min_price = max_price = format_entry(p)
            year = p[2]
    max_min_price.append([year, 'max'] + list(max_price))
    max_min_price.append([year, 'min'] + list(min_price))
    return max_min_price


def average_price_each_month(gas_prices):
    average_price_months = []
    price_month = []
    gas_prices.sort(key=lambda x: (x[2], x[0]))
    year = 0
    month = 0
    for p in gas_prices:
        if month == 0:
            month = p[0]
            year = p[2]
        if month == p[0]:
            price_month.append(p[3])
        else:
            average_price_months.append((month, year, mean(price_month)))
            month = p[0]
            year = p[2]
            price_month.clear()
    average_price_months.append((month, year, mean(price_month)))
    return average_price_months


def average_price_each_year(gas_prices):
    average_price_years = []
    price_year = []
    gas_prices.sort(key=lambda x: x[2])
    year = 0
    for p in gas_prices:
        if year == 0:
            year = p[2]
        if year == p[2]:
            price_year.append(p[3])
        else:
            average_price_years.append((year, mean(price_year)))
            year = p[2]
            price_year.clear()
    average_price_years.append((year, mean(price_year)))
    return average_price_years


def read_data():
    file_name = 'GasPrices.txt'
    gas_prices = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                date_price = line.strip().split(':')
                date = date_price[0].split('-')
                date = list(map(int, date))
                price = float(date_price[1])
                date.append(price)
                gas_prices.append(date)
    except Exception as err:
        print(err)
    return gas_prices


if __name__ == '__main__':
    main()
