# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Создайте пустую pdf страницу размером 72 пункта на 72 пункта
и сохраните ее в файл blank.pdf в текущем каталоге
"""

from PyPDF2 import PdfWriter
from pathlib import Path

pdf_writer = PdfWriter()
page = pdf_writer.add_blank_page(width = 72, height = 72)

with Path('blank.pdf').open(mode = 'wb') as output_file:
    pdf_writer.write(output_file)