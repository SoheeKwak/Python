#웹의 컨텐츠를 가져오기 위한 라이브러리
import urllib.request as req

url = "http://www.kccistc.net/images/layout/logo_09000_1.png"
savename = "test2.png"
mem = req.urlopen(url).read()

with open(savename, mode="wb") as f: #f=open(savename, mode="wb"), f.close()와 같음
    f.write(mem)
    print("저장되었습니다")
print(type(mem))

req.urlretrieve(url,"test.png")
print("이미지가 저장되었습니다.")


import urllib.request as req
url = "http://www.kccistc.net"
mem = req.urlopen(url).read()
text = mem.decode("utf-8")
print(text)


import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

api = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId':'108'
}
params = urllib.parse.urlencode(values)
#print(params)
url = api + "?" + params
#print("url=", url)

data = req.urlopen(url).read().decode("utf-8")
#print(data)

soup = BeautifulSoup(data, 'html.parser')
#print(soup)

wf = soup.find("title").string # <title> 태그 안에 내용만 나오게 할 때 string을 붙임
print(wf)



