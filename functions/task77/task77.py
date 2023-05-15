# -*- coding: utf-8 -*-

'''ЗАДАЧА: СЛОВАРНЫЙ ИНДЕКС
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая читает содержимое текстового файла. Программа
должна создать словарь, а котором пары "ключ : значение" описаны следующим
образом:
    - ключ - ключами являются отдельные слова в файле;
    - значение - каждое значение является списком, который содержит номера
    строк в файле, где найдено слово (ключ).

Например, предположим, что слово "робот" найдено в строках 7, 18, 94 и 138.
Словарь будет содержать элемент, в котором ключом будет строковое значение
"робот", а значением - список, содержащий номера 7, 18, 94 и 138.

После создания словаря программа должна создать еще один текстовый файл,
называемый словарным индексом, в котором приводится содержимое словаря.
Словарный индекс должен содержать список слов в алфавитном порядке,
хранящихся в словаре в качестве ключей, и номера строк, в которых эти слова
встречаются в исходном файле.
'''


def main():
    file_name = 'text.txt'
    output_file_name = 'word_index.txt'
    # Read file and get words and lines
    print('Reading file "%s"' % file_name)
    words, lines = get_words_and_lines_from_file(file_name)
    # Analysis and dict building
    print('Analyzing...')
    word_index = make_word_index(words, lines)
    # Save dict to file
    print('Saving the result to a file "%s"' % output_file_name)
    save_to_file(word_index, output_file_name)


def save_to_file(word_index, output_file_name):
    word_index_lst = list(word_index.items())
    word_index_lst.sort(key=lambda x: x[0])
    with open(output_file_name, 'w') as f:
        for word, line_nums in word_index_lst:
            if line_nums:
                line_nums = ' '.join(map(str, line_nums))
            f.write(f'{word}: {line_nums}\n')


def make_word_index(words, lines):
    word_index = dict.fromkeys(words, None)
    for word in words:
        for i, line in enumerate(lines, 1):
            if line.find(' ' + word + ' ') != -1 or \
                    line.startswith(word + ' ') or \
                    line.endswith(' ' + word):
                if word_index[word] is None:
                    word_index[word] = [i]
                else:
                    word_index[word].append(i)
    return word_index


def get_words_and_lines_from_file(file_name):
    text = get_text_from_file(file_name)
    text = text.lower()
    text = clear_text(text)
    lines = text.splitlines()
    lines = [line.strip() for line in lines]
    words = set(text.split())
    return words, lines


def clear_text(text):
    text = text.replace('"', ' ')
    clean_text = ''
    for s in text:
        if s.isalnum() or s.isspace() or s == "'":
            clean_text += s
        else:
            clean_text += ' '
    return clean_text


def get_text_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as err:
        print(err)
        return ''


if __name__ == '__main__':
    main()
