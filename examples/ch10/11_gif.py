from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=310, height=280)
canvas.pack()
my_image = PhotoImage(file='./images/python.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
canvas.mainloop()
