# N-Gram : 문장 유사도 분석
#레벤슈타인 거리(편집거리 알고리즘): 두개의 문자열이 어느 정도 다른가, DNA배열 유사성 조사
#ex) 가나다라, 가마바라 의 편집거리 :2 (2번 편집-추가, 변경, 삭제-해야 같아지므로): 수치가 낮을수록 가장 가까운 단어로 유사도가 높음
# LCS알고리즘 https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EA%B3%B5%ED%86%B5_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4(Traceback example 참조)

# 레벤수타인 거리 구하기
def calc_distance(a,b):
    if a==b: return 0 #문자가 완전히 일치 하면
    a_len=len(a)
    b_len=len(b)
    if a == "": return b_len #a는 공백이고 b가 단어일 때  a는 b길이만큼 추가
    if b == "": return a_len

    matrix = [[]for i in range(a_len+1)] # print(matrix) [[], [], [], [], []]
    for i in range(a_len+1):
        matrix[i]=[0 for j in range(b_len+1)] # print(matrix) [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(a_len+1):
        matrix[i][0] = i  # print(matrix) [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    for j in range(b_len + 1):
        matrix[0][j] = j   # print(matrix) [[0, 1, 2, 3, 4], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    for i in range(1, a_len+1) : # range(1,5)==>1~4
        ac= a[i-1]   # a[i-1]: a의 0번째 값, "가나다라"에서 "가"
        for j in range(1, b_len + 1):  # range(1,5)==>1~4
            bc = b[j-1] #b의 0번째 값, "가마바라"에서 "가"
            cost = 0 if (ac==bc) else 1 # cost는 문자a, 문자b 의 각각의 요소로 matrix[i][j] 행렬과 구분! 사실상 matrix[i][j]는 [i][j]에 해당하는 a, b문자 그대로임
            matrix[i][j]=min(  # matrix[i][j]에는 문자 삽입, 제거, 변경 중 가장 작은 값을 대입
                matrix[i-1][j] +1, #문자삽입, [i][j]의 바로 위
                matrix[i][j-1] + 1, #문자제거, [i][j]의 왼쪽
                matrix[i-1][j-1]+ cost #문자변경, [i][j]의 대각선
            )
    return matrix[a_len][b_len]# a와 b사이의 거리
print(calc_distance("가나다라", "가마바라"))

samples = ["신촌역", "화곡역", "동대문입구역", "신발", "상공회의소"]
base = samples[0]
r = sorted(samples, key=lambda n: calc_distance(base, n)) #samples 리스트의 각 요소들이 n에 하나씩 들어가서 calc_distance함수로 계산된 후(두문자의 편집거리) key를 기준으로 해당 역이름들이 오름차순으로 정렬됨,
# for n in range(len(samples)):
#     calc_distance(base, samples[n]) 와 같은 의미를 lambda로 구현
for n in r:
     print(calc_distance(base, n), n)


#n-gram: 두 문장 사이의 유사도를 조사하는 방법
#n? 이웃한 문자의 수. n이 커질수록 유사도가 낮아짐, n이 작을수록 엄격해짐
# ex)"오늘 상공회의소에서 문자 비교 알고리즘을 배웠다"
# ex) "문자 비교 알고리즘을 오늘 상공회의소에서 배웠습니다"
# n을 2로 한 경우,
# ['오늘', '늘 ', ' 상', '상공', '공회',....,'웠다']
# ['문자', '자 ', ' 비', '비교', ...., '니다']

def ngram(s, num): # num자리 만큼 끊어 준 문자열 리스트를 반환해라
    res = []
    slen = len(s)-num+1 # 리스트 요소의 개수
    for i in range(slen): #i는 0부터 slen-1까지
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num): # 두 문자열간 유사도 조사
    a = ngram(sa, num)
    b = ngram(sb, num)
    cnt=0
    r=[]
    for i in a:
        for j in b:
            if i==j:
                cnt+=1
                r.append(i)
    return  cnt / len(a), r
a = "오늘 상공회의소에서 문자 비교 알고리즘을 배웠다"
b = "문자간 비교하는 알고리즘을 상공회의소에서 오늘 배웠다"
#2-gram
res = diff_ngram(a,b,2)
print("2-gram", res)

#3-gram
res = diff_ngram(a,b,3)
print("3-gram", res)



