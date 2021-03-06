from bs4 import BeautifulSoup
import urllib.request as req
import re

############ 기사 두 개 텍스트 추출#########################

url = "http://news.hankyung.com/article/201808140286g"
res = req.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(res, 'html.parser')
article = soup.select("#newsView")
pat = re.compile("[^가-힣]+")
arc = pat.sub("", (article)[0].text)

url2 = "http://news.kbs.co.kr/news/view.do?ncd=4024445&ref=A"
res2 = req.urlopen(url2).read().decode('utf-8')
soup2 = BeautifulSoup(res2, 'html.parser')
article2 = soup2.select("#cont_newstext")
pat = re.compile("[^가-힣]+")
arc2 = pat.sub("", (article2)[0].text)


############ 두 기사 간 유사도 조사 #########################

def ngram(s,num):
    res = [s[i:i+num] for i in range(len(s)-num+1)]
    return res

def diff_ngram(sarc, sarc2, num):
    arc = ngram(sarc, num)
    arc2 = ngram(sarc2, num)
    cnt=0
    r=[]
    for i in arc:
        for j in arc2:
            if i==j:
                cnt+=1
                r.append(i)
    return  cnt / len(arc), r


#2-gram
same = diff_ngram(arc,arc2, 2)
print("2-gram", same)

#3-gram
same = diff_ngram(arc,arc2, 3)
print("3-gram", same)