from tkinter import *

state = ["You said me:", "I tell you:", "Diagnosis:"]

window = Tk()

border = []
for pos in range(0, 3):
    border.append(Frame(window, borderwidth=2, relief='groove'))
    border[pos].place(x=20, y=40 + pos * 90, width=460, height=50)

display = []
for pos in range(0, 3):
    display.append(Label(window, text=state[pos]))
    display[pos].place(x=20, y=10 + pos * 90, width=460, height=30)


button1 = Button(window, text="Again", command=button1_click)
button1.place(x=120, y=285, width=120, height=30)
button2 = Button(window, text="Done", command=button2_click)
button2.place(x=260, y=285, width=120, height=30)


window.mainloop()