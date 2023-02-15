# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

в текущей директории хранится файл с именем half_and_half.pdf. В нем
содержится часть текста сказки Ганса Христиана Андерсена "The Little Mermaid"
("Русалочка"). Каждая страница файла PDF состоит из двух столбцов.
Разбейте каждую страницу на две, чтобы на ней был опубликован только один
столбец.
Сохраните результат в файл cropped_pages.pdf
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from copy import deepcopy

# function to cut the page into two parts
def crop(page):
    # make 2 deepcopy
    left_page = deepcopy(page)
    right_page = deepcopy(page)
    # set new page coordinates
    left_page.mediabox.upper_right = (
        left_page.mediabox.right / 2,
        left_page.mediabox.top
    )
    right_page.mediabox.upper_left = (
        right_page.mediabox.right / 2,
        right_page.mediabox.top
    )
    return left_page, right_page

# create path to pdf
pdf_path = Path('half_and_half.pdf')
# create pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# iterate pages, cut and add to new pdf
for page in pdf_reader.pages:
    left_page, right_page = crop(page)
    pdf_writer.add_page(left_page)
    pdf_writer.add_page(right_page)
# write new pdf file "cropped_pages.pdf"
with Path('cropped_pages.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
