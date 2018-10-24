hap = 0
for i in range(1, 1001, 2) :
    hap = hap+i
    if hap >= 1000 :
        print(i)
        print(hap)
        break