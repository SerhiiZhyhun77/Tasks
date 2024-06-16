# Psychologist program
from tkinter import *

# text constant
state = ["You said me:", "I tell you:", "Diagnosis:"]
diagnose = ["This is awesome!", "This makes me happy!", "Everything is possible.",
            "This is upsetting!", "This is bad!", "If you think so..."]

# function for events
def button1_click():
    pass
def button2_click():
    pass

# main program
window = Tk()
window.title("Psychologist")
window.minsize(width=500, height=330)


border = []
display = []
for pos in range(0, 3):
    border.append(Frame(window, borderwidth=2, relief='groove'))
    border[pos].place(x=20, y=40 + pos * 90, width=460, height=50)
    display.append(Label(window, text=state[pos]))
    display[pos].place(x=20, y=10 + pos * 90, width=460, height=30)

_input = Entry(border[0])
_input.place(x=10, y=10, width=440, height=30)

answer = Label(border[1])
answer.place(x=10, y=10, width=440, height=30)

slider = Scale(border[2], orient="horizontal")
slider.config(length=430, showvalue=0)
slider.pack(pady=10)




button1 = Button(window, text="Again", command=button1_click)
button1.place(x=120, y=285, width=120, height=30)
button2 = Button(window, text="Done", command=button2_click)
button2.place(x=260, y=285, width=120, height=30)


window.mainloop()