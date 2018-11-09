## Random Forest를 이용해 mnist분류기 제작
from sklearn import datasets
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mnist = datasets.load_digits()
features,labels = mnist.data, mnist.target
print(np.shape((features)))
print(np.shape((labels)))

def cross_validation(classifier, feature, labels):# classifier 모델, feature 데이터, labels 정답
    cv_scores=[]
    for i in range(10):
        scores = cross_val_score(classifier, features, labels, cv=10, scoring='accuracy') #cv=10: cross validation 데이터를 10개로 나누어서 검증
        cv_scores.append(scores.mean())
    return cv_scores

dt_cv_scores = cross_validation(tree.DecisionTreeClassifier(),features, labels)
rf_cv_scores = cross_validation(RandomForestClassifier(),features, labels)

cv_list = [['random forest', rf_cv_scores], ['decision tree', dt_cv_scores]]
df = pd.DataFrame.from_items(cv_list)
df.plot()
plt.show() #random forest(92%정도)가 decision tree(83%)보다 정확도가 더 높게 나옴

print(np.mean(dt_cv_scores))
print(np.mean(rf_cv_scores))