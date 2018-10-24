# 길이가 1~10인 정사각형 중, 길이가 짝수인 정사각형 넓이
areas=[]
for i in range(1,11):
    if i%2 == 0:
        areas.append(i*i)
print('areas:', areas)

areas = [i*i for i in range(1,11) if i%2==0]
print('areas:', areas)

for i in range(0,3):
    for j in range(0,3):
        print(i,j)

p = [(x, y) for x in range(3) for y in range(3)]
print(p)


students = ['아톰', '똘이', '몽키', '철이']
for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다.'.format(number+1, name))

stu_dic = {
    '{}번'.format(number+1):name for number,name in enumerate(students)
}
print(stu_dic)

students = ['아톰', '똘이', '몽키', '철이']
scores = [80,70,90,100]
stu_dic = {
    students:scores for students,scores in zip(students,scores)
}
print(stu_dic)
print(zip(students,scores))

a1 = [i for i in range(5)]
print(a1)

a2 = [0 for i in range(5)]
print(a2)
a2 = [0 for _ in range(5)]
print(a2)

a3 = [[0,1] for _ in range(5)] # 5행 2열
print(a3)

a4 = [[i,i*2+1, i*2-1] for i in range(5)]
print(a4)
