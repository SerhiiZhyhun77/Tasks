# -*- coding: utf-8 -*-

"""ЗАДАЧА: ПРИСТУП ВДОХНОВЕНИЯ
Напишите программу, которая генерирует стихи.

Создайте пять списков для разных типов слов:
    1. Существительные: ['fossil', 'horse', 'aardvark', 'judge', 'chef',
        'mango', 'extrovert', 'gorilla']
    2. Глаголы: ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes',
        'curdles']
    3. Прилагательные: ['furry', 'balding', 'incredulous', 'fragrant', 
        'exuberant', 'glistening']
    4. Предлоги: ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in',
        'like', 'over', 'within']
    5. Наречия: ['curiously', 'extravagantly', 'tantalizingly', 'furiously',
        'sensuously']

Случайным образом выберите следующее количество элементов из каждого списка:
    - три существительных;
    - три глагола;
    - три прилагательных;
    - два предлога;
    - одно наречие.

Для этого можно воспользоваться функцией choice() из модуля random. Она 
получает список и возвращает случайно выбранный элемент списка.

Используя случайно выбранные слова, сгенерируйте и выведите стихотворение, 
структура которого аналогична стилю Клиффорда Пиковера:
{A/An} {прил1} {сущ1}

{A/An} {прил1} {сущ1} {гл1} {предл1} the {прил2} {сущ2}
{нареч1}, the {сущ1} {гл2}
the {сущ2} {гл3} {предл2} a {прил3} {сущ3}

При каждом запуске программы должно генерироваться новое стихотворение.
"""


import random


nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 
        'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 
        'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 
        'exuberant', 'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 
        'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 
        'sensuously']

nouns_pool = []
verbs_pool = []
adjectives_pool = []
prepositions_pool = []
adverbs_pool = []


def get_words_from_list(amount, lst):
    words = []
    for i in range(amount):
        word = random.choice(lst)
        words.append(word)
    return words


def get_words():
    global nouns_pool, verbs_pool, adjectives_pool, prepositions_pool, \
            adverbs_pool
    # get 3 nouns
    nouns_pool = get_words_from_list(3, nouns)
    # get 3 verbs
    verbs_pool = get_words_from_list(3, verbs)
    # get 3 adjectives
    adjectives_pool = get_words_from_list(3, adjectives)
    # get 2 prepositions
    prepositions_pool = get_words_from_list(2, prepositions)
    # get 1 adverb
    adverbs_pool = get_words_from_list(1, adverbs)


def main():
    #get pool of words
    get_words()
    #output rhyme
    print(f'A/An {adjectives_pool[0]} {nouns_pool[0]}')
    print()
    print(f'A/An {adjectives_pool[0]} {nouns_pool[0]} {verbs_pool[0]} ' \
          f'{prepositions_pool[0]} the {adjectives_pool[1]} {nouns_pool[1]}')
    print(f'{adverbs_pool[0]}, the {nouns_pool[0]} {verbs_pool[1]}')
    print(f'the {nouns_pool[1]} {verbs_pool[2]} {prepositions_pool[1]} a ' \
          f'{adjectives_pool[2]} {nouns_pool[2]}')

if __name__ == '__main__':
    main()
