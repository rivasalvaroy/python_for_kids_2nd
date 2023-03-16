import turtle

t1 = turtle.Pen()
t2 = turtle.Pen()

for i in range(3):
    t1.forward(100)
    t1.left(90)
for i in range(2):
    t1.forward(80)
    t1.left(90)
for i in range(2):
    t1.forward(60)
    t1.left(90)
t1.forward(40)
t1.left(90)
t1.forward(40)

t2.right(180)
for i in range(3):
    t2.forward(100)
    t2.right(90)
for i in range(2):
    t2.forward(80)
    t2.right(90)
for i in range(2):
    t2.forward(60)
    t2.right(90)
t2.forward(40)
t2.right(90)
t2.forward(40)
