# -*- coding: utf-8 -*-

'''ЗАДАЧА: ПОИСК ИМЕН
[Начинаем программировать на Python. Тони Гэддис (2022)]

У вас есть приведенные ниже файлы:
    - GirlNames.txt - файл со списком 200 самых популярных имен, данных
    девочкам, родившимся в США между 2000 и 2009 годами;
    - BoyNames.txt - файл со списком 200 самых популярных имен, данных
    мальчикам, родившимся в США между 2000 и 2009 годами.

Напишите программу, которая считывает содержимое этих двух файлов в два
отдельных списка. Пользователь должен иметь возможность ввести имя мальчика,
имя девочки или оба имени, и приложение должно вывести сообщения о том,
что введенные имена находятся среди самых популярных имен.
'''

# read names from file to list
def get_names_lst(file_name):
    name_lst = []
    try:
        f = open(file_name, 'r')
        for name in f:
            name_lst.append(name.strip())
    except Exception as err:
        print(err)
    return name_lst

def main():
    # get names
    girl_names_lst = get_names_lst('GirlNames.txt')
    boy_names_lst = get_names_lst('BoyNames.txt')
    
    # get names from user
    print('You can check the popularity of the name.')
    print('Enter the name of a boy, a girl, or both separated by spaces.')
    s = input(': ')
    names = s.split()
    if not names:
        print('You didn\'t enter any name.')

    # check names for popularity
    print()
    for name in names:
        if name in girl_names_lst:
            print(f'The girl\'s name {name} is popular.')
        elif name in boy_names_lst:
            print(f'Boy\'s name {name} is popular.')
        else:
            print(f'Name {name} is not popular.')

if __name__ == '__main__':
    main()
