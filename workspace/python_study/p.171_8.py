## 변수 선언 부분
i, k, heartNum = 0, 0, 0
numStr, ch, heartStr =  "", "", ""

## 메인(main) 코드 부분
numStr=input("숫자를 여러개 입력하세요 : ")
print("")

i = 0
ch = numStr[i]
while True:
    heartNum = int(ch)

    heartStr = ""
    for k in range(0, heartNum * 2):
      heartStr += "\u2605"
      k += 1
    print(heartStr)

    i += 1
    if (i > len(numStr) - 1):
      break

    ch = numStr[i]