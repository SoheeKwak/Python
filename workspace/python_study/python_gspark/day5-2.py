import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

search_addr = "http://book.daum.net/search/bookSearch.do?query="
# search_word = "파이썬"
# search_word_enc = urllib.parse.quote(search_word) # 한글을 유니코드로 인코딩
# print(search_word_enc)
# url = search_addr+search_word_enc
#
# response = req.urlopen(url)
# #print(response)
#
# html_data = response.read()
# #print(html_data)
# data = BeautifulSoup(html_data, 'html.parser')
# print(data)



# 파이썬, 자바, 자바스크립트 한꺼번에 검색

import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

search_addr = "http://book.daum.net/search/bookSearch.do?query="
search_word = ['파이썬', '자바', '자바스크립트']
for word in search_word :
    search_word_enc = urllib.parse.quote(word) # 한글을 유니코드로 인코딩
    url = search_addr+search_word_enc
    html_data = req.urlopen(url).read()
    data = BeautifulSoup(html_data, 'html.parser')
    # print(data)
    # print("="*70)

    res = data.select("#page_body > form > ul > li > dl > dd.price > div > span.prc > strong") #가격만 출력
    print(res)
    for r in res:
        print(r.string)

    title = data.select("#page_body > form > ul > li > dl > dt > a") # 제목만 출력
    print(title)
    for t in title:
        print(t.string)


