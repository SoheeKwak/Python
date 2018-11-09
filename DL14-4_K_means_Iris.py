from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
# print(iris)
labels = pd.DataFrame(iris.target)

labels.columns=['labels']
print(labels)

data = pd.DataFrame(iris.data)
data.columns = ["Sepal.Length","Sepal.Width","Petal.Length","Petal.Width"]
print(data)
data = pd.concat([data, labels],axis=1)
print(data)

feature = data[["Sepal.Length","Sepal.Width"]]
print(feature.head(10))
print(feature.tail())

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

model = KMeans(n_clusters=3, algorithm='auto')
model.fit(feature) #data로 모델 생성

predict = pd.DataFrame(model.predict(feature))
predict.columns = ['predict']
print(predict)
r = pd.concat([feature, predict], axis=1)
print(r)

import matplotlib.pyplot as plt
plt.scatter(r['Sepal.Length'],r['Sepal.Width'],c=r['predict'],alpha=0.5)


centers = pd.DataFrame(model.cluster_centers_, columns=['Sepal.Length','Sepal.Width'])
print(centers)

center_x = centers['Sepal.Length']
center_y = centers['Sepal.Width']
plt.scatter(center_x, center_y, s=50, marker='D', c='r')
            #x좌표,   y좌표,    크기, 마커,       색상
plt.show()


#############################################################################
from sklearn.pipeline import make_pipeline
#make_pipeline메서드는 scaler와 kmeans를 순차적으로 실행시키는 기능을 수행
from sklearn.preprocessing import StandardScaler #표준화
model = KMeans(n_clusters=3) #K-means를 수행할 수 있는 객체를 생성. 클러스터를 3개로 만드는 모델 변수를 정의(아직 모델을 만든 게 아님)
scaler = StandardScaler() #데이터를 표준화 한 후
pipeline = make_pipeline(scaler, model) #모델 생성
pipeline.fit(feature) #데이터와 모델 피팅

predict = pd.DataFrame(pipeline.predict(feature))
ks = range(1,10)
inertias = []
for k in ks:
    model=KMeans(n_clusters=k) #클러스터를 1~10개까지 모델을 만듦
    model.fit(feature) #위에서 만든 모델을 feature에 피팅
    inertias.append(model.inertia_) #inertia_: inertia value를 이용해서 적정 수준의 클러스터 개수를 파악,
plt.plot(ks, inertias, '-o')
plt.xlabel('numbers of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
ct = pd.crosstab(data['labels'],r['predict'])
print(ct)
