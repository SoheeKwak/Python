 ## 여러 개의 대용량 CSV --> SQLite, MySQL DB
from  tkinter import *
from  tkinter.simpledialog import *
from tkinter.filedialog import *
import csv
import json
import os
import os.path
import xlrd
import xlwt
import sqlite3
import pymysql
import glob

con = sqlite3.connect('c:/temp/userDB')
cur = con.cursor()

# 폴더 선택하고 그안의 파일목록 추출하기
dirName = askdirectory() # 폴더 선택
file_list = glob.glob(os.path.join(dirName,"*.csv"))
# print(file_list)

# 각 파일을 SQLite에 저장하기 (파일당 테이블 1개씩)
for input_file in file_list:
    filereader = open(input_file, 'r', newline='')
    csvReader = csv.reader(filereader)
    colList = next(csvReader) #첫째줄 읽음(열이름)
    tableName = os.path.basename(input_file).split(".")[0]
    try :
        sql = "create table" + tableName + "("
        for colName in colList :
            cList = colName.split()
            colName = ''
            for col in cList:
                colName += col + '_'
            colName = colName[:-1]
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ')'
        print(sql)
        cur.execute(sql)

    except :
        print('테이블 이상-->', input_file)  #여러개의 파일을 열어갈 때 그 중 일부 테이블이 이상이 있을 시
        # continue                            #오류 무시하고 진행
    for rowList in csvReader:
        sql = "insert into " + tableName + " values("
        for data in rowList :
            sql += "'" + data + "',"
        sql = sql[:-1] + ')'
        cur.execute(sql)


    filereader.close()
    con.commit()

cur.close()
con.close()
print("OK!")