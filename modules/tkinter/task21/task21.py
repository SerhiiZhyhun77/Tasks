# -*- coding: utf-8 -*-

from tkinter import *


# Функция для определения характеристики шрифта
def getFont():
    # Пустой список
    res = []
    # Название шрифта
    name = lst.get(lst.curselection())
    # Размер шрифта
    size = scl.get()
    # Добавление элементов в список
    res.append(name)
    res.append(size)
    # Если установлена опция применения жирного стиля
    if bold.get() != '':
        res.append(bold.get())
    # Если установлена опция применения курсивного стиля
    if italic.get() != '':
        res.append(italic.get())
    # Результат функции
    return res


# Функция для применения параметров шрифтов
def setAll(*args):
    # Вычисление шрифта
    fnt = getFont()
    # Применение шрифта к тексту в окне
    lbl.configure(font=fnt)
    # Определение цвета для текста в окне
    lbl.configure(fg=color.get())
    # Определение шаблонного текста для отображения в окне
    txt = '\nШрифт '
    # Название шрифта
    txt += fnt[0]
    # Размер шрифта
    txt += ' размера ' + str(fnt[1]) + '\n'
    # Если применяется жирный стиль
    if 'bold' in fnt:
        txt += ' жирный'
    # Если применяется курсивный стиль
    if 'italic' in fnt:
        txt += ' курсивный'
    # Цвет шрифта
    if color.get() == 'red':
        txt += ' красного'
    elif color.get() == 'blue':
        txt += ' синего'
    else:
        txt += ' черного'
    txt += ' цвета\n'
    # Отображение текста в окне
    text.set(txt)


# Списки с характеристиками шрифтов
fnt_1 = ['Arial', 12, 'italic']
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
lbl_color.pack(side='top', fill='x', padx=5, pady=5)
scl.pack(side='bottom', fill='x', padx=5, pady=5)
lbl_size.pack(side='bottom', fill='x', padx=5, pady=[25, 5])
lbl_font.pack(side='top', fill='x', padx=5, pady=5)
lbl_style.pack(side='top', fill='x', padx=5, pady=5)
# Размещение переключателей
rb_1.pack(side='left', fill='x', padx=5, pady=5)
rb_2.pack(side='left', fill='x', padx=5, pady=5)
rb_3.pack(side='left', fill='x', padx=5, pady=5)
# Размещение опций
chb_1.pack(side='left', fill='x', padx=5, pady=5)
chb_2.pack(side='left', fill='x', padx=5, pady=5)
# Размещение статического списка
lst.pack(side='top', fill='x', padx=5, pady=5)
# Размешение кнопки
btn.pack(side='bottom', fill='x', padx=50, pady=10)
# Размещение панелей
frm_text.place(x=5, y=5, width=W - 10, height=Hf)
frm_check.pack(side='bottom', fill='both', padx=5, pady=5)
frm_list.place(x=5, y=Hf + 10, height=Hl, width=Wl)
frm_scale.place(x=Wl + 10, y=Hf + 10, width=Ws, height=Hs)
frm_btn.place(x=Wl + 10, y=Hf + 15, width=Ws, height=Hb)
# Применение параметров шрифта к шаблонному тексту
setAll()
# Режим отстлеживания значения переменных
color.trace('w', setAll)
bold.trace('w', setAll)
italic.trace('w', setAll)
# Отображение окна
wnd.mainloop()
