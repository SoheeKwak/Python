import json
path = 'example.txt'
print(open(path,  encoding='utf-8').readline())
rec = [json.loads(line) for line in open(path, encoding='utf-8-sig')] # comprehension: for문을 json.loads(line)의 리스트요소로 나타내자.
print(len(rec)) #rec에 총 3560개의 라인이 있음
time_zones = [myRec['tz'] for myRec in rec if 'tz' in myRec] #각 라인들(myRec)이 모두 'tz'키를 갖고 있는 것이 아니기 때문에 #if문: 만약 myRec에 'tz'키가 있다면 tz'키에 해당하는 값을 추출해 time_zones리스트의 요소로 넣어라
print(len(time_zones)) #총 3560개 중 'tz'의 키를 갖고 있는 라인이 3440개
print(rec[0]['tz'])
print(rec[3559]['tz'])

print(time_zones[:20])

from collections import defaultdict
def get_count2(sequence): # 아래 def get_counts(sequence):와 같은 함수
    counts = defaultdict(int) # 0으로 초기화
    for x in sequence:
        counts[x]+=1
    return counts
counts = get_count2(time_zones)
print(counts)
print(counts['America/New_York']) #뉴욕도시에 해당하는 갯수:1251
print(len(counts)) #도시의 갯수


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x]+=1 #counts에 이미 들어있다면 그 특정 키에 해당하는 횟수를 추가하여 세어라.
        else:
            counts[x]=1
    return  counts

counts = get_counts(time_zones)
print(counts)
print(counts['America/New_York']) #뉴욕도시에 해당하는 갯수:1251
print(len(counts)) #도시의 갯수
