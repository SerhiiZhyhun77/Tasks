# -*- coding: utf-8 -*-

'''ЗАДАЧА: УНИКАЛЬНЫЕ СЛОВА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая открывает заданный текстовый файл и затем
показывает список всех уникальных слов в файле. (Подсказка: храните слова в
качестве элементов множества.)
'''


def main():
    file_name = 'text.txt'
    text = read_text(file_name)
    words = get_words(text)
    output(words)


def output(words):
    # Output words in 5 columns
    counter = 0
    for word in words:
        print(f'{word:<20}', end='')
        counter += 1
        if counter >= 5:
            print()
            counter = 0


def get_words(text):
    text = text.replace("\"", '')  # Remove double quotes
    words = text.split()
    clean_words = set()
    for word in words:
        clean_word = ''
        for s in word:
            if s.isalpha() or s == "'":
                clean_word += s
        if clean_word:
            clean_words.add(clean_word.lower())
    return sorted(list(clean_words))


def read_text(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as err:
        print(err)
        return ""


if __name__ == '__main__':
    main()
