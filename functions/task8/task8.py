# -*- coding: utf-8 -*-

"""
МОДЕЛИРОВАНИЕ ЭКСПЕРИМЕНТА С БРОСКОМ МОНЕТЫ
Допустим, вы многократно бросаете симметричную монету, пока орел и решка не
выпадут хотя бы по одному разу. Другими словами, после первого броска вы 
продолжаете бросать монету, пока она не упадет другой стороной вверх.
Бросая монету, вы получаете последовательность орлов и решек. Например, при 
первом проведении эксперимента (в первой попытке) вы можете получить 
последовательность "орел, орел, решка".

Сколько в среднем понадобиться бросков, чтобы в последовательности оказались 
как орел, так и решка?

Напишите программ для моделирования ситуации, когда эксперимент составляют 
10000 попыток и надо вывести среднее число подбрасываний монеты в каждой 
попытке."""

import random


def coin_flip():
    if random.randint(0, 1):
        return 'heads'
    else:
        return 'tails'


def case_coin_flip():
    heads = 0
    tails = 0
    counter = 0
    coin_flips = []
    while not heads or not tails:
        if coin_flip() == 'heads':
            heads += 1
            coin_flips.append('heads')
        else:
            tails += 1
            coin_flips.append('tails')
        counter += 1
    return counter


def main():
    NUMBER_OF_CASES = 10000
    summ  = 0
    for i in range(NUMBER_OF_CASES):
        summ += case_coin_flip()
    average = summ / NUMBER_OF_CASES
    print(f'Average number of tosses: {average}')


if __name__ == '__main__':
    main()

