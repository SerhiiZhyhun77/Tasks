# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


# Функция с тремя аргументами
def display(count, time, text):
    for k in range(count):
        # Пауза в выполнении потока
        sleep(time)
        print('[', k + 1, '] ', text, sep='')


print('Начинается выполнение программы')
# Создание объекта дочернего потока
t = Thread(target=display, args=(5, 2, 'Дочерний поток'))
# Запуск дочернего потока на выполнение
t.start()
# Вызов функции в главном потоке
display(3, 1.5, 'Главный поток')
# Ожидание завершения дочернего потока
t.join()
print('Программа завершила выполнение')
