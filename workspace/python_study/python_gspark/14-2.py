import numpy as np
arr = np.arange(0, 3*4)
a = arr.reshape([3,4])
print(a)

b = np.array([0,1,2,3,4])
print(b[2])
print(b[-1])
print(a)
#콤마를 기준으로 앞,뒤:행 열
print(a[0,1])
print(a[-1,-1])
#인덱싱: 행 지정 후, 슬라이싱: 콤마 뒤 추출열 지정
print(a[0,: ]) #첫번째 행 전체를 추출
print(a[ :,1]) #두번째 열 전체를 추출
print(a[1, 1:]) # 두번째 행의 두번째 열부터 끝열까지 추출
print(a[:2, :2]) #[[0 1]
                 # [4 5]]

print(a[1, :]) # [4 5 6 7]
print(a[1, :].shape) #(4,) rank=1
print(a[1:2, :]) # [[4 5 6 7]]
print(a[1:2, :].shape) # (1, 4) rank=2

a = np.array([[1,2],[3,4],[5,6]]) #3행2열
print(a.shape)
print(a)

print(a[[0,1,2],[0,1,0]]) #a의 [0,0],[1,1],[2,0]로 짝을 지어 해당 행렬이 참조됨: [1 4 5] array로 출력, 벡터
print(a[0,0],a[1,1], a[2,0]) # 1 4 5  그냥 숫자값으로 출력, 스칼라
print([a[0,0],a[1,1], a[2,0]]) # [1, 4, 5] 대괄호를 붙이면서 리스트로 출력
print(np.array([a[0,0],a[1,1],a[2,0]])) # [1 4 5] 위 리스트를  array로 변환

a = np.array([[1,2],[3,4],[5,6]])
print(a)
s = a[[0,1],[1,1]]
print(s)

#부울린 값
lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
x = np.array(lst)

bool_ind_arr = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False],
])
print(type(lst)) #<class 'list'>
print(type(bool_ind_arr)) #<class 'list'>

res = x[bool_ind_arr]
print(res)

lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
x = np.array(lst)
bool_ind = x%2 #2가 lst 행렬구조에 맞게 확장(브로드캐스팅)되어 각 요소에 연산됨.
print(bool_ind)

bool_ind = (x%2==0)
print(bool_ind)
print(x[bool_ind]) #[2 4 6 8]
print(x[x%2==0]) #[2 4 6 8]


