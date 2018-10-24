a = 4.2E7 #4.2 * 10의7승
print(a)

a = 4.2E-7 #4.2 * 10의-7승
print(a)

print(7/4)
print(7//4)
print(7%4)

msg = """
Life is \ttoo short
You need Python
"""
print(msg)

print("-"*100)

a="Life"
print(a[-2])
print(a[1:3])

print("I eat {0} apples, so I was sick for {1} days".format(3, 5))
print("I eat {1} apples, so I was sick for {0} days".format(3, 5))

pi=3.14
print("{0:10.4f}".format(pi))

a = ","
print(a.join('abcd'))

msg = "Life is too short"
msg = msg.replace("Life", "Your leg")
print(msg)
print(msg.split()) #공백 기준 분류
msg2 = "Life:is:too:short"
print(msg2.split(":"))

a = [1, 2, 3, ['a', 'b', 'c']] # 요소가 총4개
print(a[-1])
print(a[-1][0])

a = [1, 2, 3, ['a', 'b', ['c','d' ]]]
print(a[3][2][1])
print("="*50)
a = [4, 5, 6]
a[2] = 7
print(a)
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
# a[1] = ['a', 'b', 'c']
print(a)

#a[1:3] = []
del a[1:3]
print(a)

def sum(a,b) : #함수정의
    return a+b

print(sum(3,5)) #함수호출

def sum2(*v) :
    sum = 0
    for i in v :
        sum+=i
    return sum
print(sum2(1,2))

f = open("test.txt", "w")
for i in range(1,11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close() #메모리 해제

# f = open("test.txt", "r")
# while True:
#     line = f.readline()
#     if not line : break
#     print(line)
# f.close()

# f = open("test.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line)

# f = open("test.txt", "r")
# data = f.read()
# print(data)

# f = open("test.txt", "a") # append
# # for i in range(11, 15):
# #     data="%d번째 줄입니다.\n" % i
# #     f.write(data)

#다음과 같이 총 5줄로 구성된 input.txt파일이 있다.
#모든 숫자를 읽어 총합과 평균을 구하고 화면에 출력
#result.txt파일에도 출력(평균만)

f = open("input.txt", "r")
lines = f.readlines()
f.close()
sum = 0
print(lines)
for line in lines:
    sum = sum +int(line)
print(sum)
avg = sum/len(lines)
print(avg)

f= open("result.txt", "w")
f.write(str(avg))
f.close()