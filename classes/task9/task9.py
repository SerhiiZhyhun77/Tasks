# -*- coding: utf-8 -*-

'''ЗАДАЧА: КЛАССЫ Employee и ProductionWorker
[Начинаем программировать на Python. Тони Гэддис (2022)]
Напишите класс Employee (Сотрудник), который содержит атрибуты приведенных ниже
данных:
    - имя сотрудника;
    - номер сотрудника.
Затем напишите класс ProductionWorker (Рабочий), который является подклассом
класса Employee. Класс ProductionWorker должен содержать атрибуты приведенных
ниже данных:
    - номер смены(целое число, к примеру, 1 или 2);
    - ставка почасовой оплаты труда.
Рабочий день разделен на две смены: дневную и вечернюю. Атрибут смены будет
содержать целочисленное значение, представляющее смену, в которую сотрудник
работает. Дневная смена является сменой 1, вечерняя смена - сменой 2.
Напишите соответствующие методы-получатели и методы мутаторы для каждого класса.

Затем напишите программу, которая создает объект класса ProductionWorker и
предлагает пользователю ввестиданные по каждому атрибуту данных этого
объекта. Сохраните данные в объекте и примените в этом объекте
методы-получатели, чтобы получить эти данные и вывести их на экран.
'''


class Employee:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class ProductionWorker(Employee):

    def __init__(self, name, id, shift_number, hourly_rate):
        super().__init__(name, id)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_rate(self):
        return self.__hourly_rate


def main():
    # Get data
    print('Enter data for production worker')
    name = input('Name: ')
    id = input('ID: ')
    shift_number = input('Shift number (1 - day shift or 2 - evening shift): ')
    hourly_rate = input('Hourly rate: ')
    # Create instance
    worker = ProductionWorker(name, id, shift_number, hourly_rate)
    # Output data
    print()
    print('Name:', worker.get_name())
    print('ID:', worker.get_id())
    print('Shift number:', worker.get_shift_number())
    print('Hourly rate:', worker.get_hourly_rate())


if __name__ == '__main__':
    main()
