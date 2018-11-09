#Recommender System(collaborative filtering)
#사용자 기반, 아이템 기반 필터링(사용자 수가 적거나 아이템이 적어서 의미있는 데이터를 추출하기 어려울 때)
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus']=False #한글 깨짐 방지
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from math import sqrt
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font',family=font_name)

critics = {'BTS':{'암수살인':5, '바울':4,'할로윈':1.5},
           '손흥민':{'바울': 5, '할로윈': 2},
           '조용필':{'암수살인': 2.5, '바울': 2, '할로윈': 1},
           '나훈아':{'암수살인': 3.5, '바울': 4, '할로윈': 5}}
print(critics.get('BTS').get('바울'))

# print(pow(3,2)) #3의 제곱
def sim(i,j): #전달된 두 데이터의 유사도를 리턴하는 함수
    #i:x2-x1, j:y2-y1이 전달됨
    return sqrt(pow(i,2)+pow(j,2))
#손흥민과 나훈아 사이의 거리를 구하고 싶다.
#피타고라스 정리: 거리가 가까울수록 유사도가 높다.

var1 = critics['손흥민']['바울']-critics['나훈아']['바울']
var2 = critics['손흥민']['할로윈']-critics['나훈아']['할로윈']
print(sim(var1, var2))
print("="*50)
print("손흥민 기준으로 다른 사람과의 유사도 측정(거리이므로 값이 작을수록 유사도가 크다)")
for i in critics:
    # print(i) #i는 키
    if i !='손흥민':
        var1 = critics['손흥민']['바울'] - critics[i]['바울']
        var2 = critics['손흥민']['할로윈'] - critics[i]['할로윈']
        print(i,"와 손흥민의 유사도:",sim(var1, var2))

print("="*50)
for i in critics:
    if i !='손흥민':
        var1 = critics['손흥민']['바울'] - critics[i]['바울']
        var2 = critics['손흥민']['할로윈'] - critics[i]['할로윈']
        print(i,"와 손흥민의 유사도:",1/(1+sim(var1, var2)))
print("손흥민 기준으로 다른 사람과의 유사도 측정(값이 클수록 유사도가 크다)")

#두 점 사이의 거리
#항목(영화) 데이터가 2종류(두 편)인 경우 ->피타고라스 공식
#항목(영화) 데이터가 여러 종류(여러 편)인 경우 ->유클리디안 거리 공식
print("="*50)
#유클리디안 거리 기반 두 데이터 사이의 거리
def sim_distance(data, name1, name2):
    sum = 0
    for i in data[name1]: #손흥민이 본 영화들
        if i in data[name2]:#나훈아와 같은 영화를 봤다면
            sum +=pow(data[name1][i]-data[name2][i],2)
    return 1/(1+sqrt(sum)) #값이 클수록 유사도 높다
print(sim_distance(critics, '손흥민','나훈아'))

#손흥민과 나머지 전체 관객과의 평점간 거리(유클리디안)
def matchf(data, name, idx=3, sim=sim_distance):
    myList = []
    for i in data:
        if i!=name: #손흥민, 본인이 아닌 경우라면
            myList.append((sim(data, name, i),i)) #data:critics, name:손흥민, i:손흥민 외 나머지 전체 관객
            myList.sort()
            print("정렬:",myList)
            myList.reverse()
            print("역순:", myList)
    # print(len(myList))
    return myList[:idx]
print(matchf(critics, '손흥민'))
#손흥민과 나머지 전체 관객과의 평점간 거리를 내림차순으로 정렬
li = matchf(critics, '손흥민')
print(li)

def barchart(data, labels):#유사도(손흥민과의), 이름(손흥민 외 나머지 관객들)
    positions = range(len(data))
    print(positions) #range(0, 3)
    plt.barh(positions, data, height=0.5, color='r')
    plt.yticks(positions,labels)
    plt.xlabel('similarity')
    plt.ylabel('name')
    # plt.show()
score=[]
names=[]
for i in li:
    score.append(i[0])
    names.append(i[1])
barchart(score,names)

plt.figure(figsize=(14,8))#14,8인치
plt.plot([1,2,3],[1,2,3],'g^')
plt.text(1,1,'자동차')
plt.text(2,2,'버스')
plt.text(3,3,'열차')
plt.axis([0,6,0,6])#x,y축에 대한 크기를 재설정
plt.show()




