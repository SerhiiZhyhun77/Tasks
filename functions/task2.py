# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите функцию greet(), которая получает один строковый параметр с именем
name и выводит текст "Hello, <name>!", где <name> заменяется значением параметра
name."""

def greet(name):
    print("Hello, {}!".format(name))
  
  
def main():
    name = input('What is your name? ')
    greet(name)


if __name__ == '__main__':
    main()