# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Используя команду continue, напишите программу, которая перебирает числа от 1 до
 50 и выводит все числа, не кратные 3.
 """
 
def is_multiple_of_3(number):
   if not number % 3:
       return True
   else:
       return False

def main():
    for number in range(50):
        if not is_multiple_of_3(number):
            print(number)


if __name__ == '__main__':
    main()