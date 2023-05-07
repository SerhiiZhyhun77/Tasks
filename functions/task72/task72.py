# -*- coding: utf-8 -*-

'''ЗАДАЧА: ШИФРОВАНИЕ И ДЕШИФРОВАНИЕ ФАЙЛОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая применяет словарь для присвоения "кодов" каждой
букве алфавита. Например:
    codes = {'А': '%', 'а': '9', 'Б': '@', 'б': '#' ...)

Здесь букве А присвоен символ %, букве а - число 9, букве Б - символ @ и т.д.
Программа должна открыть заданный текстовый файл, прочитать его содержимое и
применить словарь для записи зашифрованной версии содержимого файла во второй
файл. Каждый символ по втором файле должен содержать код для соответствующего
символа из первого файла.

Напишите вторую программу, которая открывает зашифрованный файл и показывает
его дешифрованное содержимое на экране.
'''

from codec import *


def main():
    file_name = 'text.txt'
    cipher_file = 'cipher_' + file_name
    # Task 1
    print('Task 1:')
    print(f'Reading file "{file_name}"')
    text = read_text(file_name)
    print('Encrypt the text...')
    ciphertext = code(text)
    print(f'Write chiphertext to the file "{cipher_file}"')
    save_text(cipher_file, ciphertext)
    print()
    # Task 2
    print('Task 2:')
    print(f'Read ciphertext from the file "{cipher_file}"')
    ciphertext = read_text(cipher_file)
    print('Decrypt the text...')
    text = decode(ciphertext)
    print('-' * 75)
    print(text)


def read_text(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as err:
        print(err)
        return ''


def save_text(file_name, text):
    try:
        with open(file_name, 'w') as f:
            f.write(text)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
