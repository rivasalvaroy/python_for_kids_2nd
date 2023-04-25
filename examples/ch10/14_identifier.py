from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')
canvas.move(mytriangle, 10, 0)
canvas.update()
time.sleep(3)
canvas.itemconfig(mytriangle, fill='blue')
canvas.update()
time.sleep(1)
canvas.itemconfig(mytriangle, outline='red')
canvas.mainloop()
