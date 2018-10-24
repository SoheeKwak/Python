## 여러개의 대용량 CSV 파일 --> MySQL
from  tkinter import *
from  tkinter.simpledialog import *
from tkinter.filedialog import *
import csv
import json
import os
import os.path
import xlrd
import xlwt
import pymysql
import glob

con = pymysql.connect(host='192.168.5.131', user='root',
                          password='1234', db='userDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
cur = con.cursor()

# 폴더 선택하고, 그 안의 파일목록들 추출하기.
dirName = askdirectory()
file_list = glob.glob(os.path.join(dirName,"*.csv"))

# 각 파일을 SQLite에 저장하기. (파일당 테이블 1개)
for  input_file  in file_list :
    filereader = open(input_file, 'r', newline='')
    csvReader = csv.reader(filereader)
    colList = next(csvReader) # 열이름들
    tableName = os.path.basename(input_file).split(".")[0]
    try :
        sql = "CREATE TABLE " + tableName + "("
        for  colName  in  colList :
            cList = colName.split()
            colName = ''
            for col in cList :
                colName += col + '_'
            colName = colName[:-1]
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ')'
        print(sql)
        cur.execute(sql)

    except :
        print('테이블 이상 -->', input_file)
        #continue

    for rowList in csvReader :
        sql = "INSERT INTO " + tableName + " VALUES("
        for data in rowList :
            sql += "'" + data + "',"
        sql = sql[:-1] + ')'
        cur.execute(sql)

    filereader.close()
    con.commit()

cur.close()
con.close()
print("OK!")