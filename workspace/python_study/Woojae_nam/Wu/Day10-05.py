# Raw --> CSV
import os
import math
import csv


input_file = 'C:\\Users\\403-3\\Desktop\\Pet_RAW\\Pet_RAW(64x64)\\cat02_64.raw'
output_file = 'C:\\Users\\403-3\\Desktop\\Pet_RAW\csv\\cat02_64.csv' #차례대로 추출


header = ['Column', 'Row', 'Value']
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
                csvWriter.writerow(row_list)

