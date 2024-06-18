from tkinter import *

width = 500
height = 330
mode = ["Появление", "Движение", "Сокрытие"]
x, y = 120, 160

def show_image():
    global figure
    global picture

    picture = PhotoImage(file="peppa.gif")
    figure = graphic.create_image(x, y, image=picture)

def move_image():
    global figure
    for pos in range(20, width - 220, 2):
        graphic.move(figure, 2, 0)
        graphic.update()
        graphic.after(10)


def hide_image():
    global figure
    graphic.delete(figure)

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