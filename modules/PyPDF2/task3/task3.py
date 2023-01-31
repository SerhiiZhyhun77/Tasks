# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущем каталоге находится pdf документ Pride_and_Prejudice.pdf. Сохраните
первую страницу этого документа в отдельном файле с названием first_page.pdf
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# get first page
pdf_path = Path('Pride_and_Prejudice.pdf')
input_pdf = PdfReader(pdf_path)
first_page = input_pdf.pages[0]

# make new pdf and add first page
pdf_writer = PdfWriter()
pdf_writer.add_page(first_page)

# write to the file
with Path('first_page.pdf').open(mode = 'wb') as output_file:
    pdf_writer.write(output_file)