import turtle; import random

#함수 선언
def clickLeft(x,y): #파라미터, 클릭한 위치
    r = random.random()
    g = random.random() ; b = random.random()
    turtle.pencolor((r,g,b)) #파라미터를 튜플로 넘겨주기 때문에 괄호 2개
    turtle.goto(x,y)

def clickRight(x,y):
    turtle.penup(); turtle.goto(x,y); turtle.pendown()

def clickMid(x,y):
    tSize = random.randrange(1,10)
    turtle.turtlesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.turtlecolor((r,g,b))

#변수 선언
penSize = 0; r,g,b =[0]*3
pSize = random.randrange(1,10)

#메인 코드
if __name__ == '__main__':
    turtle.title('거북이가 그리기')
    turtle.shape('turtle')
    turtle.pensize(pSize)

    turtle.onscreenclick(clickLeft,1)
    turtle.onscreenclick(clickLeft,2)
    turtle.onscreenclick(clickLeft,3)


    turtle.done()



