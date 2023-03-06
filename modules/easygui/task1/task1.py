# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу которая демонстрирует взаимодействие с основными элементами
графического интерфейса easygui такими как: msgbox(), buttonbox(), indexbox(
), enterbox(), fileopenbox(), diropenbox() и filesavebox().
"""

import easygui as gui

# msgbox
btn_result = gui.msgbox(
    msg='Hello!',
    title='My first message box',
    ok_button='Click me',
)
print(btn_result)

# buttonbox
btn_result = gui.buttonbox(
    msg='What is your favorite color?',
    title='Choose wisely...',
    choices=('Red', 'Yellow', 'Blue'),
)
print(btn_result)

# indexbox
btn_result = gui.indexbox(
    msg='What are your favorite color?',
    title='Choose wisely...',
    choices=('Red', 'Yellow', 'Blue'),
)
print(btn_result)

# enterbox
btn_result = gui.enterbox(
    msg='What is your favorite color?',
    title='Favorite color',
)
print(btn_result)

# fileopenbox
btn_result = gui.fileopenbox(title='Select a file')
print(btn_result)

# diropenbox
btn_result = gui.diropenbox(title='Select a directory')
print(btn_result)

# filesavebox
btn_result = gui.filesavebox(title='Save as...')
print(btn_result)
