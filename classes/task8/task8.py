# -*- coding: utf-8 -*-

'''ЗАДАЧА: РАСХОДЫ НА ЛЕЧЕНИЕ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите класс под название Patient (Пациент), который имеет атрибуты для
приведенных ниже данных:
    - имя, отчество и фамилия;
    - адрес, город, область и почтовый индекс;
    - телефонный номер;
    - имя и телефон контактного лица для экстренной связи.

Метод __init__() класса Patient должен принимать аргумент для каждого
атрибута. Класс Patient также должен для каждого атрибута иметь
методы-мутаторы.

Затем напишите класс Procedure, который представляет пройденную пациентом
медицинскую процедура. Класс Procedure должен иметь атрибуты для приведенных
ниже данных:
    - название процедуры;
    - дата процедуры;
    - имя врача, который выполнял процедуру;
    - стоимость процедуры.

Метод __init__() класса Procedure должен принимать аргумент для каждого
атрибута. Класс Procedure также должен для каждого атрибута иметь
методы-получатели и методы-мутаторы. Далее напишите программу, которая
создает экземпляр класса Patient, инициализированного демонстрационными
данными. Затем создайте три экземпляра класса Procedure, инициализированного
приведенными данными.
Программа должна вывести на экран информацию о пациенте, сведения обо всех
трех процедурах и об общей стоимости всех трех процедур.

Процедура №1            Процедура №2            Процедура №3

Название процедуры:     Название процедуры:     Название процедуры:
врачебный осмотр        рентгенография          анализ крови

Дата: сегодняшняя       Дата: сегодняшняя       Дата: сегодняшняя

Врач: Ирвин             Врач: Джеминсон         Врач: Смит

Стоимость: 250.00       Стоимость: 500.00       Стоимость: 200.00
'''

import datetime


class Patient:

    def __init__(self, name, patronymic, surname, address, city, region,
                 postcode, phone_number, contact_person_name,
                 contact_person_phone_number):
        self.__name = name
        self.__patronymic = patronymic
        self.__surname = surname
        self.__address = address
        self.__city = city
        self.__region = region
        self.__postcode = postcode
        self.__phone_number = phone_number
        self.__contact_person_name = contact_person_name
        self.__contact_person_phone_number = contact_person_phone_number

    def __str__(self):
        return f'Patient: ' \
               f'{self.__name} {self.__patronymic} {self.__surname}\n' \
               f'Address: ' \
               f'{self.__address}, {self.__city}, {self.__region}, ' \
               f'{self.__postcode}\n' \
               f'Phone: ' \
               f'{self.__phone_number}\n' \
               f'Contact person:\n' \
               f'{self.__contact_person_name}\n' \
               f'{self.__contact_person_phone_number}\n'

    def set_name(self, name):
        self.__name = name

    def set_patronymic(self, patronymic):
        self.__patronymic = patronymic

    def set_surname(self, surname):
        self.__surname = surname

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_region(self, region):
        self.__region = region

    def set_postcode(self, postcode):
        self.__postcode = postcode

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_contact_person_name(self, contact_person_name):
        self.__contact_person_name = contact_person_name

    def set_contact_person_phone_number(self, contact_person_phone_number):
        self.__contact_person_phone_number = contact_person_phone_number


class Procedure:

    def __init__(self, procedure_name, date, doctor, cost):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__doctor = doctor
        self.__cost = cost

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_date(self, date):
        self.__date = date

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def set_cost(self, cost):
        self.__cost = cost

    def get_procedure_name(self):
        return self.__procedure_name

    def get_date(self):
        return self.__date

    def get_doctor(self):
        return self.__doctor

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return f'Procedure: {self.__procedure_name}\n' \
               f'Date: {self.__date}\n' \
               f'Doctor: {self.__doctor}\n' \
               f'Cost: {self.__cost}\n'


def main():
    patient = Patient('Oleh', 'Volodymyrovich', 'Sahno', 'Kvitkova, 12',
                      'Hornostaivka', 'Khersonska', '74601',
                      '+38(050)543-32-21', 'Yana Valensia', '+38(095)456-11-22')
    procedure1 = Procedure('Medical checkup', datetime.date.today(), 'Irvin',
                           250)
    procedure2 = Procedure('Radiography', datetime.date.today(), 'Jeminson',
                           500)
    procedure3 = Procedure('Blood analysis', datetime.date.today(), 'Smit', 200)
    # Output
    print(patient)
    print(procedure1)
    print(procedure2)
    print(procedure3)
    print('Total cost:', procedure1.get_cost() + procedure2.get_cost() +
          procedure3.get_cost())


if __name__ == '__main__':
    main()
