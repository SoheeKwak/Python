#연속형 변수 -> 이산화(2개 이상의 범주로 변환)
import numpy as np
import pandas as pd
from pandas import DataFrame
np.random.seed(777)

#데이터 재구조화(reshaping):pivot, stack, melt함수 등
data = DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'],
'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
'grade' : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})
print(data)

##행-고객id, 열-상품코드, 데이터-구매금액
# dp = data.pivot(index='cust_id', columns='prod_cd',values='pch_amt') #인덱스, 칼럼 등이 2개 이상일때는 에러가 남.되도록 아래table함수 쓰도록..
# print(dp)
dp = pd.pivot_table(data,index='cust_id', columns='prod_cd',values='pch_amt')
print(dp)
print("="*50)
dp = pd.pivot_table(data,index=['cust_id','grade'],columns='prod_cd',values='pch_amt')
print(dp)
print("="*50)
dp = pd.pivot_table(data,index='cust_id',columns=['grade','prod_cd'],values='pch_amt')
print(dp)

mul_index = pd.MultiIndex.from_tuples(
    [('cust_1','2018'), #label(범주) cust_1:0, cust_2:1 2018:0, 2018:1
     ('cust_1','2019'),
     ('cust_2','2018'),
     ('cust_2','2019')])
print(mul_index)
print("="*50)
data = DataFrame(data=np.arange(16).reshape(4,4),
          index=mul_index,
          columns=['prd_1', 'prd_2', 'prd_3', 'prd_4'],
          dtype='int')
print(data)
data_stacked = data.stack()
print(data_stacked)
print(data_stacked.index)
print(data_stacked['cust_2']['2018'][['prd_1','prd_2']])

data.ix['cust_2','prd_4'] = np.nan
print(data)
print(data.stack(dropna=False)) #default:dropna=True
print("="*50)
print(data_stacked)
print(data_stacked.unstack()) #default:level=-1
print(data_stacked.unstack(level=-1))
print(data_stacked.unstack(level=0))
print(data_stacked.unstack(level=1))
print("="*50)
data_stacked_unstacked = data_stacked.unstack(level=-1)
print(data_stacked_unstacked)
print(type(data_stacked_unstacked))
dsu_df = data_stacked_unstacked.reset_index()
print(dsu_df)
dsu_df = dsu_df.rename(columns={'level_0':'custID', #인덱스에 이름 주기
                       'level_1': 'year'})
print(dsu_df)

data = DataFrame({
'cust_id': ['c1', 'c1', 'c2', 'c2'],
'prod_cd': ['p1', 'p2', 'p1','p2'],
'pch_cnt' : [1,2,3,4],
'pch_amt': [100,200,300,400]})
print(data)

print(pd.melt(data))
print("="*50)
print(pd.melt(data, id_vars=['cust_id','prod_cd']))
print("="*50)
print(pd.melt(data,
              id_vars=['cust_id','prod_cd'],
              var_name='pch_cd',
              value_name='pch_value')) # var_name:variable, value_name:value
print("="*50)
print(data)
data_melt = pd.melt(
    data,
    id_vars=['cust_id','prod_cd'],
    var_name='pch_cd',
    value_name='pch_value')
print(data_melt)
print(data_melt.index)
print(data_melt.columns)
#
data_melt_pivot = pd.pivot_table(
        data_melt,
        index=['cust_id','prod_cd'],
        columns='pch_cd',
        values='pch_value')
print(data_melt_pivot)
print(data_melt_pivot.index)
print(data_melt_pivot.columns)
