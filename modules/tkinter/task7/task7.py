# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Создайте форму для ввода информации средствами Tkinter. Заголовок окна:
"Address Entry Form". Форма должна иметь следующие поля:
    - First Name;
    - Last Name;
    - Address Line 1;
    - Address Line 2;
    - City;
    - State/Province;
    - Postal Code;
    - Country.
Справа внизу разместите две кнопки: Clear и Submit.
Используйте любой менеджер геометрии на свое усмотрение.
"""

import tkinter as tk

window = tk.Tk()
window.title('Address Entry Form')
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1, minsize=25)
window.columnconfigure(0, weight=0, minsize=110)
window.columnconfigure(1, weight=1, minsize=350)
# labels
lbl_first_name = tk.Label(text='First Name:')
lbl_last_name = tk.Label(text='Last Name:')
lbl_addr_line1 = tk.Label(text='Address Line 1:')
lbl_addr_line2 = tk.Label(text='Address Line 2:')
lbl_city = tk.Label(text='City:')
lbl_state_province = tk.Label(text='State/Province:')
lbl_post_code = tk.Label(text='Postal Code:')
lbl_country = tk.Label(text='Country:')
#entries
ent_first_name = tk.Entry()
ent_last_name = tk.Entry()
ent_addr_line1 = tk.Entry()
ent_addr_line2 = tk.Entry()
ent_city = tk.Entry()
ent_state_province = tk.Entry()
ent_post_code = tk.Entry()
ent_country = tk.Entry()
# buttons
btn_clear = tk.Button(text='Clear')
btn_submit = tk.Button(text='Submit')

#placing label in the grid
lbl_first_name.grid(row=0, column=0, sticky='e')
lbl_last_name.grid(row=1, column=0, sticky='e')
lbl_addr_line1.grid(row=2, column=0, sticky='e')
lbl_addr_line2.grid(row=3, column=0, sticky='e')
lbl_city.grid(row=4, column=0, sticky='e')
lbl_state_province.grid(row=5, column=0, sticky='e')
lbl_post_code.grid(row=6, column=0, sticky='e')
lbl_country.grid(row=7, column=0, sticky='e')
# placing entries in the grid
ent_first_name.grid(row=0, column=1, padx=(0, 2), sticky='ew')
ent_last_name.grid(row=1, column=1, padx=(0, 2), sticky='ew')
ent_addr_line1.grid(row=2, column=1, padx=(0, 2), sticky='ew')
ent_addr_line2.grid(row=3,column=1, padx=(0, 2), sticky='ew')
ent_city.grid(row=4, column=1, padx=(0, 2), sticky='ew')
ent_state_province.grid(row=5, column=1, padx=(0, 2), sticky='ew')
ent_post_code.grid(row=6, column=1, padx=(0, 2), sticky='ew')
ent_country.grid(row=7, column=1, padx=(0, 2), sticky='ew')
# placing button in the grid
btn_submit.grid(row=8, column=1, padx=10, pady=5, sticky='e')
btn_clear.grid(row=8, column=1, padx=(0, 95), sticky='e')

window.mainloop()
