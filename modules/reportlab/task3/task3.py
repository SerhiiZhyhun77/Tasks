# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Создайте PDF файл font-colors.pdf:
    размер страницы LETTER,
    шрифт 12pt, Times New Roman,
    4 строки с текстом разного цвета
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import blue, yellow, red, green
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch

canvas = Canvas('font-colors.pdf', pagesize=LETTER)
# Times New Roman, 12
canvas.setFont('Times-Roman', 12)
# blue
canvas.setFillColor('blue')
canvas.drawString(1 * inch, 10 * inch, 'Blue text')
# yellow
canvas.setFillColor('yellow')
canvas.drawString(1 * inch, 9.5 * inch, 'Yellow text')
# red
canvas.setFillColor('red')
canvas.drawString(1 * inch, 9 * inch, 'Red text')
#green
canvas.setFillColor('green')
canvas.drawString(1 * inch, 8.5 * inch, 'Green text')

canvas.save()