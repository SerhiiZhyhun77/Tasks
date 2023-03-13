# -*- coding: utf-8 -*-

"""ЗАДАЧА: ВОЗВРАЩЕНИЕ ПОЭТА
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите GUI-приложение, генерирующее стихи. Вы можете использовать любой
менеджер геометрии на свое усмотрение, но приложение должно удовлетворять
всем требованиям из следующего списка.
    1.Пользователь должен ввести правильное количество слов в каждом виджете
    Entry:
    - не менее трех существительных;
    - не менее трех глаголов;
    - не менее трех прилагательных;
    - не менее трех предлогов;
    - хотя бы одно наречие.

    Если в каком-либо из виджетов Entry введено слишком мало слов,
    в той области, где выводится сгенерированное стихотворение, должно
    выводиться сообщение об ошибке.

    2.Программа должна случайным образом выбрать из пользовательского ввода
    три существительных, три глагола, три прилагательных и три предлога,
    а также одно наречие.

    3.Программа должна сгенерировать стихотворение по следующему шаблону:
    {A/An} {прил1} {сущ1}

    {A/An} {прил1} {сущ1} {гл1} {пред1} the {прил2} {сущ2}
    {нареч1}, the {сущ1} {гл2}
    the {сущ2} {гл3} {пред2} a {прил3} {сущ3}

    4.Приложение должно предоставить пользователю возможность экспорта
    стихотворения в файл.

    5.Дополнительное задание: удостоверьтесь, что пользователь вводит в
    виджетах Entry уникальные слова. Например,если пользователь введет одно и
    то же существительное в виджете Entry дважды, то при попытке
    сгенерировать стихотворение приложение должно вывести сообщение об ошибке.
"""

import tkinter as tk
from tkinter.filedialog import asksaveasfilename

msg = ''

# checking uniqueness
def check_uniqueness(lst):
    global msg
    if len(lst) == len(set(lst)):
        return True
    else:
        msg = '\nE R R O R !\n\n Words must be unique!'
        return False

# checking amount
def check_amount(widj, lst):
    global msg
    amount = {
        ent_nouns : 3,
        ent_verbs : 3,
        ent_aject : 3,
        ent_prepos : 3,
        ent_adverbs : 1
    }
    if amount[widj] <= len(lst):
        return True
    else:
        msg = """
        E R R O R !
        
        You must enter:
        - at least three nouns;
        - at least three verbs;
        - at least three adjectives;
        - at least three prepositions;
        - at least one adverb.
        """
        return False

# clearing words
def clear(lst):
    if lst == ['']:
        lst=[]
    return [s.strip() for s in lst]

# getting words from entry
def get_values(widj):
    values = widj.get().split(',')
    values = clear(values)
    # check amount
    checked = check_amount(widj, values)
    # check uniqueness
    if checked:
        checked = check_uniqueness(values)
    return values, checked

# generate btn click
def generate():
    # get all words from all entries
    widj_lst = [ent_nouns, ent_verbs, ent_aject, ent_prepos, ent_adverbs]
    words_lst = []
    for widj in widj_lst:
        words, checked = get_values(widj)
        # if the check fails, show an error and return
        if not checked:
            lbl_output['text'] = msg
            return
        words_lst.append(words)
    # make a poem
    poem = 'Your poem:\n\n' \
        f'A {words_lst[2][0]} {words_lst[0][0]}\n\n' \
        f'A {words_lst[2][0]} {words_lst[0][0]} {words_lst[1][0]} ' \
        f'{words_lst[3][0]} the {words_lst[2][1]} {words_lst[0][1]}\n' \
        f'{words_lst[4][0]}, the {words_lst[0][0]} {words_lst[1][1]}\n' \
        f'the {words_lst[0][1]} {words_lst[1][2]} {words_lst[3][1]} ' \
        f'a {words_lst[2][2]} {words_lst[0][2]}'
    # output to label
    lbl_output['text'] = poem

# save btn click
def save_to_file():
    # get path to place to save file
    file_path = asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    # if canceled
    if not file_path:
        return
    # write text to file
    with open(file_path, 'w') as output_file:
        text = lbl_output['text']
        output_file.write(text)

# create window
window = tk.Tk()
# set title
window.title('Make your own poem!')

# create frames
frm_title = tk.Frame(window)
frm_input = tk.Frame(window)
frm_gen_button = tk.Frame(window)
frm_output = tk.Frame(window, relief=tk.SUNKEN, borderwidth=3)

# configure window and frames
window.columnconfigure(0, weight=1)
window.rowconfigure(3, weight=1)
frm_input.columnconfigure(0, weight=0, minsize=100)
frm_input.columnconfigure(1, weight=1, minsize=400)
frm_output.rowconfigure(0, weight=1, minsize=180)
frm_output.columnconfigure(0, weight=1, minsize=400)

# TITLE FRAME
# title label
lbl_title = tk.Label(
    frm_title,
    text='Enter your favorite words, separated by commas.'
)
lbl_title.pack()

# INPUT FRAME
# labels
lbl_nouns = tk.Label(frm_input, text='Nouns:')
lbl_verbs = tk.Label(frm_input, text='Verbs:')
lbl_aject = tk.Label(frm_input, text='Ajectives:')
lbl_prepos = tk.Label(frm_input, text='Prepositions:')
lbl_adverbs = tk.Label(frm_input, text='Adverbs:')
# entries
ent_nouns = tk.Entry(frm_input)
ent_verbs = tk.Entry(frm_input)
ent_aject = tk.Entry(frm_input)
ent_prepos = tk.Entry(frm_input)
ent_adverbs = tk.Entry(frm_input)
# positioning labels on the frame
lbl_nouns.grid(row=0, column=0, sticky='e')
lbl_verbs.grid(row=1, column=0, sticky='e')
lbl_aject.grid(row=2, column=0, sticky='e')
lbl_prepos.grid(row=3, column=0, sticky='e')
lbl_adverbs.grid(row=4, column=0, sticky='e')
# positioning entries on the frame
ent_nouns.grid(row=0, column=1, sticky='ew')
ent_verbs.grid(row=1, column=1, sticky='ew')
ent_aject.grid(row=2, column=1, sticky='ew')
ent_prepos.grid(row=3, column=1, sticky='ew')
ent_adverbs.grid(row=4, column=1, sticky='ew')

# BUTTON FRAME
# generate button
btn_gen = tk.Button(frm_gen_button, text='Generate', command=generate)
btn_gen.pack()

# OUTPUT FRAME
# output label
lbl_output = tk.Label(frm_output)
lbl_output.grid(row=0, column=0, pady=(10,0), sticky='n')
# save to file button
btn_save = tk.Button(frm_output, text='Save to file', command=save_to_file)
btn_save.grid(row=1, column=0, pady=5)

# positioning frame on the window
frm_title.grid(row=0, column=0, pady=5)
frm_input.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
frm_gen_button.grid(row=2, column=0, pady=10)
frm_output.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

window.mainloop()
