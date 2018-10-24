"""
복습퀴즈3(심화). 1부터 999까지 100개의 숫자를 임의로 생성한 후에, 뒤에서 두번째
  숫자로 내림 차순 정렬한다.
   단, 뒤에서 두번째 숫자가 동일하면 마지막 숫자로 정렬한다.
  ( 한자리 숫자의 경우 001 식으로, 두자리 경우 011 식으로 처리한다.)

  예)  092   838   071  004  037
        --> 092  071  838  037  004
"""

import operator
import random

data = []
countDic = {}
for i in range(1,1000):
    num = random.randint(100)
    data.append(num)
print(data)

for a in data:
    if a in countDic:
        countDic[a] += 1
    else:
        countDic[a] = 1
print(countDic)


# tmp = None
# totalRank, currentRank = 1,1
#
# if __name__ =="__main__":
#     for tmp in num:
#         if tmp in
