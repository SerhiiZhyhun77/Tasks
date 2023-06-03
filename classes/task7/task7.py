# -*- coding: utf-8 -*-

'''ЗАДАЧА: КЛАСС RetailItem
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите класс под названием RetailItem (Розничная товарная единица), который
содержит данные о товаре в розничном магазине. Этот класс должен хранить
данные в атрибутах: описание товара, количество единиц на складе и цена.
После написания этого класса напишите программу, которая создает три объекта
RetailItem и сохраняет в них приведенные ниже данные.

            Описание                Количество на складе    Цена
Товар №1    Пиджак                          12              59.95
Товар №2    Дизайнерские джинсы             40              34.95
Товар №3    Рубашка                         20              24.95
'''


class RetailItem:

    def __init__(self, description, quantity, price):
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    def __str__(self):
        return f'Product: {self.__description}\n' \
               f'- quantity in stock: {self.__quantity}\n' \
               f'- price: {self.__price}\n\n'


def main():
    product1 = RetailItem('Jacket', 12, 59.95)
    product2 = RetailItem('Designer jeans', 40, 34.95)
    product3 = RetailItem('Shirt', 20, 24.95)
    # Output
    print(product1)
    print(product2)
    print(product3)


if __name__ == '__main__':
    main()
