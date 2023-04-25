from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)
canvas.create_rectangle(60, 10, 350, 50)
canvas.create_rectangle(10, 60, 50, 350)
canvas.mainloop()
