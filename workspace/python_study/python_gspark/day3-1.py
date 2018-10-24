"""
\d : 숫자, [0-9] = [0123456789] 동일
\D : NOT Digit(숫자가 아닌 것) = [^0-9]
\w : 문자+숫자 = [0-9A-Za-z]
\W : 문자+숫자가 아닌 것 = [^0-9A-Za-z]
\s : space문자 = [ \t\n]
\S : space문자가 아닌 것 = [^ \t\n]

2. 정규표현식 기호
1) .
- 의미 : 모든 문자(단, 줄바꿈 문자 \n은 제외)
ex) t.y
try : 매치
t7y : 매치
tya : 매치 안 됨

2) *
- 의미 : 여러번 반복, *앞에 있는 문자를 0번 이상 반복
ex) 정규식: bu*s (u가 0번 이상 반복)
    bs : 매치
    bus : 매치
    buuuuuuuus : 매치

3) +
- 의미 : 여러번 반복, +앞에 있는 문자를 1번 이상 반복
ex) 정규식 : bu+s (u가 1번 이상 반복)
bs : 매치가 안됨
bus : 매치
buuuuuuus : 매치

4) {}
- 의미 : 반복 횟수를 제한
ex) {1,}: 최소 1번 이상 반복(+와 같음)
    {0,}: 최소 0번 이상 반복(*와 같음)
ex) {3} :무조건 3번 반복
정규식 : bu{3}s
bus : 매치 안됨
buuus : 매치
buuuus : 매치 안됨

ex) {2,5} : 2번~5번 반복
정규식 : bu{2,5}s
bus : 매치 안됨
buus :매치
buuuuus : 매치

5) ?
- 의미 : 있어도 없어도 됨. {0,1}과 동일
ex)정규식 : bu?s
bus :매치
bs : 매치

3. re 모듈
-기본적으로 설치
-정규표현식을 사용할 수 있음

import re
pat = re.compile('bu*s') #정규식 선언
#이제 이것과 부합하는 것만 나오게 함


4. 정규식 그룹
() :그룹
ex) 전화번호 정규식 : '\d{3}-\d{3}-\d{4}'
지역번호, 전화번호 2개 그룹으로 구분하려면,,
'(\d{3})-(\d{3}-\d{4})'
  group1,    group2   로 구분
전체 전화번호 모두 갖고 올때는,,, group() or group(0)

"""


import re
pat = re.compile('[a-z]')
res = pat.match("3computer")
print(res) # None
res = pat.match("text") #'[a-z]+'였다면 'text'가 매치됐을 것임
print(res) #<_sre.SRE_Match object; span=(0, 1), match='t'>

text = "에러 1004 : 레퍼런스 에러\n 에러 1247: 코드 오류"
regex = re.compile("에러 1")
res = regex.search(text)
print(res) #<_sre.SRE_Match object; span=(0, 4), match='에러 1'>
if res !=None :
    print(res.group())
else :
    print("매칭안됨")


text2 = "기타 사항은 전화번호 : 02-1234-5678 로 연락 주세요"
regex2 = re.compile("\d\d-\d\d\d\d-\d\d\d\d")
res2 = regex2.search(text2)
pNumber = res2.group()
print(pNumber) # 02-1234-5678

text3 = "에러 1247 : 레퍼런스 에러\n 에러 32 : 코드 오류"
regex3 = re.compile("에러\s\d+") #공간+숫자1개 이상
res3 = regex3.findall(text3) #findall이면 group함수 쓸 필요 없음
print(res3) #['에러 1247', '에러 32']

text4 = "기타 사항은 전화번호 : 02-1234-5678 로 연락 주세요"
regex4= re.compile("\d{2}-\d{4}-\d{4}")
res4 = regex4.search(text4)
pNumber = res4.group()
print(pNumber) # 02-1234-5678


text4 = "기타 사항은 전화번호 : 02-1234-5678 로 연락 주세요"
regex4= re.compile("(\d{2})-(\d{4}-\d{4})")
res4 = regex4.search(text4)
pNumber = (res4.group(1),res4.group(2))  # group(1)지역번호, group(2)전화번호
print(pNumber) # ('02', '1234-5678')


text5 = "기타 사항은 전화번호 : 02-1234-5678 로 연락 주세요"
regex5= re.compile("(?P<area>\d{2})-(?P<number>\d{4}-\d{4})") # ?P<area>, ?P<number> 각 그룹에 그룹명을 줌
res5 = regex5.search(text5)
pNumber = (res5.group("area"),res5.group("number"))  # group명(지역번호, 전화번호)으로 검색
print(pNumber) # ('02', '1234-5678')








