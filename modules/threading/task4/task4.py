# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


# Произвольный класс
class MyThread(Thread):

    # Конструктор
    def __init__(self, count, time, text):
        # Вызов конструктора базового класса
        super().__init__()
        # Присваивание значений полям
        self.count = count
        self.time = time
        self.text = text

    # Переопределение метода для выполнения в потоке
    def run(self):
        for k in range(self.count):
            sleep(self.time)
            print('[', k + 1, '] ', self.text, sep='')


print('Начинается выполнение программы')
# Создание объектов для дочерних потоков
A = MyThread(5, 2, 'Alpha')
B = MyThread(3, 1.5, 'Bravo')
# Запуск дочерних потоков на выполнение
A.start()
B.start()
# Ожидание завершения дочерних потоков
if A.is_alive():
    A.join()
if B.is_alive():
    B.join()
print('Программа завершила выполнение')
