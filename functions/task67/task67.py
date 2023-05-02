# -*- coding: utf-8 -*-

'''ЗАДАЧА: МОЛОДЕЖНЫЙ ЖАРГОН
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая на входе принимает предложение и преобразует
каждое его слово в "молодежный жаргон". В одной из его версий во время
преобразования слова в молодежный жаргон первая буква удаляется и ставится в
конец слова. Затем в конец слова добавляется слог "ки". Вот пример.

Русский язык: ПРОСПАЛ ПОЧТИ ВСЮ НОЧЬ
Молодежный жаргон: РОСПАЛПКИ ОЧТИПКИ СЮВКИ ОЧЬНКИ
'''


def make_youth_slang(text):
    words = text.split()
    slang_words = []
    for word in words:
        slang_word = word[1:] + word[0] + 'КИ'
        slang_words.append(slang_word.upper())
    return ' '.join(slang_words)


def main():
    text = input('Enter your text: ')
    # Output
    print()
    print('Русский язык: ', text.upper())
    print('Молодежный жаргон: ', make_youth_slang(text))


if __name__ == '__main__':
    main()
