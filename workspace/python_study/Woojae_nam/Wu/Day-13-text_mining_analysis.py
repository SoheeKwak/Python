## 문제 : 주어진 텍스트 데이터를 모두 데이터베이스에 입력한 후에, 데이터 빈도수를 분석해서 중지 단어 테이블을 생성한다.
## 그리고, 요청하는 값에 대한 자연어 쿼리의 결과를 추출하는 파이썬 코드를 작성하라.
## 문제2: 주어진 CSV 텍스트 데이터를  데이터베이스에 입력하는 코드를 완성하라.

from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import csv
import json
import  os
import os.path
import sqlite3

def drawSheet(cList) :
    global cellList
    if cellList == None or cellList == [] :
        pass
    else :
        for row in cellList:
            for col in row:
                col.destroy()

    rowNum = len(cList)
    colNum = len(cList[0])
    cellList = []
    # 빈 시트 만들기
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='')
            tmpList.append(ent)
            ent.grid(row=i, column=k)
        cellList.append(tmpList)
    # 시트에 리스트값 채우기. (= 각 엔트리에 값 넣기)
    for i in range(0, rowNum):
        for k in range(0, colNum):
            cellList[i][k].insert(0, cList[i][k])

def openCSV() :
    global  csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filereader = open(input_file, 'r', newline='')

    #############################################
    # (1) CSV 파일을 읽어오는 코드 완성
    header = filereader.readline()
    header = header.strip()  # 앞뒤 공백제거
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:  # 모든행은 row에 넣고 돌리기.
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)
    #############################################

    drawSheet(csvList)
    filereader.close()


def openCSV():
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                                 filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filereader = open(input_file, 'r', newline='')
    header = filereader.readline()
    header = header.strip()  # 앞뒤 공백제거
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:  # 모든행은 row에 넣고 돌리기.
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)

    drawSheet(csvList)

    filereader.close()


def sqliteData01() :

    con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

    # 데이터베이스 내의 테이블 목록이 궁금?
    sql = "SELECT name FROM sqlite_master WHERE type='table'"
    cur.execute(sql)
    tableNameList = []
    while True :
        row = cur.fetchone()
        if row == None:
            break
        tableNameList.append(row[0]);

    def selectTable() :
        selectedIndex = listbox.curselection()[0]
        subWindow.destroy()
        # 테이블의 열 목록 뽑기
        # print(colNameList)
        #colNameList = ["userID", "userName", "userAge"]
        #csvList.append(colNameList)
        sql = "SELECT * FROM " + tableNameList[selectedIndex]
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            row_list = []
            for ii in range(len(row)) :
                row_list.append(row[ii])

            csvList.append(row_list)

            drawSheet(csvList)
            
        cur.close()
        con.close()  # 데이터베이스 연결 종료

    subWindow = Toplevel(window)  # window의 하위로 지정
    listbox = Listbox(subWindow)
    button = Button(subWindow, text='선택', command=selectTable)
    listbox.pack(); button.pack()
    for  sName in tableNameList :
        listbox.insert(END, sName)
    subWindow.lift()


    print('Ok!')

def sqliteData02() :
    global csvList, input_file
    cellList = []
    con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    # 열이름 리스트 만들기
    colList = []
    for data in csvList[0] :
        colList.append(data.replace(' ', ''))
    tableName = os.path.basename(input_file).split(".")[0]

    #############################################
    # (2) 데이터베이스에 값을 입력하는 코드 완성
    try:
        sql = "CREATE TABLE " + tableName + "("
        for colName in colList:
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)
    except:
        pass

    for i in range(1, len(csvList)):
        rowList = csvList[i]
        sql = "INSERT INTO " + tableName + " VALUES("
        for row in rowList:
            sql += "'" + row + "',"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)

    #############################################

    con.commit()

    cur.close()
    con.close()  # 데이터베이스 연결 종료
    print('Ok!')





## 전역 변수 ##
csvList, cellList = [], []
input_file = ''

## 메인 코드 ##
window = Tk()
#window.geometry('500x100')

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='CSV 열기', command=openCSV)

sqliteMenu = Menu(mainMenu)
mainMenu.add_cascade(label='SQLite 데이터 분석', menu=sqliteMenu)
sqliteMenu.add_command(label='SQLite 정보 읽기', command=sqliteData01)
sqliteMenu.add_command(label='SQLite 정보 쓰기', command=sqliteData02)


window.mainloop()
