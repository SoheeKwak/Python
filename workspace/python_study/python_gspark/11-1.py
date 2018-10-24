a = 132
if a%2 == 1:
    print('홀수')
else:
    print('짝수')

if a%2 :
    print('홀수')
else:
    print('짝수')

a = 0
if a :
    print('홀수')
else:
    print('짝수')

#입력 받은 정수가 음수/양수인지 0인지?
b = int(input())
print(type(b+1))
print(type(b))

b= input() # int없이 입력 시 문자로 인식됨
print(b+'1')
print(type(b))

b = int(input())
if b < 0 :
    print('음수')
else:
    if b > 0:
        print('양수')
    else:
        print('제로')

