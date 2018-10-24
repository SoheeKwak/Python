import turtle

num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

if __name__ == "__main__":
    turtle.title('거북이로 2진수 논리곱 표현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1 = int(input("1번 숫자를 입력하세요 : "))
    num2 = int(input("2번 숫자를 입력하세요 : "))

    binary1 = bin(num1)
    binary2 = bin(num2)
    curX = swidth / 2
    curY = 0

    binary = bin(num1) & bin(num2)

    for i in range(len(binary) - 2):
        turtle.goto(curY, curY)
        if num & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1

turtle.done()
