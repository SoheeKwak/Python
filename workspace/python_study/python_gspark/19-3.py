"""
데이터프레임 정렬:DataFrame.sort_values()
#튜플정렬:sorted(tuple,key)
#리스트정렬:sort(),sorted(list)
"""
import pandas as pd
pdf = pd.DataFrame({'seq':[1,3,2],
                    'name':['park','lee','choi'],
                    'age':[30,20,40]})
print(pdf)
print(pdf.sort_values(by=['seq'],axis=0,ascending=False))
pdf.sort_values(by=['seq'], axis=0,inplace=True)
print(pdf)
# #
import numpy as np
pdf = pd.DataFrame({'seq':[1,3, np.nan],
                    'name':['park','lee','choi'],
                    'age':[30,20,40]})
print(pdf)
pdf.sort_values(by=['seq'], axis=0,inplace=True,na_position='last')
print(pdf)
pdf.sort_values(by=['seq'], axis=0,inplace=True,na_position='first')
print(pdf)
# #
pt = [(1,'park',30),
      (3,'lee',20),
      (2,'choi',40)]
# print(pt)
print(sorted(pt, key=lambda ptf:ptf[0]))
print(sorted(pt, reverse=True,key=lambda ptf:ptf[1]))
print(sorted(pt, key=lambda ptf:ptf[2]))

#리스트: sorted(list), sort
# mlist = [9,4,1,2,7]
# print(sorted(mlist))
# print(mlist)
# #
# mlist.sort()
# print(mlist)

# Seri = pd.Series([10.,11.,12.,13.,14.])
# print(Seri)
# print(Seri[3])
# print(Seri[:3])
# #평균값 이상인 행만 추출
# print(Seri[ Seri.mean()<=Seri])
# print(Seri[[3,4,2]])

Seri_ix = pd.Series([10.,11.,12.,13.,14.],
                 index=['a','b','c','d','e'])
# print(Seri_ix)
# print(Seri_ix[['c','d','b']])
# print(Seri_ix.get(['c','d','b']))
#
# Seri_ix['c']=100
# print(Seri_ix)
#
# print('c' in Seri_ix)

## ix:위치 지정하여 데이터를 참조, 레이블을 이용하여 데이터를 참조
# loc: 레이블을 이용하여 데이터 참조(위치x)
# iloc: 위치 지정하여 데이터를 참조(레이블x)
import numpy as np
# Seri = pd.Series(np.nan, index=[19,18,17,16,15,1,2,3,4,5])
# print(Seri)
# print(Seri.iloc[:3]) #0번행~2번행까지 추출
# print(Seri.loc[:3]) #레이블3이 나올때까지 추출
# print(Seri.ix[:3]) #ix속성에 수치값을 주는 경우에는 loc와 동일한 결과



