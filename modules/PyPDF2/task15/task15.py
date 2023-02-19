# -*- coding: utf-8 -*-

""" ЗАДАЧА: ВОССТАНОВЛЕНИЕ ПОРЯДКА СТРАНИЦ
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущей директории содержится файл PDF с именем scrambled.pdf, состоящий из
семи страниц. На каждой странице находится число от 1 до 7, но порядок чисел
нарушен.
Кроме того, некоторые страницы повернуты на 90, 180 или 270 градусов по
часовой стрелке или против нее.
Напишите программу, которая восстанавливает файл PDF. Для этого она сортирует
страницы по номеру в тексте и при необходимости поворачивает их в
вертикальное положение.
Сохраните восстановленный файл PDF в файле с именем unscrambled.pdf
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# path to pdf
pdf_path = Path('scrambled.pdf')
# create pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# create dict for all need data
data_pages = dict()
# collect data
print('Collecting pages data\n')
for i, page in enumerate(pdf_reader.pages):
    page_number = page.extract_text().strip()  # get number from page
    data_pages[page_number] = (i, page['/Rotate'])  # get rotation angle
# iterate sorted pages
for key in sorted(data_pages.keys()):
    p, d = data_pages[key]
    d *= -1  # calculate the angle of rotation by 180 degrees
    print(f'Page {p} -> rotate {d} degrees', end=" ")
    page = pdf_reader.pages[p]  # get the required page
    page.rotate(d)  # rotate
    print('-> Add to new pdf')
    pdf_writer.add_page(page)  # add page to new pdf
print()
# write new pdf to file "unscrambled.pdf"
print('Write pdf to file "unscrambled.pdf"')
with Path('unscrambled.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
