# -*- coding: utf-8 -*-

'''ЗАДАЧА: МАГИЧЕСКИЙ ШАР
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, моделирующую магический шар, т.е. игрушку, которая
предсказывает и дает случайный ответ на общий вопрос, требующий ответа "да"
или "нет". У вас есть файл 8_ball_responses.txt - этот файл содержит 12
ответов, в частности: "Не думаю", "Да, конечно!", "Не уверен" и т.д.
Программа должна прочитать ответы из файла в список, предложить пользователю
задать вопрос и затем показать один из ответов, отобранных из списка
случайным образом. Программа должна продолжать работу до тех пор,
пока пользователь не будет готов из нее выйти.

Содержимое файла 8_ball_responses.txt:
Да, конечно!
Без сомнения, да.
Вы можете на это рассчитывать.
Наверняка!
Спросите меня позже.
Не уверен.
Я не могу сказать вам прямо сейчас.
Я отвечу вам после того, как вздремну.
Ни за что!
Не думаю.
Без сомнения, нет.
Совершенно очевидно, что нет!
'''

from random import choice

# read answers from file to list
def read_answ_to_list():
    answ_lst = []
    try:
        f = open('8_ball_responses.txt', 'r', errors='ignore')
        answ_lst = [line.strip() for line in f]
    except Exception as err:
        print(err)
    else:
        f.close()
    return answ_lst

def main():
    # get answers from file
    answ_lst = read_answ_to_list()
    print('Ask any question and I will try to answer it.')
    while True:
        # get question from user and check it
        question = input('(question): ')
        if not question.strip():
            print('You didn\'t ask a question.')
            print()
            continue
        # output answer
        print('(answer):', choice(answ_lst))
        print()
        # offer to repeat
        more = input('Want more? (press any key or n - to exit): ')
        if more.casefold() == 'n':
            break
        print()

if __name__ == '__main__':
    main()
