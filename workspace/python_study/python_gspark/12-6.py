import random
random.seed(999) # 샘플링한 표본을 고정시킴으로써 모델 알고리즘을 변경한 후, 그 전의 모델과 비교할 수 있게 함.
a = [random.randrange(100) for _ in range(10)]
print(a)
print([i for i in range(10)])
print([i for i in a])
print([i for i in a if i%2]) #i%2==0이면 False, 그러므로 홀수(참)만 출력하게 됨
print([i for i in a if i%2][::-1])
print([i for i in a[::-1] if i%2])
print([i for i in reversed(a) if i%2])

a1 = [random.randrange(100) for _ in range(10)]
a2 = [random.randrange(100) for _ in range(10)]
a3 = [random.randrange(100) for _ in range(10)]
b = [a1,a2,a3] #3행10열(2차원: [[] ])matrix
print(b)
print(sum([1,3,5]))
print([sum(i) for i in b])
print(sum([sum(i) for i in b]))

print([0 for i in b]) #3행
print([i for i in b]) #3행
print([0 for i in b for j in i]) #1차원(차원감소)
print([j for i in b for j in i]) #1차원(차원감소)
print([j for i in b for j in i if j%2]) #1차원(차원감소)

print([[j for j in i] for i in b]) #2차원. 컴프리헨션으로 오른쪽 for문부터 읽어줌
print([[j for j in i if j%2] for i in b])

print(b)
print([i for i in b[::-1]])
print([[j for j in i[::-1]] for i in b[::-1]]) # b요소, 즉 행을 역으로 읽은 후, 그 행의 열들을 역으로 출력

print(2**1000) #1000개의 상품 중 연관규칙을 알아보기 위한 부분집합 수
print(str(2**1000))
print(len(str(2**1000)))

#2**1000에 들어가는 숫자들의 합을 구하라.
print(sum([int(i) for i in str(2**1000)]))

s = '707'
print(s.count('7'))

#1~100000 사이에 있는 7의 개수를 세어보시오.
print(sum([str(i).count('7') for i in range(1,100001)]))

# maria 딕셔너리에 저장된 점수의 평균을 출력하세요.
maria = {'kor':94, 'eng':91, 'math':89, 'sci':83}
print(sum(maria.values())/len(maria))

# 셀프넘버 합을 구하라.
dn = []
for num in range(1,5000):
    dn.append((sum([int(i) for i in str(num)])+ num))
self_num = set(range(1,5000))-set(dn)
print(sum(self_num))


print(set(range(1,5))-set(range(1,3)))
print(sum(set(range(1,5))))






