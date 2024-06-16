# Psychologist program
from tkinter import *
import random

# text constant
state = ["You said me:", "I tell you:", "Diagnosis:"]
diagnose = ["This is awesome!", "This makes me happy!", "Everything is possible.",
            "This is upsetting!", "This is bad!", "If you think so..."]


# function for events
def button1_click():
    _input.delete(0, "end")
    answer.config(text="")


def button2_click():
    nr = random.randint(0, 5)
    answer.config(text=diagnose[nr])


def scale_value(event):
    nr = slider.get()
    answer.config(text=diagnose[nr])


# main program
window = Tk()
window.title("Psychologist")
window.minsize(width=500, height=330)

# frames & labels
border = []
display = []
for pos in range(0, 3):
    border.append(Frame(window, borderwidth=2, relief='groove'))
    border[pos].place(x=20, y=40 + pos * 90, width=460, height=50)
    display.append(Label(window, text=state[pos]))
    display[pos].place(x=20, y=10 + pos * 90, width=460, height=30)

# input & lbl for answer
_input = Entry(border[0])
_input.place(x=10, y=10, width=440, height=30)
answer = Label(border[1])
answer.place(x=10, y=10, width=440, height=30)

# slider
slider = Scale(border[2], orient="horizontal", command=scale_value)
slider.config(from_=0, to=5, length=430, showvalue=False)
slider.pack(pady=10)

# buttons
button1 = Button(window, text="Again", command=button1_click)
button1.place(x=120, y=285, width=120, height=30)
button2 = Button(window, text="Done", command=button2_click)
button2.place(x=260, y=285, width=120, height=30)

window.mainloop()
