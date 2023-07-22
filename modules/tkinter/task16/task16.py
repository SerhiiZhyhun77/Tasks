# -*- coding: utf-8 -*-

'''ЗАДАЧА: ПЕРЕВОДЧИК С ЛАТИНСКОГО
[Начинаем программировать на Python. Тони Гэддис (2022)]
Взгляните на приведенный в таблице список латинских слов и их значений.
    Латинский       Русский
    sinister        Левый
    dexter          Правый
    medium          Центральный
Напишите программу с GUI, которая переводит латинские слова на русский язык.
Окно должно иметь три кнопки, по одной для каждого латинского слова. Когда
пользователь нажимает кнопку, программа должна выводить на экран русский
перевод в виджет Label.
'''

import tkinter as tk


class GUI:

    def __init__(self):
        # Main window
        self.window = tk.Tk()
        self.window.title('Translator')
        # Frames
        self.lbl_frame = tk.Frame(self.window)
        self.btn_frame = tk.Frame(self.window)
        # Label
        self.value = tk.StringVar()
        self.lbl = tk.Label(self.lbl_frame, textvariable=self.value)
        self.lbl.pack()
        # Buttons
        self.btn1 = tk.Button(self.btn_frame,
                              text='sinister',
                              command=self.btn1_clk)
        self.btn2 = tk.Button(self.btn_frame,
                              text='dexter',
                              command=self.btn2_clk)
        self.btn3 = tk.Button(self.btn_frame,
                              text='medium',
                              command=self.btn3_clk)
        self.btn1.pack(side='left', padx=5)
        self.btn2.pack(side='left')
        self.btn3.pack(side='left', padx=5)
        self.lbl_frame.pack(side='top', pady=10)
        self.btn_frame.pack(side='bottom', pady=(0, 5))
        # Mainloop
        self.window.mainloop()

    def btn1_clk(self):
        self.value.set('Left')

    def btn2_clk(self):
        self.value.set('Right')

    def btn3_clk(self):
        self.value.set('Center')


def main():
    gui = GUI()


if __name__ == '__main__':
    main()
