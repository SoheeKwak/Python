import pandas as pd
from pandas import DataFrame
#파일 읽어오기
csv_test = pd.read_csv("test_csv_file.csv") #read_csv는 따로 구분자(delimoter)를 따로 두지 않아도 콤마에 따라 구분함
print(csv_test)
print(csv_test.shape)

text_test = pd.read_csv("test_text_file.txt", sep="|")
print(text_test)

text_test = pd.read_csv("test_text_file.txt", sep="|", index_col=0) #index_col 인덱스 컬럼을 0번째 것으로 지정. 여기선 'ID'
print(text_test)

text_test = pd.read_csv("test_text_file.txt", sep="|", index_col='ID') #index_col 인덱스 컬럼을 별도 지정
print(text_test)
print("="*50)

text_test = pd.read_csv("text_without_column_name.txt", sep="|", header=None, names=['ID','A','B','C','D'], index_col='ID') #컬럼의 이름이 없을 시 자동으로 맨 첫번째 데이터를 header로 인식하므로, header=None을 명시
print(text_test)
print("="*50)

#분석 결과를 파일로 저장하기
data = {
    'id':['a1','a2','a3','a4','a5'],
    'x1':[1,2,3,4,5],
    'x2':[3.0,4.5,3.2,4.0,3.5]
}
data_df = DataFrame(data)
print(data_df)

data_df = DataFrame(data, index=['a1','a2','a3','a4','a5'])
print(data_df)

data_df_2 = data_df.reindex(['a1','a2','a3','a4','a5','a6'])
print(data_df_2)

data_df_2.to_csv("data_df_2.csv", sep=",", na_rep='NaN') # to_csv: 데이터를 csv형식으로 저장하는 함수

