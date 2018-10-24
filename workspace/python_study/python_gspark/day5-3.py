from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename) #openurl과 같은 기능. url을 savename이라는 이름으로 가져옴
xml = open(savename, mode="r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

info = {} #딕셔너리
for location in soup.find_all("location"):
   name = location.find('city').string
   weather = location.find('wf').string
   if not(weather in info):
       info[weather] = [] # info={'구름조금':[]} 키(날씨)가 없다면 키와 함께 값을 넣을 빈 리스트 생성.이미 있다면 if를 무시하고 아래 해당 키에 도시만 추가. 키는 무조건 하나만 존재하므로
   info[weather].append(name) #if와 상관없이 무조건 해당키(날씨)에 대한 값(도시명)을 추가한다.
for w in info:
    print("+", w)
    for name in info[w]:#info[w]는 키w에 해당하는 값
        print("|-",name)



