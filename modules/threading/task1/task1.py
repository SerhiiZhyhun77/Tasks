# -*- coding: utf-8 -*-

# Импорт класса Thread
from threading import Thread
# Импорт функции sleep()
from time import sleep


# Функция для вызова в главном потоке
def alpha():
    for k in range(5):
        # Пауза в выполнении потока
        sleep(1.5)
        print('[', k + 1, '] Alpha', sep='')


# Функция для выполнения в дочернем потоке
def bravo():
    for k in range(5):
        print('[', k + 1, '] Bravo', sep='')
        # Пауза в выполнении потока
        sleep(1)


# Создание объекта дочернего потока
t = Thread(target=bravo)
# Запуск дочернего потока
t.start()
# Вызов функции в главном потоке
alpha()
