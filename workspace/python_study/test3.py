import random

list = []
i, k = 0, 0

for i in range(0, 6):
    list.append(random.randint(1, 10))

print('정렬 전 데이터:', end='')
print(list)

def bubble_sort(list):
    for i in range(len(list) - 1):
        for k in range(1, len(list) - i):
            if list[k - 1] > list[k]:
                temp = list[k - 1]
                list[k - 1] = list[k]
                list[k] = temp

bubble_sort(list)
print('정렬 후 데이터:', end= '')
print(list)
