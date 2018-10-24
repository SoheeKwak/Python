path = "datasets/bitly_usagov/example.txt" #딕셔너리 형태: json 파일
data = open(path).readline()
print(data)


import json
path = "datasets/bitly_usagov/example.txt"
records = [json.loads(line) for line in open(path, encoding='utf-8')]
print(records[0]['tz'])
# print(records)

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones)
print(time_zones[:20]) #상위 20개만 출력

def get_counts(sequence):
    counts = {} #빈 딕셔너리 초기 설정
    for x in sequence:
        if x in counts:# 해당값(지역/도시명)이 이미 저장되어 있는 경우
            counts[x] +=1
        else: #저장 안 되어 있는 경우
            counts[x] = 1 #키(지역/도시명)가 처음 등장하면 키값(도시수)에 1을 준다
    return counts

from collections import defaultdict  #위 함수보다 더 간단한 코드
def get_counts2(sequence):
    counts = defaultdict(int) # 딕셔너리에서 키값을 디폴트 0으로 초기화
    for x in sequence:
        counts[x]+=1
    return counts

counts = get_counts(time_zones)
print(type(counts))
print(counts['America/New_York'])
print(len(counts)) #'키:키값'의 갯수, 즉 도시의 개수
print(len(time_zones)) #'tz'가 있는 행의 갯수
print(counts)

#가장 많이 등장한 도시 10개를 출력
def top_counts(count_dict, n=10):
    value_key_pairs = [(value, key) for key, value in count_dict.items()] #value, key를 ()로 묶음으로써 튜플로 출력
    print(value_key_pairs)
    value_key_pairs.sort() #위에서 (value, key)순으로 넣어서 value(키값)을 기준으로 정렬
    print(value_key_pairs[-n:]) #위에서 n=10으로 초기설정했기 때문에, 뒤에서 10개 출력

top_counts(counts,3) # 상위 3개 출력

from collections import Counter #상위 10개를 출력하는 간단한 함수
counts = Counter(time_zones)
print(counts.most_common(10))
# print(counts)

eng = "fjlgjsopgjth;tkj;l'" #Counter함수 사용 방법
print(Counter(eng))



