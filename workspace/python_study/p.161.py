ch = ""
a, b = 0, 0

while True :
    a = int(input("계산할 첫 번째 수를 입력 : "))
    a = int(input("계산할 두 번째 수를 입력 : "))
    ch = input("계산할 연산자 입력")

    if(ch == "+") :
        print("%d+%d")
