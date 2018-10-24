"""
1. 정규식 함수
search(): 문자열 전체를 검색, 정규식 매치 조사
match() : 문자열 왼쪽부터 검색, 정규식 매치조사
findall() : 정규식 매치되는 모든 문자열을 리스트로 리턴
finditer() : 정규식 매치되는 모든 문자열을 iterator 객체로 리턴

2. 컴파일 옵션
1) re.I 옵션 (Ignore case) : 대소문자에 관계없이 매칭
2) . : 모든 문자와 매치(\n 제외)
   re.DOTALL 또는 re.S와 같은 의미
3) re.M (Multiline) : ^(문자열의 처음), $(문자열의 마지막)
4) re.X (Verbose)
"""
import re

p = re.compile('[a-zA-Z]+')
m = p.match("java")
print(m) #<_sre.SRE_Match object; span=(0, 4), match='java'>

m = p.match("9 java") # match는 왼쪽 첫단어부터 안맞음 매칭 그만둠
print(m) #None

m2 = p.search("9 java 7") # match와 구분
print(m2) #<_sre.SRE_Match object; span=(2, 6), match='java'>

res = p.findall("How are you?")
print(res) #['How', 'are', 'you']

res2 = p.finditer("How are you?") # callable_iterator object(반복가능한 객체)
print(res2) # res2에는 'How', 'are', 'you'라는 3개의 문자열 리스트가 객체로 저장되어 있음.
for r in res2:
    print(r) #<_sre.SRE_Match object; span=(0, 3), match='How'>
    print(r.group()) #How
    print(r.start()) #스타트 시점 추출할 때 0
    print(r.end()) #3
    print(r.span()) #(0, 3)


import re
m2 = re.match('[a-zA-Z]+', "9 java")
print(m2)


import re
pat = re.compile('a.k')
res = pat.match('a1k')
print(res)
res = pat.match('ak') # .는 문자의 의미
print(res)
res = pat.match('ask')
print(res)
res = pat.match('asak') # .는 문자 하나만
print(res)
res = pat.match('a\nk') # \n 제외
print(res)

pat = re.compile('a.k', re.DOTALL) # 여러줄로 구성된 문자열에서 \n에 상관없이 검색하고자 할 때
res = pat.match('a\nk') # re.DOTALL은 . 옵션과 같지만 \n도 검색가능
print(res)

import re
pat = re.compile('[a-z]', re.I) # re.I 대소문자 상관없이 검색 가능
print(pat.match('test'))
print(pat.match('Test'))
print(pat.match('TEST'))

import re
pat = re.compile("python\s\w+") # python 뒤에 공백(줄바꿈)과 문자까지 검색
text = """python java
python c ruby r
seoul gangseo python
python one two three
"""
print(pat.findall(text))

import re
pat = re.compile("^python\s\w+", re.M) # ^만 있으면 첫째줄만 검색됨. 따라서 re M을 넣어서 multiline으로 검색
text = """python java
python c ruby r
seoul gangseo python
python one two three
"""
print(pat.findall(text))

import re
pat = re.compile("\w+\spython$", re.M) # $ python로 끝나는 단어 검색
text = """python java
python c ruby r
seoul gangseo python
python one two three
"""
print(pat.findall(text))


"""
한글 코드
가~힣

"""
import re
def hangulTest() :
    s = "大韓민국에서 살고 있어요. 한국어는 very nice해요. English 싫어요 @.@ㅋㅋㅋ "
    hangul = re.compile('[^ㄱ-ㅎ| 가-힣]+') # 한글, 띄어쓰기를 제외한 모든 글자
    res = hangul.findall(s)
    print(res)
hangulTest()

import re
def hangulTest() :
    s = "大韓민국에서 살고 있어요. 한국어는 very nice해요. English 싫어요 @.@ㅋㅋㅋ "
    hangul = re.compile('[^ㄱ-ㅎ| 가-힣]+') # 한글, 띄어쓰기를 제외한 모든 글자
    res2 = hangul.sub('', s) #s에 있는 문자 중 한글, 띄어쓰기를 제외한 모든 글자를 없애버려라
    print(res2)
hangulTest()

import re
#pat = re.compile('&[#](0[0-7]+);')
pat = re.compile("""
&[#](
0[0-7]+
)
;
""", re.VERBOSE)