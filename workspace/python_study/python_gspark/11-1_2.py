a = [1,3,5]
print(a[0], a[1], a[2])
print(a)

a[0] = a[2]
print(a)
a.append(11)
print(a)

# a리스트를 역순으로 출력 : 11, 5, 3, 5
# a.reverse()
# print(a)

for i in reversed(a):
    print(i)

for i in reversed(range(len(a))):
    print(a[i])

for i in range(len(a)-1, -1, -1):
    print(a[i])


a, b = 3, 8
print(a, b)
a, b = b, a
print(a, b)

# 튜플: 리스트의 상수 버전
t = (1, 3, 5)
print(t)
print(t[0])
# t[0]=9  # 튜플은 읽기만 가능하므로 새로운 인수를 넣을 수 없음
print(t[0])

t2 = (100, 200)
print(t2)
t22 = 100, 200
print(t22, type(t2))
t3, t4 = t2
print(t2)
print(t3)
print(t4)
#
def order(a,b):
    if a < b:
        return a, b
    return b, a
print(order(4,9))
print(order(9,4))
#
min, max = order(9,4)
print(min, max)
_, max = order(9,4) #언더바_는 그 변수는 무시하고 출력하지 않는다는 의미
print(max)
#
ns = [1,3,5,1,3,5,1,3,5]
unique=[]
for i in ns:
    if not i in unique:
        unique.append(i)
print(unique)

print(list(set(ns)))
#
ns = [2,4,6,1,3,5]
for i in range(len(ns)):
    print(i, ns[i], end=', ')
print()
#
j = 0
for i in ns:
    print(j, i)
    j+=1
#
for i in enumerate(ns):
    print(i, i[0], i[1])
#
for i,j in enumerate(ns):
    print(i, j)
#
def dummy():
    pass
print(dummy())

#
