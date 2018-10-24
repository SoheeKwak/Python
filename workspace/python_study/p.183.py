aa = [0]*10
hap = 0

i = 0
while i<10 :
    aa[i] = int(input( str(i+1)+ "번째 숫자 :" ))
    i += 1

i = 0
while i<10 :
    hap += aa[i]
    i += 1
print("합계: %d" % hap)