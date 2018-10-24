from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import csv

def drawSheet(cList):
    global cellList
    if cellList == None or cellList == []:
        print('1111')
        pass
    else:
        print('2222')
        for row in cellList:
            for col in row:
                col.destroy()
    rowNum = len(cList)
    colNum = len(cList[0])
    cellList = []
    for i in range(0,rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='')
            tmpList.append(ent)
            ent.grid(row=i, column=k)
        cellList.append(tmpList)
    for i in range(0, rowNum):
        for k in range(0,colNum):
            cellList[i][k].insert(0, cList[i][k])


def openCSV():
    global csvList
    csvList = []
    input_file = askopenfilename(parent=window,
                filetypes = (("CSV파일", "*.csv"), ("모든파일", "*.*")))
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

def saveCSV() :
    global csvList
    if csvList == []:
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',
               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    for row_list in csvList :
        row_str = ','.join(map(str, row_list))
        filewriter.writelines(row_str + '\n')

    filewriter.close()

def csvData02() :
    global csvList
    csvList = []
    input_file = "D:/workspace/csv/supplier_data.csv"
    filereader = open(input_file, 'r', newline='')
    csvReader = csv.reader(filereader)
    header_list = next(csvReader)
    csvList.append(header_list)
    print(csvList)
    for row_list in csvReader:
        csvList.append(row_list)
    print(csvList)

    drawSheet(csvList)
    filereader.close()


def csvData03() :
    global  csvList
    csvList = []
    dirName = askdirectory()

    import glob
    import os
    file_list = glob.glob(os.path.join(dirName, "*.csv"))
    for input_file in file_list:
        filereader = open(input_file,'r',newline='')
        print(input_file)
        csvReader = csv.reader(filereader)
        header_list = next(csvReader)
        rowCount = 0
        for row in csvReader:
            rowCount +=1
        csvList.append([os.path.basename(input_file),'-->',rowCount])
        filereader.close()

    drawSheet(csvList)

def csvData04() :
    global  csvList
    csvList = []
    dirName = askdirectory()

    import glob
    import os
    file_list = glob.glob(os.path.join(dirName, "*.csv"))
    for input_file in file_list:
        filereader = open(input_file,'r',newline='')
        csvReader = csv.reader(filereader)
        header_list = next(csvReader)
        for row in csvReader:
            csvList.append(row)
    drawSheet(csvList)


    filereader.close()

## 전역 변수 ##
csvList, cellList = [], []

## 메인 코드 ##
window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='CSV 열기', command=openCSV)
fileMenu.add_command(label='CSV 저장', command=saveCSV)

csvMenu = Menu(mainMenu)
mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)
csvMenu.add_command(label='csv 패키지 활용', command=csvData02)
csvMenu.add_command(label='여러 CSV 행수 알기', command=csvData03)
csvMenu.add_command(label='CSV 파일 합치기', command=csvData04)
window.mainloop()
