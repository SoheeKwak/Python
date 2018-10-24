from bs4 import BeautifulSoup
fp = open("fruits.html", mode="r", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
print(soup)

print(soup.select_one("li").string)
print(soup.select_one("li:nth-of-type(1)").string)

#과일 이름 모두 출력
myList = soup.select("li")
for li in myList:
 print(li.string)

pos1 = "li:nth-of-type("
pos2 = ")"
for i in range(9):
    pos = pos1 + str(i+1) + pos2
    print(soup.select_one(pos).string)

myList = soup.select("#ve-list > li")
for i in range(len(myList)):
    print(soup.select("#ve-list > li")[i].string)

print(soup.select("#ve-list > li:nth-of-type(1)"))
print(soup.select("#ve-list > li:nth-of-type(1)")[0].string) #select함수는 리턴결과가 리스트이므로, string 사용하려면 select()[0]으로 인덱스로 추출해 사용



from bs4 import BeautifulSoup
fp = open("fruits.html", mode="r", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
print(soup.select("#ve-list > li[data-lo='us']"))
print(soup.select("#ve-list > li[data-lo='us']")[0].string)

print(soup.select("#ve-list > li[class='black']"))
print(soup.select("#ve-list > li.black")) #클래스 속성은 .으로 표현

cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)
print(soup.find(id = "ve-list").find("li",cond).string)



