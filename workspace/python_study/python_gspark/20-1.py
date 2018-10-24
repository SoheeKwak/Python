#데이터프레임의 문자열 컬럼들->합치는 등의 작업->새로운 컬럼
import pandas as pd
df = pd.DataFrame({
    'id':[1,2,10,20,100,200],
    'name':['aaa','bbb','ccc','ddd','eee','fff']
})
print(df)

df['id_2'] = df['id'].apply(lambda x:"{:0>5d}".format(x))
print(df)

df['id_name'] = df[['id_2','name']].apply(lambda x:'_'.join(x), axis=1)
print(df)

df['id_3'] = df['id'].apply(lambda x:"{:.2f}".format(x))
print(df)

df['name_3'] = df['name'].apply(lambda x:x.upper())
print(df)

df['id_name_3'] = df[['id_3','name_3']].apply(lambda x:':'.join(x), axis=1)
print(df)

# x = 3.141592
# print("{:.2f}".format(x)) #소수점 셋째자리에서 반올림해서 소수점 둘째자리까지 출력
# print("{:+.2f}".format(x))
# x = -3.141592
# print("{:+.2f}".format(x))
# x = 2.718
# print("{:.0f}".format(x)) #소수점 첫째자리에서 반올림해서 정수로 출력
#
# x = 5
# print("{:0>2d}".format(x)) #길이2(두자리), 0으로 채워라
# print("{:0>5d}".format(x)) #길이5(다섯자리), 0으로 채워라
#
# x=7777777
# print("{:0>5d}".format(x)) #정해진 길이보다 길때는 그대로 출력됨
# print("{:,}".format(x))
#
# x = 0.25
# print("{:.2%}".format(x))