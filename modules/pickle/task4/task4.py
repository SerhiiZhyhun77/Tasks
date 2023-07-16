# -*- coding: utf-8 -*-

'''ЗАДАЧА: СИСТЕМА УПРАВЛЕНИЯ ПЕРСОНАЛОМ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите класс под названием Employee, который в атрибутах содержит данные о
сотруднике: имя, идентификационный номер, отдел и должность.
Создайте программу, которая сохраняет объекты Employee в словаре. Используйте
идентификационный номер сотрудника в качестве ключа. Программа должна вывести
меню, которое позволяет пользователю:
    - найти сотрудника в словаре;
    - добавить нового сотрудника в словарь;
    - изменить имя, отдел и должность существующего сотрудника в словаре;
    - удалить сотрудника из словаря;
    - выйти из программы.
По завершению работы программа должна законсервировать словарь и сохранить
его в файле. При каждом запуске программы она должна попытаться загрузить
законсервированный словарь из файла. Если файл не существует, то программа
должна начать работу с пустого словаря.
'''

import pickle


class Employee:

    def __init__(self, name, id, department, position):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__position = position

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_position(self, position):
        self.__position = position

    def get_employee(self):
        return f'Name: {self.__name}\n' \
               f'Department: {self.__department}\n' \
               f'Position: {self.__position}\n'


def main():
    while True:
        n = menu()
        actions(n)


def actions(n):
    if n == 1:
        find_employee()
    elif n == 2:
        add_employee()
    elif n == 3:
        change_employee()
    elif n == 4:
        remove_employee()
    elif n == 5:
        exit()


def save():
    try:
        with open(file_name, 'wb') as f:
            pickle.dump(employee_dict, f)
            print()
            print('Data updated')
    except Exception as err:
        print(err)


def remove_employee():
    print('Removing employee:')
    id = input('Enter employee ID to remove: ')
    print()
    if employee_dict.pop(id, None) is None:
        print('Employee with this ID was not found')
    else:
        save()


def change_employee():
    print('Changing the name, department and position '
          'of an existing employee:')
    id = input('Enter employee ID for change: ')
    print()
    employee = employee_dict.get(id, None)
    if employee is None:
        print('Employee with this ID was not found')
    else:
        print('Enter new data:')
        name = input('Name: ')
        department = input('Department: ')
        position = input('Position: ')
        employee.set_name(name)
        employee.set_department(department)
        employee.set_position(position)
        save()


def find_employee():
    print('Find employee by ID:')
    id = input('Enter employee ID: ')
    print()
    employee = employee_dict.get(id, None)
    if employee is None:
        print('Employee with this ID was not found')
    else:
        print(employee.get_employee())
    print()


def add_employee():
    print('Adding an employee:')
    name = input('Name: ')
    id = input('ID: ')
    department = input('Department: ')
    position = input('Position: ')
    new_employee = Employee(name, id, department, position)
    employee_dict[id] = new_employee
    save()


def menu():
    while True:
        print('-' * 30)
        print('M E N U'.center(30))
        print('-' * 30)
        print('1.Find an employee')
        print('2.Add new employee')
        print('3.Change the name, department and position '
              'of an existing employee')
        print('4.Remove employee')
        print('5.Exit')
        print('-' * 30)
        n = input('Enter your choice: ')
        print()
        if n.isdigit():
            n = int(n)
            if 1 <= n <= 5:
                return n
        print('Your choice is wrong!\n')


if __name__ == '__main__':
    file_name = 'employee.dat'
    try:
        with open(file_name, 'rb') as f:
            employee_dict = pickle.load(f)
            print('Data loaded')
    except Exception:
        employee_dict = {}
    main()
