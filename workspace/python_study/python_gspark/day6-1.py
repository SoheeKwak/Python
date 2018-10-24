from konlpy.tag import Twitter
import  codecs
from bs4 import BeautifulSoup

twitter = Twitter() #twitter라는 객체 형성
# mlist = twitter.pos("나는 오늘 상공회의소에서 한국어 처리" #pos: 형태소 분석해주는 함수
# "관련 학습을 하고 있습니다. 재밌어욬ㅋㅋ 그래욬ㅋㅋ", norm=True, stem=True)
# print(mlist)
#
# mlist2 = twitter.pos("아버지가방에 들어가신다")
# print(mlist2)

#############여기서부터 토지 파일  형태소 분석 작업 코드###################################

fp = codecs.open("TOJI1.txt", "r", encoding="ms949") #encoding방식은 utf-16, utf-8, euc-kr, ms949 중에 선택
soup = BeautifulSoup(fp, "html.parser")
# print(soup)
text = soup.getText()
# print(text)

twitter = Twitter()
lines = text.split("\r\n")
word_dic = {}
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        #print(word[1]) word[1]은 품사, word[0]은 단어
        if word[1]=="Noun": #품사가 명사라면..
            if not word[0] in word_dic:
                word_dic[word[0]] = 0 #명사 키가 없다면 딕셔너리에 추가하고 키값으로 0을 줘서 초기화(갯수이므로 []대신 0)
            word_dic[word[0]] +=1
print(word_dic)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
            # word_dic.items() 단어들을 x에 대입하여 그에 대한 횟수 x[1], 즉 값을 기준으로 내림차순으로 정리
            # import operator
            # keys = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)
print(keys)
# for word, count in keys[:50]: #상위 50개 출력
#     print("{0}({1})".format(word, count), end="")
# print()


#Word2Vec으로 문장을 벡터로 변환하여 작업수행
#ex)영화 평, 갤럭시 사용후기 등
# 1)워드임베딩: 단어를 벡터공간에 표현
# 2)워드임베딩을 수행하면, 단어의 문맥적 의미가 보존이 됨 ->각 단어들 간 유클리디안 거이, 코사인 유사도 이용해 거리 계산
# 3)거리가 가까울 수록 의미가 비슷한 단어


