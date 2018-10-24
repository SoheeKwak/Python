cnt = 0
while True:
    if cnt >= 5:
        break
    num = input("16진수 한글자 입력 :")
    print(len(num))
    if len(num) != 1:
        continue
    if ('0' <= num and num <= '9') or ('a' <= num and num <= 'f') or ('A' <= num and num <= 'F') :
        num10 = int(num, 16)
        print("10진수 ==> %d" % num10)
        cnt = cnt + 1

    else:
        print("16진수가 아닙니다")
        exit()
