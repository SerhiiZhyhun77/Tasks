# -*- coding: utf-8 -*-

'''ЗАДАЧА: КЛАСС Car
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите класс под названием Car (Легковой автомобиль), который имеет
приведенные ниже атрибуты данных:
    - __year_model (для модели указанного года выпуска);
    - __make (для фирмы-изготовителя автомобиля);
    - __speed (для текущей скорости автомобиля).
Класс Car должен иметь метод __init__(), которыый в качестве аргументов
принимает модель указанного года выпуска и фирму-изготовителя. Эти значения
должны быть присвоены атрибутам данных __year_model и __make объекта. Он
также должен присвоить 0 атрибуту данных __speed.

Этот класс также должен иметь методы:
    - метод accelerate() (ускоряться) при каждом его вызове должен прибавлять 5
    в атрибут данных __speed;
    - метод break_() (тормозить) при каждом его вызове должен вычитать 5 из
    атрибута данных __speed;
    - метод get_speed() (получить скорость) должен возвращать текущую скорость.

Далее разработайте программу, которая создает объект Car и пятикратно
вызывает метод accelerate(). После каждого вызова метода accelerate() она
должна получать текущую скорость автомобиля и выводить ее на экран. Затем она
должна пятикратно вызвать метод break(). После каждого вызова метода break()
она должна получать текущую скорость автомобиля и выводить ее на экран.
'''


class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def break_(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return (f'Car {self.__make} {self.__year_model} created!')


def main():
    car = Car('Almera', 'Nissan')
    print(car)
    print()
    print('Acceleration!')
    print('Starting speed :', car.get_speed())
    for i in range(1, 6):
        car.accelerate()
        print(i, ': speed', car.get_speed())
    print()
    print('Braking!')
    print('Starting speed :', car.get_speed())
    for i in range(1, 6):
        car.break_()
        print(i, ': speed', car.get_speed())


if __name__ == '__main__':
    main()
