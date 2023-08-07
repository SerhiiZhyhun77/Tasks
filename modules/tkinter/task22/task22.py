# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *


# Класс для создания окна
class MyApp:

    # Конструктор
    def __init__(self):
        # Настройка параметров
        self.setValues()
        # Создание главного окна
        self.makeMainWindow()
        # Определение переменных для обработки событий
        self.setVars()
        # Создание главного меню
        self.makeMainMenu()
        # Создание панели инструментов
        self.makeToolBar()
        # Создание вспомогательной панели
        self.makeFrame()
        # Создание контекстного меню
        self.makePopupMenu()
        # Вычисление параметров шаблонного текста
        self.apply()
        # Режим отслеживания переменных
        self.traceVars()
        # Отображение главного окна
        self.showMainWindow()

    # Метод для настройки параметров
    def setValues(self):
        # Ширина и высота окна
        self.W = 500
        self.H = 200
        # Высота панели инструментов
        self.h = 40
        # Размеры главного окна
        self.position = str(self.W) + 'x' + str(self.H)
        # Названия шрифтов
        self.fonts = ['Times New Roman', 'Arial', 'Courier New']
        # Словарь с названиями цвета
        self.colors = {'red': 'Красный', 'blue': 'Синий', 'black': 'Черный'}
        # Список с названиями стиля
        self.style = [['bold', 'Жирный'], ['italic', 'Курсив']]
        # Список с названиями файлов с изображениями
        self.imgFiles = ['exit.png', 'bold.png', 'italic.png', 'normal.png']
        # Путь к каталогу с файлами
        self.path = 'images/'
        # Основной шрифт
        self.font = ('Courier New', 10, 'bold')

    # Метод для создания главного окна
    def makeMainWindow(self):
        self.wnd = Tk()
        self.wnd.title('Определяем шрифт')
        self.wnd.geometry(self.position)
        self.wnd.resizable(False, False)

    # Метод для отображения главного окна
    def showMainWindow(self):
        self.wnd.mainloop()

    # Метод для создания главного меню
    def makeMainMenu(self):
        # Создание объекта для панели меню
        self.menubar = Menu(self.wnd)
        # Создание пунктов главного меню
        self.mFont = Menu(self.wnd, font=self.font, tearoff=0)
        self.mStyle = Menu(self.wnd, font=self.font, tearoff=0)
        self.mColor = Menu(self.wnd, font=self.font, tearoff=0)
        self.mAbout = Menu(self.wnd, font=self.font, tearoff=0)
        # Заполнение пунктов меню
        self.setMenuFont(self.mFont)
        self.setMenuStyle(self.mStyle)
        self.setMenuColor(self.mColor)
        # Заполнение последнего пункта меню
        self.mAbout.add_command(label='О программе', command=self.showDialog)
        # Добавление разделителя
        self.mAbout.add_separator()
        self.mAbout.add_command(label='Выход', command=self.clExit)
        # Добавление пунктов меню на панель меню
        self.menubar.add_cascade(label='Шрифт', menu=self.mFont)
        self.menubar.add_cascade(label='Стиль', menu=self.mStyle)
        self.menubar.add_cascade(label='Цвет', menu=self.mColor)
        self.menubar.add_cascade(label='Программа', menu=self.mAbout)
        # Задаем главное меню для окна
        self.wnd.config(menu=self.menubar)

    # Метод для создания панели инструментов
    def makeToolBar(self):
        # Список с названиями методов для обработки события, связанного с
        # нажатием кнопок
        mt = [self.clExit, self.clBold, self.clItalic, self.clNormal]
        # Панель для размещения кнопок
        self.toolbar = Frame(self.wnd, bd=3, relief=GROOVE)
        # Список для изображений
        self.imgs = []
        # Список для кнопок
        self.btns = []
        # Создание изображений и кнопок
        for f in self.imgFiles:
            # Создание изображения
            self.imgs.append(PhotoImage(file=self.path + f))
            # Создание кнопки
            self.btns.append(Button(self.toolbar, image=self.imgs[-1]))
            # Добавление кнопки на панель
            self.btns[-1].pack(side='left', padx=2, pady=2)
        # Определение обработчиков для кнопок
        for k in range(len(mt)):
            self.btns[k].configure(command=mt[k])
        # Создание текстовой метки
        self.lblSize = Label(self.toolbar, text='Размер шрифта', font=self.font)
        # Размещение метки на панели
        self.lblSize.pack(side='left', padx=2, pady=2)
        # Создание спиннера
        self.spnSize = Spinbox(self.toolbar, from_=15, to=20, font=self.font,
                               width=3, justify='right', textvariable=self.size)
        # Размещение спиннера на панели
        self.spnSize.pack(side='left', padx=2, pady=2)
        # Размещени панели в окне
        self.toolbar.place(x=3, y=3, width=self.W - 6, height=self.h)

    # Метод для создания вспомогательной панели
    def makeFrame(self):
        # Создание вспомогательной панели
        self.frame = Frame(self.wnd, bd=3, relief=GROOVE)
        # Создание метки и добавление ее на панель
        Label(self.frame, text='Пример текста:', font=self.font).pack(
            side='top')
        # Создание метки для отображения шаблонного текста
        self.lblText = Label(self.frame, textvariable=self.text,
                             relief=GROOVE, bg='white', height=5)
        # Размещение метки на вспомогательной панели
        self.lblText.pack(side='top', fill='both', padx=1, pady=1)
        # Размещение вспомогательной панели в окне
        self.frame.place(x=3, y=self.h + 9, width=self.W - 6,
                         height=self.H - self.h - 12)

    # Метод для создания контекстного меню
    def makePopupMenu(self):
        # Создание объекта контекстного меню
        self.popup = Menu(self.wnd, tearoff=0, font=self.font)
        # Добавление команд в контекстное меню
        self.setMenuFont(self.popup)
        # Добавление разделителя
        self.popup.add_separator()
        # Добавление команд в контекстное меню
        self.setMenuStyle(self.popup)
        # Добавление разделителя
        self.popup.add_separator()
        # Добавление команд в контекстное меню
        self.setMenuColor(self.popup)
        # Добавление разделителя
        self.popup.add_separator()
        # Добавление команды в контекстное меню
        self.popup.add_command(label='Выход', command=self.clExit)
        # Определение обработчика события для контекстного меню
        self.wnd.bind('<Button-3>', lambda evt: self.popup.tk_popup(
            evt.x_root, evt.y_root))

    # Метод для формирования команд меню, связанных с выбором шрифта
    def setMenuFont(self, menu):
        for f in self.fonts:
            menu.add_radiobutton(label=f, value=f, variable=self.name)
        self.name.set(self.fonts[0])

    # Метод для формирования команд меню, связанных с выбором стиля
    def setMenuStyle(self, menu):
        for k in range(len(self.style)):
            menu.add_checkbutton(label=self.style[k][1], onvalue=True,
                                 offvalue=False, variable=self.bi[k])
        self.bi[0].set(True)
        self.bi[1].set(False)

    # Метод для формирования команд меню связанных с выбором цвета
    def setMenuColor(self, menu):
        for r in self.colors.keys():
            menu.add_radiobutton(label=self.colors[r], value=r,
                                 variable=self.color)
        self.color.set('blue')

    # Метод для определения параметров шрифта и вычисления шаблонного текста
    def apply(self, *args):
        # Цвет для шрифта
        clr = self.color.get()
        # Название шрифта
        nm = self.name.get()
        # Размер шрифта
        sz = self.size.get()
        # Применение цвета к метке
        self.lblText.configure(fg=clr)
        # Списокс параметрами шрифта
        fnt = [nm, sz]
        # Формирование шаблонного текста и определение параметров шрифта
        txt = self.colors[clr] + ' шрифт ' + nm + '\n'
        for k in range(len(self.style)):
            if self.bi[k].get():
                fnt.append((self.style[k][0]))
                txt += self.style[k][1].lower() + ' '
        txt += 'размера ' + str(sz)
        # Применение шрифта к метке
        self.lblText.configure(font=fnt)
        # Задаем текст для метки
        self.text.set(txt)

    # Метод для создания переменных, используемых для обработки событий
    def setVars(self):
        self.text = StringVar()
        self.name = StringVar()
        self.bi = [BooleanVar(), BooleanVar()]
        self.size = IntVar()
        self.color = StringVar()

    # Метод для перехода в режим отслеживания значений переменных
    def traceVars(self):
        mt = self.apply
        self.name.trace('w', mt)
        self.color.trace('w', mt)
        for k in range(len(self.bi)):
            self.bi[k].trace('w', mt)
        self.size.trace('w', mt)

    # Метод для обработки нажатия кнопки для завершения работы
    def clExit(self):
        self.wnd.destroy()

    # Метод для обработки нажатия кнопки применения/отмены жирного стиля
    def clBold(self):
        self.bi[0].set(not self.bi[0].get())

    # Метод для обработки нажатия кнопки применения/отмены кусивного стиля
    def clItalic(self):
        self.bi[1].set(not self.bi[1].get())

    # Метод для обработки нажатия кнопки отмены жирного и курсивного стиля
    def clNormal(self):
        self.bi[0].set(False)
        self.bi[1].set(False)

    # Метод для отображения окна с сообщением
    def showDialog(self):
        showinfo('О программе', 'Очень простая программа')


# Отображение окна на экране
MyApp()
