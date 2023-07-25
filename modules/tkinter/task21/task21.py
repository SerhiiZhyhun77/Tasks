# -*- coding: utf-8 -*-

from tkinter import *


# Списки с характеристиками шрифтов
fnt_1 = ['Arial', 12, 'Italic']
fnt_2 = ['Times New Roman', 13, 'bold', 'italic']
# Список с названиями шрифтов для статического списка
fonts = ['Times New Roman', 'Arial', 'Courier New']
# Минимальный размер шрифта
min_size = 15
# Максимальный размер шрифта
max_size = 21
# Ширина и высота окна
W = 640
H = 420
# Высота панели с шаблонным текстом
Hf = 140
# Ширина и высота панели со статическим списком
Wl = W / 3
Hl = H - Hf - 15
# Высота панели с кнопкой
Hb = 60
# Ширина и высота панели со слайдером и переключателями
Ws = W - Wl - 15
Hs = Hl - Hb - 5
# Создание окна
wnd = Tk()
wnd.title('Параметры шрифта')
wnd.geometry(str(W) + 'x' + str(H))
wnd.resizable(False, False)
# Создание панелей
frm_scale = Frame(wnd, bd=3, relief=GROOVE)
frm_text = Frame(wnd, bd=3, relief=GROOVE)
frm_btn = Frame(wnd, bd=3, relief=GROOVE)
frm_list = Frame(wnd, bd=3, relief=GROOVE)
frm_check = Frame(wnd, bd=3, relief=GROOVE)
# Переменные дла определения текстового содержимого в элементах управления
text = StringVar()
color = StringVar()
bold = StringVar()
italic = StringVar()
# Создание текстовых меток
lbl_text = Label(frm_text, text='Пример текста', font=fnt_2)
lbl_color = Label(frm_scale, text='Цвет текста', font=fnt_2)
lbl_size = Label(frm_scale, text='Размер текста', font=fnt_2)
lbl_font = Label(frm_list, text='Название шрифта', font=fnt_2)
lbl_style = Label(frm_check, text='Стиль шрифта', font=fnt_2)
# Метка для отображения шаблонного текста
lbl = Label(frm_text, textvariable=text)
# фон и рамка для метки
lbl.configure(bg='white', relief=RAISED)
# Переключатели
rb_1 = Radiobutton(frm_scale, text='красный', variable=color)
rb_1.configure(value='red', font=fnt_1)
rb_2 = Radiobutton(frm_scale, text='синий', variable=color)
rb_2.configure(value='blue', font=fnt_1)
rb_3 = Radiobutton(frm_scale, text='черный', variable=color)
rb_3.configure(value='black', font=fnt_1)
# Устанавливаем переключатель
color.set('blue')
# Создание слайдера
scl = Scale(frm_scale, orient=HORIZONTAL)
# Диапазон изменения значений
scl.configure(from_=min_size, to=max_size)
# Интервал для отображения подписей и шаг положения ползунка
scl.configure(tickinterval=1, resolution=1)
# Обработчик для события, связанного с изменением положения слайдера
scl.configure(command=setAll)
# Создание опций и настройка их параметров
chb_1 = Checkbutton(frm_check, text='жирный', variable=bold)
chb_1.configure(onvalue='bold', offvalue='', font=fnt_1)
chb_2 = Checkbutton(frm_check, text='курсив', variable=italic)
chb_2.configure(onvalue='italic', offvalue='', font=fnt_1)
# Начальное состояние опций
bold.set('')
italic.set('italic')
# Создание статического списка
lst = Listbox(frm_list, selectmode=SINGLE, font=fnt_1)
# Цвет фона и цвет для выделения пункта
lst.configure(bg='gray96', selectbackground='gray')
# способ выделения пункта и высоты списка
lst.configure(activestyle='none', height=len(fonts) + 1)
# Заполнение статического списка пунктами
for n in fonts:
    lst.insert(END, n)
# По умолчанию выбран первый пункт
lst.select_set(0)
# Обработчик для статического списка
lst.bind('<<ListboxSelect>>', setAll)
# Создание кнопки
btn = Button(frm_btn, text='OK', font=fnt_2)
# Обработчик для кнопки
btn.configure(command=wnd.destroy)
# Размещение меток и слайдера на панелях
lbl_text.pack(side='top', fill='x', padx=5, pady=5)
lbl.pack(side='top', fill='both', padx=5, pady=5)
lbl_color.pack(side='bottom')



wnd.mainloop()