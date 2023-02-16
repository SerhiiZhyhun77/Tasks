# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.В текущей директории находится файл PDF с именем top_secret.pdf.
Зашифруйте файлс паролем пользователя Unguessable, используя метод
PdfWriter.encrypt().
Сохраните зашифрованный файл с именем top_secret_encrypted.pdf

2.Откройте файл top_secret_encrypted.pdf, созданный в упражнении 1,
расшифруйте его и выведите текст, содержащийся на первой странице PDF.
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# 1
print('Task 1:')
# path to pdf
pdf_path = Path('top_secret.pdf')
# create pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# append all page to new pdf
pdf_writer.append_pages_from_reader(pdf_reader)
print('Add all page to new pdf')
# encrypt with password
pdf_writer.encrypt(user_password="Unguessable")
print('Encrypt with password')
# write protected file
with Path('top_secret_encrypted.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
    print('Write new pdf to file "top_secret_encrypted.pdf"')
print()

# 2
print('Task 2:')
# path to pdf
pdf_path = Path('top_secret_encrypted.pdf')
# create pdf instance
pdf_reader = PdfReader(pdf_path)
# decrypt pdf with password
pdf_reader.decrypt(password='Unguessable')
print('Decrypt file with password')
# get first page
first_page = pdf_reader.pages[0]
print('Get first page')
# get text from page
print('Get text from first page')
text = first_page.extract_text()
print('\nHere we go! ->\n')
print(text)