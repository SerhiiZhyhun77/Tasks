# -*- coding: utf-8 -*-

'''ЗАДАЧА: Класс Pet
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите класс Pet (Домашнее животное), который должен иметь приведенные ниже
атрибуты данных:
    - _name (для клички домашнего животного);
    - _animal_type (для типа домашнего животного, например, это может быть
    "собака", "кот" и "птица");
    - _age (для возраста домашнего животного).

Класс Pet должен иметь метод __init__(), который создает эти атрибуты. Он
также должен иметь приведенные ниже методы:
    - метод set_name() присваивает значение полю _name;
    - метод set_animal_type() присваивает значение полю _animal_type;
    - метод set_age() присваивает значение полю _age;
    - метод get_name() возвращает значение поля _name;
    - метод get_animal_type() возвращает значение поля _animal_type;
    - метод get_age() возвращает значение поля _age.

После написания данного класса напишите программу, которая создает объект
класса и предлагает пользователю ввести кличку, тип и возраст своего
домашнего животного. Эти данные должны храниться в качестве атрибутов
объекта. Примените методы-получатели, чтобы извлечь имя, тип и возраст
домашнего животного и показать эти данные на экране.
'''


class Pet:

    def __init__(self):
        self._name = ''
        self._animal_type = ''
        self._age = 0

    def set_name(self, name):
        self._name = name

    def set_animal_type(self, animal_type):
        self._animal_type = animal_type

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age


def main():
    u_pet = Pet()
    # Get data from user
    name = input('Enter the name of your pet: ')
    animal_type = input('Enter the type of your pet: ')
    age = int(input('Enter the age of your animal: '))
    # Set data to instance of pet
    u_pet.set_name(name)
    u_pet.set_animal_type(animal_type)
    u_pet.set_age(age)
    # Output
    print()
    print('Your pet\'s name is', u_pet.get_name())
    print('It\'s a', u_pet.get_animal_type())
    print(f'It is {u_pet.get_age()} years old')


if __name__ == '__main__':
    main()
