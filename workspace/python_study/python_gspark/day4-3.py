from bs4 import BeautifulSoup
fp = open("color.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("#gr").string)

sel = lambda q: print(soup.select_one(q).string)
#def sel(q)
sel("#gr")
sel("li#gr")
sel("ul > li#gr")
sel("#mycolor #gr")
sel("#mycolor > #gr")
sel("ul#mycolor > li#gr")
sel("li[id='gr']")
sel("li:nth-of-type(4)")
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
#print(soup)

alist = soup.select("#mw-content-text > div > ul > li > ul > li > a") #mw-content-text > div > ul:nth-child(6) > li > ul > li:nth-child(1) > a
for a in alist:
    print(a.string)

myurl = "https://news.sbs.co.kr/news/endPage.do?news_id=N1004883739&plink=TOPHEAD&cooper=SBSNEWSMAIN"
res9 = req.urlopen(myurl).read().decode('utf-8')
soup9 = BeautifulSoup(res9, 'html.parser')
article = soup9.select("#container > div.w_inner > div.w_article > div.w_article_cont > div.w_article_left > div.article_cont_area > div.main_text > div")
print(article)

import re
pat = re.compile('[^ 가-힣]+')
result = pat.sub('', res9)
print(result)

nyurl = "https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10405&docId=307066785&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=4&search_sort=0&spq=1"
res8 = req.urlopen(nyurl).read().decode('utf-8')
soup8 = BeautifulSoup(res8, 'html.parser')
question = soup8.select("#qna_detail_question > div.end_question._end_wrap_box")
question = str(question[0])
import re
pat = re.compile('[^가-힣ㅏ-ㅣ]+')
preQuestion = pat.sub(' ', question)
print(preQuestion)
