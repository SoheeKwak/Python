import numpy as np
import pandas as pd
from pandas import DataFrame as df, Series

data = {'key1':['a','b','b','c','c'],
        'key2':['v','w','w','x','y'],
        'col':[1,2,3,4,5]}
df = pd.DataFrame(data)
print(df)
print(df.drop_duplicates(['key1'],keep=False))