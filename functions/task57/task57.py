# -*- coding: utf-8 -*-

'''ЗАДАЧА: ИНИЦИАЛЫ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая получает строковое значение, содержащее имя,
отчество и фамилию человека и показывает инициалы. Например,
если пользователь вводит Михаил Иванович Кузнецов, то программа должна
вывести М.И.К.
'''

def make_initials(full_name):
    names = full_name.split()
    initials = ''
    for name in names:
        initials += name[0].upper() + '.'
    return initials

def main():
    full_name = input('Enter your first name and last name: ')
    initials = make_initials(full_name)
    print('Your initials:', initials)

if __name__ == '__main__':
    main()
