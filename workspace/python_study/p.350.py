inFp, outFp = None, None
inStr = ""

inFp = open("C:/Windows/notepad.exe", "rb")
outFp = open("C:/Temp/notepad.exe", "wb")

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)

outFp.close()
inFp.close()
print("---이전 파일이 정상적으로 복사되었음---")