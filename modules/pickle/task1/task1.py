# -*- coding: utf-8 -*-

'''ЗАДАЧА: ИМЕНА И АДРЕСА ЭЛЕКТРОННОЙ ПОЧТЫ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая сохраняет имена и адреса электронной почты в
словаре в виде пар "ключ : значение". Программа должна вывести меню, которое
позволяет пользователю отыскать адрес электронной почты человека, добавить
новое имя и адрес электронной почты, изменить существующий адрес электронной
почты и удалить существующие имя и адрес электронной почты. Программа должна
законсервировать словарь и сохранить его в файле при выходе пользователя из
программы. При каждом запуске программы она должна извлекать словарь из файла и
расконсервировать его.
'''

import pickle

catalog = {}


def main():
    while True:
        user_choice = menu()
        actions(user_choice)


def search_():
    print('You choosed: SEARCH')
    name = input('Enter name: ')
    # Output
    print()
    print('Name:', name)
    print('email:', catalog.get(name, 'no data for this person'))


def add_():
    print('You choosed: ADD')
    name = input('Enter new name: ')
    if name not in catalog:
        email = input(f'Enter email for {name}: ')
        catalog[name] = email
        print('\nEntry added successfully!')
    else:
        print('\nThis name already exists!')


def change_():
    print('You choosed: CHANGE')
    name = input('Enter name: ')
    if name in catalog:
        new_email = input('Enter new email: ')
        catalog[name] = new_email
        print('\nChanged successfully!')
    else:
        print('\nWrong name!')


def del_():
    print('You choosed: DELETE')
    name = input('Enter name for delete: ')
    if name in catalog:
        del catalog[name]
        print('\nSuccessfully removed!')
    else:
        print('\nWrong name!')


def exit_():
    try:
        with open('catalog.dat', 'wb') as f:
            pickle.dump(catalog, f)
    except Exception as err:
        print(err)
    exit()


def actions(user_choice):
    print()
    # Search
    if user_choice == 1:
        search_()
    # Add new name and email
    elif user_choice == 2:
        add_()
    # Change email
    elif user_choice == 3:
        change_()
    # Delete name and email
    elif user_choice == 4:
        del_()
    # Exit
    elif user_choice == 5:
        exit_()


def menu():
    while True:
        print('-' * 30)
        print(('M EN U ').center(30))
        print('-' * 30)
        print('1.Search')
        print('2.Add a new name and email')
        print('3.Change email')
        print('4.Delete name and email')
        print('5.Exit')
        print('-' * 30)
        user_choice = input('Make your choice: ')
        if user_choice.isnumeric():
            user_choice = int(user_choice)
            if 1 <= user_choice <= 5:
                return user_choice
        print('Incorrect choice.')


if __name__ == '__main__':
    # Read catalog
    try:
        with open('catalog.dat', 'rb') as f:
            catalog = pickle.load(f)
    except FileNotFoundError:
        print('Catalog is empty.')
    main()
