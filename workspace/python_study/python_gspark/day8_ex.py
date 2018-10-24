# 1. 기사 스크랩
# 2. 날씨 본문 내용을 텍스트 파일로 저장(d8output.txt)
from bs4 import BeautifulSoup
import urllib.request as req

OUTPUT_FILE_NAME = 'd8output.txt'
URL = "http://www.newsis.com/view/?id=NISX20180816_0000392289&cID=10401&pID=10400"

def get_text(URL):
    print(URL)
    sourceFromURL = req.urlopen(URL)
    soup = BeautifulSoup(sourceFromURL, 'lxml', from_encoding='utf-8')
    text=""
    for item in soup.find_all('div', id='textBody'):
        text = text+str(item.find_all(text=True))
    return text

def main():
    open_output_file = open(OUTPUT_FILE_NAME, "w")
    res = get_text(URL)
    open_output_file.write(res)
    open_output_file.close()

if __name__ == '__main__':
    main()


# 3. 데이터 정제(크리닝)-영어, 특수기호 제거(정규식)
# 4. 정제된 결과를 텍스트 파일로 저장(d8output_cleaned.txt)
import re

INPUT_FILE_NAME = "d8output.txt"
OUTPUT_FILE_NAME = "d8output_cleaned.txt"

def clean_text(myText):
    cleaned_text = re.sub('[a-zA-Z]', '', myText)
    cleaned_text = re.sub('[\{\}\[\]\(\)【】\\\.,…@\'\"=]', '', cleaned_text)
    return cleaned_text

def main():
    read_file = open(INPUT_FILE_NAME, "r")
    write_file = open(OUTPUT_FILE_NAME, "w")
    text = read_file.read()
    print("before:")
    print(text)
    cleaned_text = clean_text(text)
    print("after:")
    print(cleaned_text)
    write_file.write(cleaned_text)
    read_file.close()
    write_file.close()

if __name__ == "__main__":
    main()


# 5. 정제된 파일을 읽어서 형태소 분석->명사추출->빈도수
# 6. 명사로 구성된 단어별 빈도수를 텍스트 파일로 저장(d8output_final.txt)
from konlpy.tag import Twitter
from collections import Counter

def get_tags(gtext, ntags=30):
    twitter=Twitter()
    nouns = twitter.nouns(gtext)
    count = Counter(nouns)
    return_list = []
    for word, cnt in count.most_common(ntags):
        temp = {'tag':word, 'count':cnt}
        return_list.append(temp)
    return return_list

def main():
    text_file_name = "d8output_cleaned.txt"
    noun_count = 30
    output_file_name = "d8output_final.txt"
    open_text_file = open(text_file_name, "r")
    text = open_text_file.read()
    res = get_tags(text, noun_count)
    open_text_file.close()

    open_output_file = open(output_file_name, "w")
    for data in res:
        noun = data['tag']
        count = data['count']
        open_output_file.write("{} {}\n".format(noun, count))

if __name__ =='__main__':
    main()


# 7. 상위 10개에 해당하는 단어를 시각화
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system()=="Windows":
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

f = open("d8output_final.txt", "r")
i = 1
news_word = []
word_cnt = []
while True:
    line = f.readline()
    word, count = line.split(" ")
    news_word.append(word)
    word_cnt.append(int(count))
    if i ==10: break
    i +=1
f.close()
print(news_word)
print(word_cnt)

xs = [i for i, _ in enumerate(news_word)]
print(xs)
plt.bar(xs,word_cnt) # x, y 좌표로 구현된 bar
plt.ylabel('등장 단어의 수')
plt.title('경제부총리 상공회의소 방문 기사 키워드')
plt.xticks([i for i, _ in enumerate(news_word)], news_word)
plt.show()


