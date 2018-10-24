# 1)텍스트-->학습-->모델
# 2)모델-->새로운 텍스트 입력-->분류 결과

import math, sys
from konlpy.tag import Twitter
class BayesianFilter: #클래스(변수, 함수)를 모듈(bayes.py)에 생성
    def __init__(self):
        print("생성자 함수")
        self.words=set() #중복이 안됨
        self.word_dict={}
        self.category_dict={}

    # 전달받은 text에 대한 형태소 분석
    def split(self, text):
        twitter=Twitter()
        malist=twitter.pos(text, norm=True, stem=True)
        # print(malist)
        results=[]
        for word in malist:
            if not word[1] in ["Josa", "Eomi", "Punctuation"]: #word[1]:형태소 형태
                results.append(word[0]) #word[0]: 형태소 단어
        return results

    # 단어를 카테고리에 추가
    def inc_word(self, word, category):
        # print(word, category)
        if not category in self.word_dict:  # category를 key로 word를 value로 해서 딕셔너리self.word_dict={}에 넣음
            self.word_dict[category]={}     # {}->{'광고':{}} 처음에 categorys인'광고'가 self.word_dict(아직 빈 딕셔너리)에 없으므로 key로 넣고, 그 value자리에 또다른 딕셔너리를 넣는다.즉,딕셔너리중첩{키1:{키a:값, 키b:값}, 키2:{키aa:값, 키bb:값}}
        if not word in self.word_dict[category]: # '광고'에 해당하는 value인 '파격'이 없으므로
            self.word_dict[category][word]=0  # {'광고':{'파격':0 }}파격값 초기화
        self.word_dict[category][word]+=1 # {'광고':{'파격':1 }{'세일':1}.., '중요':{}}
        self.words.add(word)
        # print("="*50)
        # print(self.word_dict)
        # print("="*50)
        # print(self.words)

    def category_prob(self, category):
        sum_categories = sum(self.category_dict.values()) #{'광고': 5, '중요': 5}에서 value값 총합
        category_v = self.category_dict[category] #5개: '광고'에 해당하는 단어들
        return category_v / sum_categories #'광고'=>5/10이 리턴, '중요'=>5/10이 리턴
    def score(self, words, category):
        score = math.log(self.category_prob(category))
        print("스코어:", score)
        for word in words:
            score +=math.log(self.word_prob(word, category))
        return score

    #카테고리 내부의 단어 출현 비율 계산
    def word_prob(self, word, category):
        n = self.get_word_count(word, category)+1 # n이 0일때를 피하기 위해 강제로 1을 줌.'광고', '중요' 에 검사하는 문장들이 기존의 단어들과 일치하는 횟수
        d = sum(self.word_dict[category].values())+len(self.words) #sum(self.word_dict[category].values()): 광고 카테고리에 속하는 단어들의 등장횟수 총합
        print(n/d)
        return n/d

    def get_word_count(self, word, category):
        if word in self.word_dict[category]:#word_dict딕셔너리 안에 '광고'키에 해당하는 value들('파격', '세', 일'...)
            return self.word_dict[category][word] #위에서 일치하는 단어가 있다면 해당 단어를 리턴
        else:
            return 0
    def predict(self, text):
        best_category = None
        words=self.split(text) # words=['재고', '정리', '할인', '무료', '배송']
        score_list=[]
        max_score=-sys.maxsize
        for category in self.category_dict.keys(): #category:'광고', '중요'
            score = self.score(words, category)    #각각의 카테고리에 대해['재고', '정리', '할인', '무료', '배송']와 score함수(광고메일인지 아닌지 확률을 구하는 계산) 수행
            score_list.append((category, score))
            if score > max_score:
                max_score = score
                best_category = category
        return  best_category, score_list



    def fit(self, text, category):   #텍스트를 읽어 학습
        word_list = self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)

    #카테고리 계산
    def inc_category(self, category):
         print("inc카테고리:")
         if not category in self.category_dict: #category_dict에 (광고, 중요)가 없다면
             self.category_dict[category]=0
         self.category_dict[category]+=1
         print(self.category_dict)



