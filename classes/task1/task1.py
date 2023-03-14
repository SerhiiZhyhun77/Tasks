# -*- coding:utf-8 -*-

"""Напишите класс Rectangle, представляющий прямоугольник. Экземпляры класса 
должны создаваться с двумя атрибутами: .length и .width. Добавьте в класс 
метод .area(), который возвращает площадь прямоугольника (length * width).

Затем напишите класс Square, представляющий квадрат. Этот класс должен 
наследовать от класса Rectangle и создаваться с одним атрибутом .side_length. 
Протестируйте класс Square: создайте экземпляр Square с атрибутом .side_length 
равным 4. Вызов .area() должен возвращать 16.
Задайте свойству .width вашего экземпляра SSquare значение 5. Затем снова 
вызовите .area(). Метод должен вернуть значение 20."""


class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


def main():
    print('*' * 30)
    print('Create a square with side length = 4')
    square = Square(4)
    print(f'Area = {square.area()}')
    print('Change: width = 5')
    square.width = 5
    print(f'Area = {square.area()}')
    print('*' *30)


if __name__ == '__main__':
    main()
