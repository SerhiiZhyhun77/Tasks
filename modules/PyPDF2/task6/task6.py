# -*- coding: utf-8 -*-

"""ЗАДАЧА: КЛАСС PdfSplitter
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Создайте класс с именем PdfSplitter, который читает данные из файла PDF из
существующего экземпляра класса PdfReader и разбивает их на два новых объекта
PDF. При создании экземпляра класа должна передаваться строка пути.
Например, следующая команда создает экземпляр PdfSplitter на основе файла PDF
mydoc.pdf в текущем каталоге:

pdf_splitter = PdfSplitter('mydoc.pdf')

Класс PdfSplitter должен содержать два метода.
    1. Метод .split() получает один параметр breakpoint, в котором передается
    целое число - номер страницы, которая становится последней в первой части
    разбиваемого файла PDF.
    2. Метод .write() получает один параметр filename, в котором передается
    строка пути.

После вызова .split() класс PdfSplitter должен содержать атрибут .writer1,
которому присваивается экземпляр PdfWriter со всеми страницами исходного
файла PDF до страницы breakpoint (не включая ее). Также должен присутствовать
атрибут .writer2, которому присваивается экземпляр PdfWriter с остальными
страницами исходного файла PDF.

При вызове .write() записываются два файла PDF - первый с именем filename +
'_1.pdf', а второй с именем filename + '_2.pdf'.

В следующем примере файл mydoc.pdf разделяется на две части, первая из
которых заканчивается страницей 4,а результаты разбиения записываются в два
файла с именами mydoc_split_1.pdf и mydoc_split_2.pdf:

pdf_splitter.split(breakpoint=4)
pdf_splitter.write('mydoc_split')

"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

class PdfSplitter:

    def __init__(self, file):
        # path to the file
        self.file_path = Path(file)
        # create instance pdf
        self.pdf = PdfReader(self.file_path)

    def split(self, breakpoint):
        """Split the pdf into two parts. The first part before the breakpoint
        is stored in writer1. The rest is stored in writer2"""
        # create instance writer1
        self.writer1 = PdfWriter()
        # create instance writer2
        self.writer2 = PdfWriter()

        # check breakpoint
        if type(breakpoint) != int:
            print('TypeError breakpoint!')
            return

        # create part1 (before breakpoint) and store in writer1
        for page in self.pdf.pages[:breakpoint]:
            self.writer1.add_page(page)
        # create part2 (after breakpoint) and store in writer2
        for page in self.pdf.pages[breakpoint:]:
            self.writer2.add_page(page)

    def write(self, filename):
        """Writes parts of a pdf to a files"""
        with Path(filename + '_1.pdf').open(mode='wb') as file:
            self.writer1.write(file)
        with Path(filename + '_2.pdf').open(mode='wb') as file:
            self.writer2.write(file)


def main():
    # create an instance PdfSplitter
    print('Reading a pdf file.')
    pdf_splitter = PdfSplitter('Pride_and_Prejudice.pdf')
    # split pdf
    print('Spliting.')
    pdf_splitter.split(breakpoint=4)
    # write to a file
    print('Writing files.')
    pdf_splitter.write('PaP_split')

if __name__ == '__main__':
    main()
    