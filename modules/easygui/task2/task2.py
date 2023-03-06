# -*- coding: utf-8 -*-

"""ЗАДАНИЕ: ПРОГРАММА ДЛЯ ПОВОРОТА СТРАНИЦ PDF
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу поворота страниц PDF файла, которая будет работать
согласно указанной ниже последовательности действий.
    1.Вывести диалоговое окно выбора файла для открытия документа PDF.
    2.Если пользователь отменяет диалоговое окно, завершить работу программы.
    3.Предложить пользователю выбрать угол поворота в градусах - одно из
    значений 90, 180 или 270 градусов.
    4.Открыть диалоговое окно для выбора файла, чтобы сохранить документ PDF
    с повернутыми страницами.
    5.Если пользователь пытается сохранить файл с таким же именем,
    как у входного файла:
        - уведомить пользователя, что операция недопустима;
        - вернуться к шагу 4.
    6.Если пользователь отменит диалоговое окно для сохранения файла,
    завершить работу программы.
    7.Выполнить поворот страниц:
        - открыть выбранный файл PDF;
        - повернуть все страницы;
        - сохранить документ PDF с повернутыми страницами в выбранном файле.
"""

import easygui as gui
from PyPDF2 import PdfReader, PdfWriter

# 1
input_path = gui.fileopenbox(
    title='Select a PDF to rotate...',
    default='*.pdf'
)
# 2
if input_path is None:
    exit()
# 3
choices = ('90', '180', '270')
degrees = None
while degrees is None:
    degrees = gui.buttonbox(
        msg='Rotate the PDF clockwise by how many degrees?',
        title='Choose rotation...',
        choices=choices,
    )
degrees = int(degrees)
# 4
save_title = 'Save the rotated PDF as...'
file_type = '*.pdf'
output_path = gui.filesavebox(title=save_title, default=file_type)
# 5
while input_path == output_path:
    gui.msgbox(msg='Cannot overwrite original file!')
    output_path = gui.filesavebox(title=save_title, default=file_type)
# 6
if output_path is None:
    exit()
# 7
# open PDF
input_file = PdfReader(input_path)
output_pdf = PdfWriter()
# rotate
for page in input_file.pages:
    page = page.rotate(degrees)
    output_pdf.add_page(page)
# save PDF
with open(output_path, 'wb') as output_file:
    output_pdf.write(output_file)
