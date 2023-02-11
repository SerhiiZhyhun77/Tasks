# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В папке с программой лежат три одностраничных pdf отчета. Програмно создайте из
них один полный отчет и сохраните его в expense_reports.pdf.
"""

from PyPDF2 import PdfMerger
from pathlib import Path

# create instance for merger
pdf_merger = PdfMerger()
# create path to directory
reports_dir = Path.cwd()
# get list of path to pdf files
expense_reports = list(reports_dir.glob('*.pdf'))
# sort path by file name
expense_reports.sort()
# append files to pdf instance
for path in expense_reports:
    pdf_merger.append(path)
    print(f'File "{path.name}" was appended.')
# write file
with Path('expense_reports.pdf').open(mode='wb') as output_file:
    pdf_merger.write(output_file)
print('New file "expense_reports.pdf" was writen.')
