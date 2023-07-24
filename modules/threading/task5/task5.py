# -*- coding: utf-8 -*-

from threading import *
from time import sleep


# Функция для выполнения в потоке
def calc(txt, op):
    # Глобальная переменная
    global number
    # Оператор цикла
    for k in range(3):
        # Блокировка ресурса
        mylock.acquire()
        print(txt, ': ресурс заблокирован', sep='')
        # Контролируемый код
        try:
            # Считывание значения переменной
            print(txt, ': прочитано: ', number, sep='')
            # Запоминается значение переменной
            val = number
            # Пауза в выполнении потока
            sleep(1)
            # Изменение значения переменной
            if op:
                number = val + 1
            else:
                number = val - 1
            # Отображение значения переменной
            print(txt, ': записано: ', number, sep='')
        # Код выполняется всегда
        finally:
            print(txt, ': ресурс разблокирован', sep='')
            print('------------------------')
            # Разблокировка ресурса
            mylock.release()
        # Пауза в выполнении потока
        sleep(1)


# Начальное значение глобальной переменной
number = 0
# Объект блокировки
mylock = Lock()
# Объекты дочерних потоков
A = Thread(target=calc, args=['A', True])
B = Thread(target=calc, args=['B', False])
# Запуск дочерних объектов на выполнение
A.start()
B.start()
# Ожидание завершения потоков
A.join()
B.join()
