# -*- coding: utf-8 -*-

'''ЗАДАЧА: НАЛОГ НА НЕДВИЖИМОСТЬ
[Начинаем программировать на Python. Тони Гэддис (2022)]
Территориальный округ собирает налоги на недвижимое имущество, опираясь на
оценочную стоимость имущества, которая составляет 60% фактической стоимости
недвижимого имущества. Если акр земли оценивается в $10000, то его оценочная
стоимость составляет $6000. Налог на имущество в таком случае составит $0.75
для каждого $100 оценочной стоимости. Налог на акр, оцененный в $6000,
составит $45.00. Напишите программу с GUI, которая выводит на экран оценочную
стоимость и налог на недвижимое имущество при вводе пользователем фактической
стоимости недвижимого имущества.
'''

import tkinter as tk


class GUI:

    def __init__(self):
        # Main window
        self.window = tk.Tk()
        self.window.title('Tax calculation')
        self.window.geometry('260x140')
        # Frames
        self.frm_ent = tk.Frame(self.window)
        self.frm_assessed = tk.Frame(self.window)
        self.frm_tax = tk.Frame(self.window)
        self.frm_btn = tk.Frame(self.window)
        # Property value
        self.lbl_val = tk.Label(self.frm_ent, text='Property value:')
        self.ent_val = tk.Entry(self.frm_ent, justify='right', width=10)
        # Assessed value
        self.lbl_assessed_prompt = tk.Label(self.frm_assessed,
                                            text='Assessed value:')
        self.lbl_assessed = tk.Label(self.frm_assessed,
                                     width=10,
                                     borderwidth=1,
                                     relief='ridge')
        # Tax
        self.lbl_tax_prompt = tk.Label(self.frm_tax, text='Tax:')
        self.lbl_tax = tk.Label(self.frm_tax,
                                width=10,
                                borderwidth=1,
                                relief='ridge')
        # Calculation button
        self.btn_calc = tk.Button(self.frm_btn,
                                  text='Calculation',
                                  command=self.calc)
        # Packs
        self.lbl_val.pack(side='left', padx=(0, 10))
        self.ent_val.pack(side='left')
        self.lbl_assessed_prompt.pack(side='left', padx=(0, 5))
        self.lbl_assessed.pack(side='left')
        self.lbl_tax_prompt.pack(side='left', padx=(0, 82))
        self.lbl_tax.pack(side='left')
        self.btn_calc.pack()
        self.frm_ent.pack(pady=5)
        self.frm_assessed.pack(pady=5)
        self.frm_tax.pack(pady=5)
        self.frm_btn.pack(pady=5)
        # Mainloop
        self.window.mainloop()

    def calc(self):
        property_value = self.ent_val.get()
        try:
            property_value = float(property_value)
        except Exception:
            self.lbl_assessed['text'] = 'Error'
            self.lbl_tax['text'] = 'Error'
            return
        self.lbl_assessed['text'] = f'{property_value * 0.6:,.2f}'
        self.lbl_tax['text'] = f'{property_value * 0.6 / 100 * 0.75:,.2f}'


def main():
    gui = GUI()


if __name__ == '__main__':
    main()
