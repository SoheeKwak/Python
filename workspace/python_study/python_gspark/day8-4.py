# 7. 상위 10개에 해당하는 단어를 시각화

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system()=="Windows": #시각화 시 한글이 깨지는 문제 해결 (malgun부분만 조정하고, 나머지는 그대로 씀)
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

f = open("output_final.txt", "r")
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

xs = [i for i, _ in enumerate(news_word)]  #i, _ 언더바는 i 뒤의 두번째 인수는 무시하라는 의미(만약 _, i면 앞의 인수를 무시하란 의미), enumerate은 하나하나 읽어간다는 의미
print(xs)                                   # 즉, news_word 리스트에서 word는 무시하고 index(0~9)만 출력하라
plt.bar(xs,word_cnt) # x, y 좌표로 구현된 bar
plt.ylabel('등장 단어의 수')
plt.title('오늘의 날씨 키워드')
plt.xticks([i for i, _ in enumerate(news_word)], news_word)
plt.show()

# myName = ['kim', 'Park', 'Lee']
# for _, name in enumerate(myName):
#     print(name)
# for i, _ in enumerate(myName):
#     print(i)
# v = [i for _, name in enumerate(myName)]
# print(v)