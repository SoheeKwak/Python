print(range(5))
print(list(range(5)))
print(list(range(0,5)))
print(list(range(3,8,2)))#3~7까지 홀수만
print(list(range(8,-5,-2)))

#sorted함수:값을 정렬->결과를 리스트로 리턴
#sort함수:리턴값이 없음
print(sorted([5,3,4]))
print(sorted(['k','i','m']))
print(sorted("seoul"))

data = [5,3,4]
data = sorted(data)
print(data)

data2 = [5,3,4]
print(data2.sort())
data2.sort()
print(data2)

#zip:자료들을 묶어주는 함수(자료들은 동일한 갯수)
print(list(zip([1,2,3])))
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))

print(list(zip("xyz", "ijk", [4,5,6])))
print("="*20, "여기까지 내장함수", "="*20)

print("="*20, "지금부터 외장함수", "="*20)
#pickle:딕셔너리와 같은 객체상태를 유지하면서 파일 입출력 모드
#dump 함수를 이용
import pickle #객체 저장/로드
f = open("sleep.txt","wb") #write, binary
data = {1:"big", 2:"data"}
pickle.dump(data,f) #f.write(data)대신 딕셔너리를 입출력하기 위해 pickle이용
f.close()

f = open("sleep.txt","rb")
data = pickle.load(f)
print(data)

import glob
print(glob.glob("d*"))

import random
print(random.random())

for i in range(1,7):
    random.randint(1, 46)
    if set([1,2,2,3,2]) == 6 :
        print


a = set([1,2,2,3,2])
print(len(a))



#정규표현식:일정규칙을 갖는 문자열을 표현하는 방법
#거의 대부분의 언어가 지원. 정규식이라고도 함
"""
복잡한 문자열에서 특정규칙을 만족하는 문자열을 검색한 다음
전처리(치환, 삽입 등). 주어진 문자열이 규칙에 맞는지
확인하고자 하는 경우.
Regular Expression:REGEX
https://docs.python.org/3/howto/regex.html

"""

jumin = """
kim 980102-1234567
park 970807-2345678
"""
sj = jumin.split("\n")
print(sj)

res = []
for line in jumin.split("\n"):
    # print(line)
    word_res = []
    for word in line.split(" "):
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit(): #print(word)
           word = word[0:6]+"-"+"*******"
           #print(word)
        word_res.append(word)
    res.append(" ".join(word_res))
print("\n".join(res))

import re
jumin = """
kim 980102-1234567
park 970807-2345678
"""
pattern = re.compile("(\d{6})[-]\d{7}")
print(pattern.sub("\g<1>-*******", jumin))

# 메타문자:[] {} () | \ 등
# 문자메타:[],[]사이에는 모든 문자가 들어갈 수 있다.
# 정규식이 [xyz]라면, x,y,z 중 한개의 문자와 매치
#ex)"a" :정규식에 매치가 안됨
#   "text" :정규식에 일치하는 'x'가 있음-> 매치
#ex) 정규식이 [a-zA-Z]라면, 알파벳 전체
#     [0-9]라면 숫자 전체

import re
p = re.compile('[xyz]')
m = p.match("text")
print(m)

p = re.compile('[a-z]')
m = p.match("text")
print(m)

p = re.compile('a.b') #a와 b문자 사이에 어떤 문자가 들어가도 매치가 됨
m = p.match("a7b")
print(m)
m = p.match("aab")
print(m)
m = p.match("abcd")
print(m)

p = re.compile('a[.]b') #a[.]b는 문자 그대로의 의미
m = p.match("aaa.bb")
print(m)
m = p.match("a.baabb")
print(m)

# 1. map과 lambda 함수를 이용하여 [5,7,9] 리스트의 각 요소값에 5가 곱해진 [25, 35, 45]라는 리스트를 만드시오.
def five_times(num): return num*5
print(map(five_times, [5,7,9]))
print(list(map(five_times, [5,7,9])))

print(list(map(lambda x: x*5, [5,7,9])))


# 2. [1, 2, 3, 4]와 ['a', 'b', 'c', 'd']라는 리스트가 있다. 이 두개의 리스트를 합쳐 다음과 같은 리스트를 만드시오.
# 결과 : [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print(list(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])))

# 3. random모듈을 이용하여 로또번호(1~45 사이의 숫자 6개)를 생성하시오. (단, 중복된 숫자가 있으면 안됨)
import random

def getNumber():
    return random.randrange(1,46)

lotto = []
num = 0
while True:
    num = getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto)>=6:
        break
lotto.sort()
for i in range(0,6):
    print("%d" % lotto[i], end ='  ')




