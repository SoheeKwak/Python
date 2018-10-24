import turtle
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

if __name__ == "__main__":
    turtle.title('거북이로 두숫자 비트 논리곱 연산')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.left(90)

    num1 = int(input("1번 숫자를 입력:"))
    num2 = int(input("2번 숫자를 입력:"))
    num3 = num1 & num2


    binary1 = bin(num1)
    curX = swidth/2
    curY = 0
    binary = bin(num1) & bin(num2)

    for i in range(len(binary)-2):
        turtle.goto(curX,)