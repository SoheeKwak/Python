## PCA
import pandas as pd

df = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape']) #5차원 데이터('body_shape'sms y값)
df.loc[0] = [1200, 1, 0, 0, 2, 'Skinny']
df.loc[1] = [2800, 1, 1, 1, 1, 'Normal']
df.loc[2] = [3500, 2, 2, 1, 0, 'Fat']
df.loc[3] = [1400, 0, 1, 0, 3, 'Skinny']
df.loc[4] = [5000, 2, 2, 2, 0, 'Fat']
df.loc[5] = [1300, 0, 0, 1, 2, 'Skinny']
df.loc[6] = [3000, 1, 0, 1, 1, 'Normal']
df.loc[7] = [4000, 2, 2, 2, 0, 'Fat']
df.loc[8] = [2600, 0, 2, 0, 0, 'Normal']
df.loc[9] = [3000, 1, 2, 1, 1, 'Fat']

print(df)

X = df[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
print(X)
Y=df[['body_shape']]
print(Y) #실제값
## 스케일링
from sklearn.preprocessing import StandardScaler
x_std = StandardScaler().fit_transform(X) #'calory'가 다른 feature의 값들보다 너무 크므로 표준화
print(x_std)

import numpy as np
## 공분산
print(x_std.shape) #(10, 5)
features = x_std.T #Transpose:각 feature가 행 단위로 구성
print(features.shape)#(5, 10)
covariance_matrix = np.cov(features)
print(covariance_matrix) #첫번째 공분산[ 1.11111111  0.88379717  0.76782385  0.89376551 -0.93179808] 칼-칼(표준화한 칼로리값의 자기자신과의 분산이므로 1), 칼-아침, 칼-점심, 칼-저녁, 칼-운동간의 공분산

## 고유벡터, 고유값
eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
print("고유벡터를 출력:\n%s" % eig_vecs) #5차원이므로 고유벡터 5개 출력 [-0.508005   -0.0169937  -0.84711404  0.11637853  0.10244985] 1,2,3,4,5번째 고유벡터(1)칼이 변할때-아점저운이 변하는 정도,2)아-칼점저운, 3)점-칼아저운 4)저-칼아점운, 5)운-칼아점저

print("고유값을 출력:\n%s" % eig_vals)
print(eig_vals[0]/sum(eig_vals)) #0.7318321731427544: 원 데이터의 73%의 특성을 담을 수 있다(27%데이터 손실)

print(x_std.shape) #(10, 5) 5차원
print(eig_vecs.T)
print(eig_vecs.T[0])
print(eig_vecs.T[0].shape)#(5,)

projected_X = x_std.dot(eig_vecs.T[0]) #5차원 데이터를 1번째 고유벡터로 fitting(5차원->1차원)
print(projected_X) #df.loc[0] = [1200, 1, 0, 0, 2]가  2.22600943 로 바뀜, 각각의 축이 한개의 벡터로 바뀜

res = pd.DataFrame(projected_X, columns=['PC1'])
res['y-axis']=0.0
res['label']=Y
print(res)

import matplotlib.pyplot as plt
import seaborn as sns
sns.lmplot('PC1','y-axis',data=res, fit_reg=False, scatter_kws={"s":50}, hue='label')
plt.title('PCA result')
plt.show()  #5차원을 1차원으로 구현