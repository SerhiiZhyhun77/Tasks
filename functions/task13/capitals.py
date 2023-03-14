# -*- coding: utf-8 -*-

""" ЗАДАЧА: ЦИКЛ ПО СТОЛИЦАМ

Сначала заполните словарь названиями штатов и их столиц и сохраните в файле 
capitals.py:

capitals_dict = {
    'Alabama' : 'Montgpmery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
}

Затем выберите из словаря случайное название штата и присвойте название штата 
и его столицы двум переменным. Первой строкой кода своей программы 
импортируйте модуль random.

Затем выведите название штата и предложите пользователю указать столицу. Если 
пользователь задал неправильный ответ, повторяйте вопрос, пока пользователь не 
ответит правильно или не введет команду "exit" для завершения. Если 
пользователь ответил правильно, выведите сообщение "Correct" и завершите 
программу. Но если пользователь завершает программу без указания правильного 
ответа, выведите проавильный ответ и слово "Goodbye".

Проследите за тем, чтобы пользователь не пострадал из-за регистра символов. 
Другими словами, ответ "Denver" считается идентичным "denver". Сделайте 
то же самое для команды выхода - "EXIT" и "Exit" должны работать точно так 
же, как и "exit".
"""

import random


capitals_dict = {
    'Alabama' : 'Montgpmery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
}


def get_rand_state_capital():
    return random.choice(list(capitals_dict.items()))


def main():
    state, capital = get_rand_state_capital()
    print('To exit type "exit"')
    print(f'What is the name of the state capital of {state}?')
    result = False
    while not result:
        text = input().lower()
        if text == 'exit':
            print('Goodbye')
            break
        if text == capital.lower():
            result = True
        else:
            print('Not correct. Try again!')
    else:
        print('Correct')


if __name__ == '__main__':
    main()
