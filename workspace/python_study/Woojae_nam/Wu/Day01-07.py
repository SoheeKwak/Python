#2차원 리스트 조작
# 3*4 크기의 빈 리스트
myList = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

myList = []
tmpList = []
for i in range(3):
    tmpList = []
    for k in range(4):
        tmpList.append(0)
    myList.append(tmpList)
print(myList)


ROW = int(input('행-->'))
COL = int(input('열-->'))
myList = []
tmpList = []
ROW=3; COL=4
for i in range(ROW):
    tmpList = []
    for k in range(COL):
        tmpList.append(0)
    myList.append(tmpList)
print(myList)