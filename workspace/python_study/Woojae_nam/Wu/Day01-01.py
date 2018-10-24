#1부터 100까지 3의 배수의 합계

start, end, hap = [0]*3
if __name__ == '__main__':
    for i in range(1,101, 1):
        if i%3 == 0:
            hap += i
        else:
            pass
    print(hap)


