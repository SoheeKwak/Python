from bs4 import BeautifulSoup
html = """
<html><body>
    <ul>
        <li>
        <a href="http://www.naver.com">naver</a>
        </li>
        <li>
        <a href="http://www.daum.net">daum</a>
        </li>
    </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
link = soup.find("a")
print(link)
link2 = soup.find_all("a")
print(link2)
for i in link2:
    # print(i)
    myhref = i.attrs['href']
    print(myhref)
    text = i.string
    print(text, "-->", myhref)

from bs4 import BeautifulSoup
html="""
<html><body>
<h1>빅데이터 분석</h1>
<p>데이터 수집</p>
<p>데이터 전처리</p>
<p>데이터 마이닝</p>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.h1
print(h1)
h1 = soup.body.h1
print(h1)
h1 = soup.html.body.h1
print(h1)

p1 = soup.html.body.p
print(p1.string)
p2 = p1.next_sibling.next_sibling
print(p2)
p3 = p2.next_sibling.next_sibling
print(p3)


from bs4 import BeautifulSoup
import urllib.request as req

url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')
p = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string
print("krw/usd=",p)


html = """
<html><body>
<div id = "test">
<h1>빅데이터 분석</h1>
<ul class = "lec">
<li>파이썬</li>
<li>머신러닝</li>
<li>통계분석</li>
</ul>
</div>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
print(soup)
res = soup.select_one("#test > h1").string
print(res)

res = soup.select_one("div#test > ul.lec > li").string
print(res)
res = soup.select_one("li").string
print(res)

res = soup.li
res2 = res.next_sibling.next_sibling
res3 = res2.next_sibling.next_sibling
print(res.string)
print(res2.string)
print(res3.string)

myList = soup.select("div#test > ul.lec > li")
for li in myList:
    print(li.string)

test = soup.find(id = "test")
print(test)


