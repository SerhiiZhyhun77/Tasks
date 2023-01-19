# -*- coding: utf-8 -*-

"""Напишите программу, которая предлагает пользователю ввести строку и целое
число n, а затем выводит символ с индексом n во введенной строке.

Используйте механизм обработки ошибок для того, чтобы предотвратить аварийное 
завершение программы, если пользователь задаст что-то кроме целого числа или 
или если индекс выходит за границы массива. Программа должна выводить разные 
сообщения об ошибках в зависимости от типа ошибки."""

def main():
    text = input('Enter any text string: ')
    while True:
        try:
            entered = input('Enter an integer for getting simbol from text ' \
                    '(or "q" for quit): ')
            if entered == 'q':
                break
            index = int(entered)
            symbol = text[index]
        except ValueError:
            print('It is not an integer! Try again.')
        except IndexError:
            print('You integer is longer than the string! Try again.')
        else:
            print(f'Symbol "{symbol}"')
            break


if __name__ =='__main__':
    main()
