import json
path = "datasets/bitly_usagov/example.txt"
records = [json.loads(line) for line in open(path, encoding='utf-8')]
print(records[0]['tz'])


# Pandas: 데이터분석 패키지(모듈(.py:함수,클래스, 변수 등 구성요소 묶음)
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records) # DataFrame: 데이터를 표 형태로 변환시켜주는 함수
# print(frame)
# print(frame.info()) #자료정보 제공
print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts() #내림차순으로 출력
print(tz_counts)
print(tz_counts[:10]) #상위 10개 출력

clean_tz = frame['tz'].fillna('Missing') # tz키가 존재하지 않는 경우
print(clean_tz)
clean_tz[clean_tz ==''] = 'NA' # NA:Not Available. tz키는 있지만 값이 없는 경우(결측값)
print(clean_tz)

import matplotlib.pyplot as plt
tz_counts = clean_tz.value_counts()
print(tz_counts)
tz_counts[:10].plot(kind='barh')
plt.show()

results = Series([x.split()[0] for x in frame.a.dropna()]) # a키에 해당하는 값만 출력,na행도 제거한 후,, 공백을 기준으로 분할된 후 맨앞의 문자 출력
print(results.value_counts()[:5]) #[x.split()[0] for x in frame.a.dropna()]가 List형태이므로 value_counts함수를 사용하려면 Series형태로 위와 같이 변환시켜줌.

cframe = frame[frame.a.notnull()] #a라는 키가 null이 아닌가? 즉, a키가 존재하는가? True, or False? True인 것만 출력하라.
# print(len(frame))
# print(len(cframe)) # cframe:'a'키가 없는 행은 제거된 상태
"""
a키값(운영체제:OS)이 
Windows 포함하면-> windows
Windows 포함 안하면-> notwindows
"""
# print(cframe.a) # <==> print(cframe['a'])

import numpy as np
# print(cframe.a.str.contains('Windows')) # cframe에 a키에 해당하는 문자열 중 Windows를 갖고 있느냐? True or False로 출력
os = np.where(cframe.a.str.contains('Windows'), 'Windows','Not Windows') # where조건:Windows를 갖고 있다면 'Windows', 'not Windows'형태로 출력하라
print(os[:5])

by_tz_os = cframe.groupby(['tz', os]) # cframe을 os별로 'tz'값에 따라 그룹화
agg_counts = by_tz_os.size().unstack().fillna(0)
print((agg_counts))
# print(agg_counts.sum(1))

indexer = agg_counts.sum(1).argsort() # 각 tz별 Not Windows, Windows 총합을 기준으로 인덱싱
print(indexer)
print(indexer[-10:])

count_subset = agg_counts.take(indexer) # Not Windows, Windows 총합의 오름차순으로 정렬 후 하위 10개 출력
print(count_subset)

normed_subset = count_subset.div\
    (count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True) # 각 tz별 os 비중을 보기 위해 1을 100%로 두고 출력
count_subset.plot(kind='barh', stacked=True) # 총합 순(절대값)대로 출력
plt.show()