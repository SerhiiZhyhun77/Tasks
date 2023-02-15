# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущей директории находится файл ugly.pdf, который содержит текст сказки
Ганса Христиана Андерсена "Ugly Duckling", но каждая нечетная страница
повернута на 90 градусов против часовой стрелки.

1. Исправьте этот недостаток повернув каждую четную страницу на 90 градусов и
сохраните в файле ugly_rotated.pdf.

2. Выполните это же задание используя для поворота ключ метаданных страницы
/Rotate и сохраните результат в файл ugly_rotated2.pdf.
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path('ugly.pdf')

# 1
print('Task1:')
# create necessary pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# rotate even pages and add to new pdf
print('Rotate even pages')
for i, page in enumerate(pdf_reader.pages):
    if i % 2 == 0:
        page.rotate(90)
    pdf_writer.add_page(page)
# write result to file "ugly_rotated.pdf"
print('Write to file "ugly_rotated.pdf"')
with Path('ugly_rotated.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
print()

# 2
print('Task2:')
# create new pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# check metadata /Rotate. If its = -90 - rotate(90). Add page to new pdf.
for page in pdf_reader.pages:
    if (page['/Rotate']) == -90:
        page.rotate(90)
        print(f'\t-> Rotate {page["/StructParents"] + 1} page')
    pdf_writer.add_page(page)
# write result to file "ugly_rotated2.pdf"
print('Write to file "ugly_rotated2.pdf"')
with Path('ugly_rotated2.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
