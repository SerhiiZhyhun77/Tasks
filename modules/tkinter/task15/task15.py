# -*- coding: utf-8 -*-

'''ЗАДАЧА: ФИО и адрес
[Начинаем программировать на Python. Тони Гэддис (2022)]
Напишите программу с GUI, которая при нажатии кнопки выводит на экран ваше
полное имя и адрес. Когда пользователь нажимает кнопку "Показать инфо",
программа должна вывести на экран ваше имя и адрес.
'''

import tkinter


class GUI:

    def __init__(self):
        # Main window
        self.main_window = tkinter.Tk()
        self.main_window.title('FIO & address')
        self.main_window.geometry('300x100')
        # Info
        self.value = tkinter.StringVar()
        self.lbl_frame = tkinter.Frame(self.main_window)
        self.lbl = tkinter.Label(self.lbl_frame, textvariable=self.value)
        self.lbl.pack()
        self.lbl_frame.pack(pady=10)
        # Buttons
        self.btn_frame = tkinter.Frame(self.main_window)
        self.btn_info = tkinter.Button(self.btn_frame,
                                       text='Show info',
                                       command=self.show_info)
        self.btn_exit = tkinter.Button(self.btn_frame,
                                       text='Exit',
                                       command=self.main_window.destroy)
        self.btn_info.pack(side='left', padx=(0, 5))
        self.btn_exit.pack(side='right', padx=(5, 0))
        self.btn_frame.pack(side='bottom', pady=(0, 10))
        # Mainloop
        tkinter.mainloop()

    def show_info(self):
        info = '123 ELF ROAD, NORTH POLE 88888\nSanta Claus\' Main Post Office'
        self.value.set(info)


def main():
    gui = GUI()


if __name__ == '__main__':
    main()
