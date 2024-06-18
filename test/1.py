from tkinter import *

width = 500
height = 330
mode = ["Появление", "Движение", "Сокрытие"]
x, y, z = 20, 50, 200

def show_image():
    global circle
    circle=graphic.create_oval(x, y, x + z, y + z, fill="red")

def move_image():
    global circle
    for pos in range(20, width - 220, 2):
        graphic.move(circle, 2, 0)
        graphic.update()
        graphic.after(20)


def hide_image():
    global circle
    graphic.delete(circle)

window = Tk()
window.title("Анимация")
window.config(width=width, height=height)
graphic = Canvas(window, width=width, height=height)
graphic.pack()

knob = []
for nr in range(3):
    knob.append(Button(window, text=mode[nr]))
    knob[nr].place(x=30 + nr *150, y=height - 50, width=140, height=30)
knob[0].config(command=show_image)
knob[1].config(command=move_image)
knob[2].config(command=hide_image)

window.mainloop()