# -*- coding: utf-8 -*-

"""ЗАДАЧА: ПРИЛОЖЕНИЕ ДЛЯ ИЗВЛЕЧЕНИЯ СТРАНИЦЫ PDF
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Примените EasyGUI для написания GUI-приложения, извлекающего страницы из
файла PDF.

Подробный план:
    1.Предложить пользователю выбрать файл PDF.
    2.Если файл PDF не выбран, завершить программу.
    3.Запросить начальный номер страницы.
    4.Если пользователь не ввел начальный номер страницы, завершить программу.
    5.Допустимыми номерами страниц являются положительные целые числа. Если
    пользователь ввел недопустимый номер страницы:
    - предупредить пользователя о том, что введенное значение недопустимо;
    - вернуться к шагу 3.
    6.Запросить конечный номер страницы.
    7.Если пользователь не ввел конечный номер страницы, завершить программу.
    8.Если пользователь ввел недопустимый номер страницы:
    - предупредить пользователя о том, что введенное значение недопустимо;
    - вернутьсяк шагу 6.
    9.Запросить место (путь) для сохранения извлеченных страниц.
    10.Если пользователь не выбрал место для сохранения, завершить программу.
    11.Если выбранное место совпадает с путем входного файла:
    - предупредить пользователя о том, что перезапись входного файла
    недопустима;
    - вернуться к шагу 9.
    12.Выполнить извлечение страниц:
    - открыть входной файл PDF;
    - записать новый файл PDF, который содержит только страницы из выбранного
    диапазона.
"""

import easygui as gui
from PyPDF2 import PdfReader, PdfWriter

# 4 - 5, 7 - 8
def get_page(msg, title):
    while True:
        num_page = gui.enterbox(
            msg=msg,
            title=title
        )
        if num_page is None:
            exit()
        if num_page.isdigit():
            break
        else:
            gui.msgbox(
                msg='The enter is not valid. Must be a positive number.',
                title='Input error!',
                ok_button='OK'
            )
    return int(num_page)

# 1
pdf_path = gui.fileopenbox(
    msg='Select the PDF file you want...',
    title='Path to PDF',
    default='*.pdf'
)
# 2
if pdf_path is None:
    exit()
# 3
start_page = get_page('Enter the start page', 'Start page')
# 6
end_page = get_page('Enter the last page', 'Last page')
# 9
while True:
    new_pdf_path = gui.filesavebox(
        msg='Select where to save the file',
        title='Save as...',
        default='*.pdf'
    )
    # 10
    if new_pdf_path is None:
        exit()
    # 11
    if pdf_path == new_pdf_path:
        gui.msgbox(
            msg='Overwriting the input file is not allowed!',
            title='Path error!',
            ok_button='OK'
        )
    else:
        break

# 12
pdf = PdfReader(pdf_path)
writer = PdfWriter()
for page in pdf.pages[start_page - 1 : end_page - 1]:
    writer.add_page(page)
with open(new_pdf_path, 'wb') as output_file:
    writer.write(output_file)
