# JASON 데이터도 처리하기
import json
jsonDic = {}
jsonLIst = []
csvLIst = []

filereader = open('TEST01.json','r',encoding='utf-8')
jsonDic = json.load(filereader)
# print(jsonDic)
csvName = list(jsonDic.keys())  #테이블 네임 추출 ['userTest']
# print(csvName)
jsonLIst = jsonDic[csvName[0]]
# print(jsonLIst)
#헤더 추출
header_list = list(jsonLIst[0].keys())
# print(header_list) #['ID', 'NAME', 'ADDR']
csvLIst.append((header_list))
#행들 추출
for tmpDic in jsonLIst:
    tmpList = []  #딕셔너리는 차례가 없으므로, 순서대로 들어있지 않을 수도 있음. 그러므로  value로 추출하면 안 되고 key를 기준으로 추출하는 것이 리스크를 줄임
    for header in header_list:
        data = tmpDic[header]
        tmpList.append(data)
    csvLIst.append(tmpList)
print(csvLIst)
filereader.close()


