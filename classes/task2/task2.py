# -*- coding: utf-8 -*-

"""ЗАДАЧА: МОДЕЛЬ ФЕРМЫ
В этой задаче вы создадите упрощенную модель фермы.Не упускайте из виду, что 
правильных ответов может быть несколько.

Требования задачи открыты для интерпретации,но постарайтесь придерживаться 
следующих рекомендаций:
    1. В программе должно быть по крайней мере четыре класса: родительский 
    класс Animal и не менее трех производных классов животных, наследующих 
    от Animal.
    2. Каждый класс должен содержать несколько атрибутов и по крайней мере 
    один метод, моделирующий поведение, присущее конкретному животному или 
    всем животным, - они должны ходить, бегать, есть, спать и т.д.
    3. Не усложняйте. Используйте наследование. Предусмотрите возможность 
    вывода подробной информации о животных и их поведении. """


class Animal:

    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type

    def __str__(self):
        return f'{self.animal_type} {self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.animal_type} {self.name} says {sound}'


class Cow(Animal):
    coat_color = 'brown'
    tail_length = '50 cm'

    def speak(self, sound = 'Moooo!'):
        return super().speak(sound)
    
    def eat_grass(self):
        return f'{self.animal_type} {self.name} eats  grass. Hrum-hrum...'


class Pig(Animal):
    skin_color = 'black'
    tail_length = '20 cm'

    def speak(self, sound = 'Oink!'):
        return super().speak(sound)

    def digs_ground(self):
        return f'{self.animal_type} {self.name} digs the ground. Hrrrrr!...'


class Chicken(Animal):
    color = 'yellow'
    number_of_legs = 2

    def speak(self, sound = 'Co-co-co!'):
        return super().speak(sound)

    def pecks_grain(self):
        return f'{self.animal_type} {self.name} pecks grain...'


def main():
    print('*' * 30)
    print('Create a cow.')
    cow = Cow('Flower', 4, 'Cow')
    print(cow)
    print(f'Its coat color {cow.coat_color} and tail length {cow.tail_length}')
    print(cow.eat_grass())
    print(cow.speak())
    print('Yes!!!')
    print()
    print('Create a pig')
    pig = Pig('Naf', 2, 'Pig')
    print(pig)
    print(f'Its skin color {pig.skin_color} and tail length {pig.tail_length}')
    print(pig.digs_ground())
    print(pig.speak())
    print('Super! And now we...')
    print()
    print('Create a chicken.')
    chicken = Chicken('Lusi', 1, 'Chicken')
    print(chicken)
    print(f'Its color {chicken.color} and it has {chicken.number_of_legs} legs')
    print(chicken.pecks_grain())
    print(chicken.speak())
    print('Wooow!')
    print('*' * 30)


if __name__ == '__main__':
    main()
