# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Откройте pdf файл из текущей директории Pride_and_Prejudice.pdf
    1. Получите количество страниц в этом файле
    2. Получите все метаданные файла
    3. Получите заголовок документа title
    4. Получите текст первой страницы
    5. Запишите в новый текстовый файл:
        - Заголовок документа
        - Количество страниц
        - Весь текст
"""

import PyPDF2, pathlib

# creater path to pdf
pdf_path = pathlib.Path.cwd() / 'Pride_and_Prejudice.pdf'
# create pdf instance
print('Create pdf instance')
pdf = PyPDF2.PdfReader(pdf_path)

# 1
# get num pages
num_pages = len(pdf.pages)
print(f'This file has {num_pages} pages')

# 2
# get metadata
print(f'\nMetadata: \n{pdf.metadata}\n')

# 3
# get title
title = pdf.metadata.title
print(f'Title: "{title}"')

# 4
# get first page
first_page = pdf.pages[0]
# get text from first page
print('First page:')
print('*' * 50)
text = first_page.extract_text()
print(text)

# 5
# path to output_file
output_file_path = pathlib.Path.cwd() / 'Pride_and_Prejudice.txt'
with output_file_path.open(mode = 'w', encoding = 'utf-8') as output_file:
    print('*' * 50)
    print('Write title, num page and text to new file:')
    print(str(output_file_path))
    output_file.write(f'{title} \nNumber of pages: {num_pages} \n\n')
    # write all text
    for page in pdf.pages:
        text = page.extract_text()
        output_file.write(text)
