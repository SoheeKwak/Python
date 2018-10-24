import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

fp = codecs.open("BEXX0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one("body > text")
text = body.getText() #순수하게 텍스트만 추출. 태그는 모두 제거됨
twitter = Twitter()
lines = text.split("\r\n")
results = []
for line in lines:
    malist = twitter.pos(line, norm=True, stem=True)
    res = []
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation", "Foreign"]:
            res.append(word[0])
    r1 = (" ".join(res)) #위에서 각 line에 대해서 형태소로 분리해 조사, 어미 등을 제외한 나머지를 한줄로 r1에 넣음
    results.append(r1)
    # print(results)
########################여기까지는 워드 추출##################################

#######################지금부터 워드->벡터화(워드 임베딩)######################

toji_file = "toji.data"
with open(toji_file, "w", encoding="utf-8") as fp:
    fp.write("\n".join(results))
data = word2vec.LineSentence(toji_file) #toji_file의 모든 내용을 읽어서 data에 저장
model = word2vec.Word2Vec(data, size=200, window=10, min_count=5, iter=10, sg=1)
#size:벡터의 차원, window:앞뒤로 참조하는 단어의 개수, 수치가 클수록 느려짐. 수치가 너무 크거나 너무 작아도 의미가 약해짐
#min_count:최소 30번 이상 등장한 단어들에 대해서만 임베딩, sg:CBOW(sg=0) 아니면 Skip-Gram(sg-1)중 택일
model.save("toji.model")
print("모델이 만들어 졌습니다")

#모델 불러오기
model = word2vec.Word2Vec.load("toji.model")
print(model.most_similar(positive=["집"]))
print(model.most_similar(negative=["밭"]))
print(model.most_similar(positive=["땅", "집"]))
