# -*- coding: utf-8 -*-

'''ЗАДАЧА: КЛАСС ПЕРСОНАЛЬНЫХ ДАННЫХ Information
[Начинаем программировать на Python. Тони Гэддис (2022)]

Разработайте класс, который содержит следующие персональные данные: имя,
адрес, возраст и телефонный номер. Напишите соответствующие методы-получатели и
методы-мутаторы. Кроме того, напишите программу, которая создает три
экземпляра класса. Один экземпляр должен содержать информацию о вас,
а два других - информацию о ваших друзьях или членах семьи.
'''


class Information:

    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        return f'Name: {self.get_name()}\n' \
               f'Address: {self.get_address()}\n' \
               f'Age: {self.get_age()}\n' \
               f'Phone number: {self.get_phone_number()}\n'


def main():
    person1 = Information('Serhii', 'Ezupil, Bandery, 22, Ukraine', '45',
                     '+(380)50-999-22-34')
    person2 = Information('Olha', 'Ezupil, Bandery, 22, Ukraine', '40',
                     '+(380)95-321-02-04')
    person3 = Information('Mykola', 'Ezupil, Bandery, 22, Ukraine', '17',
                     '+(380)95-100-45-21')
    # Output
    print(person1)
    print(person2)
    print(person3)


if __name__ == '__main__':
    main()
