# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.В текущей директории находится PDF файл newsletter.pdf. Добавьте парольную
защиту к файлу:
    user_password - задает пароль пользователя, позволяющий открыть и
    прочитать файл PDF.
    owner_password - задает пароль владельца, позволяющий открыть файл PDF
    без каких-либо ограничений, включая редактирование.
Сохраните зашифрованные данные PDF в выходной файл newsletter_protected.pdf

2.Дешифруйте файл созданный в предыдущем задании и сохраните его в
незащифрованом виде с названием newsletter_unprotected.pdf
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# 1
print('Task 1:')
# path to pdf
pdf_path = Path('newsletter.pdf')
# create pdf instances
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# append all pages from reader to writer
pdf_writer.append_pages_from_reader(pdf_reader)
print('Read')
# passwords for user and owner
user_password = 'SuperSecret'
owner_password = 'ReallySuperSecret'
# encrypt pdf with passwords
pdf_writer.encrypt(user_password=user_password, owner_password=owner_password)
print('Protect with a password')
# write new pdf to file "newsletter_protected.pdf"
with Path('newsletter_protected.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
    print('Write protected pdf to file "newsletter_protected.pdf"')
print()

# 2
print('Task 2:')
# path to pdf
pdf_path = Path('newsletter_protected.pdf')
# create pdf instance
pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()
# decrypt
pdf_reader.decrypt(password="SuperSecret")
print('Decript pdf')
# append all pages to new pdf
pdf_writer.append_pages_from_reader(pdf_reader)
print('Read all pages')
# write new pdf to file "newsletter_unprotected.pdf"
with Path('newsletter_unprotected.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)
    print('Write unprotected pdf to file "newsletter_unprotected.pdf"')
