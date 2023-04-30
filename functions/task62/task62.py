# -*- coding: utf-8 -*-

'''ЗАДАЧА: СРЕДНЕЕ КОЛИЧЕСТВО СЛОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

В текущей директории у вас есть файл text.txt. В нем в каждой строке хранится
одно предложение. Напишите программу, которая читает содержимое файла и
вычисляет среднее количество слов в расчете на предложение.
'''

from statistics import mean

def main():
    file_name = 'text.txt'
    print(f'Reading the file "{file_name}"...')
    try:
        with open(file_name, 'r') as f:
            word_count = []
            print('Counting...')
            for line in f:
                word_count.append(len(line.split()))
            print('Result:')
            print('Average number of words per line:', mean(word_count))
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
