myList = []
for i in range(0, 3) :
    myList.append(0)
hap = 0

for i in range(0, 3) :
    myList[i] = int(input(str(i + 1) + "번째 숫자:"))

for i in range (0, 3) :
    hap = hap + myList[i]
print("합계=>%d" % hap)