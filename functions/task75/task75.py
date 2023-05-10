# -*- coding: utf-8 -*-

'''ЗАДАЧА: АНАЛИЗ ФАЙЛА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая читает содержимое двух текстовых файлов и
сравнивает их следующим образом:
    - показывает список всех уникальных слов, содержащихся в обоих файлах;
    - показывает список слов, входящий в оба файла;
    - показывает список слов из первого файла, не входящих во второй;
    - показывает список слов из второго файла, не входящих в первый;
    - показывает список слов, входящих либо в первый, либо во второй файл,
    но не входящих в оба файла одновременно.

Подсказка: для выполнения этого анализа используйте операции над множествами.
'''


def main():
    # Get unique words from files
    words1 = get_words_from_file('text1.txt')
    words2 = get_words_from_file('text2.txt')
    # List of all unique words from text1.txt
    print('List of all unique words from file "text1.txt":')
    output(words1)
    # List of all unique words from text2.txt
    print('List of all unique words from file "text2.txt":')
    output(words2)
    # List of all unique words
    print('List of all unique words contained in both files:')
    output(words1 | words2)
    # List of words from the first file that are not included in the second
    print('List of words from the first file that are not included in the '
          'second:')
    output(words1 - words2)
    # List of words from the second file that are not included in the first
    print('List of words from the second file that are not included in the '
          'first:')
    output(words2 - words1)
    # List of words in either the first or second file, but not in both files
    # at the same time
    print('List of words in either the first or second file, but not in both '
          'files at the same time')
    output(words1 ^ words2)


def get_words_from_file(file_name):
    text = read_file(file_name)
    text = clear_text(text)
    words = get_words(text)
    return words


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as err:
        print(err)
        return ''


def clear_text(text):
    text = text.replace('\n', ' ')
    text = text.replace('"', ' ')
    new_text = ''
    for s in text:
        if s.isalpha() or s.isspace() or s == "'":
            new_text += s
    return new_text.lower()


def get_words(text):
    words = text.split()
    return set(words)


def output(words):
    counter = 0
    words = list(words)
    words.sort()
    print('-' * 75)
    for word in words:
        if counter >= 4:
            print()
            counter = 0
        print(word.ljust(15), end='')
        counter += 1
    print()
    print()


if __name__ == '__main__':
    main()
