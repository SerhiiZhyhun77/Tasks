# -*- coding: utf-8 -*-

'''ЗАДАЧА: ЛОТЕРЕЯ POWERBALL
[Начинаем программировать на Python. Тони Гэддис (2022)]

Для того чтобы сыграть в лотерею PowerBall, покупают билет, в котором имеется
пять чисел от 1 до 69 и число PowerBall в диапазоне от 1 до 26. (Эти числа
можно выбрать самому либо дать билетному автомату их выбрать за вас случайным
образом.) Затем в заданный день автомат случайным образом отбирает выигрышный
ряд чисел. Если первые пять чисел совпадают с первыми пятью выигрышными
числами в любом порядке и ваше число PowerBall соответствует выигрышному
числу PowerBall, то вы выигрываете джек-пот, который составляет очень крупную
сумму денег. Если ваши числа совпадают лишь с некоторыми выигрышными числами, то
вы выигрываете меньшую сумму в зависимости от того, сколько выигрышных
номеров совпало.

В текущей директории у вас есть файл pbnumbers.txt, содержащий выигрышные
номера PowerBall, которые были отобраны между 3 февраля 2010 года и 11 мая
2016 года (файл содержит 654 набора выигрышных чисел). Каждая строка в файле
содержит набор из шести чисел, которые были выбраны в заданную дату. Числа
разделены пробелом, и последнее число в каждой строке является числом
PowerBall для этого дня. Например, первая строка в файле показывает числа за
3 февраля 2010 года, которые равнялись 17, 22, 36, 37, 52, и число PowerBall,
равное 24.

Напишите одну или несколько программ, которые работают с этим файлом и
показывают:
    - 10 наиболее распространенных чисел, упорядоченных по частоте;
    - 10 наименее распространенных чисел, упорядоченных по частоте;
    - частоту каждого числа от 1 до 69 и частоту каждого PowerBall-числа от
    1 до 26.
'''


def sort_stat(stat, cut=0, reverse=True):
    # Make sorted list from dictionary
    stat_lst_sorted = sorted(stat.items(), key=lambda x: x[1], reverse=reverse)
    # If cut not 0 - shorten the list
    if cut:
        cut_lst = []
        for i in range(cut):
            cut_lst.append(stat_lst_sorted.pop(0))
        stat_lst_sorted = cut_lst
    # Make dict from lst and return
    return dict(stat_lst_sorted)


def analisis(data):
    # Preparation of dictionaries for statistics
    stat_num = {str(n) if n > 9 else '0' + str(n): 0 for n in range(1, 70)}
    stat_pb = {str(n) if n > 9 else '0' + str(n): 0 for n in range(1, 27)}
    # Convert strings to lists of numbers
    for line in data:
        line = line.strip()
        num_lst = line.split()
        # Count the numbers and PowerBalls
        for i, num in enumerate(num_lst, 1):
            if i == 6:  # PowerBall
                stat_pb[num] += 1
            else:
                stat_num[num] += 1
    return stat_num, stat_pb


# Read data from file
def get_data():
    data = []
    try:
        with open('pbnumbers.txt', 'r') as f:
            data = f.readlines()
    except Exception as err:
        print(err)
    return data


def main():
    # Get data from file
    data = get_data()
    if data:
        stat_num, stat_pb = analisis(data)
        # Output
        print('The 10 most common numbers, sorted by frequency: ')
        print(*sort_stat(stat_num, 10, True).keys())
        print()
        print('The 10 most common numbers PowerBall, sorted by frequency: ')
        print(*sort_stat(stat_pb, 10, True).keys())
        print()
        print('The 10 least common numbers, sorted by frequency:')
        print(*sort_stat(stat_num, 10, False).keys())
        print()
        print('The 10 least common numbers PowerBall, sorted by frequency:')
        print(*sort_stat(stat_pb, 10, False).keys())
        print()
        print('Number frequency:')
        print('Num: Freq')
        for num, freq in stat_num.items():
            print(num, ':', freq)
        print()
        print('PowerBall frequency:')
        print('Num: Freq')
        for num, freq in stat_pb.items():
            print(num, ':', freq)


if __name__ == '__main__':
    main()
