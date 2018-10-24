import random

numbers = []
jumsu = 0

for i in range(0, 10):
     numbers.append(random.randrange(0, 10))
print("생성된 리스트", numbers)

for i in range(0, 5):
     num = int(input("숫자입력(0~9):"))
     if num in numbers:
        print("10점 획득")
        jumsu += 10

     else:
        print("0점 획득")

print("당신이 획득한 점수는 %d점입니다." % jumsu)

#for num in range(0, 10):
     #if num not in numbers :
         #print("숫자 %d는 리스트에 없네요." %num)