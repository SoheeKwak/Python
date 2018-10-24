aa = [0, 0, 0, 0]
hap = 0

aa[0] = int(input("숫자"))
aa[1] = int(input("숫자"))
aa[2] = int(input("숫자"))
aa[3] = int(input("숫자"))

for i in range(0,4) :
    hap += aa[i]

print(hap)