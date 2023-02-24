# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Создайте PDF файл font-exemple.pdf:
    страница - размер LETTER,
    4 строки написанные разными видами шрифта Times New Roman,
    шрифт 18pt
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER

canvas = Canvas('font-example.pdf', pagesize=LETTER)

# Times New Roman
canvas.setFont('Times-Roman', 18)
canvas.drawString(1 * inch, 10 * inch, 'Times New Roman (18pt)' )
# Times New Roman Italic
canvas.setFont('Times-Italic', 18)
canvas.drawString(1 * inch, 9.5 * inch, 'Times New Roman Italic (18pt)')
# Times New Roman Bold
canvas.setFont('Times-Bold',18)
canvas.drawString(1 * inch, 9 * inch, 'Times New Roman Bold (18pt)')
# Times New Roman Bold Italic
canvas.setFont('Times-BoldItalic', 18)
canvas.drawString(1 * inch, 8.5 * inch, 'Times New Roman Bold Italic (18pt)')

canvas.save()