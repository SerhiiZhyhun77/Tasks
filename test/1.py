from tkinter import *

answer = ["Супер", "Хорошо", "Так себе", "Плохо", "Ужасно", "Не скажу"]
diagnose = ["Это здорово!", "Это радует!", "Все возможно.", "Это огорчает!",
            "Это плохо!", "Раз ты так думаешь..."]

def button_click():
    display.config(text=diagnose[Number.get()])

window = Tk()
window.title("Привет!")
window.minsize(width=260, height=260)
display = Label(window, text="Как это сделать?")
display.pack()

Number = IntVar()
Number.set(-1)

option = []
for nr in range(0, 6):
    option.append(Radiobutton(window, variable=Number, value=nr, text=answer[nr]))
    option[nr].config(command=button_click)
    option[nr].pack(anchor="w")

window.mainloop()