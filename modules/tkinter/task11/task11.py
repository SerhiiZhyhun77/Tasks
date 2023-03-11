# -*- coding: utf-8 -*-

"""ЗАДАЧА: КОНВЕРТЕР ТЕМПЕРАТУР
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу преобразования температур: пользователь вводит температуру в
градусах по шкале Фаренгейта и щелчком кнопки преобразует ее к значению по
Цельсию.
"""

import tkinter as tk

# conversion from fahrenheit to celsius
def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'

# create window
window = tk.Tk()
# set title
window.title('Temperature Converter')

# frame for entry+label
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text='\N{DEGREE FAHRENHEIT}')
# positioning on the frame
ent_temperature.grid(row=0, column=0, sticky='e')
lbl_temp.grid(row=0, column=1, sticky='w')
# button
btn_convert = tk.Button(
    master=window,
    text ='\N{RIGHTWARDS BLACK ARROW}',
    command=fahrenheit_to_celsius
)
# label result
lbl_result = tk.Label(master=window, text='\N{DEGREE CELSIUS}')
# positioning on the window
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()