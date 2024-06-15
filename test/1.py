from tkinter import *

answer = ["Супер", "Хорошо", "Так себе", "Плохо", "Ужасно", "Не скажу"]
diagnose = ["Это здорово!", "Это радует!", "Все возможно.", "Это огорчает!",
            "Это плохо!", "Раз ты так думаешь..."]


def listbox_select(event):
    select = box.curselection()
    nr = select[0]
    display.config(text=diagnose[nr])

window = Tk()
window.title("Привет!")
window.config(width=260, height=230)
display = Label(window, text="Как это сделать?")
display.place(x=20, y=10, width=160, height=30)

box = Listbox(window)
for nr in range(0,6):
    box.insert(nr, answer[nr])
box.bind("<<ListboxSelect>>", listbox_select)
box.place(x=30, y=50, width=200, height=150)

window.mainloop()
