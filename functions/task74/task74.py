# -*- coding: utf-8 -*-

'''ЗАДАЧА: ЧАСТОТА СЛОВА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая считывает содержимое текстового файла. Она должна
создать словарь, а котором ключами являются отдельные слова в файле,
а значениями - количество появлений каждого слова. Например, если слово "это"
появляется 128 раз, то словарь должен содержать элемент с ключом "это" и
значением 128. Программа должна либо показать частотность каждого слова,
либо создать второй файл, содержащий список слов и их частот.
'''


def main():
    file_name = 'text.txt'
    text = read_file(file_name)
    text = clear_text(text)
    words_number = count_words(text)
    save_to_file(words_number)


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
    clear_text = ''
    for s in text:
        if s.isalpha() or s.isspace() or s == "'":
            clear_text += s
    return clear_text


def count_words(text):
    words_number = {}
    words_lst = text.split()
    for word in words_lst:
        if word not in words_number:
            word = word.lower()
            words_number.setdefault(word, 1)
        else:
            words_number[word] += 1
    return words_number


def save_to_file(words_number):
    try:
        with open('frequency of words.txt', 'w') as f:
            for word, freq in words_number.items():
                f.write(f'{word}: {freq}\n')
            print('Frequency of words saved in file "frequency of words.txt"')
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
