from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import re
url = "http://www.cgv.co.kr/movies/"
savename = "movie.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
xml = open(savename, mode="r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

rank = {}
for score in soup.find_all("div","box-contents"):
   name = score.find("strong","title").string
   review = score.find("span","percent")
   # pattern=r"^\w"
   # res=re.match(pattern,review)
   # print(res)
   if not(review in rank):
       rank[review] = []
   rank[review].append(name)
for r in rank:
    print("+", r)
    for name in rank[r]:
        print("|-",name)