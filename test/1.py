from tkinter import *


def button_click1():
    display.configure(text="Это здорово!")
def button_click2():
    display.configure(text="Это радует!")
def button_click3():
    display.configure(text="Все возможно.")
def button_click4():
    display.configure(text="Это огорчает!")
def button_click5():
    display.configure(text="Это плохо!")
def button_click6():
    display.configure(text="Раз ты так думаешь...")



window = Tk()
window.config(width=300, height=190)
display = Label(window, text="Как это сделать?")
display.place(x=80, y=10, width=160, height=30)
button1 = Button(window, text="Супер", command=button_click1)
button2 = Button(window, text="Хорошо", command=button_click2)
button3 = Button(window, text="Так себе", command=button_click3)
button4 = Button(window, text="Плохо", command=button_click4)
button5 = Button(window, text="Ужасно", command=button_click5)
button6 = Button(window, text="Не скажу", command=button_click6)
button1.place(x=20, y=60, width=120, height=30 )
button2.place(x=160, y=60, width=120, height=30)
button3.place(x=20, y=100, width=120, height=30)
button4.place(x=160, y=100, width=120, height=30)
button5.place(x=20, y=140, width=120, height=30)
button6.place(x=160, y=140, width=120, height=30)

window.mainloop()
