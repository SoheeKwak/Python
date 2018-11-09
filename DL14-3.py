## KNN 모델 : 새로운 선수는 기존의 nba 어느 선수와 닮았나?
import pandas
import math

with open('nba_2013.csv','r') as csvfile:
    nba = pandas.read_csv(csvfile)
# print(nba)
# print(nba.columns)

#string값을 가진 feature(컬럼) 제거
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga',
       'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft',
       'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf',
       'pts']
print(len(distance_columns))
selected_player = nba[nba["player"]=="LeBron James"].iloc[0]
print(selected_player)
def euclidian_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value+=(selected_player[k]-row[k])**2
    return math.sqrt(inner_value)

Lebron_distance = nba.apply(euclidian_distance, axis=1) #선수 한명한명의 데이터에 euclidian_distance함수를 적용
print(Lebron_distance)

nba_numeric = nba[distance_columns]
print(nba_numeric)
nba_normalized = (nba_numeric-nba_numeric.mean())/nba_numeric.std()  #특정값이 너무 크거나 작으면 문제가 되므로 정규화
print(nba_normalized)

from scipy.spatial import distance
nba_normalized.fillna(0, inplace=True)# inplace=True:기준 객체(nba_normalized)에 저장된 값을 바꾸겠다.
Lebron_normalized = nba_normalized[nba["player"]=="LeBron James"]

euclidean_distances = nba_normalized.apply(lambda row:distance.euclidean(row, Lebron_normalized),axis=1) #distance.euclidean 함수 적용, row모든 선수들
print(euclidean_distances)

distance_frame = pandas.DataFrame(data={"dist":euclidean_distances,
                       "idx":euclidean_distances.index})
print(distance_frame)

distance_frame.sort_values("dist", inplace=True)
print(distance_frame) #Lebron 자신을 포함한(제일 상위)거리가 가장 가까운 선수 순으로 출력
print(distance_frame.iloc[1])
print(distance_frame.iloc[1]["idx"])
## distance_frame.iloc[:2, 2]
# second_smallest = distance_frame.iloc[1]["idx"]
# most_similar_to_Lebron = nba.loc[int(second_smallest)]["player"]
# print("가장 비슷한 성적의 선수:", most_similar_to_Lebron)