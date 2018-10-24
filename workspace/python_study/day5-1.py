import re
from bs4 import BeautifulSoup
html = """
<ul>
    <li> <a href="www.naver.com">naver</a></li>
    <li> <a href="https://www.naver.com">naver</a></li>
    <li> <a href="https://www.daum.net">daum</a></li>
    <li> <a href="http://www.naver.com">naver</a></li>
</ul>
"""
soup = BeautifulSoup(html, 'html.parser')
#정규식으로 href속성이 https인 것만 추출
li = soup.find_all(href=re.compile("^https://"))
print(li)
for e in li:
    print(e.attrs['href'])

#상대 경로로  웹주소를 지정하는 방법
from urllib.parse import urljoin
base = "http://example.com/html/a.html"
print(urljoin(base, "b.html"))
print(urljoin(base, "sub/c.html")) #"http://example.com/html/sub/c.html" 이 서브 주소를 갖고 오고 싶을때
print(urljoin(base, "../index.html")) #http://example.com/index.html 베이스 주소의 상위주소를 갖고 올때
print(urljoin(base, "../img.sky.png")) #http://example.com/img.sky.png
print(urljoin(base, "http://other.com/test"))
print(urljoin(base, "//other.com/test")) #앞에 매칭되는 게 없을 때 베이스 주소가 무시됨

#파이썬으로 사이트 로그인 -> 개인 정보를 추출 -> 화면 출력
import requests
USER = "july"
PASS = "ks"
session = requests.session() #세션 객체 생성
#세션? 서버와 클라이언트가 연결
#클라이언트에서 서버에 데이터를 전달하기 위한 목적으로 연결할 때 SESSION 사용
login_info = {
    "m_id":USER,
    "m_passwd":PASS
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
# print(res)
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
# print(res)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span").string
print("마일리지:"+str(mileage))
ecoin = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").string
print("이코인:"+ecoin)



