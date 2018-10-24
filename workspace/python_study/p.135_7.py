import random

a=random.randrange(1, 7)
b=random.randrange(1, 7)

if a>b :
    print("a가 이겼습니다")
elif a<b :
    print("b가 이겼습니다")
else :
    print("비겼습니다")

print(a, b)

