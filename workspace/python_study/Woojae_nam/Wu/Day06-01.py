## 텍스트마이닝 기반 데이터 분석(부제:텍스트 기반 데이터 분석 및 처리)
#!/usr/bin/env python3
import sys  # 명령창과 연결하는 기능
# 명령창: python Day06-01.py 파라미터1 파라미터2...
input_file = "D:\\workspace\\csv\\supplier_data.csv"
output_file = "D:\\workspace\\output\\result01.csv"

filereader = open(input_file,'r', newline='')
filewriter = open(output_file,'w', newline='')

header = filereader.readline()
header = header.strip() #앞뒤 공백제거
print(header)
header_list = header.split(',')
print(header_list)
# 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.
header_str = ','.join(map(str, header_list))
print(header_str)
filewriter.write(header_str + '\n')
for row in filereader : #모든 행을 row에 넣고 돌리기
    row = row.strip()
    row_list = row.split(',')
    row_str = ','.join(map(str,row_list))
    print(row_str)
    filewriter.write(row_str + '\n')




filereader.close()
filewriter.close()
print('Ok~~')