a = dict(name='kim', age=20)
print(a)
print(a['name'])
a['addr'] = 'seoul'
print(a)

print(a.keys())
print(a.values())
print(a.items())

for k in a.keys():
    print(k, a[k])

for v in a.values():
    print(v)

for item in a.items():
    print(item, item[0], item[1])

for k,v in a.items():
    print(k,v)

for k in a: #기본적으로 딕셔너리에서 읽히는 게 키
    print(k, a[k])

for k in reversed(list(a.keys())):
    print(k, a[k])

a = [1,3,5,7,9]
print(a[len(a)-1])
print(a[0:len(a)])
print(a[0:len(a)//2]) #//2 2로 나눈 몫
print(a[len(a)//2:])
