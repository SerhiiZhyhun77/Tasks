from tkinter import *

width = 500
height = 330
mode = ["Появление", "Движение", "Сокрытие"]

def show_image():
    pass

def move_image():
    pass

def hide_image():
    pass

window = Tk()
window.title("Анимация")
window.config(width=width, height=height)
graphic = Canvas(window, width=width, height=height)
graphic.pack()

knob = []
for nr in range(3):
    knob.append(Button(window, text=mode[nr]))
    knob.place(x=30 + nr *150, y=height -50, width=140, height=30)
knob[0].config(command=show_image)
knob[1].config(command=move_image)
knob[2].config(command=hide_image)

window.mainloop()