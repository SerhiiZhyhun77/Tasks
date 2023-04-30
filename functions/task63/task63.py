# -*- coding: utf-8 -*-

'''ЗАДАЧА: АНАЛИЗ СИМВОЛОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Дан файл text.txt. Напишите программу, которая читает содержимое файла и
определяет:
    - количество букв в файле в верхнем регистре;
    - количество букв в файле в нижнем регистре;
    - количество цифр в файле;
    - количество пробельных символов в файле.
'''

def main():
    file_name = 'text.txt'
    # Initial statistics
    stat_dict = {
        'upper' : 0,
        'lower' : 0,
        'digit' : 0,
        'space' : 0
    }
    text = ''
    # Read file
    print(f'Reading file "{file_name}"...')
    try:
        with open(file_name, 'r') as f:
            text = f.read().replace('\n', '')
    except Exception as err:
        print(err)
    # Counting statistics
    print('Counting...')
    for s in text:
        if s.isupper():
            stat_dict['upper'] += 1
        elif s.islower():
            stat_dict['lower'] += 1
        elif s.isdigit():
            stat_dict['digit'] += 1
        elif s.isspace():
            stat_dict['space'] += 1
    # Output
    print('In this text:')
    print('- number of uppercase letters:', stat_dict['upper'])
    print('- number of lowercase letters:', stat_dict['lower'])
    print('- number of digits:', stat_dict['digit'])
    print('- number of whitespace characters:', stat_dict['space'])

if __name__ == '__main__':
    main()
