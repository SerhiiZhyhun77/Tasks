import tkinter
window = tkinter.Tk()


def button_click1():
    display.configure(text="Це радує!")


def button_click2():
    display.configure(text="Це засмучує!")


display = tkinter.Label(window, text="Привіт, як справи?")
display.pack()
button1 = tkinter.Button(window, text="Добре", command=button_click1)
button2 = tkinter.Button(window, text="Не дуже", command=button_click2)
button1.pack(side="left")
button2.pack(side="right")

window.mainloop()
