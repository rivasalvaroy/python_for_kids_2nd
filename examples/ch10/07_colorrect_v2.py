from tkinter import *
from tkinter import colorchooser
import random

tk = Tk()
canvas = Canvas(tk, height=400, width=400)
canvas.pack()


def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


c = colorchooser.askcolor()
random_rectangle(400, 400, c[1])
canvas.mainloop()
