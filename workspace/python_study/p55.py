import turtle

def screenLeftClick(x,y):
    global r, g, b
# 마우스 왼쪽 버튼 기능
# 레드, 그린, 블루
# global = 전역변수
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)




pSize=10
r,g,b = 0.0,0.0,0.0
turtle.title("거북이로 그림을 그리기")
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 2)

turtle.done()


