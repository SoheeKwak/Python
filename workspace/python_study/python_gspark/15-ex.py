import numpy as np

#영어 성적을 기준으로 각 열(column)을 재정렬하라.
grade =np.array([
       [  1,    2,    3,    4], #학번
       [ 46,   99,  100,   71], #영어성적
       [ 81,   59,   90,  100]  #수학 성적
])
eng_indexer = np.argsort(grade[1], axis=0)
print(eng_indexer)
new_grade=grade[:,eng_indexer]
print(new_grade)

#실수로 이루어진 5 x 6 형태의 데이터 행렬
a = np.random.random((5,6))
print(a)
#1.전체의 최댓값
print(np.max(a))
#2.각 행의 합
print(np.sum(a, axis=1))
#3.각 열의 평균
print(np.mean(a,axis=0))



