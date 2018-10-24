outFp = None
outStr = ""

outFp = open("c:/temp/data3.txt", "a")

while True :

    outStr = input("내용 입력 :")
    if outStr !="" :
        outFp.writelines(outStr +"\n")
    else :
        break

outFp.close()
print("---정상적으로 파일에 씀---")
