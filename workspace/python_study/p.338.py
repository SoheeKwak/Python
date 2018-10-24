iinFp = None
inStr = ""
cnt = 0
inFp = open("c:/temp_1/data1.txt", "r")

while True:
    inStr = inFp.readline()
    cnt += 1
    if inStr == "":
        break
    print("%d : %s" % (cnt, inStr), end="")

inFp.close()