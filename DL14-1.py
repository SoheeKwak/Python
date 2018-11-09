## Confusion Matrix 생성
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set(font_scale=2)

array = [[9, 1, 0,  0], #행은 실제값, 열은 예측값, ex)실제A인데 A로 예측한 것이 5건
         [1, 15, 3, 1],
         [5, 0, 24, 1],
         [0, 4, 1, 15]]

df_cm = pd.DataFrame(array,index=[i for i in "ABCD"],columns=[i for i in "ABCD"])
print(df_cm)
plt.figure(figsize=(10,7))
plt.title('confusion matrix')
sns.heatmap(df_cm, annot=True) #열 지도 (heatmap): 값이 0일수록 어두움, 값이 클수록 밝은색
plt.show()






