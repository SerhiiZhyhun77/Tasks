# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Компания Google, Inc. подготовила квартальный отчет, но забыла включить в
него оглавление. Программист заметил ошибку и быстро создал PDF с
отсутствующим оглавлением. Теперь необходимо объединить этот файл PDF с
исходным отчетом "full_report.pdf".

Оба файла PDF - отчет и оглавление - находятся в подкаталоге
quarterly_report/. Отчет хранится в файле report.pdf, а оглавление - в файле
toc.pdf.
"""

from PyPDF2 import PdfMerger
from pathlib import Path

# create instance for merger
pdf_merger = PdfMerger()
# create path to source directory
report_dir = Path.cwd() / 'quarterly_report'
# path to report
report_path = report_dir / 'report.pdf'
# path to toc
toc_path = report_dir / 'toc.pdf'
# append report
print(f'Add "{report_path.name}"')
pdf_merger.append(report_path)
# insert toc in position 1 with merge
print(f'Insert "{toc_path.name}" as 2 page')
pdf_merger.merge(1, toc_path)
# write "full_report.pdf"
print('Write new report "full_report.pdf"')
with Path('full_report.pdf').open(mode='wb') as output_file:
    pdf_merger.write(output_file)
