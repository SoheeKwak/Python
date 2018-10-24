import turtle
import random

swidth, sheight, psize = 300, 300, 3
r, g, b, dist = [0]*4

turtle.title("거북이 소라 그리기")
turtle.shape("turtle")
turtle.pensize(psize)
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)

dist = 5
for i in range(1, 80) :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    turtle.forward(dist)
    turtle.left(30)
    dist += 1