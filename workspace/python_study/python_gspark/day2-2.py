# print(abs(-2))
# print(all([2, 5, 7])) #모두가 참이냐?
# print(all([2, 5, -7]))
# # 0:거짓, 0이 아닌 값:참
# print(any([1, 2, 0])) #하나라도 참이면 참
# print(any([0, ""]))
#
# name = ['gildong','sunsin', 'sejong']
# for n in name :
#     print(n)
#
# for n in ['gildong','sunsin', 'sejong'] :
#     print(n)
#
for n in enumerate(['gildong', 'sunsin', 'sejong']):
     print(n)
#
# for i, n in enumerate(['gildong', 'sunsin', 'sejong']):
#     print(n[1])
#     #print(i)
#
# # eval(): 문자열로 된 수식 등을 실행한 결과값을 리턴해줌
# print(eval('1+2'))
# print(eval('int(3.14)'))
# print('int(3.14)')
#
# a = input("입력하세요")
# print(a)
#
print(len("today"))
print(len([3,4,5]))
print(type("today"))
print(type('t' 'o' 'd' 'a' 'y'))

print(list("today"))
a = list("today")
print(a)

#map (적용함수, 데이터) 데이터를 함수에 적용해라.
def two_times(num) :
    res = []
    for n in num:
        print(n)
        res.append(num*2)
    return res
print(two_times([1,2,3]))
#None:함수를 호추하여 수행한 결과가 리턴되지 않았다

def two_times(num) :
    res = []
    for n in num:
        res.append(num*2)
    return res
res = two_times([1,2,3])
print(res)

def two_times(num): return num*2
print(map(two_times, [1,2,3]))
print(list(map(two_times, [1,2,3])))
#map함수를 출력하면 map 객체가 나옴
#map함수 결과를 리스트로 변환하여 보기위해 list함수 적용

#lambda함수: 함수구문을 간략화
print(list(map(lambda x: x*2, [1,2,3])))

myList = [1,2,3,4,5]
myList = list(map(lambda num: num+10, myList))
print(myList)

list1 = [1,2,3,4,5]
list2 = [10,20,30,40]
hapList = list(map(lambda n1, n2 : n1+n2, list1, list2))
print(hapList)