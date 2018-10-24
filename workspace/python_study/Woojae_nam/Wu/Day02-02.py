# 시 또는 소설 등의 빅데이터에서 빈도분석하고 순위 매기기
inStr = """
님은 갔습니다. 아아 사랑하는 나의 님은 갔습니다.
푸른 산빛을 깨치고 단풍나무 숲을 향하여 난 적은 길을 걸어서 차마 떨치고 갔습니다.
황금의 꽃같이 굳고 빛나던 옛 맹서는 차디찬 티끌이 되어서 한숨의 미풍에 
날어갔습니다.
날카로운 첫 키스의 추억은 나의 운명의 지침(指針)을 돌려 놓고 뒷걸음쳐서 
사라졌습니다.
나는 향기로운 님의 말소리에 귀먹고 꽃다운 님의 얼굴에 눈멀었습니다.
사랑도 사람의 일이라 만날 때에 미리 떠날 것을 염려하고 경계하지 아니한 
것은 아니지만, 이별은 뜻밖의 일이 되고 놀란 가슴은 새로운 슬픔에 터집니다.
그러나 이별을 쓸데없는 눈물의 원천을 만들고 마는 것은 스스로 사랑을 깨치는 
것인 줄 아는 까닭에, 걷잡을 수 없는 슬픔의 힘을 옮겨서 새 희망의 정수
박이에 들어부었습니다.
우리는 만날 때에 떠날 것을 염려하는 것과 같이 떠날 때에 다시 만날 것을 
믿습니다.
아아 님은 갔지마는 나는 님을 보내지 아니하였습니다.
제 곡조를 못 이기는 사랑의 노래는 님의 침묵을 휩싸고 돕니다.
"""
# 한글 글자의 빈도수를 출력하고, 많은 빈도수의 차례대로 순위를 매기기(동일 순의 처리하기)
import operator
countDic = {}
countList = []

if __name__ == "__main__":
    for ch in inStr:
        if '가'<= ch and ch <= '힣':
            if ch in countDic:
                countDic[ch] +=1
            else:
                countDic[ch] = 1
    countList = sorted(countDic.items(), key=operator.itemgetter(1),reverse=True)
    for i in range(0, len(countList)):
        print(countList[i][0],'\t', countList[i][1])



# 단어들에 대한 빈도수 처리하기
from konlpy.tag import Okt
import  codecs
from bs4 import BeautifulSoup
okt = Okt()
soup = BeautifulSoup(inStr, "html.parser")
text = soup.getText()

lines = text.split("\r\n")
word_dic = {}
for line in lines:
    malist = okt.pos(line)
    for word in malist:
        #print(word[1]) word[1]은 품사, word[0]은 단어
        if word[1]=="Noun": #품사가 명사라면..
            if not word[0] in word_dic:
                word_dic[word[0]] = 0 #명사 키가 없다면 딕셔너리에 추가하고 키값으로 0을 줘서 초기화(갯수이므로 []대신 0)
            word_dic[word[0]] +=1
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
print(keys)

print("="*100)
###라이브러리 없이 빈도수 출력
strList = inStr.split()
countDic = {}
for data in strList:
    if data[-1] in ['.',',','가','는','이','은','에','를','을']:
        data = data[:-1]
    if data in countDic:
        countDic[data] += 1
    else:
        countDic[data] = 1
print(countDic)
