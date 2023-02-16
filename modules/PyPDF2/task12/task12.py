# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.В текущей директории находится файл с именем split_and_rotate.pdf. Создайте
новый файл rotated.pdf, который содержит страницы split_and_rotate.pdf,
повернутые на 90 градусов против часовой стрелки.

2.Используя файл rotated.pdf, созданный в упражнении 1, разбейте каждую
страницу PDF по вертикали по центру страницы. Создайте новый файл PDF
split.pdf со всеми страницами,полученными в результате разбиения. Файл
split.pdf должен содержать четыре страницы с номерами 1, 2, 3 и 4 в указанном
порядке.
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from copy import deepcopy

# 1
print('Task 1:')
# path to file
pdf_path = Path('split_and_rotate.pdf')
# create pdf instances
pdf = PdfReader(pdf_path)
writer = PdfWriter()
# if page is rotated - rotate
for i, page in enumerate(pdf.pages):
    deg_rotate = page['/Rotate'] * -1
    page.rotate(deg_rotate)
    writer.add_page(page)
    print(f'\t-> Rotate {i + 1} page')
# write new pdf to file "rotated.pdf"
with Path('rotated.pdf').open(mode='wb') as output_file:
    writer.write(output_file)
    print('Write new pdf to file "rotated.pdf"')
print()

# 2
print('Task 2:')

# function that crop pages
def crop(page):
    left_page = deepcopy(page)
    right_page = deepcopy(page)
    # crop left page
    left_page.mediabox.upper_right = (
        left_page.mediabox.right / 2,
        left_page.mediabox.top
    )
    # crop right page
    right_page.mediabox.upper_left = (
        right_page.mediabox.right / 2,
        right_page.mediabox.top
    )
    return left_page, right_page

# path to pdf file
pdf_path = Path('rotated.pdf')
# create pdf instances
pdf = PdfReader(pdf_path)
writer = PdfWriter()
# crop all pages
for i, page in enumerate(pdf.pages):
    print(f'Crop {i + 1} page:')
    left_page, right_page = crop(page)
    print('\t-> add new page')
    writer.add_page(left_page)
    print('\t-> add new page')
    writer.add_page(right_page)

# write pdf to new file "split.pdf"
with Path('split.pdf').open(mode='wb') as output_file:
    writer.write(output_file)
    print('Write new pdf to file "split.pdf"')
