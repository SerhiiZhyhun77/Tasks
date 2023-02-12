# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1. В текущей директории содержатся три файла PDF с именами merge1.pdf,
merge2.pdf и merge3.pdf. Используя экземпляр PdfMerger, выполните слияние
двух файлов merge1.pdf и merge2.pdf методом .append(). Сохраните результат в
файле с именем concatenated.pdf в текущем каталоге.

2. Создайте новый экземпляр PdfMerger и используйте .merge() для слияния
файла merge3.pdf и файла concatenated.pdf из задания 1, вставив merge3.pdf
между двумя страницами concatenated.pdf. Сохраните новый файл в текущем
каталоге с именем merged.pdf.
Результатом должен стать файл PDF из 3 страниц. На первой странице должно
выводиться число 1, на второй - 2 и на третьей - 3.
"""

from pathlib import Path
from PyPDF2 import PdfMerger

# 1
print('Task 1:')
# create instance for merge
pdf_merger = PdfMerger()
# create path to pdf sources
file1_path = Path('merge1.pdf')
file2_path = Path('merge2.pdf')
# append pdf sources to instance
print('Append sources to new pdf')
pdf_merger.append(file1_path)
pdf_merger.append(file2_path)
# write file "concatenated.pdf"
print('Write "concatenated.pdf"')
with Path('concatenated.pdf').open(mode='wb') as output_file:
    pdf_merger.write(output_file)
print('Done!')
print()

# 2
print('Task2:')
# create new instance for merge
pdf_merger = PdfMerger()
# create path to sources
file3_path = Path('merge3.pdf')
concatenated_path = Path('concatenated.pdf')
# append first pdf file
print(f'Append "{concatenated_path.name}" to new pdf')
pdf_merger.append(concatenated_path)
# merge second pdf file on second position
print(f'Merge "{file3_path.name}" on second position')
pdf_merger.merge(1, file3_path)
# write new pdf "merged.pdf"
print('Write "merged.pdf"')
with Path('merged.pdf').open(mode="wb") as output_file:
    pdf_merger.write(output_file)
print('Done!')