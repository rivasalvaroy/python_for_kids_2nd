import turtle
from tkinter import *

turtle.setup(width=500, height=500)
t = turtle.Turtle()
t.up()
t.goto(-250, 250)
t.down()
t.goto(500, -500)

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.mainloop()
