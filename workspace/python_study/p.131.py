answer = 0
select = int(input("1.수식입력 2.숫자 2개 입력 3.숫자 3개 입력"))

if select == 1:
    numStr = input("수식입력")
    answer = eval(numStr)
    print(answer)

elif select == 2:
    num1 = int(input("시작수"))
    num2 = int(input("마지막수"))
    for i in range(num1, num2+1):
           answer = answer + i
    else:
        for i in range(num1, num2+1):
           answer = answer + i
    print("두수 사이의 합은 %d" % answer)
