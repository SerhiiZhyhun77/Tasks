# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


# Класс для создания вызываемого объекта
class MyClass:

    # Конструктор
    def __init__(self, text):
        self.text = text

    # Метод вызывается при вызове объекта
    def __call__(self, count, time):
        for k in range(count):
            sleep(time)
            print('[', k + 1, '] ', self.text, sep='')


print('Начинается выполнение программы')
# Создание вызываемого объекта
obj = MyClass('Дочерний поток')
# Создание объекта дочернего потока
t = Thread(target=obj, kwargs={'time': 2, 'count': 5})
# Запуск дочернего потока
t.start()
# Вызов анонимного объекта в главном потоке
MyClass('Главный поток')(3, 1.5)
# Ожидание завершения дочернего потока
if t.is_alive():
    t.join()
print('Программа завершила выполнение')
