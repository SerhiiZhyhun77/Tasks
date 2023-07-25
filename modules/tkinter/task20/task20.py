# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import Combobox
from pathlib import Path


# Функция для обработки события, связанного с выбором пункта
# в раскрывающемся списке
def change(evt):
    # Считывание значения, выбранного в списке
    t = cb.get()
    # Определение изображения, по выбранному значению
    for k in range(len(names)):
        # Если выбранное изображение совпадает с текстом в списке
        if t == names[k]:
            # Новое изображение в метке
            lbl.configure(image=imgs[k])
            # Завершение оператора цикла
            break


# Переменная с путем к файлам изображений
path = str(Path.cwd() / 'images') + '/'
# Названия животных
names = ['Tiger', 'Lion', 'Bear']
# Названия файлов с изображениями
files = ['tiger.png', 'lion.png', 'bear.png']
# Создание объекта окна
wnd = Tk()
# Параметры окна
wnd.title('Predators')
wnd.geometry('220x300')
wnd.resizable(False, False)
# Список с объектами изображений
imgs = [PhotoImage(file=path + f) for f in files]
# Индекс для выбранного в начале пункта
index = 0
# Создание объекта метки
lbl = Label(wnd, image=imgs[index])
# Параметры метки и ее размещение в окне
lbl.configure(relief=GROOVE)
lbl.place(x=10, y=10, width=200, height=200)
# Создание объекта для раскрывающегося списка
cb = Combobox(wnd, state='readonly')
# Содержимое раскрывающегося списка
cb.configure(values=names)
# Выбранное в начале значение (пункт)
cb.current(index)
# Шрифт для раскрывающегося списка
cb.configure(font=('Arial', 11, 'bold'))
# Определение обработчика события, связанного с выбором в списке нового значения
cb.bind('<<ComboboxSelected>>', change)
# Размещение списка в окне
cb.place(x=10, y=220, width=200, height=30)
# Создание объекта кнопки
btn = Button(wnd, text='OK')
# Определение обработчика для события, связанного с нажатием кнопки
btn.configure(command=wnd.destroy)
# Размеры кнопки и ее размещение в окне
btn.place(x=60, y=260, width=100, height=30)
# Отображение окна на экране
wnd.mainloop()
