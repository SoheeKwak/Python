inFp, outFp = None, None
inFpp, outFpp, inStr = "", "", ""

inFpp = input("소스 파일명을 입력:")
outFpp = input("타깃 파일명을 입력:")

inFp = open(inFpp, "r")
outFp = open(outFpp, "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

outFp.close()
inFp.close()
print("--%s파일이 %s파일로 복사되었음--"%(inFpp, outFpp))
