# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущей директории создайте новый PDF файл hello.pdf с текстом "Hello, World!"
который должен быть расположен в левом нижнем углу на расстоянии 72 пункта от
левой и нижней стороны. Размер страницы формата LETTER (8.5 x 11)
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

# create canvas, set filename and pagesize
canvas = Canvas('hello.pdf', pagesize=LETTER)
# draw string
canvas.drawString(72, 72, "Hello, World!")
# write file
canvas.save()
