# -*- coding: utf-8 -*-

"""Напишите программу, которая предлагает пользователю ввести целое число. 
Если пользователь ввел что-то другое, программа должна перехватить ошибку 
ValueError и вывести сообщение "Try again."

Когда пользователь задаст целое число, программа должна вывести это число и 
завершить работу без сбоев."""

def main():
    while True:
        try:
            entered = input('Enter an integer (or "q" for quit): ')
            if entered == 'q':
                break
            number = int(entered)
        except ValueError:
            print('Try again.')
        else:
            print(f'You entered an integer {number}')
            break


if __name__ == '__main__':
    main()
