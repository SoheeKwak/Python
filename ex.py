import matplotlib as mpl
mpl.rcParams['axes.unicode_minus']=False #한글 깨짐 방지
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from math import sqrt
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font',family=font_name)

critics = {
    '조용필': {
        '택시운전사': 2.5,
        '겨울왕국': 3.5,
        '리빙라스베가스': 3.0,
        '넘버3': 3.5,
        '사랑과전쟁': 2.5,
        '세계대전': 3.0,
    },
    'BTS': {
        '택시운전사': 1.0,
        '겨울왕국': 4.5,
        '리빙라스베가스': 0.5,
        '넘버3': 1.5,
        '사랑과전쟁': 4.5,
        '세계대전': 5.0,
    },
    '강감찬': {
        '택시운전사': 3.0,
        '겨울왕국': 3.5,
        '리빙라스베가스': 1.5,
        '넘버3': 5.0,
        '세계대전': 3.0,
        '사랑과전쟁': 3.5,
    },
    '을지문덕': {
        '택시운전사': 2.5,
        '겨울왕국': 3.0,
        '넘버3': 3.5,
        '세계대전': 4.0,
    },
    '김유신': {
        '겨울왕국': 3.5,
        '리빙라스베가스': 3.0,
        '세계대전': 4.5,
        '넘버3': 4.0,
        '사랑과전쟁': 2.5,
    },
    '유성룡': {
        '택시운전사': 3.0,
        '겨울왕국': 4.0,
        '리빙라스베가스': 2.0,
        '넘버3': 3.0,
        '세계대전': 3.5,
        '사랑과전쟁': 2.0,
    },
    '이황': {
        '택시운전사': 3.0,
        '겨울왕국': 4.0,
        '세계대전': 3.0,
        '넘버3': 5.0,
        '사랑과전쟁': 3.5,
    },
    '이이': {'겨울왕국': 4.5, '사랑과전쟁': 1.0,
           '넘버3': 4.0},
}


def sim_pearson(data, name1, name2):
    #피어슨 상관계수
    #x와 y가 함께 변하는 정도(공분산)
    # /
    # (x가 변화는정도*y가 변하는정도)
    sumX=0 #x의 합
    sumY=0 #y의 합
    sumPowX=0 #x 제곱의 합
    sumPowY=0 #y 제곱의 합
    sumXY=0 #x*y의 합
    count=0 #영화의 개수(n)

    for i in data[name1]:
        if i in data[name2]:#BTS와 유성룡이가 모두 본 영화
            sumX+=data[name1][i]#BTS의 i영화에 대한 평점
            sumY+=data[name2][i]#유성룡의 i영화에 대한 평점
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i], 2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1

    return (sumXY-((sumX*sumY)/count))/ \
           sqrt((sumPowX- (pow(sumX,2)/count))*
                (sumPowY- (pow(sumY,2)/count)))


print("BTS와 유성룡 피어슨 상관계수:",sim_pearson(critics,'BTS', '유성룡'))
print("이황과 조용필 피어슨 상관계수:",sim_pearson(critics,'이황', '조용필'))

#딕셔너리를 수행하면서 기준(BTS)과 다른 데이터(사람)와의
#상관계수를 구해보자. => 내림차순 정렬
def top_match(data, name, index=2,
              sim_function=sim_pearson):
#data:영화평점딕셔너리, name:기준이 되는 사람의 이름
#index:피어슨 상관계수에서 상위(가장 가까운) 몇명을 추출
#피어슨 함수 호출 지정
    li=[]
    for i in data: #전체 영화를 돌겠다
        if name != i: #자신이(BTS) 아니라면
            li.append((sim_function(data, name, i),i))
    li.sort()
    li.reverse()
    return li[:index]
#BTS와 성향이 가장 비슷한 3명 추출
print(top_match(critics, 'BTS', 5))

#영화를 추천하는 시스템 구성, 예상되는 평점 출력
"""
*추천 시스템 구성 순서*
1)자신을 제외한 나머지 사람들과의 평점에대한 유사도를 구함.
BTS와 강감찬의
추측되는 평점 = 유사도*(다른 사람의)영화평점
 0.7  *(강감찬)4
2) 추측되는 평점들의 총합을 구함
3) 추측되는 평점들의 총합/유사도의 총합 =>모든 사람들을
근거로 했을때 예상되는 평점이 추출됨.
4) 아직 안본 영화를 대상으로 예상되는 평점을 구하여,
예상되는 평점이 가장 높은 영화를 추천하자.

"""

def getRecommendataion(data, person,
                       sim_function=sim_pearson):
    li=[] #최종적으로 결과를 리턴하는 리스트
    score_dic={}#유사도의 총합을 저장하기 위한 딕셔너리
    sim_dic={} #평점의 총합을 저장하기 위한 딕셔너리
    score=0
    result=top_match(data, person, len(data))
    print("중간:",result)
    for sim, name in result:   #유사도, 이름
        if sim<0 : continue #유사도 0보다 작으면 빼자
        for movie in data[name]:
            if movie not in data[person]:#이이가 안본영화
                score+=sim*data[name][movie]
                #score변수에 누적<-유사도 * 이이가 아닌 다른 사람의 영화평점
                score_dic.setdefault(movie,0)
                score_dic[movie]+=score#평점 총합

                #유사도의 누적합
                sim_dic.setdefault(movie,0)
                sim_dic[movie]+=sim
            score=0


        #     print(name," movie:",movie)
        # print("==============")

    for key in score_dic:
        score_dic[key]=score_dic[key]/sim_dic[key] #평점 총합/유사도 총합
        li.append((score_dic[key], key))
    li.sort()
    li.reverse()
    return li[0][1]

print("이이 님에게는 ",getRecommendataion(critics, '이이'),"영화를 가장 추천합니다")
#기준이되는 사람이 '이이'가 안본 영화를 추출
#안본 영화 각각에 대한 예상 평점을 준다
#예상 평점이 가장 큰 영화를 추천하자






# movie="가나다라"
# score_dic={}
# score_dic.setdefault(movie,0)
# print(score_dic)
# 출력 결과 ==>  {'가나다라': 0}

