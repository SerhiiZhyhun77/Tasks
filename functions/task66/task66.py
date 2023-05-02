# -*- coding: utf-8 -*-

'''ЗАДАЧА: РАЗДЕЛИТЕЛЬ СЛОВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая на входе принимает предложение, в котором все
слова написаны без пробелов, но первая буква каждого слова находится в
верхнем регистре. Преобразуйте предложение в строковое значение, в котором
слова отделены пробелами, и только первое слово начинается с буквы в верхнем
регистре. Например, строковое значение "ОстановисьИПочувствуйЗапахРоз" будет
преобразовано в "Остановись и почувствуй запах роз".
'''


def splitter(text):
    words = []
    word = ''
    for s in text:
        if s.isupper() and word:
            words.append(word)
            word = ''
        word += s
    # Append last word
    words.append(word)
    return words


def main():
    # Get text
    text = input('Enter your text: ')
    # Split text
    words = splitter(text)
    # Build a sentence
    text = ' '.join(words).capitalize()
    # Output
    print(text)


if __name__ == '__main__':
    main()
