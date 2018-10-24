#행,열을 입력받고 1부터 채워나가기
ROW = int(input('행-->'))
COL = int(input('열-->'))
# List1 = []
# List2 = []
# value = 1
# for i in range(ROW):
#     List1 = []
#     for k in range(COL):
#         List1.append(value)
#         value +=1
#     List2.append(List1)
# print(List2)
#
# for i in range(ROW):
#     for k in range(COL):
#         print("%3d" % List2[i][k], end=" ")
#     print("")

import numpy as np
List1 = []
value = 1
for i in range(ROW):
    for k in range(COL):
        List1.append(value)
        value +=1
List1.reverse()
print(List1)
print(np.array(List1).reshape(ROW,COL))



# for i in range(ROW):
#     for k in range(COL):
#         print("%3d" % List2[i][k], end=" ")
#     print("")

