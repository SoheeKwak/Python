import pandas as pd
import numpy as np
from pandas import DataFrame, Series

# groupby 집계함수
#1. 딕셔너리를 이용한 그룹화
df = DataFrame(data = np.arange(20).reshape(4,5),
               columns=['c1','c2','c3','c4','c5'],
               index=['r1','r2','r3','r4'])
print(df)

mdr = {'r1':'row_g1',
       'r2':'row_g1',
       'r3':'row_g2',
       'r4':'row_g2'}
gbr = df.groupby(mdr)
print(gbr.sum())

mdc = {'c1':'col_g1',
       'c2':'col_g1',
       'c3':'col_g2',
       'c4':'col_g2',
       'c5':'col_g2'}
gbc = df.groupby(mdc, axis=1)
print(gbc.sum())

print(type(mdr))
# dict -> Series 자료구조를 바꿈-> Series를 이용한 그룹화
msr = Series(mdr)
print(type(msr))
print(mdr)
print(msr)

print(df.groupby(msr).sum())

msc = Series(mdc) #딕셔너리를 Series로 변경
print(msc)
print(df.groupby(msc, axis=1).sum())

#함수를 이용한 그룹화
def rgf(x): # df에 대한 정보가 x에 전달
    if x=='r1' or x=='r2':
        rg = 'row_g1'
    else:
        rg = 'row_g2'
    return rg
print(df.groupby(rgf).sum())