# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущей директории находится файл ugly.pdf, который содержит текст сказки
Ганса Христиана Андерсена "Ugly Duckling", но каждая нечетная страница
повернута на 90 градусов против часовой стрелки.
Исправьте этот недостаток и сохраните в новом файле ugly_rotated.pdf.
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path('ugly.pdf')

# create necessary pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# rotate even pages and add to new pdf
print('Rotates even pages')
for i, page in enumerate(pdf_reader.pages):
    if i % 2 == 0:
        page.rotate(90)
    pdf_writer.add_page(page)
# write resule to file "ugly_rotated.pdf"
print('Write to file "ugly_rotated.pdf"')
with Path('ugly_rotated.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
