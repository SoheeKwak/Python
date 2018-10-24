a = [1, 2, 3, 4]
res = []
for num in a:
    res.append(num*2)
print(res)

#리스트 내포 이용한 코드
res = [num*2 for num in a]
print(res)

#a리스트의 요소값에 대해 짝수인 경우 2배를 해서 res에 저장
res = [num*2 for num in a if num%2==0]

res = [x*y for x in range (2,5)
         for y in range(1,10)]
print(res)

a = [1, 2, 3, 4, 5]
res = []
# for n in a :
#     if n %2 == 1:
#         res.append(n*2)
#     else:
#         res.append(n)
# print(res)

res = [n*2 if n%2 == 1 else n for n in a ]
print(res)

msj = "How are you? Fine thank you, and you?"
#리스트 내포를 이용해 모음을 제거한 후 msg를 출력
v = 'aeiou'
print(''.join([a for a in msj if a not in v]))








