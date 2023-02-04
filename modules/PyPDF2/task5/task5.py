# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1. Извлеките последнюю страницу из файла Pride_and_Prejudice.pdf, который
находится в текущем каталоге и сохраните ее в файле last_page.pdf.
2. Извлеките из файле Pride_and_Prejudice.pdf все страницы с четными индексами
(не номерами страниц!) и сохраните их в новом файле every_other_page.pdf
3. Разбейте файл Pride_and Prejudice.pdf на два новых файла PDF. Первый должен
содержать первые 150 страниц,а второй - все оставщиеся страницы. Сохраните
оба файла в домашнем каталоге с именами part_1.pdf и part_2.pdf
"""

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# create path
pdf_path = Path('Pride_and_Prejudice.pdf')
# create pdf instance
pdf = PdfReader(pdf_path)
# create writer
writer = PdfWriter()

# 1
# get last page
page = pdf.pages[-1]
writer.add_page(page)
# write page to the file last_page.pdf
with Path('last_page.pdf').open(mode='wb') as file:
    writer.write(file)
print('Task 1 complited.')
print('\tFile "last_page.pdf" created.')

# 2
# create new writer
writer = PdfWriter()
# get pages with even indexes
for page in pdf.pages[::2]:
    writer.add_page(page)
# write pages to the file every_other_page.pdf
with Path('every_other_page.pdf').open(mode='wb') as file:
    writer.write(file)
print('Task 2 complited.')
print('\tFile "every_other_page.pdf" created.')

# 3
# create new writers
writer_part_1 = PdfWriter()
writer_part_2 = PdfWriter()
# create writer for part 1: pages 0 - 150
for page in pdf.pages[:150]:
    writer_part_1.add_page(page)
# create writer for part 2: pages 151 - END
for page in pdf.pages[150:]:
    writer_part_2.add_page(page)
# write pages part_1 to the file part_1.pdf
with Path('part_1.pdf').open(mode='wb') as file:
    writer_part_1.write(file)
# write pages part_2 to the file part_2.pdf
with Path('part_2.pdf').open(mode='wb') as file:
    writer_part_2.write(file)
print('Task 3 complited.')
print('\tFile "part_1.pdf" created.')
print('\tFile "part_2.pdf" created.')