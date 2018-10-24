import turtle; import random

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0]*7

def main():
    global exitCount,swidth, sheight, pSize, exitCount,r, g, b, angle, dist, curX, curY
# if __name__ == '__main__':
#     main()
    turtle.shape('turtle'); turtle.pensize(pSize)
    turtle.setup(width=swidth+30, height=sheight+30)
    turtle.screensize(swidth,sheight)
    while True:
        r=random.random();g=random.random();b=random.random();
        turtle.pencolor((r,g,b))
        angle=random.randint(0,360)
        dist = random.randint(0,100)
        turtle.left(angle);turtle.forward(dist)
        curX = turtle.xcor(); curY = turtle.ycor();
        if (-swidth/2 < curX < swidth/2) and (-sheight/2 < curY < sheight/2):
            pass
        else:
            turtle.penup();turtle.goto(0,0);turtle.pendown()
            exitCount +=1
            if exitCount >=3:
                break
