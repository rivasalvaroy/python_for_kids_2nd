import turtle


def rotate(i, angle):
    if i < 1:
        t[i].left(angle)
    else:
        t[i].right(angle)


t = []
for i in range(2):
    t.append(turtle.Turtle())

for i in range(2):
    if i % 2 != 0:
        rotate(i, 180)
    for j in range(3):
        t[i].forward(100)
        rotate(i, 90)
    for j in range(2):
        t[i].forward(80)
        rotate(i, 90)
    for j in range(2):
        t[i].forward(60)
        rotate(i, 90)
    t[i].forward(40)
    rotate(i, 90)
    t[i].forward(40)
