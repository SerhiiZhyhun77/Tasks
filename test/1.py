from tkinter import *

answer = ["Супер", "Хорошо", "Так себе", "Плохо", "Ужасно", "Не скажу"]
diagnose = ["Это здорово!", "Это радует!", "Все возможно.", "Это огорчает!",
            "Это плохо!", "Раз ты так думаешь..."]
state = ["Духовно", "Морально", "Физически"]

def button_click():
    display.config(text=diagnose[OptNum.get()])

def check_click():
    text = "Привет! "
    for nr in range(0, 3):
        if ChkNum[nr].get() == 1:
            text = text + state[nr] + " "
    window.title(text)




window = Tk()
window.title("Привет!")
window.minsize(width=420, height=300)
display = Label(window, text="Как это сделать?")
display.grid(row=0, column=1)

links = Frame(window, borderwidth=2, relief="sunken")
links.place(x=20, y=50, width=180, height=220)
rechts = Frame(window, borderwidth=2, relief="raised")
rechts.place(x=220, y=50, width=180, height=110)


ChkNum = [0, 0, 0]
OptNum = IntVar()
OptNum.set(-1)

option = []
for nr in range(0, 6):
    option.append(Radiobutton(links, variable=OptNum, value=nr, text=answer[nr]))
    option[nr].config(command=button_click)
    option[nr].grid(row=nr + 1, column=0, sticky="w")

choice = []
for nr in range(0, 3):
    ChkNum[nr] = IntVar()
    choice.append(Checkbutton(rechts, variable=ChkNum[nr], text=state[nr]))
    choice[nr].config(command=check_click)
    choice[nr].grid(row=nr + 1, column=2, sticky="w")

window.mainloop()