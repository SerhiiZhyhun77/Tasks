# -*- coding: utf-8 -*-

'''ЗАДАЧА: КАЛЬКУЛЯТОР МИЛЬ НА ГАЛЛОН БЕНЗИНА
[Начинаем программировать на Python. Тони Гэддис (2022)]
Напишите программу с GUI, которая вычисляет экономичность автомобиля. Окно
программы должно содержать виджеты Entry, которые позволяют пользователю
вводить объем бензина в галлонах, заправленного в автомобиль, и число миль,
которые он может пройти с полным баком. При нажатии кнопки "Вычислить MPG"
программа должна вывести на экран число миль, которые автомобиль может пройти в
расчете на галлон бензина. Для вычисления показателя числа миль на галлон
примените приведенную ниже формулу:

    Показатель миль на галлон = мили / галлоны
'''

import tkinter as tk


class GUI:

    def __init__(self):
        # Main window
        self.window = tk.Tk()
        self.window.title('Calc MPG')
        self.window.geometry('150x180')
        # Frames
        self.ent_frame = tk.Frame(self.window)
        self.btn_frame = tk.Frame(self.window)
        # Labels + Entries
        self.value = tk.StringVar()
        self.lbl_gal = tk.Label(self.ent_frame, text='Gallons of gasoline')
        self.ent_gal = tk.Entry(self.ent_frame, width=10)
        self.lbl_miles = tk.Label(self.ent_frame, text='Miles')
        self.ent_miles = tk.Entry(self.ent_frame, width=10)
        self.lbl_res = tk.Label(self.ent_frame,
                                textvariable=self.value,
                                borderwidth=1,
                                relief='ridge', width=6)
        self.lbl_prompt = tk.Label(self.ent_frame, text='MPG')
        # Button
        self.btn_calc = tk.Button(self.btn_frame,
                                  text='Calc MPG',
                                  command=self.calc)
        self.lbl_gal.pack()
        self.ent_gal.pack()
        self.lbl_miles.pack()
        self.ent_miles.pack()
        self.lbl_res.pack(side='left', padx=(22, 5), pady=15)
        self.lbl_prompt.pack(side='left')
        self.btn_calc.pack(side='bottom', pady=(0, 5))
        self.ent_frame.pack()
        self.btn_frame.pack()
        # Mainloop
        self.window.mainloop()

    def calc(self):
        gal = self.ent_gal.get()
        miles = self.ent_miles.get()
        try:
            gal = float(gal)
            miles = float(miles)
            self.value.set(f'{miles / gal:.2f}')
        except Exception:
            self.value.set('Error')


def main():
    gui = GUI()


if __name__ == '__main__':
    main()
