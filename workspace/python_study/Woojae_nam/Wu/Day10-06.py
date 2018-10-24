# Raw --> CSV
import os
import math
import csv
import random

input_file = 'C:\\Users\\403-3\\Desktop\\Pet_RAW\\Pet_RAW(64x64)\\cat02_64.raw'
output_file = 'C:\\Users\\403-3\\Desktop\\Pet_RAW\csv\\cat02_64#2.csv'

header = ['Column', 'Row', 'Value']
rowFIleList = []
with open(input_file, 'rb') as filereader :
    with open(output_file, 'w', newline='') as filewriter :
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)
        fsize = os.path.getsize(input_file)
        XSIZE = YSIZE = int(math.sqrt(fsize))
        for row in range(XSIZE):
            for col in range(YSIZE):
                data = int(ord(filereader.read(1)))
                row_list = [col,row,data]
                rowFIleList.append(row_list)#위에서 차례대로 추출한 것은 섞을 수 없으므로 밑에서 따로 메모리에 저장하여 추출
        random.shuffle(rowFIleList)
        for row_list in rowFIleList:
            csvWriter.writerow(row_list)