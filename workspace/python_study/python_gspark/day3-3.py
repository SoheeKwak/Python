import re

re.compile('\\white') # \white를 \w hite 로 혼동할 수 있으므로 \\ 중복 사용

pat = re.compile('Java|Python') # Java 또는 Python이 나오면 매칭
res = pat.match('Python')
print(res) #<_sre.SRE_Match object; span=(0, 6), match='Python'>
res = pat.match('Java')
print(res) #<_sre.SRE_Match object; span=(0, 4), match='Java'>
res = pat.match('JavaPython')
print(res) #<_sre.SRE_Match object; span=(0, 4), match='Java'>
res = pat.match('PythonJava')
print(res) #<_sre.SRE_Match object; span=(0, 6), match='Python'>
res = pat.match('PythonRuby')
print(res) #<_sre.SRE_Match object; span=(0, 6), match='Python'>
res = pat.match('RubyJava')
print(res) # None
res = pat.match('JavaRuby')
print(res) #<_sre.SRE_Match object; span=(0, 4), match='Java'>

print(re.search('How', 'How are you'))
print(re.search('are', 'How are you'))
print(re.match('are', 'How are you'))
print(re.search('^How', 'How are you'))
print(re.search('^are', 'How are you'))

print(re.search('you$', 'How are you'))
print(re.search('you$', 'How are you. Hi'))

pat = re.compile('(ABC)+') #ABC가 계속 반복되는 경우
res = pat.search('ABCABCABCDEFABCDED OK?')
print(res)
print(res.group())

pat = re.compile('(\w+)\s+((\d)+[-](\d)+[-]\d+)')
res = pat.search("kim 010-1234-5678")
print(res.group(1))
print(res.group(2))
print(res.group(3))
print(res.group(4))

pat = re.compile('(어제|오늘|내일)')
print(pat.sub('DAY', '어제 날씨 그리고 오늘')) # 웹 텍스트 스크래핑->치환/삭제(sub)
print(pat.sub('', '어제 날씨 그리고 오늘')) # 웹 텍스트 스크래핑->치환/삭제(sub)

pat = re.compile('(어제|오늘|내일)')
print(pat.sub('', '어제 날씨 그리고 오늘 날씨', count=1)) #1개 번경
print(pat.sub('', '어제 날씨 그리고 오늘 날씨', count=2)) #2개 번경

pat = re.compile("(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(pat.sub("\g<phone> \g<name>","kim 010-1234-5678"))
print(pat.sub("\g<2> \g<1>","kim 010-1234-5678"))


"""
정규표현식 예
^Test : Test로 시작하는 문자열
test$ : test로 끝나는 문자열
^xyz$ : xyz로 시작하고 끝나는 문자열(xyz도 해당)
abc : acb가 들어있는 문자열
ab* : a뒤에 b가 0개 이상 있는 문자열(a, ab, abbbbb)
ab? : b가 있을수도 없을 수도 있다(ab, a)
a?b+$: a는 있을수도 없을수도 있고, 그뒤에 반드시 한개 이상의 b로 끝남

ab{2} (abb)
ab{3, } (abbb.abbbbbb)
ab{2,4} (abb, abbb, abbbb)

a(bc)*: a뒤에 bc가 0번 이상 반복
a(bc){1,3} a뒤에 bc가 1번 이상 3번 이하 반복

hi|bye : hi또는 bye가 있는 문자열
(a|bc)de: ade 또는 bcde
(a|b)*c : a와 b가 뒤섞여서 0번 이상 반복, 그 뒤에 반드시 c (aababaaaaaac)

. : 한 문자
..: 두문자
...: 세문자
a.[0-9] : a뒤에 문자가 1개 있으면 그뒤에 숫자가 붙음
^.{3}$ : 반드시 3문자

[ab] : a|b
[a-d] : 소문자 a-d, a|b|c|d 또는 [abcd]
^[a-zA-Z] :영문자로 시작
[0-9]% : %문자 앞에 하나의 숫자가 있다
[a-zA-Z0-9]$ ; 숫자, 영문자로 끝남

XML : 확장가능한 마크업 언어 (사용자가 태그를 정의)
"""




