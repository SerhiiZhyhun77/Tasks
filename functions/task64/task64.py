# -*- coding: utf-8 -*-

'''ЗАДАЧА: ГЛАСНЫЕ И СОГЛАСНЫЕ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу с функцией, которая в качестве аргумента принимает
строковое значение и возвращает количество содержащихся в нем гласных.
Приложение должно иметь еще одну функцию, которая в качестве аргумента
принимает строковое значение и возвращает количество содержащихся в нем
согласных. Приложение должно предоставить пользователю возможность ввести
строковое значение и показать содержащееся в нем количество гласных и согласных.
'''

def vowel_count(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for s in text:
        if s.lower() in vowels:
            counter += 1
    return counter

def consonant_count(text):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
                  'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    counter = 0
    for s in text:
        if s.lower() in consonants:
            counter += 1
    return counter

def main():
    text = input('Enter your text: ')
    # Output
    print('In the text:')
    print(f'- vowels: {vowel_count(text)}')
    print(f'- consonants: {consonant_count(text)}')

if __name__ == '__main__':
    main()
