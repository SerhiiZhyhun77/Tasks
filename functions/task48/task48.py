# -*- coding: utf-8 -*-

'''ЗАДАЧА: ПРОВЕРКА ДОПУСТИМОСТИ НОМЕРА РАСХОДНОГО СЧЕТА
[Начинаем программировать на Python. Тони Гэддис (2022)]

В файле charge_accounts.txt содержится список допустимых номеров расходных
счетов компании. Каждый номер счета представляет собой семизначное число,
в частности 5658845.

Напишите программу, которая считывает содержимое файла в список. Затем она
должна попросить пользователя ввести номер расходного счета. Программа должна
определить, что номер является допустимым, путем его поиска в списке. Если
число в списке имеется, то программа должна вывести сообщение, указывающее на
то, что номер допустимый. Если числа в списке нет, то программа должна
вывести сообщение, указывающее на то, что номер недопустимый.
'''

def get_account_num_lst():
    account_num_lst = []
    try:
        f = open('charge_accounts.txt', 'r')
        for num in f:
            account_num_lst.append(num.strip())
        return account_num_lst
    except Exception as err:
        print(err)

def main():
    account_num_lst = get_account_num_lst()
    account_num = input('Enter the account number (seven-digit number): ')
    if account_num in account_num_lst:
        print('Number valid')
    else:
        print('Number invalid')

if __name__ == '__main__':
    main()
