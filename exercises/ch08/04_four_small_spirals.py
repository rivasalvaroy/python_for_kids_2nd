import turtle

t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()

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

for i in range(3):
    t3.forward(100)
    t3.right(90)
for i in range(2):
    t3.forward(80)
    t3.right(90)
for i in range(2):
    t3.forward(60)
    t3.right(90)
t3.forward(40)
t3.right(90)
t3.forward(40)

t4.left(180)
for i in range(3):
    t4.forward(100)
    t4.left(90)
for i in range(2):
    t4.forward(80)
    t4.left(90)
for i in range(2):
    t4.forward(60)
    t4.left(90)
t4.forward(40)
t4.left(90)
t4.forward(40)
