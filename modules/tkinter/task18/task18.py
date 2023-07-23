# -*- coding: utf-8 -*-

'''ЗАДАЧА: ИЗ ШКАЛЫ ЦЕЛЬСИЯ В ШКАЛУ ФАРЕНГЕЙТА
[Начинаем программировать на Python. Тони Гэддис (2022)]
Напишите программу с GUI, которая преобразует показания температуры по шкале
Цельсия в температуру по шкале Фаренгейта. Пользователь должен иметь
возможность вводить температуру по шкале Цельсия, нажимать кнопку и затем
получать эквивалентную температуру по шкале Фаренгейта. Для выполнения этого
преобразования примените приведенную ниже формулу:
         F = 9/5 * C + 32,
где F - это температура по Фаренгейту; С - температура по шкале Цельсия.
'''

import tkinter as tk


class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title(f'\N{DEGREE CELSIUS} \N{RIGHTWARDS BLACK ARROW}'
                          f' \N{DEGREE FAHRENHEIT}')
        self.window.geometry('210x50')
        self.frm = tk.Frame(self.window)
        self.ent_c = tk.Entry(self.frm, width=4)
        self.lbl_c = tk.Label(self.frm, text=f'\N{DEGREE CELSIUS}')
        self.btn = tk.Button(self.frm,
                             text=f'\N{RIGHTWARDS BLACK ARROW}',
                             command=self.cel2far)
        self.lbl_far = tk.Label(self.frm,
                                width=4,
                                borderwidth=1,
                                relief='ridge')
        self.lbl_far_prompt = tk.Label(self.frm, text=f'\N{DEGREE FAHRENHEIT}')
        self.ent_c.pack(side='left', padx=(5, 0))
        self.lbl_c.pack(side='left', padx=(0, 5))
        self.btn.pack(side='left', padx=5)
        self.lbl_far.pack(side='left', padx=(5, 0))
        self.lbl_far_prompt.pack(side='left', padx=(0, 5))
        self.frm.pack(padx=5, pady=10)
        self.window.mainloop()

    def cel2far(self):
        c = self.ent_c.get()
        try:
            c = int(c)
            self.lbl_far['text'] = round(9 / 5 * c + 32)
        except Exception:
            self.lbl_far['text'] = 'Err'


def main():
    gui = GUI()


if __name__ == '__main__':
    main()
