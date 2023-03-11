# -*- coding: utf-8 -*-

"""ЗАДАЧА: ТЕКСТОВЫЙ РЕДАКТОР
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Постройте текстовый редактор, который должен уметь создавать, открывать,
редактировать и сохранять файлы.
Используйте три основных элемента:
    1.Виджет Button с именем btn_open - открывает файл для редактирования;
    2.Виджет Button с именем btn_save - сохраняет файл;
    3.Виджет TextBox с именем txt_edit - создает и редактирует текстовый файлю

При помощи виджетов две кнопки разместите в левой части окна, а текстовое
поле - в правой.
Окно должно иметь минимальную высоту 800 пикселей, а поле txt_edit -
минимальную ширину 800 пикселей. Макет сделайте динамичным, чтобы при
изменении размеров окна также корректировались размеры виджета txt_edit. При
этом ширина виджета Frame, содержащего кнопки, меняться не должна.
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# open file
def open_file():
    # get path to file
    file_path = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    # if canceled
    if not file_path:
        return
    # clear txt_edit
    txt_edit.delete('1.0', tk.END)
    # read the file and insert new text into the txt_edit
    with open(file_path, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    # set new title
    window.title(f'Simple Text Editor - {file_path}')

# save file
def save_file():
    # get path to place to save file
    file_path = asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    # if canceled
    if not file_path:
        return
    # write text to file
    with open(file_path, 'w') as output_file:
        text = txt_edit.get('1.0', tk.END)
        output_file.write(text)
    # set new title
    window.title(f'Simple Text Editor - {file_path}')

# create window
window = tk.Tk()
# set title
window.title('Simple Text Editor')
# configure window grid
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# create widgets
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window)
btn_open = tk.Button(frm_buttons, text='Open', command=open_file)
btn_save = tk.Button(frm_buttons, text='Save As...', command=save_file)
# positioning button on the frame
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)
# positioning Frame and Text on the window
frm_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()