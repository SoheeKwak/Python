numStr = '', ''
numStr = input("숫자를 입력하세요")
print('')
i=0
ch=numStr[i]
while True:
    heartNum = int(ch)

    heartNum = ""
    for k in range(0, heartNum) :
        heartStr +="\u2665"
        k += 1

    print(heartStr)

    i+= 1
    if(i > len(numStr)-1) :
        break

    ch =