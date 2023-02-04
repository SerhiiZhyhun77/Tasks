# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущем каталоге находится pdf файл Pride_and_Prejudice.pdf
Создайте новый pdf файл chapter1.pdf, который будет содержать первую главу
из исходного файла.
"""

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# create path to source file
pdf_input_path = Path('Pride_and_Prejudice.pdf')
# create instance for read
input_pdf = PdfReader(pdf_input_path)
# create instance for write
pdf_writer = PdfWriter()

# get page 1 - 3
for page in input_pdf.pages[1:4]:
    # add to pdf_writer
    pdf_writer.add_page(page)

# write to file 'chapter1.pdf'
with Path('chapter1.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)

print('Chapter 1 was written to file "chapter1.pdf"')
