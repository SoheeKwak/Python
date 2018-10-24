answer = 0

num1 = int(input("첫번째 숫자를 입력:"))
num2 = int(input("두번째 숫자를 입력:"))
num3 = int(input("더할 숫자를 입력:"))


for i in range(num1, num2+1, num3) :
    answer = answer + i

print("%d+%d...+%d는 %d." % (num1, num1+num3, num2, answer))
