from sklearn import datasets
import pandas as pd
iris=datasets.load_iris()
#print(iris)
labels=pd.DataFrame(iris.target)
labels.columns=['labels']
#print(labels)

data=pd.DataFrame(iris.data)
data.columns=['Sepal_Length','Sepal_width',
              'Petal_Length','Petal_width']
print(data)
print("="*50)
print(labels)
print("="*50)

data=pd.concat([data,labels],axis=1)
print(data)
print("="*50)
feature=data[['Sepal_Length','Sepal_width']]
print(feature.head(10))

from sklearn.cluster import KMeans
import matplotlib.pyplot as plot

model=KMeans(n_clusters=3, algorithm='auto')
model.fit(feature)

predict=pd.DataFrame(model.predict(feature))
predict.columns=['predict']
print(predict)
r=pd.concat([feature, predict],axis=1)
print(r)
import matplotlib.pyplot as plt
plt.scatter(r['Sepal_Length'],r['Sepal_width'],
            c=r['predict'],alpha=0.5)
#plt.show()

centers=pd.DataFrame(model.cluster_centers_,
             columns=['Sepal_Length','Sepal_width'])



